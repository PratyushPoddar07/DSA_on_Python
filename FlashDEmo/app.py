## Flask App Routing




from flask import Flask

# create a simple flask application
FlaskApp = Flask(__name__)

@FlaskApp.route('/',methods =["GET"]) # decorator

def home():
    return "Hello World"


@FlaskApp.route('/dance',methods =["GET"]) # decorator

def dance():
    return "Welcome to the dancing page"

if __name__ == "__main__":
    FlaskApp.run(debug =True) 