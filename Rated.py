from flask import Flask, render_template

app = Flask(__name__)


@app.route('/',methods=["GET", "POST"])
def hello_world():
    likes = 0
    return render_template("indexx.html", value=likes)


if __name__ == '__main__':
    app.run()
