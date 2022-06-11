from flask import Flask, render_template
import pandas as pd
import folium

corona_df = pd.read_csv('./datasets/Taiwan-covid-19.csv')
by_country = corona_df.groupby('縣市別').sum()[
    ['新增確診人數', '累計確診人數']]
cdf = by_country.nlargest(15, '累計確診人數')[['累計確診人數']]


# corona_df = pd.read_csv('./datasets/covid-19-dataset-1.csv')

# corona_df = corona_df.dropna()

m = folium.Map(location=[23.6581417, 120.1685611],
               tiles='Stamen toner',
               zoom_start=7)

pairs = [(country, confirmed)
         for country, confirmed in zip(cdf.index, cdf['累計確診人數'])]


def circle_maker(x):
    print(x)
    folium.Circle(location=[x[0], x[1]],
                  radius=float(x[2])*0.08,
                  color="red",
                  popup='{}\n confirmed cases:{}'.format(x[1], x[0])).add_to(m)


corona_df = corona_df.dropna(subset=['Lat'])

corona_df = corona_df.dropna(subset=['Long_'])

corona_df[['Lat', 'Long_', '累計確診人數']].apply(
    lambda x: circle_maker(x), axis=1)

html_map = m._repr_html_()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", table=cdf, cmap=html_map, pairs=pairs)


if __name__ == "__main__":
    app.run(debug=True)
