from flask import Flask, render_template, request, redirect, url_for, flash
from .models import db, User

def configure_routes(app: Flask):
    @app.route('/')
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    #@app.route('/usuario/<id>')
    #def form(id):
    #    userById = User.query.filter_by(id=id)

    @app.route('/novoUser', methods=['GET', 'POST'])
    def novoUser():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            
            try:
                new_user = User(nome=nome, email=email)
                db.session.add(new_user)
                db.session.commit()
                flash('Usuario criado com sucesso', 'success')

                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao criar usuario: {str(e)}', 'danger')

        return render_template('form.html')