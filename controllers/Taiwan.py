import pandas as pd
import folium


class Taiwan:

    def __init__(self) -> None:
        self.corona_df = pd.read_csv("./datasets/Taiwan-covid-19-all.csv")

    def circle_maker(self, x, m):
        folium.Circle(location=[x[0], x[1]],
                      radius=float(x[2])*0.1,
                      color="red",
                      popup='{}\n confirmed cases:{}'.format(x[3], x[2])).add_to(m)

    def main(self):
        by_country = self.corona_df.groupby('全稱').sum()[
            ['新增確診人數', '累計確診人數']]
        cdf = by_country.nlargest(15, '累計確診人數')[['累計確診人數']]
        m = folium.Map(location=[23.6581417, 120.1685611],
                       tiles='Stamen toner',
                       zoom_start=7)

        pairs = [(country, confirmed)
                 for country, confirmed in zip(cdf.index, cdf['累計確診人數'])]

        corona_df = self.corona_df.dropna(subset=['Lat'])
        corona_df = corona_df.dropna(subset=['Long_'])
        corona_df[['Lat', 'Long_', '累計確診人數', '全稱']].apply(
            lambda x: self.circle_maker(x, m), axis=1)

        return {
            "pairs": pairs,
            "cdf": cdf,
            "html_map": m._repr_html_(),
        }
