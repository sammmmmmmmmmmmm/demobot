from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "404 site not found"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    return "fuck you jason"


@app.route('/ncss')
def ncss():
    return "<h1>ncss</h1>"

if __name__ == "__main__":
    app.run()