from flask import Flask, render_template

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


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About Page")


if __name__ == "__main__":
    app.run(debug=True)
