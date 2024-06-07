from flask import Flask, render_template, request, redirect, url_for, flash, session
from .models import db, User
import logging

def configure_routes(app: Flask):
    @app.route('/')
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    @app.route('/novoUser', methods=['GET', 'POST'])
    def novoUser():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            telefone = request.form['telefone']
            cep = request.form['cep']
            dataNascimento = request.form['dataNascimento']
            
            try:
                new_user = User(nome=nome, email=email, telefone=telefone, cep=cep, dataNascimento=dataNascimento)
                db.session.add(new_user)
                db.session.commit()
                flash('Usuario criado com sucesso', 'success')

                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao criar usuario: {str(e)}', 'danger')

        return render_template('form.html')
    
    @app.route('/deleteUser/<int:id>')
    def deleteUser(id):
        userById = User.query.get_or_404(id)
        try:
            db.session.delete(userById)
            db.session.commit()
            flash('Usuario deletado com sucesso', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            db.session.rollback()
            flash(f'Erro ao deletar usuario: {str(e)}', 'danger')
            return redirect(url_for('index'))

    @app.route('/editUser/<int:id>', methods=['GET', 'POST'])
    def editUser(id):
        userById = User.query.get_or_404(id)
        if request.method == 'POST':
            try:
                userById.nome = request.form['nome']
                userById.email = request.form['email']
                userById.telefone = request.form['telefone']
                userById.cep = request.form['cep']
                userById.dataNascimento = request.form['dataNascimento']
                db.session.commit()
                flash('Usuario atualizado com sucesso', 'success')
                return redirect(url_for('editUser', id=userById.id))
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao deletar usuario: {str(e)}', 'danger')
                print(e)
                return redirect(url_for('editUser', id=userById.id))

        return render_template('formEdit.html', userById=userById)
    
    @app.route('/detalhes/<int:id>')
    def detalhes(id):
        userById = User.query.get_or_404(id)

        return render_template('detalhes.html', userById=userById)
    
    @app.route('/login', methods=['POST'])
    def login():
        nome = request.form['nome']
        email = request.form['email']
        userFirst = User.query.filter_by(email=email).first()
        if userFirst and userFirst.nome == nome :
            session['user'] = email
            print(session)
            flash('Logado com sucesso', 'success')
        else:
            print('nada ainda')
            flash('Email ou nome esta errado', 'danger')
    
        return redirect(url_for('index'))

    @app.route('/logout')
    def logout():
        session.pop('user', None)
        flash('Logout com sucesso', 'success')
        return redirect(url_for('index'))
    


    if __name__ == "__main__":
        app.run(debug=True)

