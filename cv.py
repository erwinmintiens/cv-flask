import xml.etree.ElementTree as ET


def add_job(superelement: ET.Element, from_when: str, until_when: str, company_name: str, function,
            address: str) -> None:
    job = ET.SubElement(superelement, 'job')

    job_from = ET.SubElement(job, 'from')
    job_to = ET.SubElement(job, 'to')
    job_company = ET.SubElement(job, 'company')
    job_function = ET.SubElement(job, 'function')
    job_address = ET.SubElement(job, 'address')

    job_from.text = from_when
    job_to.text = until_when
    job_company.text = company_name
    job_function.text = function
    job_address.text = address


def add_courses_specialties_certifications(superelement: ET.Element, kind: str, name: str, timeframe: str,
                                           company: str) -> None:
    course_specialty_certification = ET.SubElement(superelement, 'course_specialty_certification')

    course_specialty_certification_kind = ET.SubElement(course_specialty_certification, 'kind')
    course_specialty_certification_name = ET.SubElement(course_specialty_certification, 'name')
    course_specialty_certification_time = ET.SubElement(course_specialty_certification, 'timeframe')
    course_specialty_certification_company = ET.SubElement(course_specialty_certification, 'company')

    course_specialty_certification_kind.text = kind
    course_specialty_certification_name.text = name
    course_specialty_certification_time.text = timeframe
    course_specialty_certification_company.text = company


def add_project(superelement: ET.Element, name: str, description: str, function: str, timeframe: str) -> None:
    project = ET.SubElement(superelement, 'project')

    project_name = ET.SubElement(project, 'name')
    project_description = ET.SubElement(project, 'description')
    project_function = ET.SubElement(project, 'function')
    project_time = ET.SubElement(project, 'timeframe')

    project_name.text = name
    project_description.text = description
    project_function.text = function
    project_time.text = timeframe


def add_skill(superelement: ET.Element, name: str, level: str, category: str) -> None:
    skill = ET.SubElement(superelement, 'skill')
    skill.set('category', category)

    skill_name = ET.SubElement(skill, 'name')
    skill_level = ET.SubElement(skill, 'level')

    skill_name.text = name
    skill_level.text = level


def add_reference(superelement: ET.Element, name: str, link: str) -> None:
    reference = ET.SubElement(superelement, 'reference')

    reference_name = ET.SubElement(reference, 'name')
    reference_link = ET.SubElement(reference, 'link')

    reference_name.text = name
    reference_link.text = link


