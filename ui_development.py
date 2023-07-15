
def get_event_details() -> tuple:
    """
    Interacts with the user to collect the necessary details for the event.
    :return: A tuple containing the event details (start time, end time, summary, description, location, recurrence rule)
    """
    start_time = input('Enter the start time of the event in RFC3339 timestamp format: ')
    end_time = input('Enter the end time of the event in RFC3339 timestamp format: ')
    summary = input('Enter the summary or title of the event: ')
    description = input('Enter the description of the event: ')
    location = input('Enter the location of the event: ')
    recurrence_rule = input('Enter the recurrence rule in RFC2445 iCalendar format: ')
    return (start_time, end_time, summary, description, location, recurrence_rule)