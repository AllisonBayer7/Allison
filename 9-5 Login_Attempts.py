class User:
    """Represents a user profile."""
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\nUser: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nHello, {self.username}!")

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts."""
        self.login_attempts = 0


allison = User('allison', 'bayer', 'allisonb',
               'allisonb@example.com', 'savannah')
allison.describe_user()
allison.greet_user()

print("\nMaking 3 login attempts...")
allison.increment_login_attempts()
allison.increment_login_attempts()
allison.increment_login_attempts()
print(f"Login attempts: {allison.login_attempts}")

print("Resetting login attempts...")
allison.reset_login_attempts()
print(f"Login attempts: {allison.login_attempts}")