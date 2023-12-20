from clear_module import clear_screen
class Email: # Initialize object
    def __init__(self, email=""):
        self.email = email

    def update_info(self): # Method to assign values to attributes of the Email class
        clear_screen()
        raw_email = input("Enter Email: ")
        self.email = raw_email

    def display_info(self): # Method to display values of the attributes of the Email class
        clear_screen()
        info = f"Email: {self.email}\n"
        print(info)

# Everything past this point is URL generation -->

    def generate_thatsthem_url(self):
        if '@' not in self.email:
            return "No valid email provided; missing '@'"
        else:
            return f"https://thatsthem.com/email/{self.email}"

    def generate_truepeoplesearch_url(self):
        if self.email:
            # Handle specific domain substitutions
            domain_substitutions = {
                '@yahoo.com': 'fdgsdfjwert',
                '@gmail.com': 'ertpoiqwertr',
                '@hotmail.com': 'cvxnfdjtyui',
                '@outlook.com': 'ghoekcdktrmwd',
                '@icloud.com': 'ytowesdghtyow',
                '@aol.com': 'nmqwuisdfyure',
                '@live.com': 'dfsxczgirejdf',
                # Add more domains and substitutions as needed
            }

            for domain, substitution in domain_substitutions.items():
                if domain in self.email:
                    formatted_email = self.email.replace(domain, substitution)
                    return f"https://www.truepeoplesearch.com/resultemail?email={formatted_email}"

            # If the domain is not in the substitutions, use the default format
            formatted_email = self.email.replace('@', '_at_').replace('.', '_dot_')
            return f"https://www.truepeoplesearch.com/resultemail?email={formatted_email}"
        else:
            return "No valid email provided; missing '@'"
            
    def generate_hunter_io_url(self):
        if '@' not in self.email:
            return "No valid email provided; missing '@'"
        else:
            return f"https://hunter.io/verify/{self.email}"
            
    def generate_emailsherlock_url(self):
        if '@' not in self.email:
            return "No valid email provided; missing '@'"
        else:
            return f"https://www.emailsherlock.com/emailsearch/{self.email}/"
