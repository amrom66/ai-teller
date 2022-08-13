from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/opencv', methods=['GET'])
def opencv():
    return 'opencv'