from flask import Flask, render_template as render

app = Flask(__name__)

@app.route('/')
def home():
    return render(template_name_or_list="index.html")