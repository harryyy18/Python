# 1. A program that creates a simple web server and serves a static HTML page.
# 2. A program that creates a web application that allows users to register and login.
# 3. A program that creates a web application that allows users to upload and download files.
# 4. A program that creates a web application that displays data from a database in a tabular format.
# 5. A program that creates a web application that accepts user input and sends it to a server-side script for processing.


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    users[username] = password
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return "File uploaded successfully"

@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def index():
    data = Data.query.all()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['input']
    # Process the user input here
    return "Processed: " + user_input

if __name__ == '__main__':
    app.run(debug=True)

