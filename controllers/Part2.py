import pandas as pd
import folium


class Part2:

    def __init__(self) -> None:
        self.corona_df = pd.read_csv("./datasets/covid-19-dataset-2.csv")

    def find_top_confirmed(self, n=15):
        by_country = self.corona_df.groupby('Country_Region').sum(
        )[['Confirmed', 'Deaths', 'Recovered', 'Active']]
        cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
        return cdf

    def circle_maker(self, x, m):
        folium.Circle(location=[x[0], x[1]],
                      radius=float(x[2]),
                      color="red",
                      popup='confirmed cases:{}'.format(x[2])).add_to(m)

    def main(self):
        cdf = self.find_top_confirmed()
        pairs = [(country, confirmed)
                 for country, confirmed in zip(cdf.index, cdf['Confirmed'])]
        corona_df = self.corona_df[['Lat', 'Long_', 'Confirmed']]
        corona_df = corona_df.dropna()
        m = folium.Map(location=[34.223334, -82.461707],
                       tiles='Stamen toner',
                       zoom_start=8)
        corona_df.apply(lambda x: self.circle_maker(x, m), axis=1)

        return {
            "pairs": pairs,
            "cdf": cdf,
            "html_map": m._repr_html_(),
        }
