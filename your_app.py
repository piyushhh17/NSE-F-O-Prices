import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, render_template
import pandas as pd
import os
import glob

download_dir = 'C:\\Users\\piyush.kaushal\\Downloads' 

list_of_files = glob.glob(os.path.join(download_dir, '*.csv'))
latest_file = max(list_of_files, key=os.path.getctime)


df = pd.read_csv(latest_file)

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)