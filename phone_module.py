from clear_module import clear_screen
class PhoneNumber: # Initialize object
    def __init__(self, phone_number=""):
        self.phone_number = phone_number

    def update_info(self): # Method to assign values to attributes of the PhoneNumber class
        clear_screen()
        raw_phone_number = input("Phone Number: ")

        # Remove non-numeric characters and format as (xxx)xxx-xxxx
        formatted_phone_number = ''.join(filter(str.isdigit, raw_phone_number))
        if len(formatted_phone_number) == 10:
            self.phone_number = f"({formatted_phone_number[:3]}){formatted_phone_number[3:6]}-{formatted_phone_number[6:]}"
        else:
            self.phone_number = ""

    def display_info(self): # Method to display values of the attributes of the PhoneNumber class
        clear_screen()
        info = f"Phone Number: {self.phone_number}\n"
        print(info)

# Everything past this point is URL generation -->

    def generate_truepeoplesearch_url(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            return f"https://www.truepeoplesearch.com/resultphone?phoneno={phone_number}"
        else:
            return "No valid phone number provided."

    def generate_411_url(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number and format as xxx-xxx-xxxx
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            formatted_phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
            return f"https://www.411.com/phone/1-{formatted_phone_number}"
        else:
            return "No valid phone number provided."

    def generate_thatsthem_url(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number and format as xxx-xxx-xxxx
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            formatted_phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
            return f"https://thatsthem.com/phone/{formatted_phone_number}"
        else:
            return "No valid phone number provided."

    def generate_usphonebook_url(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number and format as xxx-xxx-xxxx
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            formatted_phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
            return f"https://www.usphonebook.com/{formatted_phone_number}"
        else:
            return "No valid phone number provided."

    def generate_npnr_url(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number and format as xxx/xxx/xxxx/xxxxxxxxxx.html
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            return f"https://npnr.org/{phone_number[:3]}/{phone_number[3:6]}/{phone_number[6:]}/{phone_number}.html"
        else:
            return "No valid phone number provided."

    def generate_whocalld_url(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            return f"https://whocalld.com/search?p={phone_number}"
        else:
            return "No valid phone number provided."

    def generate_reversephonecheck_url1(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number and format as 1-xxx/xxx/xx/#xxxxxxxxxx
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            return f"https://www.reversephonecheck.com/1-{phone_number[:3]}/{phone_number[3:6]}/{phone_number[6:8]}/#{phone_number}"
        else:
            return "No valid phone number provided."
    
    def generate_reversephonecheck_url2(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number and format as 1-xxx/xxx/xxxx/?number=xx
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            return f"https://www.reversephonecheck.com/1-{phone_number[:3]}/{phone_number[3:6]}/{phone_number[6:]}/?number={phone_number[-2:]}"
        else:
            return "No valid phone number provided."
    
    def generate_thisnumber_url(self):
        if self.phone_number:
            # Remove non-numeric characters from the phone number and format as xxx-xxx-xxxx
            phone_number = ''.join(filter(str.isdigit, self.phone_number))
            formatted_phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
            return f"https://www.thisnumber.com/{formatted_phone_number}"
        else:
            return "No valid phone number provided."
