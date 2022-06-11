import pandas as pd
import folium


class Part1:

    def __init__(self) -> None:
        self.m = folium.Map(location=[34.223334, -82.461707],
                            tiles='Stamen toner',
                            zoom_start=8)
        self.corona_df = pd.read_csv('./datasets/covid-19-dataset-1.csv')
        self.corona_df = self.corona_df.dropna(subset=['Lat'])
        self.corona_df = self.corona_df.dropna(subset=['Long_'])

    def circle_maker(self, x):
        folium.Circle(location=[x[0], x[1]],
                      radius=float(x[2])*10,
                      color="red",
                      popup='{}\n confirmed cases:{}'.format(x[3], x[2])).add_to(self.m)

    def main(self):
        by_country = self.corona_df.groupby('Country_Region').sum()[
            ['Confirmed', 'Deaths', 'Recovered', 'Active']]
        cdf = by_country.nlargest(15, 'Confirmed')[['Confirmed']]
        pairs = [(country, confirmed)
                 for country, confirmed in zip(cdf.index, cdf['Confirmed'])]
        self.corona_df[['Lat', 'Long_', 'Confirmed', 'Combined_Key']].apply(
            lambda x: self.circle_maker(x), axis=1)
        return {
            "pairs": pairs,
            "cdf": cdf,
            "html_map": self.m._repr_html_()
        }
