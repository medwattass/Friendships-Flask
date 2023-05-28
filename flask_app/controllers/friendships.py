from flask_app import app
from flask import redirect, render_template,request
from ..models.user import User
from ..models.friend import Friend


@app.route('/' )
def index():
    return redirect('/friendships')

@app.route('/friendships', methods=['GET','POST'])
def users_with_friends():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        data = {'id': user_id}
        non_friends = User.non_friends(data)
    else:
        user_id = None
        non_friends = []
    return render_template('friendships.html', users_with_friends=Friend.get_all_users_with_friends(), users=User.get_all_users(), user_id=user_id)


@app.route('/friendships/create_user',methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname']
    }
    user_id = User.save(data)
    return redirect('/friendships')

@app.route('/friendships/create_friendship',methods=['POST'])
def create_friendship():
    data = {
        'u_id': request.form.get('user_id'),
        'f_id': request.form.get('friend_id')
    }
    friendship_result = Friend.save_f(data)
    
    return redirect('/friendships')
