# cv-flask
## Description
cv-flask is a Python Flask project which can be run on a desktop or server with REST API endpoints to fetch all CV data from Erwin Mintiens.
cv-flask also has a web view with all present CV data.

## Tests and development

This application was created and tested on Arch Linux, with Python 3.10.1.

## Installation
### Prerequisites

Python should be installed on your system in order to be able to run this program. Instructions on how to install Python can be found [here](https://www.python.org/downloads/).

#### Option 1: Git command
Install git on your system with one of the following commands:

| Distribution | Command |
| ------------- | ------------- |
| Arch Linux | ```sudo pacman -S git``` |
| Debian/Ubuntu | ```sudo apt-get install git``` |
| Fedora | ```yum install git``` (up to Fedora 21)<br>```dnf install git``` (Fedora 22 and later) |
| openSUSE | ```zypper install git``` |
| Windows | Download and install [Git for Windows](https://git-scm.com/download/win) |

Check if git is installed correctly with the commmand ```git --version``` in your terminal.
The output should look like this:

```
erwin@arch$ git --version
git version 2.34.1
```

Clone this repository to your local computer with the command ```git clone https://github.com/erwinmintiens/cv-flask.git```.

#### Option 2: Download zip

Click on the button "Code" and select the option "Download ZIP" from the dropdown menu. Save the zip file at your desired location and unzip this file.

#### Install required Python packages

Navigate to your unzipped (or cloned) folder and create a virtual environment with command:

```python3 -m venv venv``` (Linux)

``` python -m venv venv``` (Windows)

Activate the newly created virtual environment with command:

```source ./venv/bin/activate``` (Linux)

``` venv\Scripts\activate``` (Windows)

Install the required packages with command:

```pip install -r requirements.txt```

## Usage

Be sure to run all commands below while the virtual environment is active.

### Running the application as a REST API

#### Linux

Run the application by executing ```python3 -m flask run```. You should see something like this:

``` bash
(venv) erwin@arch ~/Testing/cv-flask-main$ python3 -m flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

which shows that the application is successfully running on port 5000.

#### Windows

Run the flask application by executing ```flask run```. You should see something like this:

```
(venv) >flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

which shows that the application is successfully running on port 5000.

#### Endpoints

GET calls can now be made to:
- ```http://localhost:5000/personal```
- ```http://localhost:5000/experience```
- ```http://localhost:5000/education```
- ```http://localhost:5000/courses_specialties_certifications```
- ```http://localhost:5000/projects```
- ```http://localhost:5000/skills```
- ```http://localhost:5000/references```

Which will return the requested info in JSON format.

#### Web view

While the application runs, a web page version of the CV can be found by requesting the URL ```http://localhost:5000/web/index``` in the browser.

### Getting info via a CLI command

All CV info can be printed out on the terminal by using the command:

#### Linux

```python3 -m flask print-cv```

#### Windows

```flask print-cv```
