from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home/index.html')

@app.route('/about')
def profile():
    return render_template('About/about.html')

@app.route('/login')
def login():
    return render_template('Login/login.html')



