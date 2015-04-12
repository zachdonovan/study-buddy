# tiny Flask microservice to 
# redirect users to 1 of N urls

from flask import Flask
import choices
app = Flask(__name__)

@app.route('/')
def flip():
  return flask.redirect(app.urls.next())

if __name__ == "__main__":
  app.run()
  app.choices = choices.start()
