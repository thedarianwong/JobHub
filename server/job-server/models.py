from extensions import db

class Job(db.Model):
    __tablename__ = 'jobs'

    title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    job_url = db.Column(db.String(255), nullable=False, primary_key=True)
    site = db.Column(db.String(255))
    company_url = db.Column(db.String(255))
    location = db.Column(db.String(255))
    job_type = db.Column(db.String(255))
    date_posted = db.Column(db.String(255))
    interval = db.Column(db.String(255))
    min_amount = db.Column(db.Float)
    max_amount = db.Column(db.Float)
    currency = db.Column(db.String(255))
    is_remote = db.Column(db.Integer)
    num_urgent_words = db.Column(db.Integer)
    benefits = db.Column(db.Text)
    emails = db.Column(db.Text)
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            'title': self.title,
            'company': self.company,
            'job_url': self.job_url
        }
