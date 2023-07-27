from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home template
    return render_template('home.html')

# Define other routes and views

if __name__ == '__main__':
    app.run()
