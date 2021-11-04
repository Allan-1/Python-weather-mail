import requests, smtplib, time


def getWeather():
    '''This get the current weather from the weather api and returns the weather information'''
    try:
        req  = requests.get('https://api.weatherapi.com/v1/current.json?key=<your weather api key>&q=nairobi')
        return req.json()
    except:
        return 'An error has occured with the api'


def sendmail(sendermail, senderpassword, receivermail, message):
    'Send the mail using the smtp protocol'
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sendermail, senderpassword)
        server.sendmail(sendermail, receivermail, message)
        server.close()
    except:
        return 'An error has occured with the mail'    

def messageFormat():
    'Formats the message to be sent to the mail and returns the string'
    message = '''
    Good Morning
    The weather on {} is {} and it is {} degrees
    '''
    time.sleep(5)
    return message.format(getWeather()['location']['region'], getWeather()['current']['condition']['text'], getWeather()['current']['temp_c'])


sender_email = 'senders@mail.com'
senderspassword = 'pass12345'
recieversemail = 'reciever@mail.com'

sendmail(sender_email, senderspassword, recieversemail, messageFormat())