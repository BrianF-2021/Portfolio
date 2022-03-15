# from flask_app import app
# from flask import render_template,redirect,request,session,flash
from my_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.user import User
from my_app import app
from flask import render_template, redirect, request, session
from my_app.models import user as usr, painting


@app.route('/painting/add')
def add_painting():
    if 'id' not in session:
        return redirect('/')
    return render_template('painting_add_form.html')


@app.route("/painting/creating", methods = ["POST"])
def painting_creating():
    if 'id' not in session:
        return redirect('/')
    print("request.form:",request.form)
    if not painting.Painting.validate_painting(request.form):
        return redirect('/painting/add')
    user_id = session['id']
    print('user id', user_id)
    data = {
        'title' : request.form['title'],
        'description' : request.form['description'],
        'price' : request.form['price'],
        'user_id' : user_id,
    }
    print("painting data", data)
    painting_id = painting.Painting.save_painting(data)
    print('SAVED TREE ID', painting_id)
    return redirect('/user/home')


@app.route("/painting/info/<int:painting_id>")
def view_painting(painting_id):
    if 'id' not in session:
        return redirect('/')
    painting_id_data = {'id': painting_id}
    data = {'id': painting_id}
    this_painting = painting.Painting.get_painting_with_user(painting_id_data)
    user_id = { 'id' :session['id']}
    print('USER_ID', user_id)
    print('THIS_PAINTING ID', painting_id_data)
    user = usr.User.get_one(user_id)
    return render_template('painting_info.html', user = user, this_painting = this_painting)



@app.route("/painting/edit/<int:painting_id>")
def painting_edit(painting_id):
    if 'id' not in session:
        return redirect('/')
    print('painting id', painting_id)
    id = session['id']
    print('user id', id)
    user_id = {
        'id': id
    }
    user = usr.User.get_one(user_id)
    print('user', user)
    id = {
        'id':painting_id,
    }
    print('PAINTING ID', id)
    this_painting = painting.Painting.get_one_painting(id)
    return render_template('painting_edit_form.html', user = user, this_painting = this_painting)


@app.route("/painting/editing/<int:painting_id>", methods = ["POST"])
def painting_editing(painting_id):
    if 'id' not in session:
        return redirect('/')
    print("request.form:",request.form)
    if not painting.Painting.validate_painting(request.form):
        return redirect(f'/painting/edit/{painting_id}')
    user_id = session['id']
    # print('user id', user_id)
    # print('reason: ', request.form['reason'])
    data = {
        'id' : painting_id,
        'title' : request.form['title'],
        'description' : request.form['description'],
        'price' : request.form['price'],
        'user_id' : user_id,
    }
    print("painting data", data)
    painting.Painting.update_painting(data)
    return redirect('/user/home')


@app.route("/painting/destroy/<int:painting_id>")
def painting_destroy(painting_id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id':painting_id
    }
    print('painting id', painting_id)
    painting.Painting.delete_painting(data)
    return redirect('/user/home')
