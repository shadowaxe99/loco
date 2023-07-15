
def create_recurring_event(service: object, start: str, end: str, summary: str, description: str, location: str, recurrence: str) -> str:
    """
    Creates a recurring event.
    :param service: The authenticated Google Calendar service object
    :param start: The start time of the event in RFC3339 timestamp format
    :param end: The end time of the event in RFC3339 timestamp format
    :param summary: The summary or title of the event
    :param description: The description of the event
    :param location: The location of the event
    :param recurrence: The recurrence rule in RFC2445 iCalendar format
    :return: The event's html link if the event is created successfully
    """
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [recurrence],
    }
    try:
        created_event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {created_event['htmlLink']}")
        return created_event['htmlLink']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
