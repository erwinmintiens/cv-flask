from flask import Flask, jsonify, make_response
import click
from flask.cli import with_appcontext
import json
from web import *

__author__ = 'Erwin Mintiens'
__version__ = '0.0.1'

app = Flask(__name__)
app.register_blueprint(web_views, url_prefix='/web')


@click.command(name='print-cv')
@with_appcontext
def print_cv():
    titles = ('Personal Details', 'Education', 'Experience', 'Courses, Specialties and Certifications', 'Projects',
              'Skills', 'References')
    personal_data = json.loads(personal().data)
    experience_data = json.loads(experience().data)
    education_data = json.loads(education().data)
    courses_specialties_certifications_data = json.loads(courses_specialties_certifications().data)
    projects_data = json.loads(projects().data)
    skills_data = json.loads(skills().data)
    references_data = json.loads(references().data)
    data_list = (personal_data, experience_data, education_data, courses_specialties_certifications_data,
                 projects_data, skills_data, references_data)
    for index, data in enumerate(data_list):
        print(f'---------- {titles[index]} ----------')
        print(json.dumps(data, indent=4))


app.cli.add_command(print_cv)


# Test API by getting root
@app.route('/', methods=['GET'])
def home():
    return make_response(jsonify({'Status': 'Success'}), 200)


@app.route('/personal', methods=['GET'])
def personal():
    name, address, email, telephone, birth_date, birth_place, sex, marital_status, nationality, drivers_licence, \
    dutch_skill, english_skill, french_skill = get_personal_details()

    return make_response(jsonify({
        "Name": name,
        "Address": address,
        "Email address": email,
        'Telephone': telephone,
        'Birth date': birth_date,
        'Birth place': birth_place,
        'Sex': sex,
        'Marital status': marital_status,
        'Nationality': nationality,
        'Drivers licence': drivers_licence,
        'Languages': {
            'Dutch': dutch_skill,
            'English': english_skill,
            'French': french_skill
        }
    }), 200)


@app.route('/experience', methods=['GET'])
def experience():
    companies, froms, tos, functions, addresses = get_experience_from_xml()
    dictionary = dict()
    for index, value in enumerate(companies):
        dictionary[value] = {
            'Function': functions[index],
            'From': froms[index],
            'To': tos[index],
            'Address': addresses[index]
        }
    return make_response(jsonify(dictionary), 200)


@app.route('/education', methods=['GET'])
def education():
    level, value, from_when, until_when, place = get_education_from_xml()

    return make_response(jsonify({
        'Level': level,
        'Course': value,
        'From': from_when,
        'To': until_when,
        'Place': place
    }), 200)


@app.route('/courses_specialties_certifications', methods=['GET'])
def courses_specialties_certifications():
    kinds, names, timeframes, companies = get_courses_specialties_certifications_from_xml()
    dictionary = dict()
    for index, value in enumerate(names):
        dictionary[value] = {
            'Kind': kinds[index],
            'Timeframe': timeframes[index],
            'Issuing company': companies[index]
        }
    return make_response(jsonify(dictionary), 200)


@app.route('/projects', methods=['GET'])
def projects():
    names, descriptions, functions, timeframes = get_projects_from_xml()
    dictionary = dict()
    for index, value in enumerate(names):
        dictionary[value] = {
            'Description': descriptions[index],
            'Function': functions[index],
            'Timeframe': timeframes[index]
        }
    return make_response(jsonify(dictionary), 200)


@app.route('/skills', methods=['GET'])
def skills():
    names, levels = get_skills_from_xml()
    dictionary = dict()
    for index, name in enumerate(names):
        dictionary[name] = levels[index]
    return make_response(jsonify(dictionary), 200)


@app.route('/references', methods=['GET'])
def references():
    names, links = get_references_from_xml()
    dictionary = dict()
    for index, name in enumerate(names):
        dictionary[name] = links[index]
    return make_response(jsonify(dictionary), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
