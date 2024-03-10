
import urllib.request
import json
from twilio.rest import Client

url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=MY_KEY'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

news_string = ""
articles = result["articles"]
for x in range(5):
    article = articles[x]
    news_string += article["title"] + "\n"

print(news_string)

account_sid = ''       #<--- Acount SID
auth_token = ''           #<--- Authenticacian Token
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body= news_string,
                     from_='',    #<----- Twillio Phone
                     to=''      #<-----  Your phone
                 )

print(message.sid)

