from flask import Flask, jsonify
from extensions import db
from models import Job
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../database/JobBoard.db'
db.init_app(app)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    jobs_data = [job.to_dict() for job in jobs]
    if jobs_data:
        jobs_data = jobs_data[1:]  # Skip the first row
    return jsonify(jobs_data)

if __name__ == '__main__':
    app.run(debug=True)

