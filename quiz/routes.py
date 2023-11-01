from quiz import app
from flask import render_template, redirect, url_for, flash, request, session
from quiz.models import User, Question
from quiz.forms import RegisterForm, QuizForm, LoginForm
from quiz import db
from flask_login import login_user, current_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    session['points'] = 0
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! Please Log in.', 'success')
        return redirect(url_for('login_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f' There was error with creating an account! {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            session['points'] = 0
            flash('Login succesful!', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccesful! Please check your username and password', category='danger')

    return render_template('login.html', form=form)


@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def quiz_page(id):
    if id > Question.query.count():
        return redirect(url_for('results_page'))
    form = QuizForm()
    ques = Question.query.filter_by(question_id=id).first()
    form.question.choices = [ques.answer1, ques.answer2, ques.answer3]
    if request.method == 'POST':
        if request.form['question'] == ques.correct_answer:
            session['points'] += 10
        return redirect(url_for('quiz_page', id=id+1))

    return render_template('quiz.html', form=form, ques=ques)


@app.route('/results')
def results_page():
    current_user.points = session['points']
    db.session.commit()
    users = User.query.all()
    return render_template('results.html', users=users)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
