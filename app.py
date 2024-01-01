from flask import render_template, url_for, request, redirect
from models import db, Project, app
import datetime


# CLEANER FUNCTIONS

def clean_date(date_str):
    date_split = date_str.split('-')
    year = int(date_split[0])
    month = int(date_split[1])
    return datetime.date(year, month, 1)


def month_string(month):
    str_month = month.strftime('%B %Y')
    return str_month


def display_month(month):
    updated_month = month.strftime('%Y-%m')
    return updated_month


def skills_list(skills):
    skills_split = skills.split(', ')
    return skills_split



# ROUTES

@app.route('/')
def index():
    projects = Project.query.all()

    return render_template('index.html', projects=projects)


@app.route('/projects/<id>')
def project_details(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    project.date = month_string(project.date)
    project.skills = skills_list(project.skills)

    return render_template('detail.html', project=project, projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new():
    projects = Project.query.all()

    if request.form:
        new_project = Project(name=request.form['title'], date=request.form['date'],
                              description=request.form['desc'], skills=request.form['skills'],
                              link=request.form['github'])
        new_project.date = clean_date(new_project.date)
        db.session.add(new_project)
        db.session.commit()
        print('item committed')
        return redirect( url_for('index'))

    return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def update(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)

    if request.form:
        project.name = request.form['title']
        project.date = clean_date(request.form['date'])
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.link = request.form['github']
        db.session.commit()

        return redirect( url_for('index') )

    project.date = display_month(project.date)


    return render_template('editform.html', project=project, projects=projects)


@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()

    return redirect( url_for('index') )


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5500, host='127.0.0.1')

        