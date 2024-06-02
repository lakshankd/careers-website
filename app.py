from flask import Flask, render_template, jsonify

app = Flask(__name__)
print(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'San Francisco',
        'salary': 'Rs. 10,000,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'New York',
        'salary': 'Rs. 10,000,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineering',
        'location': 'Remote',
        'salary': 'Rs. 10,000,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineering',
        'location': 'Delhi, India',
        'salary': 'Rs. 10,000,000'
    }
]


@app.route('/')
def home_page():
    return render_template('home.html', jobs=JOBS)


@app.route('/about/<username>')
def about(username):
    return f'<h1>This is About Page of {username}</h1>'


@app.route('/api/jobs')
def list_all_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run()
