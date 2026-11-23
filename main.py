import csv
import os
import datetime
import requests

# Facebook Page ki details - ye GitHub Secrets se aayegi
PAGE_ID = os.environ.get("FB_PAGE_ID")
PAGE_TOKEN = os.environ.get("FB_PAGE_TOKEN")

# Aaj ki date se kaun sa Day hai, ye nikalenge
# Day 1 se Day 30 tak ghumta rahega
start_date = datetime.date(2026, 11, 24)
today = datetime.date.today()
day_number = (today - start_date).days % 30 + 1

print(f"Aaj Day {day_number} ka post hoga")

# content.csv se aaj ka caption nikalna
caption = ""
with open("content.csv", encoding="utf-8") as f:
    reader = list(csv.DictReader(f))
    for row in reader:
        if int(row["day"]) == day_number:
            caption = row["caption"]
            break

print("Caption mil gaya")

# Poster ka rasta
poster_path = f"posters/day{day_number}.jpg"

# Facebook pe Photo Post karna
url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/photos"

with open(poster_path, "rb") as img:
    files = {"source": img}
    data = {"message": caption, "access_token": PAGE_TOKEN}
    response = requests.post(url, files=files, data=data)

print(response.text)
print("Ho gaya! Post chala gaya.")
