from flask import request, jsonify, json
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4

from models.post_model import PostModel

from . import bp
from schemas import PostSchema
from db import cars, posts

@bp.route('/post/')
class PostList(MethodView):
    
    @bp.arguments(PostSchema)
    @bp.response(201, PostSchema)
    
    def post(self, post_data): 
        try:
        # posts[post_id] = post_data
            post = PostModel()
            post.from_dict(post_data)

            post.save_post()

        # if post_data['author'] not in users:
        #     return {"message": "user does not exist"}, 400
        # post_id = uuid4().hex
        # posts[post_id] = post_data

            return post
        except:
            abort(400, message=f"{post.title} failed to post")

    @bp.response(200, PostSchema(many=True))
    def get(self):
        return PostModel.query.all()

@bp.route('/post/<post_id>')
class Post(MethodView):

    @bp.response(200, PostSchema)
    def get(self, post_id):
        try: 
            return PostModel.query.get(post_id)
        except KeyError:
            abort(400, message="Post not found")

    @bp.arguments(PostSchema)
    @bp.response(201, PostSchema)
    def put(self, post_data, post_id):

        post = PostModel.query.get(post_id)
        if not post:
            abort(400, message = 'post not found')

        if post_data['user_id'] == post.user_id:
            og_user_id = post.user_id
            post.from_dict(post_data)
            post.user_id = og_user_id

            post.save_post()
            return post

    def delete(self, post_id):

        post = PostModel.query.get(post_id)
        if not post:
            abort(400, message = "post not found")
        post.delete_post()
        return {'message': f'Post: {post_id} deleted'}, 200

