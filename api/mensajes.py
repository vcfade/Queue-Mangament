

from twilio.rest import Client

account_sid = 'ACa39f28e58e87b6ff6ab53121b1b785b6'
auth_token = '28139e8faf9a6adc74a243badedcd9a7'
client = Client(account_sid, auth_token)


def send_message(number,message):
    account_sid = 'ACa39f28e58e87b6ff6ab53121b1b785b6'
    uth_token = '28139e8faf9a6adc74a243badedcd9a7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                from_='+12053089012',
                                body= message,
                                to= number
                            )

    print(message.sid)

