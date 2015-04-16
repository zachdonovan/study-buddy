# tiny Flask microservice to 
# redirect users to 1 of N urls

from flask import Flask, redirect
import choices as c
app = Flask(__name__)

@app.route('/')
def flip():
  url, app.config['ix'] = c.next_url(app.config['ix'])
  return redirect(url)

if __name__ == "__main__":
  app.config['ix'] = c.start_ix()
  app.run(debug=True)
