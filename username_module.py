from clear_module import clear_screen
class Username: # Initialize object
    def __init__(self, username=""):
        self.username = username

    def update_info(self): # Method to assign values to attributes of the Username class
        clear_screen()
        self.username = input("Username: ")

    def display_info(self): # Method to display values of the attributes of the Username class
        clear_screen()
        info = f"Username: {self.username}\n"
        print(info)

# Everything past this point is URL generation -->

    def generate_idcrawl_url(self):
        if self.username:
            username = self.username.replace(" ","")
            return f"https://www.idcrawl.com/u/{username}"
        else:
            return "No valid username provided."

    def generate_uvrX_url(self):
        if not self.username:
            return "No valid username provided."
        else:
            return f"http://www.uvrx.com/results-social/index.html?cx=008219812513279254587%3Ao2g7x-v-esw&cof=FORID%3A9&ie=UTF-8&q={self.username}&sa=Search&siteurl=www.uvrx.com%2Fsocial.html&ref=&ss=544j83516j6"
