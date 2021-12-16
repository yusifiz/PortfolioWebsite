from run import app,db
from flask import render_template, redirect, request

@app.route("/adminhome", methods = ["GET","POST"])
def admin():
    from models import Service
    services = Service.query.all()
    if request.method == 'POST':
        service = Service(
            service_title = request.form["service_title"],
            service_description = request.form["service_description"]
        )
        db.session.add(service)
        db.session.commit()
        return redirect("/adminhome")
    return render_template("admin/service.html", services=services)
    
@app.route("/adminhome/delete/<int:id>",methods=["GET","POST"])
def service_delete(id):
    from models import Service
    service = Service.query.filter_by(id=id).first()
    db.session.delete(service)
    db.session.commit()
    return redirect("/adminhome")

@app.route("/adminhome/update/<int:id>", methods= ["GET","POST"])
def service_update(id):
    from models import Service
    service = Service.query.filter_by(id=id).first()
    if request.method == 'POST':
        service = Service.query.filter_by(id=id).first()
        service.service_title = request.form["service_title"]
        service.service_description = request.form["service_description"]
        db.session.commit()
        return redirect("/adminhome")
    return render_template("admin/service-update.html", service=service)


@app.route("/adminhome/works", methods = ["GET","POST"])
def admin_works():
    from models import Work
    import os
    works = Work.query.all()
    if request.method == 'POST':
        file = request.files['work_img']
        filename = file.filename
        file.save(os.path.join("static/uploads/",filename))
        work = Work(
            work_title = request.form["work_title"],
            work_client_name = request.form["work_client_name"],
            work_img = file.save(os.path.join("static/uploads/",filename)),
            work_url = request.form["work_url"]
        )
        db.session.add(work)
        db.session.commit()
        return redirect("/adminhome/works")
    return render_template("admin/works.html", works=works)


@app.route("/adminhome/works/delete/<int:id>")
def works_delete(id):
    from models import Work
    work = Work.query.filter_by(id=id).first()
    db.session.delete(work)
    db.session.commit()
    return redirect("/adminhome/works")

@app.route("/adminhome/works/update/<int:id>", methods= ["GET","POST"])
def works_update(id):
    from models import Work
    works = Work.query.filter_by(id=id).first()
    if request.method == 'POST':
        work = Work.query.filter_by(id=id).first()
        work.work_title = request.form["work_title"]
        work.work_url = request.form["work_url"]
        work.work_client_name = request.form["work_client_name"]
        db.session.commit()
        return redirect("/adminhome/works")
    return render_template("admin/works-update.html", works=works)