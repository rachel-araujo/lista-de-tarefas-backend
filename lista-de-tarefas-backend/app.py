from config import app, db
from models import Task

with app.app_context():
    db.create_all()

import routes

if __name__ == '__main__':
    app.run(debug=True)
