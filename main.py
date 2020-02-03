from flask import Flask, render_template, request
from file_proc import read_file

app = Flask(__name__)

@app.route('/')
def index():
  return "<a href='/home'>Hi!</a>"

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html', active_page = 'about')

@app.route('/contact')
def contact():
  # Pieslegtsanas DB
  return render_template('contact.html', phone = 778787)

@app.route('/params')
def params():
  return render_template('params.html', args = request.args.to_dict())

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

@app.route('/read_from_file')
def readFromFile():
  content = read_file()
  return content


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)