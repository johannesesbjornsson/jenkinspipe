from flask import Flask
import letter_mod
import number_mod
app = Flask(__name__)

@app.route("/")
def hello():
    numbs = number_mod.get_some_numbers()
    string = letter_mod.get_some_letters(numbs)
    return "Oi!! Look at these sick, randomly generated letters. Pretty cool, hey?  "+ string

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
