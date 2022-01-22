from cv import generate_cv
from flask import Flask, jsonify, render_template, make_response

__author__ = 'Erwin Mintiens'
__version__ = '0.0.1'

app = Flask(__name__)
cv = generate_cv()


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


@app.route('/website/index', methods=['GET'])
def website_index():
    return render_template('index.html')


@app.route('/website/personal', methods=['GET'])
def website_personal():
    name, address, email, telephone, birth_date, birth_place, sex, marital_status, nationality, drivers_licence, \
    dutch_skill, english_skill, french_skill = get_personal_details()

    return render_template('personal.html', name=name, address=address, email=email, telephone=telephone,
                           birth_date=birth_date, birth_place=birth_place, sex=sex, marital_status=marital_status,
                           nationality=nationality, drivers_licence=drivers_licence, dutch_skill=dutch_skill,
                           english_skill=english_skill, french_skill=french_skill)


@app.route('/website/education', methods=['GET'])
def website_education():
    level, value, from_when, until_when, place = get_education_from_xml()

    course, math = value.split(" - ")

    return render_template('education.html', level=level, course=course, math=math, place=place, from_when=from_when,
                           until_when=until_when)


@app.route('/website/experience', methods=['GET'])
def website_experience():
    companies, froms, tos, functions, addresses = get_experience_from_xml()

    return render_template('experience.html', companies=companies, functions=functions, froms=froms, tos=tos,
                           addresses=addresses, length=len(companies))


@app.route('/website/courses_specialties_certifications', methods=['GET'])
def website_courses_specialties_certifications():
    kinds, names, timeframes, companies = get_courses_specialties_certifications_from_xml()
    return render_template('courses_specialties_certifications.html', kinds=kinds, names=names, timeframes=timeframes,
                           companies=companies, length=len(kinds))


@app.route('/website/projects', methods=['GET'])
def website_projects():
    names, descriptions, functions, timeframes = get_projects_from_xml()
    return render_template('projects.html', names=names, descriptions=descriptions, functions=functions,
                           timeframes=timeframes, length=len(names))


@app.route('/website/skills', methods=['GET'])
def website_skills():
    names, levels = get_skills_from_xml()
    return render_template('skills.html', names=names, levels=levels, length=len(names))


@app.route('/website/references', methods=['GET'])
def website_references():
    names, links = get_references_from_xml()
    return render_template('references.html', names=names, links=links, length=len(names))


def get_path_value(path: str) -> str:
    return cv.find(path).text


def get_personal_details() -> tuple:
    name = get_path_value('personal/name')
    address = get_path_value('personal/address')
    email = get_path_value('personal/email_address')
    telephone = get_path_value('personal/telephone')
    birth_date = get_path_value('personal/birthday/date')
    birth_place = get_path_value('personal/birthday/place')
    sex = get_path_value('personal/sex')
    marital_status = get_path_value('personal/marital_status')
    nationality = get_path_value('personal/nationality')
    drivers_licence = get_path_value('personal/drivers_licence')
    dutch_skill = get_path_value('personal/languages/dutch')
    english_skill = get_path_value('personal/languages/english')
    french_skill = get_path_value('personal/languages/french')

    return name, address, email, telephone, birth_date, birth_place, sex, marital_status, nationality, \
           drivers_licence, dutch_skill, english_skill, french_skill


def get_experience_from_xml() -> tuple:
    prefix = 'experience/job'
    companies = [x.text for x in cv.findall(f'{prefix}/company')]
    froms = [x.text for x in cv.findall(f'{prefix}/from')]
    tos = [x.text for x in cv.findall(f'{prefix}/to')]
    functions = [x.text for x in cv.findall(f'{prefix}/function')]
    addresses = [x.text for x in cv.findall(f'{prefix}/address')]
    return companies, froms, tos, functions, addresses


def get_education_from_xml() -> tuple:
    prefix = 'educations/education'
    level = get_path_value(f'{prefix}/level')
    value = get_path_value(f'{prefix}/value')
    from_when = get_path_value(f'{prefix}/from')
    until_when = get_path_value(f'{prefix}/to')
    place = get_path_value(f'{prefix}/place')

    return level, value, from_when, until_when, place


def get_courses_specialties_certifications_from_xml() -> tuple:
    prefix = 'courses_specialties_certifications/course_specialty_certification'
    kinds = [x.text for x in cv.findall(f'{prefix}/kind')]
    names = [x.text for x in cv.findall(f'{prefix}/name')]
    timeframes = [x.text for x in cv.findall(f'{prefix}/timeframe')]
    companies = [x.text for x in cv.findall(f'{prefix}/company')]

    return kinds, names, timeframes, companies


def get_projects_from_xml() -> tuple:
    prefix = 'projects/project'
    names = [x.text for x in cv.findall(f'{prefix}/name')]
    descriptions = [x.text for x in cv.findall(f'{prefix}/description')]
    functions = [x.text for x in cv.findall(f'{prefix}/function')]
    timeframes = [x.text for x in cv.findall(f'{prefix}/timeframe')]

    return names, descriptions, functions, timeframes


def get_skills_from_xml() -> tuple:
    prefix = 'skills/skill'
    names = [x.text for x in cv.findall(f'{prefix}/name')]
    levels = [x.text for x in cv.findall(f'{prefix}/level')]

    return names, levels


def get_references_from_xml() -> tuple:
    prefix = 'references/reference'
    names = [x.text for x in cv.findall(f'{prefix}/name')]
    links = [x.text for x in cv.findall(f'{prefix}/link')]

    return names, links


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=59876)
