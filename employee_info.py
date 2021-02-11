# these are just random names pls don't mind :)
"""This contains three dictionaries in which the email ids are linked with: 1.Passowords , 2.Employee codes, and 3.Their names"""
"""There is provision for adding and removing an employee and also for ptrinting the employee details"""
"""This file is imported to the main file"""

employee_dict = {
    "ramesh@abc.com": "ramesh123",
    "mohit@abc.com": "mohitkr07",
    "surendra@xyzmail.com": "surendraxp45",
    "vaishali@abc.com": "vaishali789",
    "janhavi@cpp.com": "janhavi0606",
}


def employee_details():
    print(employee_dict)


def add_employee(username: str, password: str):
    employee_dict[username] = password


def remove_employee(name: str):
    if name in employee_dict:
        employee_dict.pop(name)
    else:
        print("EMPLOYEE NOT FOUND.")


def supermarket_name(name: str):
    print(f"\t\t\t\t\t {name} \t\t\t\t\t")
    print()


employee_ids = {
    "ramesh@abc.com": 2799,
    "mohit@abc.com": 2801,
    "surendra@xyzmail.com": 7160,
    "vaishali@abc.com": 9899,
    "janhavi@cpp.com": 3317
}

employee_names = {
    "ramesh@abc.com": "RAMESH",
    "mohit@abc.com": "MOHIT",
    "surendra@xyzmail.com": "SURENDRA",
    "vaishali@abc.com": "VAISHALI",
    "janhavi@cpp.com": "JANHAVI"
}

# end 
