#Code for keeping the bot running
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "My name is VeK and I Stand Tall"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()