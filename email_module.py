from clear_module import clear_screen
import re # Import regular expressions for email validation

class Email:
    def __init__(self, email=""):
        self.email = email

    def update_info(self):
        clear_screen()
        while True:
            raw_email = input("Enter Email: ")
            if self.is_valid_email(raw_email):
                self.email = raw_email
                break
            else:
                print("\nInvalid email format. Please try again.\n")

    def display_info(self):
        clear_screen()
        print(f"Email: {self.email}\n")

    def is_valid_email(self, email): # Email validation
        return re.match(r"^[^@]+@[^@]+\.[a-zA-Z]{2,}$", email) is not None

    # URL generation methods

    def generate_url(self, base_url): # URL generation base
        if not self.is_valid_email(self.email):
            return "No valid email provided; missing or invalid '@'"
        return f"{base_url}/{self.email}"

    def generate_thatsthem_url(self):
        return self.generate_url("https://thatsthem.com/email")

    def generate_hunter_io_url(self):
        return self.generate_url("https://hunter.io/verify")

    def generate_truepeoplesearch_url(self):
        if not self.is_valid_email(self.email):
            return "No valid email provided; missing or invalid '@'"
        
        # Handle specific domain substitutions
        domain_substitutions = {
            '@yahoo.com': 'fdgsdfjwert',
            '@gmail.com': 'ertpoiqwertr',
            '@hotmail.com': 'cvxnfdjtyui',
            '@outlook.com': 'ghoekcdktrmwd',
            '@icloud.com': 'ytowesdghtyow',
            '@aol.com': 'nmqwuisdfyure',
            '@live.com': 'dfsxczgirejdf',
            # Add more domains as needed
        }

        for domain, substitution in domain_substitutions.items():
            if domain in self.email:
                formatted_email = self.email.replace(domain, substitution).replace('.', '_dot_')
                return f"https://www.truepeoplesearch.com/resultemail?email={formatted_email}"

        # Default format for other domains
        formatted_email = self.email.replace('@', '_at_').replace('.', '_dot_')
        return f"https://www.truepeoplesearch.com/resultemail?email={formatted_email}"
