
def choose_calendar_service() -> str:
    """
    Asks the user to choose between Google Calendar and Outlook Calendar.
    :return: The user's choice ('Google' or 'Outlook')
    """
    print('Which calendar service would you like to use?')
    print('1. Google Calendar')
    print('2. Outlook Calendar')
    choice = input('Enter the number of your choice: ')
    if choice == '1':
        return 'Google'
    elif choice == '2':
        return 'Outlook'
    else:
        print('Invalid choice. Please enter 1 for Google Calendar or 2 for Outlook Calendar.')
        return choose_calendar_service()