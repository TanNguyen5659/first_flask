from flask import request
from app import app
from uuid import uuid4
from db import posts, cars

@app.post('/post')
def create_post():
    post_data = request.get_json()
    if post_data['vehicle'] not in cars:
        return {"message" : "user does not exist"}, 400
    post_id = uuid4().hex
    posts[post_id] = post_data
    return {'message' : "Post created",
            'post-id' : post_id
            }, 201

@app.get('/post')
def get_posts():
    try:
        return list(posts.values()), 200
    except:
        return {"message" : "FAILED to get post"},400

@app.get('/post/<post_id>')
def get_ind_post(post_id):
    if post_id in posts:
        return posts[post_id], 200
    return {'message' : 'invalid post'}, 400

@app.put('/post')
def update_post():
    post_data = request.get_json()
    
    if post_data['vehicle'] in posts:

        posts[post_data['vehicle']] = {k:v for k,v in post_data.items() if k!= 'vehicle'}

        return {'message' : f"post: {post_data['vehicle']} updated"},201
    
    return {'message' : "invalid post"}, 400

@app.delete('/post')
def delete_post():
    post_data = request.get_json()
    post_id = post_data['vehicle']

    if post_id not in posts:
        return {'message' : "invalid post"}, 400
    
    posts.pop(post_id)
    return {'message' : f'Post: {post_id} deleted'}


