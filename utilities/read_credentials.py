import configparser

class CredentialManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(r'C:\Users\hp\PycharmProjects\CallTest\data\config.ini')

    def get_email(self, role):
        section_name = f"credentials {role}"
        print(f"Looking for section: {section_name}")
        try:
            email_key = f"{role}_email"
            return self.config.get('credentials', email_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error:{e}")
            return None

    def get_password(self, role):
        try:
            password_key = f"{role}_password"
            return self.config.get('credentials', password_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error{e}")
            return None

    def get_phone(self, role):
        try:
            number_key = f"{role}_number"
            return self.config.get('numbers', number_key)
        except(configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"error{e}")
            return None


