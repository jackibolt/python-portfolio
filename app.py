from flask import render_template, url_for, request, redirect
from models import db, Project, app
import datetime


def clean_date(date_str):
    date_split = date_str.split('-')
    year = int(date_split[0])
    month = int(date_split[1])
    return datetime.date(year, month, 1)



@app.route('/')
def index():
    projects = Project.query.all()

    return render_template('index.html', projects=projects)


@app.route('/detail/<id>')
def project_details(id):
    project = Project.query.get(id)

    return render_template('detail.html', project=project)


@app.route('/new', methods=['GET', 'POST'])
def new():

    print(request.form)

    if request.form:
        new_project = Project(name=request.form['title'], date=request.form['date'],
                              description=request.form['desc'], skills=request.form['skills'],
                              link=request.form['github'])
        new_project.date = clean_date(new_project.date)
        db.session.add(new_project)
        db.session.commit()
        print('item committed')
        return redirect( url_for('index'))

    return render_template('projectform.html')


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):


    return render_template('editform.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5500, host='127.0.0.1')