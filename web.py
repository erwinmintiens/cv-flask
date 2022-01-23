from flask import Blueprint, render_template
from cv import generate_cv


web_views = Blueprint(__name__, 'web_views')
cv_xml_root = generate_cv()


@web_views.route('/index', methods=['GET'])
def website_index() -> str:
    return render_template('index.html')


@web_views.route('/personal', methods=['GET'])
def website_personal() -> str:
    name, address, email, telephone, birth_date, birth_place, sex, marital_status, nationality, drivers_licence, \
    dutch_skill, english_skill, french_skill = get_personal_details()

    return render_template('personal.html', name=name, address=address, email=email, telephone=telephone,
                           birth_date=birth_date, birth_place=birth_place, sex=sex, marital_status=marital_status,
                           nationality=nationality, drivers_licence=drivers_licence, dutch_skill=dutch_skill,
                           english_skill=english_skill, french_skill=french_skill)


@web_views.route('/education', methods=['GET'])
def website_education() -> str:
    level, value, from_when, until_when, place = get_education_from_xml()
    course, math = value.split(' - ')

    return render_template('education.html', level=level, course=course, math=math, place=place, from_when=from_when,
                           until_when=until_when)


@web_views.route('/experience', methods=['GET'])
def website_experience() -> str:
    companies, froms, tos, functions, addresses = get_experience_from_xml()

    return render_template('experience.html', companies=companies, functions=functions, froms=froms, tos=tos,
                           addresses=addresses, length=len(companies))


@web_views.route('/courses_specialties_certifications', methods=['GET'])
def website_courses_specialties_certifications() -> str:
    kinds, names, timeframes, companies = get_courses_specialties_certifications_from_xml()
    return render_template('courses_specialties_certifications.html', kinds=kinds, names=names, timeframes=timeframes,
                           companies=companies, length=len(kinds))


@web_views.route('/projects', methods=['GET'])
def website_projects() -> str:
    names, descriptions, functions, timeframes = get_projects_from_xml()
    return render_template('projects.html', names=names, descriptions=descriptions, functions=functions,
                           timeframes=timeframes, length=len(names))


@web_views.route('/skills', methods=['GET'])
def website_skills() -> str:
    names, levels = get_skills_from_xml()
    return render_template('skills.html', names=names, levels=levels, length=len(names))


@web_views.route('/references', methods=['GET'])
def website_references() -> str:
    names, links = get_references_from_xml()
    return render_template('references.html', names=names, links=links, length=len(names))


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
    companies = [x.text for x in cv_xml_root.findall(f'{prefix}/company')]
    froms = [x.text for x in cv_xml_root.findall(f'{prefix}/from')]
    tos = [x.text for x in cv_xml_root.findall(f'{prefix}/to')]
    functions = [x.text for x in cv_xml_root.findall(f'{prefix}/function')]
    addresses = [x.text for x in cv_xml_root.findall(f'{prefix}/address')]
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
    kinds = [x.text for x in cv_xml_root.findall(f'{prefix}/kind')]
    names = [x.text for x in cv_xml_root.findall(f'{prefix}/name')]
    timeframes = [x.text for x in cv_xml_root.findall(f'{prefix}/timeframe')]
    companies = [x.text for x in cv_xml_root.findall(f'{prefix}/company')]

    return kinds, names, timeframes, companies


def get_projects_from_xml() -> tuple:
    prefix = 'projects/project'
    names = [x.text for x in cv_xml_root.findall(f'{prefix}/name')]
    descriptions = [x.text for x in cv_xml_root.findall(f'{prefix}/description')]
    functions = [x.text for x in cv_xml_root.findall(f'{prefix}/function')]
    timeframes = [x.text for x in cv_xml_root.findall(f'{prefix}/timeframe')]

    return names, descriptions, functions, timeframes


def get_skills_from_xml() -> tuple:
    prefix = 'skills/skill'
    names = [x.text for x in cv_xml_root.findall(f'{prefix}/name')]
    levels = [x.text for x in cv_xml_root.findall(f'{prefix}/level')]

    return names, levels


def get_references_from_xml() -> tuple:
    prefix = 'references/reference'
    names = [x.text for x in cv_xml_root.findall(f'{prefix}/name')]
    links = [x.text for x in cv_xml_root.findall(f'{prefix}/link')]

    return names, links


def get_path_value(path: str) -> str:
    return cv_xml_root.find(path).text
