from flask import Flask, render_template, request, url_for
import csv

app = Flask(__name__)


@app.route('/')
def display_index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def display_website(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        topic = data["topic"]
        message = data["message"]
        database.write(f'\n{email},{topic},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        topic = data["topic"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,topic,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return render_template('submit_form.html')
    else:
        return render_template('error.html')


@app.errorhandler(404)
def error_page():
    return render_template('error.html')