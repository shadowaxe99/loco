# API Documentation

This application interacts with the Google Calendar API. Here are the main API calls that the application makes:

1. **Authenticate**: The application authenticates with the Google Calendar API using OAuth 2.0. This involves redirecting the user to a Google sign-in page, where the user can grant the application access to their Google Calendar data.

2. **Fetch upcoming events**: The application fetches the upcoming events on the user's calendar using the `events().list` method of the Google Calendar API.

3. **Create event**: The application creates an event on the user's calendar using the `events().insert` method of the Google Calendar API.

4. **Delete event**: The application deletes an event from the user's calendar using the `events().delete` method of the Google Calendar API.

5. **Update event**: The application updates an event on the user's calendar using the `events().update` method of the Google Calendar API.

For more detailed information on the Google Calendar API, refer to the [official documentation](https://developers.google.com/calendar).