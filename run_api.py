from api import api, db
from app.models import Job, User, Model, Energy

@api.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Job': Job, 'Model': Model, 'Energy': Energy}

if __name__ == '__main__':
    api.run(debug=True, port=1234)