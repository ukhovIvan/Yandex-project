from flask import jsonify
from flask_restful import reqparse, abort, Resource
from data.models.culture import Culture
from data.db_session import create_session

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('instruction', required=True)


class CultureResource(Resource):
    def get(self, culture_id):
        abort_if_news_not_found(culture_id)
        session = create_session()
        culture = session.query(Culture).get(culture_id)
        return jsonify({'culture': culture.to_dict(
            only=('name', 'instruction'))})

    def delete(self, culture_id):
        abort_if_news_not_found(culture_id)
        session = create_session()
        culture = session.query(Culture).get(culture_id)
        session.delete(culture)
        session.commit()
        return jsonify({'success': 'OK'})


class CultureListResource(Resource):
    def get(self):
        session = create_session()
        cultures = session.query(Culture).all()
        return jsonify({'cultures': [item.to_dict(
            only=('name', 'instruction')) for item in cultures]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        culture = Culture(
            name=args['name'],
            instruction=args['instruction']
        )
        session.add(culture)
        session.commit()
        return jsonify({'id': culture.id})


def abort_if_news_not_found(culture_id):
    session = create_session()
    news = session.query(Culture).get(culture_id)
    if not news:
        abort(404, message=f"Culture {culture_id} not found")