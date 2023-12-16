from clear_module import clear_screen

class Person:
    def __init__(self, first_name="", mid_name="", last_name="", zip_code="", state="", city="", age="", county="", street_address=""):
        self.firstName = first_name
        self.midName = mid_name
        self.lastName = last_name
        self.zip = zip_code
        self.state = state
        self.city = city
        self.age = age
        self.county = county
        self.street_address = street_address

    def update_info(self):
        clear_screen()
        self.firstName = input("First Name: ")
        self.midName = input("Middle Name: ")
        self.lastName = input("Last Name: ")
        self.zip = input("ZIP Code: ")
        self.state = input("State: ")
        self.city = input("City: ")
        self.county = input("County: ")
        self.street_address = input("Street Address: ")
        self.age = input("Age: ")

    def display_info(self):
        clear_screen()
        info = f"First Name: {self.firstName}\n"\
               f"Middle Name: {self.midName}\n"\
               f"Last Name: {self.lastName}\n"\
               f"ZIP Code: {self.zip}\n"\
               f"State: {self.state}\n"\
               f"City: {self.city}\n"\
               f"County: {self.county}\n"\
               f"Street Address: {self.street_address}\n"\
               f"Age: {self.age}\n"
        print(info)

    def generate_thatsthem_url(self):
        name_parts = []
        if self.firstName:
            name_parts.append(self.firstName)
        if self.midName:
            name_parts.append(self.midName)
        if self.lastName:
            name_parts.append(self.lastName)

        other_parts = []
        if self.zip:
            other_parts.append(self.zip)
        if self.state:
            other_parts.append(self.state)
        if self.city:
            other_parts.append(self.city.replace(" ", "-"))

        if not name_parts:
            return "https://thatsthem.com/name"
        
        url = "https://thatsthem.com/name/" + "-".join(name_parts)
        
        if other_parts:
            url += "/" + "-".join(other_parts)
        url = url.replace(" ", "-")
        
        return url

    def generate_truepeoplesearch_url(self):
        name_parts = []
        if self.firstName:
            name_parts.append(self.firstName)
        if self.midName:
            name_parts.append(self.midName)
        if self.lastName:
            name_parts.append(self.lastName)

        if not name_parts:
            return "No valid name components to generate a URL."

        name_url = "%20".join(name_parts)
        name_url = name_url.replace(" ", "%20")
        location_parts = []

        if self.city:
            location_parts.append(self.city.replace(" ", "%20"))
        if self.state:
            location_parts.append(self.state)
        if self.zip:
            location_parts.append(self.zip)

        if location_parts:
            location_url = "%20".join(location_parts)
            return f"https://www.truepeoplesearch.com/results?name={name_url}&citystatezip={location_url}"
        else:
            return f"https://www.truepeoplesearch.com/results?name={name_url}"

    def generate_411_url(self):
        name_parts = []
        if self.firstName:
            name_parts.append(self.firstName)
        if self.midName:
            name_parts.append(self.midName)
        if self.lastName:
            name_parts.append(self.lastName)

        if not name_parts:
            return "No valid name components to generate a URL."

        name_url = "-".join(name_parts)
        name_url = name_url.replace(" ", "-")
        location_parts = []
        if self.city:
            location_parts.append(self.city.replace(" ", "-"))
        if self.state:
            location_parts.append(self.state)

        if location_parts:
            return f"https://www.411.com/person-search/{name_url}/{self.state}/{self.city}"
        else:
            return f"https://www.411.com/person-search/{name_url}"

    def generate_usphonebook_url(self):
        name_parts = []
        if self.firstName:
            name_parts.append(self.firstName)
        if self.midName:
            name_parts.append(self.midName)
        if self.lastName:
            name_parts.append(self.lastName)

        if not any(name_parts):
            return "No valid name components to generate a URL."

        name_url = "-".join(name_parts)
        name_url = name_url.replace(" ", "-")

        location_parts = []
        if self.state:
            location_parts.append(self.state)
        if self.city:
            location_parts.append(self.city.replace(" ", "-"))

        if location_parts:
            location_url = "/".join(location_parts)
            return f"https://www.usphonebook.com/{name_url}/{location_url}"
        else:
            return f"https://www.usphonebook.com/{name_url}"

    def generate_familytreenow_url(self):
        name_parts = []
        if self.firstName:
            name_parts.append(f"first={self.firstName}")
        if self.lastName:
            name_parts.append(f"last={self.lastName}")

        name_url = "&".join(name_parts)
        name_url = name_url.replace(' ', '%20')

        location_parts = []
        if self.city:
            location_parts.append(f"citystatezip={self.city.replace(' ', '%20')}")
        if self.state:
            location_parts.append(f"{self.state.replace(' ', '%20')}")

        location_url = ",%20".join(location_parts)

        return f"https://www.familytreenow.com/search/genealogy/results?{name_url}&{location_url}"

    def generate_zabasearch_url(self):
        name_parts = []
        if self.firstName and self.lastName:
            name_parts.append(self.firstName.replace(' ', '%20'))
            name_parts.append(self.lastName.replace(' ', '%20'))

        if not name_parts:
            return "No valid name components to generate a URL."

        name_url = "+".join(name_parts)

        location_parts = []
        if self.city:
            if self.state:
                location_parts.append(f"{self.city.replace(' ', '%20')}+{self.state.replace(' ', '%20')}")
            else:
                return "If a city is provided, a state must also be provided."

        location_url = "+".join(location_parts)

        if location_url:
            return f"https://www.zabasearch.com/people/{name_url}/{location_url}/"
        else:
            return f"https://www.zabasearch.com/people/{name_url}/"
