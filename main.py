from flask import Flask
from data.db_session import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init('db/meloch.sqlite')
    app.run()


if __name__ == '__main__':
    main()