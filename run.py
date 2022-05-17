from os import environ
from application import app

if __name__ == '__main__':
    #print(environ)
    port = int(environ.get("FLASK_RUN_PORT", 5000))
    host = environ.get("FLASK_RUN_HOST", '0.0.0.0')
    app.run(host=host, port=port)
