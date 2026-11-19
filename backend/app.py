from flask import Flask, render_template, request, redirect, session
import pymysql

app = Flask(__name__, template_folder='../frontend')
app.secret_key = 'kunci_bebas_alp'

def get_db():
    return pymysql.connect(
        host='127.0.0.1',
        port=8553,
        user='alp_user',
        password='alp12345',
        database='db_alp',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
                user = cursor.fetchone()
                if user:
                    session['user'] = user['username']
                    return redirect('/dashboard')
                else:
                    error = 'Username atau password salah!'
        finally:
            conn.close()
            
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', username=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
