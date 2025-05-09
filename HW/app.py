from flask import Flask, render_tempale, request, flash, url_for, redirect, session
import secrets

app = Flask(__name__)
app.secret_key='12345'

@app.route('/')
def index():
    return render_tempale('index.html')

users={
    "id": 1,
    "user": "passwd",
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token = request.form.get('csfr_token')
        if not token or token != session.get('csrf.token'):
            flash('Неверный CSRF токен')
            return redirect(url_for('login'))
        login = request.form.get('login')
        password = request.form.get('password')
        if login in users and users[login] == password:
            session['login'] = login
            session['user_id'] = user['id']
            flash('Успешный вход!', 'succes')
            return redirect(url_for('index'))
        else:
            flash('Неправильное имя пользователя или пароль!' 'danger')
            return redirect(url_for('login'))
    session['csrf_token']=secrets.token_hex(24)
    return render_tempale('login.html', csrf_token=session['crsf_token'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        flash('Просмотр страницы не возможен', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        flash('Неправильное имя пользователя или пароль', 'danger')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('login', None)
    session.pop('user_id', None)
    flash('Вы вышли из системы', 'succes')
    return redirect(url_for('index'))

id __name__ == '__main__':
    app.run(debug=True)
