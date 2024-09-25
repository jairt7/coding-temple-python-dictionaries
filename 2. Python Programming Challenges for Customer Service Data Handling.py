# 2. Python Programming Challenges for Customer Service Data Handling
# Copied a bit of code from my to-do list program since it works, also copied a bit of code from tutoring

tickets = []

def welcome_menu():
    print("Customer Service Ticket Tracker")
    print("1. Open a new service ticket")
    print("2. Update the status of an existing ticket")
    print("3. Display all tickets")
    print("4. Display all open tickets")
    print("5. Display all closed tickets")
    print("6. Quit")

def what_to_do():
    what = input("What would you like to do? ").lower()
    if what == "1" or what == "open" or what == "open a new service ticket":
        return 1
    elif what == "2" or what == "update" or what == "update status" or what == "update the status of an existing ticket":
        return 2
    elif what == "3" or what == "display" or what == "display tickets" or what == "display all tickets":
        return 3
    elif what == "4" or what == "display open tickets" or what == "display all open tickets":
        return 4
    elif what == "5" or what == "display closed tickets" or what == "display all closed tickets":
        return 5
    elif what == "6" or what == "quit":
        return 6
    else:
        return 0
    
def open_ticket():
    global tickets
    title = input("Enter the title of the issue: ")
    description = input("Describe the issue: ")
    status = "open"
    tickets.append({ "title": title, "description": description, "status": status })

def update_ticket():
    global tickets
    ticket_number = int(input("Enter the number of the ticket whose status you'd like to update: "))
    try:
        if tickets[ticket_number - 1]['status'] == 'open':
            tickets[ticket_number - 1].update({'status' : 'closed'})
        else:
            tickets[ticket_number - 1].update({'status': 'open'})
        print("Status updated.")
    except ValueError:
        print("That's not a ticket number. Please enter a ticket number next time.")
    

def display_tickets():
    global tickets
    for idx, ticket in enumerate(tickets, start=1):
        print(f"Ticket #{idx}:")
        print(f"Title: {ticket['title']}")
        print(f"Description: {ticket['description']}")
        print(f"Status: {ticket['status']}")
        print("-" * 20)

def display_open_tickets():
    for idx, ticket in enumerate(tickets, start=1):
        if ticket['status'] == 'open':
            print(f"Ticket #{idx}:")
            print(f"Title: {ticket['title']}")
            print(f"Description: {ticket['description']}")
            print(f"Status: {ticket['status']}")
        else:
            continue

def display_closed_tickets():
    global tickets
    for idx, ticket in enumerate(tickets, start=1):
        if ticket['status'] == 'open':
            print(f"Ticket #{idx}:")
            print(f"Title: {ticket['title']}")
            print(f"Description: {ticket['description']}")
            print(f"Status: {ticket['status']}")
        else:
            continue

def main_program():
    global keep_going
    do_what = what_to_do()
    if do_what == 1:
        open_ticket()
    elif do_what == 2:
        update_ticket()
    elif do_what == 3:
        display_tickets()
    elif do_what == 4:
        display_open_tickets()
    elif do_what == 5:
        display_closed_tickets()
    elif do_what == 6:
        print("\nQuitting program.")
        keep_going = False
    elif do_what == 0:
        print("Invalid entry. Try a number from 1 to 5?")
    else:
        print("Oh no! Something went wrong.")


keep_going = True

while keep_going:
    welcome_menu()
    main_program()