from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=["POST"])
def sms():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    ### create function to get user input and put the rest under a single function to make UI part easier.
    ### create other functions for other diseases if we have time
    def user_input():
        stringval = incoming_msg
        return stringval
    
    if 'good morning' or 'good afternoon' or 'good evening' or 'hello' or 'hey' or 'hi' in incoming_msg:
        # take in values from user input 
        # and submit those values into script 
        # to app.py. figure out permissions error 
        msg.body("Happy to help you.\nEnter your details for the following:\nTotal Pregnancies: \nGlucose levels: \nBlood Pressure: \nSkin Thickness: \nInsulin: \nBMI: \nDiabetes Pedigree Function: \nAge: ")

    elif 'exit' or 'clear' or 'bye' in incoming_msg:
        msg.body("Glad to be of service.\nHave a nice day.")

    elif 'who made you' in incoming_msg:
        msg.body("A group of students trying to make a change. (We can only do so much for now, but we hope to do more)")

    elif "who are you" in incoming_msg:
        msg.body("If you've seen Big Hero 6, you can think of me as your virtual Baymax. Otherwise, you can simply think of me as a personal healthcare assistant that you can text when you're feeling off.")

    elif 'who developed you' in incoming_msg:
        msg.body("A group of students trying to make a change. (We can only do so much for now, but we hope to do more)")

    elif 'how are you' in incoming_msg:
        msg.body("I'm doing good. Did you need any help with your diagnosis?")

    elif '#about' in incoming_msg:
        msg.body("Hello, I am your virtual healthcare assistant. I can help predict whether you have diabetes to an accuracy of 96%.\nI can also tell you the latest COVD stats when you message '#coronastats'.\nSimply text me a greeting and I will tend to you.\nWishing you a happy and healthy life.")

    elif '#coronastats' in incoming_msg:
        #! Return covid19 stats.
        url = 'https://coronavirus-19-api.herokuapp.com/countries/india'
        r = requests.get(url)
        rj = r.json()
        try:
            totalCases = rj['cases']
            totalRecovered = rj['recovered']
            totalDeaths = rj['deaths']
            active = rj['active']
            critical = rj['critical']
            todaysCases = rj['todayCases']
            todaysDeaths = rj['todayDeaths']
            msg.body(f"The current stats for COVID-19 in India:\nTotal Cases: {totalCases}\nTotal Recovered: {totalRecovered}\nTotal Deaths: {totalDeaths}\nActive Cases: {active}\nCritical Cases: {critical}\nNew Cases Today: {todaysCases}\nNew Deaths: {todaysDeaths}\n\nYou can get the latest stats by sending #coronastats")
        except:
            msg.body('Sorry I am unable to retrive corona stats at this time, try later.')

    else:
        msg.body("I am unable to process what you said.\nTry *#about* ")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

