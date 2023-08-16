from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField


app = Flask(__name__)
app.config["SECRET_KEY"] = "Very hard to guess string"

class B(FlaskForm):
    b1 = StringField("B1 Label: ")
    b2 = StringField("B2 Label: ")

    
class A(FlaskForm):
    a1 = StringField("A1 Label: ")
    a2 = FieldList(FormField(B), min_entries=3)
    submit = SubmitField("Submit")


@app.route("/")
def index():
    form = A()
    return render_template("index.html", form=form)

@app.route("/result", methods=["POST"])
def result():
    a = request.form["a1"]
    b = request.form
    br = { x:b[x] for x in b if "a2-" in x}
    return render_template("result.html", a=a, b=br)

if __name__ == "__main__":
    app.run(debug=True)