import flask # server lib
import pypandoc # html to docx lib

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to my python server</h1>"

@app.route('/get-word-doc', methods=['POST'])
def getDoc():
    output = pypandoc.convert_file('markup.html', format='html', to='docx', outputfile="profile.docx")
    assert output == ""


app.run()
