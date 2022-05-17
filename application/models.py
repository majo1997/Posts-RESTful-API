from marshmallow_sqlalchemy import auto_field

from application import ma, db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)


class PostSchema(ma.SQLAlchemyAutoSchema):
    user_id = auto_field(data_key='userId')

    class Meta:
        model = Post
        #load_instance = True
        #sqla_session = db.session
        fields = ('id', 'user_id', 'title', 'body')
        ordered = True


post_schema = PostSchema()
posts_schema = PostSchema(many=True)
