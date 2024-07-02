from getpass import getpass

from flask import Flask, render_template
import requests
import getpass

from datetime import datetime
app = Flask(__name__)


# Get the data of Blogs
data = requests.get("https://api.npoint.io/548bb22abe9204c52867").json()



@app.route("/")
def get_all_posts():
    return render_template("index.html", data=data)



@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template("post.html", post=data[post_id - 1])

if __name__ == "__main__":
    app.run(debug=True, port=4008)
