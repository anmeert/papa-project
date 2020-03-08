from app import app, db
from app.models import User, Job, Model, Energy

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Job': Job, 'Model': Model, 'Energy': Energy}
