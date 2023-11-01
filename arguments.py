def user_info(name, age=0, city="Amsterdam"):
    """This function prints name, age and city from an argument provided to the function"""
    print("{} is {} years old from {}".format(name, age, city))


user_info("Anna", 30, "Haarlem")
user_info("Nina")
user_info(age=67, name="Thomas")


def application(first_name, last_name, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}".format(first_name, last_name, company, email))


application("Jessica", "Black", "JBlack@mail.com", "CZC Corporation", 890000, hire_date="September 2020")
