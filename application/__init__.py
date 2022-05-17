from flask import Flask
from flask_cors import CORS
from flask_restful import Api


#from models import db
#from config import Config

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from config import db, ma, Config


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/db.sqlite'
app.config.from_object(Config)



db.init_app(app)

#db.drop_all() #todo remove or comment?
#db.create_all()#

#db.session.add(Post(user_id=1, title='xxx', body='xxxxxx'))
#db.session.add(Post(user_id=2, title='ff', body='s'))
#db.session.commit()

        
api = Api(app)

from application.resources.postsapi import PostsAPI

api.add_resource(PostsAPI, '/api/posts/')

