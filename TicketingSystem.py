import matplotlib.pyplot as plt
from Event import Event
from colorama import *


class TicketingSystem:

    def __init__(self):

        self.events = []
        self.tickets = {}  # Key: National ID, Value: List of reserved tickets

    def load_events(self, filename):
        """Loads events from a file."""
        with open(filename, 'r') as file:
            for line in file:
                title, total_capacity, remaining_capacity, date = line.strip().split(',')
                event = Event(title, int(total_capacity), int(remaining_capacity), date)
                self.events.append(event)

    def save_events(self, filename):
        """Saves the current events to a file."""
        with open(filename, 'w') as file:
            for event in self.events:
                file.write(f"{event.title},{event.total_capacity},{event.remaining_capacity},{event.date}\n")

    def create_event(self, title, total_capacity, date):
        """Creates a new Event object and adds it to the events list."""
        event = Event(title, total_capacity, total_capacity, date)
        self.events.append(event)

    def view_events(self):
        """Returns the list of events."""
        return self.events

    def reserve_ticket(self, national_id, event_title):
        """Attempts to reserve a ticket for a user."""
        for event in self.events:
            if event.title == event_title and event.reserve_ticket():
                self.tickets.setdefault(national_id, []).append(event_title)
                return True
        return False

    def cancel_ticket(self, national_id, event_title):
        """Cancels a ticket for the user."""
        if national_id in self.tickets and event_title in self.tickets[national_id]:
            self.tickets[national_id].remove(event_title)
            for event in self.events:
                if event.title == event_title:
                    event.cancel_ticket()
                    return True
        return False

    def tickets_by_user(self, national_id):
        """Returns a list of events the user has tickets for."""
        return self.tickets.get(national_id, [])

    def report_by_event_type(self):
        """Generates a report of event details by event type."""
        event_types = {}
        for event in self.events:
            event_type = event.title.split(' - ')[0]  # Assuming event type is before the ' - '
            event_types.setdefault(event_type, []).append(event)

        report_data = []
        for event_type, events in event_types.items():
            tickets_sold = 0
            for event in events:
                tickets_sold += event.total_capacity - event.remaining_capacity
            report_data.append({
                'Event Type': event_type,
                'Tickets Sold': tickets_sold
            })
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f" {report_data}")

    def report(self):
        """Generates a report of event details."""
        report_data = []
        for event in self.events:
            report_data.append({
                'Event Title': event.title,
                'Tickets Sold': event.total_capacity - event.remaining_capacity,
                'Remaining Tickets': event.remaining_capacity,
                'Event Date': event.date
            })
        return report_data

    def report_sales_in_date_range(self, start_date, end_date):
        """Generates a report for events in specified date range."""
        sales_report = []
        for event in self.events:
            if start_date <= event.date <= end_date:
                sales_report.append({
                    'Event Title': event.title,
                    'Tickets Sold': event.total_capacity - event.remaining_capacity
                })
        return sales_report

    def report_chart(self):
        """Displays a chart of the overall event report."""
        report_data = self.report()
        event_titles = [data['Event Title'] for data in report_data]
        tickets_sold = [data['Tickets Sold'] for data in report_data]

        plt.figure(figsize=(10, 6))  # Adjust chart size if needed
        plt.bar(event_titles, tickets_sold, color=['red', 'green', 'blue'])
        plt.xlabel('Event Titles')
        plt.ylabel('Tickets Sold')
        plt.title('Overall Event Report')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to avoid overlapping elements
        plt.show()

    def report_sales_in_date_range_chart(self, start_date, end_date):
        """Displays a chart of tickets sold in a date range."""
        sales_report = self.report_sales_in_date_range(start_date, end_date)
        event_titles = [data['Event Title'] for data in sales_report]
        tickets_sold = [data['Tickets Sold'] for data in sales_report]

        plt.figure(figsize=(20, 16))  # Adjust chart size if needed
        plt.bar(event_titles, tickets_sold, color=['red', 'green', 'blue'])
        plt.xlabel('Event Titles')
        plt.ylabel('Tickets Sold')
        plt.title(f'Tickets Sold between {start_date} and {end_date}')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to avoid overlapping elements
        plt.show()
