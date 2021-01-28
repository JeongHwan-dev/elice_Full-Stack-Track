from flask import Flask

app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %s' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return "Subpath %s" % subpath


if __name__ == "__main__":
    app.run()
