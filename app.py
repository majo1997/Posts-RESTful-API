from flask import Flask
from flask_restful import Api

from models import db

from resources.postsapi import PostsAPI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'

db.init_app(app)

db.drop_all() #todo remove or comment?
db.create_all()#


db.session.add(Post(user_id=1, title='xxx', body='xxxxxx'))
db.session.add(Post(user_id=2, title='ff', body='s'))
db.session.commit()
        
api = Api(app)

api.add_resource(PostsAPI, '/api/posts/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) # todo debug = False