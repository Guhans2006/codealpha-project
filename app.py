from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# HTML form template
login_form = '''
    <h2>Login</h2>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    <p>{{ message }}</p>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to DB and use parameterized query (safe!)
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            message = "✅ Login successful!"
        else:
            message = "❌ Invalid username or password."

    return render_template_string(login_form, message=message)

if __name__ == '__main__':
    app.run(debug=True)
