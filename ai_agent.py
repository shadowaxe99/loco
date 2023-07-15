import nlp_processing
import ml_model
import calendar_integration
import data_storage
import feature_selection
import personalization_options
import continuous_learning
import privacy_security

class AIAgentScheduler:
    def __init__(self):
        self.user_preferences = {}
        self.user_schedule = {}
        self.user_appointments = []
        self.calendar_data = {}

    def parse_user_input(self, user_input):
        return nlp_processing.parse_user_input(user_input)

    def generate_schedule(self):
        return ml_model.generate_schedule(self.user_preferences, self.user_schedule, self.user_appointments)

    def sync_calendar(self):
        self.calendar_data = calendar_integration.sync_calendar(self.user_schedule, self.user_appointments)
        return self.calendar_data

    def update_UI(self):
        ui_development.update_UI(self.user_schedule, self.user_appointments, self.user_preferences)

    def store_data(self):
        data_storage.store_data(self.user_preferences, self.user_schedule, self.user_appointments)

    def select_features(self, features):
        self.user_preferences = feature_selection.select_features(features)

    def define_personalization(self, personalization_level):
        self.user_preferences = personalization_options.define_personalization(personalization_level)

    def learn_and_improve(self):
        self.user_preferences, self.user_schedule = continuous_learning.learn_and_improve(self.user_preferences, self.user_schedule, self.user_appointments)

    def ensure_privacy(self):
        privacy_security.ensure_privacy(self.user_preferences, self.user_schedule, self.user_appointments)