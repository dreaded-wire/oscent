from person_module import Person
from address_module import StreetAddress
from phone_module import PhoneNumber  # Import the PhoneNumber module
from username_module import Username
from email_module import Email
from clear_module import clear_screen
from ip_module import IP
from banner import banner

# Example usage:
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

    if choice == "1":
        # Create a Person object
        person = Person()

        # Update information based on user input
        person.update_info()

        # Display updated information
        person.display_info()

        # Generate and display both URLs
        thatsthem = person.generate_thatsthem_url()
        truepeoplesearch = person.generate_truepeoplesearch_url()
        four = person.generate_411_url()
        usphone = person.generate_usphonebook_url()
        famtree = person.generate_familytreenow_url()
        zaba = person.generate_zabasearch_url()
        print(zaba)
        print(famtree)
        print(usphone)
        print(thatsthem)
        print(truepeoplesearch)
        print(four)
        input("\nPress enter to continue: ")
    elif choice == "2":
        # Use the StreetAddress class from the address_module
        street_address = StreetAddress()

        # Update information based on user input
        street_address.update_info()

        # Display updated information
        street_address.display_info()

        # Generate and display the TruePeopleSearch.com and ThatsThem.com URL for street address
        truepeoplesearch = street_address.generate_truepeoplesearch_url()
        thatsthem = street_address.generate_thatsthem_url()
        zillow = street_address.generate_zillow_url()
        print(zillow)
        print(truepeoplesearch)
        print(thatsthem)
        input("\nPress enter to continue: ")
    elif choice == "3":  # Handle the option for Phone Number
        # Create a PhoneNumber object
        phone_number = PhoneNumber()

        # Update information
        phone_number.update_info()

        # Display updated information
        phone_number.display_info()

        # Generate and display phone-related URLs
        truepeoplesearch = phone_number.generate_truepeoplesearch_url()
        four = phone_number.generate_411_url()
        thatsthem = phone_number.generate_thatsthem_url()
        usphonebook = phone_number.generate_usphonebook_url()
        npnr = phone_number.generate_npnr_url()
        whocalld = phone_number.generate_whocalld_url()
        reversephonecheck_url1 = phone_number.generate_reversephonecheck_url1()
        reversephonecheck_url2 = phone_number.generate_reversephonecheck_url2()
        thisnumber = phone_number.generate_thisnumber_url()

        print(truepeoplesearch)
        print(four)
        print(thatsthem)
        print(usphonebook)
        print(npnr)
        print(whocalld)
        print(reversephonecheck_url1)
        print(reversephonecheck_url2)
        print(thisnumber)
        input("\nPress enter to continue: ")

    elif choice == "4":
        # Create username object
        username = Username()

        # Update information
        username.update_info()

        # Display updated informaion
        username.display_info()

        # Generate and display username-related URLs
        idcrawl = username.generate_idcrawl_url()
        uvrX = username.generate_uvrX_url()

        print(idcrawl)
        print(uvrX)
        input("\nPress enter to continue: ")

    elif choice == "5":
       # Create email object
       email = Email()

       # Update Information
       email.update_info()

       # Display updated information
       email.display_info()

       # Generate and display email-related URLs
       thatsthem = email.generate_thatsthem_url()
       truepeoplesearch = email.generate_truepeoplesearch_url()
       hunter = email.generate_hunter_io_url()

       print(thatsthem)
       print(truepeoplesearch)
       print(hunter)
       input("\nPress enter to continue: ")
    elif choice == "6":
        # Create IP object
        ip = IP()

        # Update Information
        ip.update()

        # Display updated information
        ip.display()

        # Generate and display ip-related URLs
        whatis = ip.generate_whatismyipaddress()
        mx = ip.generate_mxtoolbox()
        thatsthem = ip.generate_thatsthem()
        keycdn = ip.generate_keycdn()
        geo = ip.generate_geolocation()

        print(whatis)
        print(mx)
        print(thatsthem)
        print(keycdn)
        print(geo)
        input("\nPress enter to continue: ")
    else:
        clear_screen()
        print("Invalid choice.")
