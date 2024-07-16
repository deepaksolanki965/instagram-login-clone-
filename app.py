from flask import Flask, render_template, request

app = Flask(__name__)

# List to store login details
logins = []

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        logins.append({'username': username, 'password': password})
        return f'Logged in as: {username}'

    return render_template('index.html')

@app.route('/logins', methods=['GET'])
def show_logins():
    return render_template('logins.html', logins=logins)

if __name__ == '__main__':
    app.run(debug=True)
