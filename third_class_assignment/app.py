from flask import Flask

app = Flask(__name__)


@app.route('/content', methods=['GET'])
def get_content():
    return open("words.txt").read(), 200


@app.route('/register', methods=['POST'])
def register():
    open("words.txt", 'w').write("hello")
    return "success", 201


if __name__ == '__main__':
    app.run(port=30000)
