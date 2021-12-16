from run import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_title = db.Column(db.String(100))
    service_description = db.Column(db.Text())
    
class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_title = db.Column(db.String(100))
    work_client_name = db.Column(db.String(100))
    work_img = db.Column(db.String(250))
    work_url = db.Column(db.String(250))
    