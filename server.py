from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results', methods=['POST'])
def display_results():
    name_from_form = request.form['name']
    dojo_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("results.html", name_on_template=name_from_form, dojo_on_template=dojo_from_form,language_on_template = language_from_form, comment_on_template= comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)