from flask import Flask, render_template, request
import json

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
    with open('model/data.json', 'r') as file: # open a file in read only way
        breeds = json.load(file) # read the data and assign it to a variable

        # read the users preferred values
        user_active_value = int(result['active'])
        user_shedding_value = int(result['shedding'])
        user_aggression_value = int(result['aggression'])
        user_space_value = int(result['space'])
        user_time_commitment_value = int(result['time_commitment'])

        # do a for loop of all the breeds and calculate how far each trait if from users preferred values
        for i, breed in enumerate(breeds):
            breed_name = breed["name"]
            breed_active_value = breed["active"]
            breed_shedding_value = breed["shedding"]
            breed_aggression_value = breed["aggression"]
            breed_space_value = breed["space"]
            breed_time_commitment_value = breed["time_commitment"]
            print(f"Breed: {breed_name}")
            active_distance = abs((breed_active_value - user_active_value) / user_active_value)
            shedding_distance = abs((breed_shedding_value - user_shedding_value) / user_shedding_value)
            aggression_distance = abs((breed_aggression_value - user_aggression_value) / user_aggression_value)
            space_distance = abs((breed_space_value - user_space_value) / user_space_value)
            time_commitment_distance = abs((breed_time_commitment_value - user_time_commitment_value) / user_time_commitment_value)
            breeds[i]["match"] = (active_distance + shedding_distance + aggression_distance + space_distance + time_commitment_distance)
        # sort the values such that the closest value is first
        breeds = sorted(breeds, key=lambda x: x["match"])
    return render_template('discover.html',
                           breeds=breeds,
                           active=user_active_value,
                           shedding=user_shedding_value,
                           aggression=user_aggression_value,
                           time_commitment=user_time_commitment_value,
                           space=user_space_value,
                           )


@application.route('/match')
def match():
    return render_template('match.html')


@application.route('/discover')
def discover():
    return render_template('discover.html')


if __name__ == '__main__':
    application.run(debug=True)
