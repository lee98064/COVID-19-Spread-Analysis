from flask import Flask, redirect, render_template, url_for
from controllers.Part1 import Part1
from controllers.Part2 import Part2

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('part1'))


@app.route('/Part1')
def part1():
    part1 = Part1().main()
    return render_template("home.html", table=part1['cdf'], cmap=part1['html_map'], pairs=part1['pairs'], title="Part 1")


@app.route('/Part2')
def part2():
    part2 = Part2().main()
    return render_template("home.html", table=part2['cdf'], cmap=part2['html_map'], pairs=part2['pairs'], title="Part 2")


@app.route('/Part3')
def part3():
    pass


if __name__ == "__main__":
    app.run(debug=True)
