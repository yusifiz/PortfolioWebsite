from run import app
from flask import redirect, render_template, request

@app.route("/")
def app_index():
    from models import Service
    from models import Work
    
    service = Service.query.all()
    works = Work.query.all()
    return render_template("app/index.html", service=service, works=works)