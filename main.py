from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from Post import Post
from store import PostStore

app = Flask(__name__)

posts = [
    Post(id=1,
        photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=100&w=100', 
        name='Sara', 
        body='Lorem Ipsum',
        date='2019-01-01 12:47:29'),
    Post(id=2,
        photo_url='https://images.pexels.com/photos/36483/aroni-arsa-children-little.jpg?cs=srgb&dl=child-girl-little-36483.jpg&fm=jpg', 
        name='Maryam', 
        body='Hello Everyone',
        date='2019-04-11 18:47:29'),
    ]

store = PostStore()
store.add(posts[0])
store.add(posts[1])

app.app_name = 'Blog'
app.current_id = 3

@app.route('/say-hello/<name>')
def foo(name):
    return 'Hello ' + name

@app.route('/')
def home():
    return render_template('index.html', app_name = app.app_name, posts=store.get_all())

@app.route('/posts/<int:id>')
def post_by_id(id):
    post = store.get_by_id(id)
    return render_template('post.html', app_name = app.app_name, post = post)

@app.route('/posts/add', methods=['GET', 'POST'])
def post_add():
    if request.method == 'GET':
        return render_template('post-add.html')
    elif request.method == 'POST':
        date_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        new_post = Post(id = app.current_id,
                        name = request.form['name'],
                        photo_url = request.form['photo_url'],
                        body = request.form['body'],
                        date = date_now)
        store.add(new_post)
        app.current_id += 1
        return redirect(url_for('home'))

@app.route('/posts/update/<int:id>', methods = ['GET', 'POST'])
def post_update(id):
    if request.method == 'GET':
        post = store.get_by_id(id)
        return render_template('post-update.html', post=post)
    elif request.method == 'POST':
        date_now = ''
        update_fields = {
            'name': request.form['name'],
            'photo_url': request.form['photo_url'],
            'body': request.form['body'],
            'date': date_now
        }
        store.update(id, update_fields)
        return redirect(url_for("home"))

@app.route('/posts/delete/<int:id>')
def post_delete(id):
    store.delete(id)
    return redirect(url_for("home"))
