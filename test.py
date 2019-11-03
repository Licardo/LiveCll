from flask import Flask
from flask import request
import json
from flask import abort
from flask import make_response
from db.db_operate import DbOperator
from server.cll_db import CllDB

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


@app.route('/love/orange')
def love():
    return 'I love U Hon By Hao'


@app.route('/todo/list/get_item/<int:page_index>')
def get_item(page_index):
    datas = DbOperator.query(page_index)
    resp = make_response(json.dumps(datas), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/todo/list/get_item/<int:page_min>/<int:page_max>')
def get_item_for_row(page_min, page_max):
    datas = DbOperator.query_for_row(page_min, page_max)
    resp = make_response(json.dumps(datas), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(json.dumps({'error': 'Not Found'}), 404)


# 获取app首页的标题和图片
@app.route('/cll/tab/info')
def get_tab_info():
    datas = CllDB.get_tab_info()
    resp = make_response(json.dumps(datas), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/cll/home/info')
def get_home_info():
    datas = CllDB.get_home_info()
    resp = make_response(json.dumps(datas), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/cll/info', methods=['get', 'post'])
def get_cll_info():
    source = request.args.get('source')
    platform = request.args.get('platform')
    page = request.args.get('page')
    datas = CllDB.get_cll_info(source, platform, page)
    resp = make_response(json.dumps(datas), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(debug=False, host='172.21.0.16', port='8000')

