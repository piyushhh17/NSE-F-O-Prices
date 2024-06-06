import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, render_template

df = pd.read_csv("MW-FO-nse50_opt-27-May-2024.csv")
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)