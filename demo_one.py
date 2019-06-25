from flask import Flask
class Demo(object):
    a = '1'
class Demo_two(Demo):
    DEBUG = True
app = Flask(__name__)
app.config.from_object(Demo_two)
@app.route('/')
def index():
    return 'hello world2'
if __name__ == '__main__':
    app.run()

