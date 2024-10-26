from flask import Flask, render_template_string
import requests

app = Flask(__name__)

def fetch_astronomy_events():
    url = "https://www.timeanddate.com/astronomy/sights-to-see.html"
    response = requests.get(url)
    
    # Return the full HTML content of the page
    return response.text

@app.route('/')
def events():
    astronomy_events_html = fetch_astronomy_events()
    
    # Render the full HTML directly
    return render_template_string(astronomy_events_html)

if __name__ == '__main__':
    app.run(debug=True)
