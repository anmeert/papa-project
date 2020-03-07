from api import app
from flask import Flask, jsonify, abort

tasks = [
        {
            'model': 1,
            'FoldX': -75.6,
            'InterfaceAnalyzer': -347.0, 
            'ZRANK': -200
        },
        {
            'model': 2,
            'FoldX': -54.6,
            'InterfaceAnalyzer': -350, 
            'ZRANK': -230.5
        }
]

@app.route('/job/api', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/job/api/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['model'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})



if __name__ == '__main__':
    app.run(debug=True)