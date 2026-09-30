import tkinter as tk
from tkinter import ttk, messagebox


# -------------------------------------------------------
# AIRPORT MANAGEMENT SYSTEM
# -------------------------------------------------------

class AirportManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Airport Management System")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        # ---------------- FLIGHT DATA ----------------
        self.flights = [
            {
                "number": "AI101",
                "airline": "Air India",
                "source": "Delhi",
                "destination": "Mumbai",
                "time": "08:30 AM",
                "seats": 45
            },
            {
                "number": "6E202",
                "airline": "IndiGo",
                "source": "Mumbai",
                "destination": "Bangalore",
                "time": "11:45 AM",
                "seats": 38
            },
            {
                "number": "UK303",
                "airline": "Vistara",
                "source": "Delhi",
                "destination": "Kolkata",
                "time": "02:15 PM",
                "seats": 28
            },
            {
                "number": "SG404",
                "airline": "SpiceJet",
                "source": "Hyderabad",
                "destination": "Delhi",
                "time": "05:30 PM",
                "seats": 32
            },
            {
                "number": "6E505",
                "airline": "IndiGo",
                "source": "Bangalore",
                "destination": "Chennai",
                "time": "08:00 PM",
                "seats": 40
            },
            {
                "number": "AI606",
                "airline": "Air India",
                "source": "Chennai",
                "destination": "Delhi",
                "time": "09:45 PM",
                "seats": 25
            }
        ]

        self.passengers = []

        self.create_header()
        self.create_menu()
        self.create_main_area()
        self.show_home()

    # -------------------------------------------------------
    # HEADER
    # -------------------------------------------------------

    def create_header(self):

        header = tk.Frame(self.root, bg="#17365D", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="✈️ AIRPORT MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"),
            bg="#17365D",
            fg="white"
        )
        title.pack(pady=20)

    # -------------------------------------------------------
    # MENU
    # -------------------------------------------------------

    def create_menu(self):

        menu = tk.Frame(self.root, bg="#EAF2F8", height=55)
        menu.pack(fill="x")

        buttons = [
            ("Home", self.show_home),
            ("Flights", self.show_flights),
            ("Book Ticket", self.book_ticket_window),
            ("Cancel Ticket", self.cancel_ticket_window),
            ("Passengers", self.show_passengers),
            ("Exit", self.exit_program)
        ]

        for text, command in buttons:

            button = tk.Button(
                menu,
                text=text,
                command=command,
                font=("Arial", 10, "bold"),
                bg="white",
                fg="#17365D",
                relief="flat",
                padx=18,
                pady=8,
                cursor="hand2"
            )

            button.pack(side="left", padx=5, pady=8)

    # -------------------------------------------------------
    # MAIN AREA
    # -------------------------------------------------------

    def create_main_area(self):

        self.main_frame = tk.Frame(
            self.root,
            bg="white"
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def clear_main(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # -------------------------------------------------------
    # HOME PAGE
    # -------------------------------------------------------

    def show_home(self):

        self.clear_main()

        welcome = tk.Label(
            self.main_frame,
            text="Welcome to the Airport Management System",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="#17365D"
        )
        welcome.pack(pady=30)

        info = tk.Label(
            self.main_frame,
            text=(
                "Manage flights, book tickets, cancel reservations\n"
                "and view passenger information easily."
            ),
            font=("Arial", 13),
            bg="white",
            fg="#555555",
            justify="center"
        )
        info.pack(pady=10)

        # Statistics
        stats_frame = tk.Frame(
            self.main_frame,
            bg="white"
        )
        stats_frame.pack(pady=40)

        total_flights = len(self.flights)
        total_passengers = len(self.passengers)

        available_seats = sum(
            flight["seats"] for flight in self.flights
        )

        self.create_stat_card(
            stats_frame,
            "TOTAL FLIGHTS",
            total_flights,
            0
        )

        self.create_stat_card(
            stats_frame,
            "PASSENGERS",
            total_passengers,
            1
        )

        self.create_stat_card(
            stats_frame,
            "AVAILABLE SEATS",
            available_seats,
            2
        )

    # -------------------------------------------------------
    # STAT CARD
    # -------------------------------------------------------

    def create_stat_card(self, parent, title, value, column):

        card = tk.Frame(
            parent,
            bg="#F4F6F7",
            width=220,
            height=120,
            relief="ridge",
            bd=1
        )

        card.grid(
            row=0,
            column=column,
            padx=15
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Arial", 10, "bold"),
            bg="#F4F6F7",
            fg="#666666"
        ).pack(pady=(20, 5))

        tk.Label(
            card,
            text=str(value),
            font=("Arial", 24, "bold"),
            bg="#F4F6F7",
            fg="#17365D"
        ).pack()

    # -------------------------------------------------------
    # FLIGHT PAGE
    # -------------------------------------------------------

    def show_flights(self):

        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Available Flights",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#17365D"
        ).pack(anchor="w", pady=(0, 15))

        columns = (
            "number",
            "airline",
            "source",
            "destination",
            "time",
            "seats"
        )

        table = ttk.Treeview(
            self.main_frame,
            columns=columns,
            show="headings",
            height=18
        )

        table.heading("number", text="Flight No.")
        table.heading("airline", text="Airline")
        table.heading("source", text="From")
        table.heading("destination", text="To")
        table.heading("time", text="Departure")
        table.heading("seats", text="Available Seats")

        table.column("number", width=100)
        table.column("airline", width=150)
        table.column("source", width=130)
        table.column("destination", width=130)
        table.column("time", width=130)
        table.column("seats", width=130)

        for flight in self.flights:

            table.insert(
                "",
                "end",
                values=(
                    flight["number"],
                    flight["airline"],
                    flight["source"],
                    flight["destination"],
                    flight["time"],
                    flight["seats"]
                )
            )

        table.pack(fill="both", expand=True)

    # -------------------------------------------------------
    # BOOK TICKET
    # -------------------------------------------------------

    def book_ticket_window(self):

        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Book a Flight Ticket",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#17365D"
        ).pack(anchor="w", pady=(0, 20))

        form = tk.Frame(
            self.main_frame,
            bg="white"
        )
        form.pack()

        # Name
        tk.Label(
            form,
            text="Passenger Name:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        name_entry = tk.Entry(
            form,
            width=35,
            font=("Arial", 11)
        )
        name_entry.grid(row=0, column=1, pady=10)

        # Age
        tk.Label(
            form,
            text="Age:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        age_entry = tk.Entry(
            form,
            width=35,
            font=("Arial", 11)
        )
        age_entry.grid(row=1, column=1, pady=10)

        # Phone
        tk.Label(
            form,
            text="Phone Number:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        phone_entry = tk.Entry(
            form,
            width=35,
            font=("Arial", 11)
        )
        phone_entry.grid(row=2, column=1, pady=10)

        # Flight selection
        tk.Label(
            form,
            text="Select Flight:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

        flight_options = [
            f"{flight['number']} - {flight['airline']} "
            f"({flight['source']} → {flight['destination']})"
            for flight in self.flights
        ]

        flight_combo = ttk.Combobox(
            form,
            values=flight_options,
            width=32,
            state="readonly"
        )
        flight_combo.grid(row=3, column=1, pady=10)

        # Book button
        def confirm_booking():

            name = name_entry.get().strip()
            age = age_entry.get().strip()
            phone = phone_entry.get().strip()
            selected = flight_combo.get()

            if not name or not age or not phone or not selected:
                messagebox.showwarning(
                    "Missing Information",
                    "Please fill in all the details."
                )
                return

            if not age.isdigit():
                messagebox.showwarning(
                    "Invalid Age",
                    "Please enter a valid age."
                )
                return

            if not phone.isdigit():
                messagebox.showwarning(
                    "Invalid Phone",
                    "Please enter a valid phone number."
                )
                return

            flight_no = selected.split(" - ")[0]

            selected_flight = None

            for flight in self.flights:

                if flight["number"] == flight_no:
                    selected_flight = flight
                    break

            if selected_flight["seats"] <= 0:

                messagebox.showerror(
                    "Flight Full",
                    "Sorry, no seats are available on this flight."
                )

                return

            selected_flight["seats"] -= 1

            passenger = {
                "name": name,
                "age": age,
                "phone": phone,
                "flight": flight_no
            }

            self.passengers.append(passenger)

            messagebox.showinfo(
                "Booking Successful",
                f"Ticket booked successfully!\n\n"
                f"Passenger: {name}\n"
                f"Flight: {flight_no}\n"
                f"Airline: {selected_flight['airline']}\n"
                f"Route: {selected_flight['source']} → "
                f"{selected_flight['destination']}"
            )

            self.show_home()

        tk.Button(
            self.main_frame,
            text="BOOK TICKET",
            command=confirm_booking,
            font=("Arial", 11, "bold"),
            bg="#17365D",
            fg="white",
            width=20,
            pady=10,
            relief="flat",
            cursor="hand2"
        ).pack(pady=25)

    # -------------------------------------------------------
    # CANCEL TICKET
    # -------------------------------------------------------

    def cancel_ticket_window(self):

        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Cancel Ticket",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#17365D"
        ).pack(anchor="w", pady=(0, 25))

        box = tk.Frame(
            self.main_frame,
            bg="white"
        )
        box.pack()

        tk.Label(
            box,
            text="Passenger Name:",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, padx=10, pady=10)

        name_entry = tk.Entry(
            box,
            width=35,
            font=("Arial", 11)
        )
        name_entry.grid(row=0, column=1, pady=10)

        def cancel():

            name = name_entry.get().strip()

            if not name:

                messagebox.showwarning(
                    "Enter Name",
                    "Please enter the passenger name."
                )

                return

            found_passenger = None

            for passenger in self.passengers:

                if passenger["name"].lower() == name.lower():
                    found_passenger = passenger
                    break

            if found_passenger is None:

                messagebox.showerror(
                    "Not Found",
                    "No booking was found for this passenger."
                )

                return

            flight_number = found_passenger["flight"]

            for flight in self.flights:

                if flight["number"] == flight_number:
                    flight["seats"] += 1
                    break

            self.passengers.remove(found_passenger)

            messagebox.showinfo(
                "Ticket Cancelled",
                "The ticket has been cancelled successfully."
            )

            self.show_home()

        tk.Button(
            self.main_frame,
            text="CANCEL TICKET",
            command=cancel,
            font=("Arial", 11, "bold"),
            bg="#A93226",
            fg="white",
            width=20,
            pady=10,
            relief="flat",
            cursor="hand2"
        ).pack(pady=25)

    # -------------------------------------------------------
    # PASSENGER PAGE
    # -------------------------------------------------------

    def show_passengers(self):

        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Passenger Details",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#17365D"
        ).pack(anchor="w", pady=(0, 15))

        if len(self.passengers) == 0:

            tk.Label(
                self.main_frame,
                text="No tickets have been booked yet.",
                font=("Arial", 12),
                bg="white",
                fg="#777777"
            ).pack(pady=80)

            return

        columns = (
            "name",
            "age",
            "phone",
            "flight",
            "airline"
        )

        table = ttk.Treeview(
            self.main_frame,
            columns=columns,
            show="headings",
            height=18
        )

        table.heading("name", text="Passenger Name")
        table.heading("age", text="Age")
        table.heading("phone", text="Phone")
        table.heading("flight", text="Flight")
        table.heading("airline", text="Airline")

        table.column("name", width=200)
        table.column("age", width=80)
        table.column("phone", width=160)
        table.column("flight", width=100)
        table.column("airline", width=150)

        for passenger in self.passengers:

            flight_name = ""

            for flight in self.flights:

                if flight["number"] == passenger["flight"]:
                    flight_name = flight["airline"]
                    break

            table.insert(
                "",
                "end",
                values=(
                    passenger["name"],
                    passenger["age"],
                    passenger["phone"],
                    passenger["flight"],
                    flight_name
                )
            )

        table.pack(fill="both", expand=True)

    # -------------------------------------------------------
    # EXIT
    # -------------------------------------------------------

    def exit_program(self):

        result = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if result:
            self.root.destroy()


# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------

root = tk.Tk()

app = AirportManagementSystem(root)

root.mainloop()