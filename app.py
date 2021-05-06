from flask import Flask , render_template

from user import routes
app = Flask(__name__)

#Routes
from user import routes

@app.route('/')
def index():
   return render_template('home.html')

if __name__ == '__main__':
   app.run()