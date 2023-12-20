from clear_module import clear_screen
class StreetAddress: # Initialize object
    def __init__(self):
        self.street = ""
        self.zip = ""
        self.state = ""
        self.city = ""

    def update_info(self): # Method to assign values to attributes of the StreetAddress class
        clear_screen()
        self.street = input("Street: ")
        self.zip = input("ZIP Code: ")
        self.state = input("State: ")
        self.city = input("City: ")

    def display_info(self): # Method to display values of the attributes of the StreetAddress class
        clear_screen()
        info = f"Street: {self.street}\n"\
               f"ZIP Code: {self.zip}\n"\
               f"State: {self.state}\n"\
               f"City: {self.city}\n\n"
        print(info)

# Everything past this point is URL generation -->

    def generate_truepeoplesearch_url(self):
        if self.street and ((self.city and self.state) or self.zip):
            address_parts = [self.street.replace(" ", "%20")]
            location_parts = []

            if self.city:
                location_parts.append(self.city)
                location_parts.append(self.state)

            if self.zip:
                location_parts.append(self.zip)

            location_url = "%20".join(location_parts) if location_parts else ""
            location_url = location_url.replace(" ", "%20")
            return f"https://www.truepeoplesearch.com/resultaddress?streetaddress={address_parts[0]}&citystatezip={location_url}"

        return "No valid address components to generate a URL."

    def generate_thatsthem_url(self):
        if self.street and ((self.city and self.state) or self.zip):
            address_parts = [self.street.replace(" ", "-")]
            location_parts = []

            if self.city:
                location_parts.append(self.city.replace(" ", "-"))
                location_parts.append(self.state)

            if self.zip:
                location_parts.append(self.zip)

            location_url = "-".join(location_parts) if location_parts else ""
            location_url = location_url.replace(" ", "-")
            return f"https://thatsthem.com/address/{address_parts[0]}-{location_url}"

        return "No valid address components to generate a URL."

    def generate_zillow_url(self):
        if self.street:
            address_parts = [self.street.replace(" ", "-")]

            if self.city:
                address_parts.append(self.city.replace(" ", "-"))
            if self.state:
                address_parts.append(self.state)
            if self.zip:
                address_parts.append(self.zip)

            url = "https://www.zillow.com/homes/" + "-".join(address_parts)
            return url

        return "No valid address components to generate a URL."
