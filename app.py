from flask import Flask
app = Flask(__name__)

count = 0

@app.route('/')
def index():
    global count
    count += 1
    return "Hello from app " + str(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0')