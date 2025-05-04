from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('full.html')  # Default route

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('comment')
        if not name or not comment:
            return render_template('feedback.html', error='Please fill out all fields.')
        print(f"Feedback received from {name}: {comment}")
        return render_template('feedback.html', success=True)
    return render_template('feedback.html')

@app.route('/guestbook', methods=['GET', 'POST'])
def guest():
    if request.method == 'POST':
        name = request.form.get('guest-name')
        email = request.form.get('guest-email')
        comment = request.form.get('guest-comment')
        if not name or not comment:
            return render_template('guest.html', error='Please fill out all fields.')
        print(f"Feedback received from {name} : {email} : {comment}")
        return render_template('guest.html', success=True)
    return render_template('guest.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
