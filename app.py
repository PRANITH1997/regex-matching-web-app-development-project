from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        test_string = request.form.get('test_string')
        regex_pattern = request.form.get('regex_pattern')
        if not regex_pattern:
            return render_template('home.html', error="Please enter a valid regex pattern")
        try:
            matched_strings = re.findall(regex_pattern, test_string)
        except re.error as e:
            return render_template('home.html', error=str(e))
        return render_template('home.html', matched_strings=matched_strings, test_string=test_string, regex_pattern=regex_pattern)
    return render_template('home.html')

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email')
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Valid email ID"
    else:
        return "Invalid email ID"

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)

