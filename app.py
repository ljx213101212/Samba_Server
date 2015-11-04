from flask import Flask
from flask import render_template
from flask import request
from flask import url_for, redirect
from database import *
from jsonConstants import *
import flask

def make_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app

app = make_app()

Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def hello_world():
    return render_template('index.html')
    # tested how to write functions in models lol
    # but I'm not sure whether it is the right way
    #return a


@app.route('/query_events_all')
def query_events():

    events = session.query(Event).order_by(Event.event_id.desc())
    res = []
    for event in events:
        result = {}
        #print "event is "+ event
        for i in event.__dict__:
            if i[0] == '_':
                continue
            else:
                result[i] = event.__dict__[i]
        res.append(result)

    r = {}
    r['result'] = res
    print "You are excuting query_events_all api"

    return flask.jsonify(**r)


@app.route('/query_modules_all')
def query_modules():

    modules = session.query(Module).order_by(Module.module_id.desc())
    res = []
    for module in modules:
        result = {}
        #print "event is "+ module
        for i in module.__dict__:
            if i[0] == '_':
                continue
            else:
                result[i] = module.__dict__[i]
        res.append(result)

    r = {}
    r['result'] = res
    print "You are excuting query_modules_all api"

    return flask.jsonify(**r)

@app.route('/createModules',methods=["POST"])
def createClinic():
    ## this one is dangerous, cause there should at least be some management part for the id management
    ## this one assume that you already have an exclusive ID
    ## in the new version you don't have to care about the ID number anymore cause it
    ## can auto increment
    data = request.form
    if not data:
        return "No data!"

    module = Module()
    if module_id in data:
        module.module_id = data[module_id]
    if module_name in data:
        module.module_name = data[module_name]
    if mod_details in data:
        module.mod_details = data[mod_details]

    session.add(module)
    session.commit()

    return "SUCCESS"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
