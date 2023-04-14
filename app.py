from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': "Sleuth",
    'location': 'London',
    'department': 'SleuthMaster',
    'salary': "£ 60,000"
  },
  {
    'id': 2,
    'title': "Private Investigator",
    'location': "56 Baker Street, London",
    'department': "DetectiveOne",
    'salary': "£ 30,000"
  },
  {
    'id': 3,
    'title': "Revenue Official",
    'location': 'London',
    'department': "Taxation",
    'salary': "£ 10,000"
  },
  {
    'id': 4,
    'title': "Investigator",
    'location': 'London',
    'department': "SleuthMaster",
    'salary': "£ 100,000"
  }

]


@app.route("/")
def poop():
  return render_template('home.html', jobs = JOBS)

@app.route("/aboutus")
def pop():
  return render_template('AboutUs.html')
  
@app.route("/contactus")
def popo():
  return render_template('contactus.html')
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
