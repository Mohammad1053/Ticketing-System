from colorama import Fore, Style


class Event:

    def __init__(self, title, total_capacity, remaining_capacity, date):
        self.title = title
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.date = date

    def reserve_ticket(self):
        """Attempts to reserve a ticket for the event."""
        if self.remaining_capacity > 0:
            submit = input(Fore.YELLOW + Style.BRIGHT + "do you want to submit (yes/no) ")
            print(Fore.YELLOW + Style.BRIGHT + f"{self.remaining_capacity} ticket have remaining capacity")
            if submit == "yes":
                self.remaining_capacity -= 1
                return True
            elif submit == "no":
                self.remaining_capacity = self.remaining_capacity
                return False

    def cancel_ticket(self):
        """Increases remaining capacity by 1, effectively canceling a ticket."""
        self.remaining_capacity += 1

    def __str__(self):
        return Fore.LIGHTBLUE_EX + Style.BRIGHT + f"{self.title} - Date: {self.date} - Remaining Capacity: {self.remaining_capacity}"