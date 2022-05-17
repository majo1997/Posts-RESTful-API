from flask_restful import abort, reqparse, Resource

from application.rest import get_post_by_id, get_user_by_id
from application.models import Post, post_schema, posts_schema

from config import db

class PostsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        
        self.reqparse.add_argument('id', type=int)
        self.reqparse.add_argument('userId', type=int)
        self.reqparse.add_argument('title', type=str)
        self.reqparse.add_argument('body', type=str)
        
        super(PostsAPI, self).__init__()
        
    def get(self):
        args = self.reqparse.parse_args()

        id = args['id']
        user_id = args['userId']
                    
        if id is None and user_id is None:
            abort(404)
        
        post_query = Post.query
        if id is not None:
            post_query = post_query.filter_by(id=id)
            if user_id is not None:
                post_query = post_query.filter_by(user_id=user_id)
                
                
            post = post_query.first()

            #raise Exception()
            
            #post = Post.query.get(id) #alebo oboje? a ak je none volaco tak sa nehlada?
            #post = Post.query.filter_by(id=id, user_id=user_id).first()

            #print(post, 'xxxaaaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')#ak nenajde cez get je None, ak cez filterby tak exception # cez one je exc cez first je None
            
            if post is None:
                post = get_post_by_id(id)
                
                if post is None:
                    abort(404)

                post = Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body'])

                db.session.add(post)
                db.session.commit()
                
            return post_schema.dump(post), 200
        elif user_id is not None:
            post_query = post_query.filter_by(user_id=user_id)
            posts = post_query.all()
            
            return posts_schema.dump(list(posts)), 200 # podla poctu kolko ich je? skontrolovat este pocet? ci neni 0?

        abort(404) #todo
        
    def delete(self):
        args = self.reqparse.parse_args()
        
        id = args['id']
        
        post = Post.query.get(id)

        if post is None:
            abort(404) # 'Post with that id doesn\'t exist'
        
        db.session.delete(post)
        db.session.commit()
        
        return post_schema.dump(post), 200 
        
    def put(self):
        args = self.reqparse.parse_args()

        id = args['id']
        title = args['title']
        body = args['body']
        #mozno nemusie byt zadane vsetky argumenty?? hlavne id a este jeden? kontrolovat aj ci je id not None atd... aj user_id atd...
        
        post = Post.query.get(id)

        if post is None:
            abort(404)
        
        if title is not None:
            post.title = title

        if body is not None:
            post.body = body
        
        db.session.add(post)
        db.session.commit()
        
        return post_schema.dump(post), 200

    def post(self):
        args = self.reqparse.parse_args()

        user_id = args['userId']
        title = args['title']
        body = args['body']
        
        if get_user_by_id(user_id) is None:
            abort(404) #todo message: user with that id doesn't exist

        post = Post(user_id=user_id, title=title, body=body)
        db.session.add(post)
        db.session.commit()
        
        return post_schema.dump(post), 201