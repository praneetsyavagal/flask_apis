from flask import Flask, render_template, url_for
app = Flask(__name__)




@app.route("/")
@app.route("/home")
@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/protect_animals")
@app.route("/protect_animals.html")
def protect_animals():
    return render_template('protect_animals.html')

@app.route("/humanitarian_value.html")
@app.route("/humanitarian_value")
def humanitarian_value():
    return render_template('humanitarian_value.html')

@app.route("/save_nature.html")
@app.route("/save_nature")
def save_nature():
    return render_template('save_nature.html')

@app.route("/save_water.html")
@app.route("/save_water")
def save_water():
    return render_template('save_water.html')


#@app.route("/about")
#def about():
#   return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)