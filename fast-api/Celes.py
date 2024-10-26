from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Function to scrape event data
def fetch_events():
    url = "https://www.astronomy.com/observing/upcoming-events/"
    response = requests.get(url)
    print("Response status:", response.status_code)  # Check if the page loads successfully
    soup = BeautifulSoup(response.content, "html.parser")
    
    events = []
    event_elements = soup.select(".event-item")  # Adjust selector as needed
    print("Found event elements:", len(event_elements))  # Check how many events are found
    
    for element in event_elements:
        title = element.find("h3").get_text(strip=True)
        date = element.find(class_="event-date").get_text(strip=True)
        description = element.find("p").get_text(strip=True)
        events.append({"title": title, "date": date, "description": description})
    return events

# FastAPI endpoint to return events as JSON
@app.get("/events", response_class=JSONResponse)
async def get_events():
    events = fetch_events()
    return events

# Mounting static files (for serving events.html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
