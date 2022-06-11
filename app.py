from flask import Flask, redirect, render_template, url_for
from flask_ngrok import run_with_ngrok
from controllers.Part1 import Part1
from controllers.Part2 import Part2
from controllers.Part3 import Part3
from controllers.Taiwan import Taiwan

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def home():
    return redirect(url_for('part1'))


@app.route('/Part1')
def part1():
    part1 = Part1().main()
    return render_template("home.html", table=part1['cdf'], cmap=part1['html_map'], pairs=part1['pairs'], title="Part 1", datasource="Data-flair")


@app.route('/Part2')
def part2():
    part2 = Part2().main()
    return render_template("home.html", table=part2['cdf'], cmap=part2['html_map'], pairs=part2['pairs'], title="Part 2", datasource="Data-flair")


@app.route('/Part3')
def part3():
    part3 = Part3().main()
    return render_template("home.html", table=part3['cdf'], cmap=part3['html_map'], pairs=part3['pairs'], title="Part 3", datasource="Data-flair")


@app.route('/Taiwan')
def taiwan():
    taiwan = Taiwan().main()
    return render_template("home.html", table=taiwan['cdf'], cmap=taiwan['html_map'], pairs=taiwan['pairs'], title="Taiwan", datasource="中央疫情指揮中心")


if __name__ == "__main__":
    app.run()
