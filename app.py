from flask import Flask
print("Nick was here 2021")
print(" Dan was here 2021")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
