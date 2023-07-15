import requests
from datetime import datetime

# Google Calendar API
GOOGLE_CALENDAR_API = "https://www.googleapis.com/calendar/v3/calendars"

# Microsoft Outlook Calendar API
OUTLOOK_CALENDAR_API = "https://graph.microsoft.com/v1.0/me/calendar"

def sync_calendar(user_id, calendar_type, token):
    if calendar_type == "Google":
        return sync_google_calendar(user_id, token)
    elif calendar_type == "Outlook":
        return sync_outlook_calendar(user_id, token)
    else:
        return None

def sync_google_calendar(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{GOOGLE_CALENDAR_API}/{user_id}/events", headers=headers)
    
    if response.status_code == 200:
        events = response.json().get('items', [])
        return parse_events(events)
    else:
        return None

def sync_outlook_calendar(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{OUTLOOK_CALENDAR_API}/events", headers=headers)
    
    if response.status_code == 200:
        events = response.json().get('value', [])
        return parse_events(events)
    else:
        return None

def parse_events(events):
    parsed_events = []
    for event in events:
        start_time = datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
        end_time = datetime.strptime(event['end']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
        parsed_events.append({
            'id': event['id'],
            'summary': event['summary'],
            'start': start_time,
            'end': end_time
        })
    return parsed_events