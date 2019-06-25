from flask import Flask
app = Flask(__name__)
app.config.from_envvar('SETTING',silent=True)
@app.route('/')
def index():

    return '1111'
if __name__ == '__main__':
    print(app.config['HELLO'])
