import flask # server lib
import pypandoc # html to docx lib

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/get-word-doc', methods=['POST'])
def getDoc():
    output = pypandoc.convert_file('markup.html', format='html', to='docx', outputfile="profile.docx")
    assert output == ""


app.run()
