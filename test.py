from flask import Flask
import json
from flask import abort
from flask import make_response

app = Flask(__name__)


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


@app.route('/todo/list/<int:task_id>', methods=['GET'])
def index(task_id):
    ts = [task for task in tasks if task['id'] == task_id]
    if len(ts) == 0:
        abort(404)
    return json.dumps(ts[0])


@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(json.dumps({'error':'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

