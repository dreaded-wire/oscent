from person_module import Person
from address_module import StreetAddress
from phone_module import PhoneNumber
from username_module import Username
from email_module import Email
from clear_module import clear_screen
from ip_module import IP
from banner import banner

def display_urls(urls): # URL output
    for url in urls:
        print(url)
    input("\nPress enter to continue: ")

def handle_choice(option): # Sets URL generation methods
    if option == "1":
        person = Person()
        person.update_info()
        person.display_info()
        urls = [
            person.generate_thatsthem_url(),
            person.generate_truepeoplesearch_url(),
            person.generate_411_url(),
            person.generate_usphonebook_url(),
            person.generate_familytreenow_url(),
            person.generate_zabasearch_url()
        ]
    elif option == "2":
        street_address = StreetAddress()
        street_address.update_info()
        street_address.display_info()
        urls = [
            street_address.generate_truepeoplesearch_url(),
            street_address.generate_thatsthem_url(),
            street_address.generate_zillow_url()
        ]
    elif option == "3":
        phone_number = PhoneNumber()
        phone_number.update_info()
        phone_number.display_info()
        urls = [
            phone_number.generate_truepeoplesearch_url(),
            phone_number.generate_411_url(),
            phone_number.generate_thatsthem_url(),
            phone_number.generate_usphonebook_url(),
            phone_number.generate_npnr_url(),
            phone_number.generate_whocalld_url(),
            phone_number.generate_reversephonecheck_url1(),
            phone_number.generate_reversephonecheck_url2(),
            phone_number.generate_thisnumber_url()
        ]
    elif option == "4":
        username = Username()
        username.update_info()
        username.display_info()
        urls = [
            username.generate_idcrawl_url(),
            username.generate_uvrX_url()
        ]
    elif option == "5":
        email = Email()
        email.update_info()
        email.display_info()
        urls = [
            email.generate_thatsthem_url(),
            email.generate_truepeoplesearch_url(),
            email.generate_hunter_io_url()
        ]
    elif option == "6":
        ip = IP()
        ip.update()
        ip.display()
        urls = [
            ip.generate_whatismyipaddress(),
            ip.generate_mxtoolbox(),
            ip.generate_thatsthem(),
            ip.generate_keycdn(),
            ip.generate_geolocation()
        ]
    else:
        clear_screen()
        print("Invalid choice.")
        return

    display_urls(urls)

# Main loop
while True:
    clear_screen()
    banner()
    print("1. Person")
    print("2. Street Address")
    print("3. Phone Number")
    print("4. Username")
    print("5. Email")
    print("6. IP")
    print("0. Exit\n")

    choice = input("Enter numeric option: ")
    if choice == "0":
        exit()

    handle_choice(choice)
