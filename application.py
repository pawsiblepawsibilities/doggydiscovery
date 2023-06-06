from flask import Flask, render_template, request

application = Flask(__name__)


@application.route('/')
@application.route('/home')
def home():
    return render_template('home.html')


@application.route('/about_me')
def about():
    return render_template('about_me.html')


@application.route('/donation')
def donation():
    return render_template('donation.html')


@application.route('/questionnaire', methods=["POST"])
def questionnaire():
    result = request.form
    return render_template('questionnaire.html')


@application.route('/match')
def match():
    return render_template('match.html')


@application.route('/discover')
def discover():
    return render_template('discover.html')


if __name__ == '__main__':
    application.run(debug=True)
