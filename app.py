from flask import Flask,render_template


app = Flask(__name__)
projects = [
    {
        'id': 1,
        'project': 'Web Scraping',
        'skills': 'urllib python, Python Requests, Selenium, Beautiful Soup'
    },
    {
        'id': 2,
        'project': 'AI model for flare monitoring',
        'skills': 'Python pandas, scikit-learn, matplotlib, Microsoft Azure, pychatgpt'
    }
]

@app.route("/")

def hello_world():
    return render_template("home.html",projects=projects,)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)