# Generate CV XML file
def generate_cv():
    root = ET.Element('cv')
    personal = ET.SubElement(root, 'personal')
    experience = ET.SubElement(root, 'experience')
    educations = ET.SubElement(root, 'educations')
    courses_specialties_certifications = ET.SubElement(root, 'courses_specialties_certifications')
    projects = ET.SubElement(root, 'projects')
    skills = ET.SubElement(root, 'skills')
    references = ET.SubElement(root, 'references')

    # Personal
    name = ET.SubElement(personal, 'name')
    name.text = 'Erwin Maria Mintiens'

    address = ET.SubElement(personal, 'address')
    address.text = 'Bampsstraat 2, 3540 Herk-de-Stad'

    email = ET.SubElement(personal, 'email_address')
    email.text = 'erwin.mintiens@gmail.com'

    telephone = ET.SubElement(personal, 'telephone')
    telephone.text = '+32 494 68 91 05'

    birth = ET.SubElement(personal, 'birthday')
    birth_date = ET.SubElement(birth, 'date')
    birth_date.text = '23-05-1995'
    birth_place = ET.SubElement(birth, 'place')
    birth_place.text = 'Leuven, Belgium'

    sex = ET.SubElement(personal, 'sex')
    sex.text = 'Male'

    marital_status = ET.SubElement(personal, 'marital_status')
    marital_status.text = 'Unmarried'

    nationality = ET.SubElement(personal, 'nationality')
    nationality.text = 'Belgian'

    drivers_licence = ET.SubElement(personal, 'drivers_licence')
    drivers_licence.text = 'B'

    languages = ET.SubElement(personal, 'languages')
    dutch = ET.SubElement(languages, 'dutch')
    english = ET.SubElement(languages, 'english')
    french = ET.SubElement(languages, 'french')

    dutch.text = '*****'
    english.text = '****'
    french.text = '**'

    # Education
    education = ET.SubElement(educations, 'education')
    education_level = ET.SubElement(education, 'level')
    education_from = ET.SubElement(education, 'from')
    education_to = ET.SubElement(education, 'to')
    education_value = ET.SubElement(education, 'value')
    education_place = ET.SubElement(education, 'place')

    education_level.text = 'High School'
    education_from.text = 'September 2007'
    education_to.text = 'June 2013'
    education_value.text = 'Industrial sciences - 8 hours mathematics'
    education_place.text = 'Damiaaninstituut, Aarschot'

    # Experience

    add_job(superelement=experience, from_when='June 2019', until_when='...', company_name='KeySign NV',
            function='Jr. Developer and Support Engineer', address='Veldkant 33a, 2550 Kontich')
    add_job(superelement=experience, from_when='April 2018', until_when='June 2019',
            company_name='Media Markt Machelen', function='Student job: Solutions Corner Expert',
            address='Woluwelaan 11, 1830 Machelen')
    add_job(superelement=experience, from_when='August 2017', until_when='January 2018',
            company_name='Quo Vadis Belgium', function='Solution Support Engineer',
            address='Schaliënhoevedreef 20T, 2800 Mechelen')
    add_job(superelement=experience, from_when='Summer 2012', until_when='Summer 2013',
            company_name='\'t Ydee Aarschot', function='Student job: Waiter',
            address='Bogaardenstraat 3, 3200 Aarschot')

    # Courses, specialties and certifications
    add_courses_specialties_certifications(superelement=courses_specialties_certifications, kind='Certification',
                                           name='PCAP-31-03: Certified Associate in Python Programming',
                                           timeframe='December 2021', company='Python Institute')
    add_courses_specialties_certifications(superelement=courses_specialties_certifications, kind='Course',
                                           name='Python Advanced', timeframe='January 2021 - March 2021',
                                           company='Syntra - Remote')
    add_courses_specialties_certifications(superelement=courses_specialties_certifications, kind='Course',
                                           name='Basics course Python', timeframe='October 2020 - November 2020',
                                           company='SBM - Thomas More, Geel')
    add_courses_specialties_certifications(superelement=courses_specialties_certifications, kind='Course',
                                           name='3-day course: Thales PayShield 10k payment HSM',
                                           timeframe='October 2019', company='Thales - Madrid')
    add_courses_specialties_certifications(superelement=courses_specialties_certifications, kind='Course',
                                           name='5-day course: Linux Professional',
                                           timeframe='November 2017 - December 2017', company='SBM - Wijgmaal')

    # Projects
    add_project(superelement=projects, name='Python package: signinghubapi',
                description='signinghubapi is a Python package which integrates with the SigningHub REST API',
                function='Development and maintenance', timeframe='June 2021 - ...')
    add_project(superelement=projects, name='Gatekeeper',
                description='The gatekeeper project is a Python Flask project which communicates with the SigningHub '
                            'REST API to insert an approver in a workflow if workflows are shared with certain '
                            'recipients. The gatekeeper project is an expansion upon the QR project.',
                function='Development and maintenance', timeframe='Februari 2021 - ...')
    add_project(superelement=projects, name='O365',
                description='O365 is a Python Flask project which acts as a translation layer between the Datapower at '
                            'the Flemish Government and their dedicated SigningHub environment to translate their '
                            'access token obtained from the Datapower to an access token obtained from SigningHub.',
                function='Development and maintenance', timeframe='November 2020 - ...')
    add_project(superelement=projects, name='QR',
                description='The QR project is the base of the Gatekeeper project. This project adds QR codes to '
                            'documents shared within certain enterprises, and pushes these documents to a digital '
                            'archive at Zeticon. The goal of this project is verifying the validity of the signatures '
                            'upon these documents.',
                function='Development and maintenance', timeframe='November 2020 - ...')
    add_project(superelement=projects, name='PayShield 10k payment HSM',
                description='Installation and initial setup of PayShield 10k HSM in high availability for Monizze.',
                function='Setup and installation', timeframe='May 2020')
    add_project(superelement=projects, name='SigningHub API Client',
                description='A tool with GUI written for Cronos Public Services which merges given Word files and an '
                            'Excel file, and uploads these documents to SigningHub by communicating with '
                            'SigningHub\'s REST API.',
                function='Development and maintenance', timeframe='November 2019 - ...')
    add_project(superelement=projects, name='Jira and Confluence',
                description='Setup of the KeySign servicedesk, together with Jira Core, Software and Confluence on a '
                            'Linux server.',
                function='Installation and administration', timeframe='September 2019 - ...')

    # Skills
    add_skill(superelement=skills, name='Python', level='Advanced', category='programming')
    add_skill(superelement=skills, name='Java', level='Basic', category='programming')
    add_skill(superelement=skills, name='JavaScript', level='Elementary', category='programming')

    add_skill(superelement=skills, name='Linux Server/Desktop', level='Basic', category='computer')
    add_skill(superelement=skills, name='Windows Server/Desktop', level='Basic', category='computer')
    add_skill(superelement=skills, name='Luna HSM', level='Basic', category='computer')
    add_skill(superelement=skills, name='PayShield 10k HSM', level='Advanced', category='computer')
    add_skill(superelement=skills, name='Jira (Software, Service Desk, Admin)', level='Advanced', category='computer')
    add_skill(superelement=skills, name='SigningHub', level='Advanced', category='computer')
    add_skill(superelement=skills, name='ADSS', level='Advanced', category='computer')
    add_skill(superelement=skills, name='Microsoft Office', level='Advanced', category='computer')
    add_skill(superelement=skills, name='Cell phone reparation', level='Advanced', category='other')

    add_skill(superelement=skills, name='Problem Solving', level='', category='interpersonal')
    add_skill(superelement=skills, name='Customer Support', level='', category='interpersonal')



    # References
    add_reference(references, name='GitHub', link='https://github.com/erwinmintiens')
    add_reference(references, name='LinkedIn', link='https://www.linkedin.com/in/erwinmintiens')
    add_reference(references, name='Stackoverflow', link='https://stackoverflow.com/users/8689498/erwin')

    return root


if __name__ == '__main__':
    xml = ET.ElementTree(generate_cv())
    xml.write('xml.xml')
