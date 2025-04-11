from flask import Flask
from flask_restful import Api
from data.db_session import *
from data.resources.culture_resources import *
from data.resources.batch_resources import *

app = Flask(__name__)
api = Api(app)
api.add_resource(CultureResource, '/api/v1/cultures/<int:culture_id>')
api.add_resource(CultureListResource, '/api/v1/cultures')
api.add_resource(BatchResource, '/api/v1/batches/<int:batch_id>')
api.add_resource(BatchListResource, '/api/v1/batches')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init('db/meloch.sqlite')
    app.run()


if __name__ == '__main__':
    main()