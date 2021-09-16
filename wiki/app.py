import random
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

posts = [
    {
        "author": "Small Python",
        "title": "Post 00",
        "content": "This is some content.",
        "date_posted": "August 28, 2021",
    },
    {
        "author": "Small Python",
        "title": "Post 01",
        "content": "This is some other content.",
        "date_posted": "August 29, 2021",
    }
]

quotes = [
    "I put that shit on everything!",
    "I'm just going to take the L on that one.",
    "Fake it until you make it.",
    "If you don't chew Big Red, then fuck you.",
    "Get good, scrub."
]


def random_quote():
    quote = random.choice(quotes)
    return quote

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", posts=posts, quote=random_quote())


@app.route("/about")
def about():
    return render_template("about.html", title="About Page")


if __name__ == "__main__":
    app.run(debug=True)
