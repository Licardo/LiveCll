from flask import Flask
import json
from flask import abort
from flask import make_response
from db import db_operate

app = Flask(__name__)

# 09ca272c1feb245ed8807cadb23dd4e8

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/list/<int:task_id>', methods=['GET'], )
def index(task_id):
    ts = [task for task in tasks if task['id'] == task_id]
    if len(ts) == 0:
        abort(404)
    resp = make_response(json.dumps(ts[0]), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/todo/list/get_item/<int:page_index>')
def get_item(page_index):
    datas = db_operate.DbOperator.query(page_index)
    resp = make_response(json.dumps(datas), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(json.dumps({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

