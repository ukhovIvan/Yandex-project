from flask import jsonify
from flask_restful import reqparse, abort, Resource
from datetime import datetime
from data.models.batch import Batch
from data.db_session import create_session

parser = reqparse.RequestParser()
parser.add_argument('order_id', required=True)
parser.add_argument('culture_id', required=True)
parser.add_argument('count', required=True)
parser.add_argument('end_date', required=True)


class BatchResource(Resource):
    def get(self, batch_id):
        abort_if_batch_not_found(batch_id)
        session = create_session()
        batch = session.query(Batch).get(batch_id)
        return jsonify({'batch': batch.to_dict(
            only=('order.buyer.name', 'culture.name', 'count', 'start_date', 'end_date', 'status_real'))})

    def delete(self, batch_id):
        abort_if_batch_not_found(batch_id)
        session = create_session()
        batch = session.query(Batch).get(batch_id)
        session.delete(batch)
        session.commit()
        return jsonify({'success': 'OK'})


class BatchListResource(Resource):
    def get(self):
        session = create_session()
        batches = session.query(Batch).all()
        return jsonify({'batches': [item.to_dict(
            only=('culture.name', 'count', 'end_date', 'status_real')) for item in batches]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        batch = Batch(
            order_id=args['order_id'],
            culture_id=args['culture_id'],
            count=args['count'],
            start_date=str(datetime.now()),
            end_date=args['end_date'],
            status_view='accepted',
            status_real='accepted'
        )
        session.add(batch)
        session.commit()
        return jsonify({'id': batch.id})


def abort_if_batch_not_found(batch_id):
    session = create_session()
    batch = session.query(Batch).get(batch_id)
    if not batch:
        abort(404, message=f"Culture {batch_id} not found")