from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('index.html')


@app.route('/drug')
def getDrugInfo():
    drugName = request.args.get('keyword')
    urlDict = getUrls('', True)
    return render_template('drugInfo.html', drugName = drugName)


def getUrls(drugName, testing):
    urlDict = dict()
    if testing:
      urlDict = {'patientsLikeMe' : 'testing'}
    else:
      # pull info from database, will do that later
      urlDict = {}
    return urlDict

