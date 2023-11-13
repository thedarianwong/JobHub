from flask import Flask, jsonify
from extensions import db
from models import Job

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../database/JobBoard.db'
db.init_app(app)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

if __name__ == '__main__':
    app.run(debug=True)

