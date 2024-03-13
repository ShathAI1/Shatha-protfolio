from flask import Flask, render_template

app = Flask(__name__)
projects = [{
    'id':1,
    'project':'Web scraping',
    'skills':'urllib Python, Python Request, Selenium, BeautifulSoup, Seaborn, Scikit-learn'
},
{
    'id':2,
    'project':'AI model for flare monitoring',
    'skills':'Python pandas, Numpy, Scikit-learn, Tensorflow, matblotlib, Keras'
},
{
    'id':3,
    'project':'Digitalization',
    'skills':'Python, Flask, HTML, CSS, Javascript, SQL, MySQL, AWS, Heroku'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', myskills=projects, 
                         myname = 'Shatha')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=True)  # run flask server
