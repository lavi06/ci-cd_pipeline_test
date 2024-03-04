import requests
import datetime


bot = "5142268509:AAFez1kA6hQFIWEHuKG5IC65cHiJ6jKrKsQ"
group = "@TestSposbhose"

def broadcast(msg):

    to_url = f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={group}&text={msg}&parse_mode=HTML"

    resp = requests.get(to_url)
    print(resp.content)


now = datetime.datetime.now()
broadcast(now)
