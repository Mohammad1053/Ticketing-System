from TicketingSystem import *


def main():
    # Create a TicketingSystem object
    system = TicketingSystem()
    system.load_events("events.txt")
    init(autoreset=True)
    while True:
        try:
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ".....MAIN MENU.....")
            print(Fore.YELLOW + Style.BRIGHT + "1- Admin Login")
            print(Fore.BLUE + Style.BRIGHT + "2- View Events")
            print(Fore.BLUE + Style.BRIGHT + "3- Reserve Ticket")
            print(Fore.BLUE + Style.BRIGHT + "4- Cancel Ticket")
            print(Fore.BLUE + Style.BRIGHT + "5- View My Tickets")
            print(Fore.RED + Style.BRIGHT + "6- Exit")
            print()

            choice = input(Fore.GREEN + Style.BRIGHT + "Enter your choice: ")

            if choice == '1':
                username = input(Fore.BLUE + Style.BRIGHT + "Username: ")
                password = input(Fore.BLUE + Style.BRIGHT + "Password: ")

                ascii_sum_user = 0
                ascii_sum_pass = 0
                for char in username:
                    ascii_sum_user += ord(char)
                for char_pas in password:
                    ascii_sum_pass += ord(char_pas)

                if ascii_sum_user == 521 and ascii_sum_pass == 202:
                    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "Login successful")
                    print(
                        Fore.GREEN + Style.BRIGHT + "------Hello & Welcome " + Fore.LIGHTGREEN_EX + "{ " + username + " }")

                    while True:

                        print(Fore.YELLOW + Style.BRIGHT + "1- Create New Event")
                        print(Fore.BLUE + Style.BRIGHT + "2- Overall Event Report")
                        print(Fore.BLUE + Style.BRIGHT + "3- Report of Tickets Sold in Date Range")
                        print(Fore.BLUE + Style.BRIGHT + "4- View Overall Event Report Chart")  # Add chart option
                        print(Fore.BLUE + Style.BRIGHT + "5- View Sales Report Chart")  # Add chart option
                        print(Fore.BLUE + Style.BRIGHT + "6- Report by event type")
                        print(Fore.RED + Style.BRIGHT + "7- Exit Admin Mode")
                        admin_choice = input(Fore.GREEN + Style.BRIGHT + "Select your option: ")

                        if admin_choice == '1':
                            while True:
                                try:
                                    title = input("Event Title: ")
                                    total_capacity = int(input("Total Capacity: "))
                                    print()
                                    date = input("Event Date (YYYY-MM-DD): ")

                                    system.create_event(title, total_capacity, date)
                                    system.save_events("events.txt")
                                    print()
                                    print(f"Event '{title}' successfully added.")
                                    break
                                except ValueError:
                                    print("Invalid input.")
                                    print()
                        elif admin_choice == '2':
                            reports = system.report()
                            for report in reports:
                                print(report)
                        elif admin_choice == '3':
                            start_date = input("Start date (YYYY-MM-DD): ")
                            end_date = input("End date (YYYY-MM-DD): ")

                            sales_reports = system.report_sales_in_date_range(start_date, end_date)
                            for report in sales_reports:
                                print(report)

                        elif admin_choice == '4':
                            system.report_chart()
                        elif admin_choice == '5':
                            start_date = input("Start date (YYYY-MM-DD): ")
                            end_date = input("End date (YYYY-MM-DD): ")

                            system.report_sales_in_date_range_chart(start_date, end_date)
                        elif admin_choice == '6':
                            system.report_by_event_type()
                        elif admin_choice == '7':
                            break

                        else:
                            print(Fore.RED + Style.BRIGHT + "Invalid option.")
                else:
                    print(Fore.RED + Style.BRIGHT + "**** Login failed ****")
                    print(Fore.YELLOW + Style.BRIGHT + "<<<Please try again>>>")

            elif choice == '2':
                events = system.view_events()
                for event in events:
                    print(event)

            elif choice == '3':
                national_id = input("Enter your National ID: ")
                event_title = input("Enter the event title: ")
                if system.reserve_ticket(national_id, event_title):

                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Ticket reservation successful")
                else:
                    print(Fore.RED + Style.BRIGHT + "Failed to reserve ticket")


            elif choice == '4':
                national_id = input("Enter your National ID: ")
                event_title = input("Enter the title of the event to cancel: ")
                if system.cancel_ticket(national_id, event_title):
                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Ticket cancellation successful")
                else:
                    print(Fore.RED + Style.BRIGHT + "Failed to cancel ticket")

            elif choice == '5':
                national_id = input("Enter your National ID: ")
                if not national_id.isdigit():
                    print(Fore.RED + Style.BRIGHT + "Invalid input.")
                tickets = system.tickets_by_user(national_id)
                print(Fore.MAGENTA + Style.BRIGHT + "Your Tickets:")
                for ticket in tickets:
                    print(ticket)

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print(Fore.RED + Style.BRIGHT + "Invalid option.")

        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Invalid option.")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()