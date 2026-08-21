

# available seats
# input user number of seats
# check with available seats
# decrement booked seats from available seats and update
# display message if seats not available


class RailwayReservation:
    available_seats = 50
    pnr_counter = 1001
    bookings = {}

    def __init__(self,name,destination,seats,date):
        self.name = name
        self.destination = destination
        self.seats = seats
        self.date = date
        self.pnr = None 

    def booking_ticket(self):
        if self.seats > RailwayReservation.available_seats:
            print(f"Booking failed! Only {RailwayReservation.available_seats} seats available")
            return
        RailwayReservation.available_seats -= self.seats
        self.pnr = RailwayReservation.pnr_counter
        RailwayReservation.bookings[self.pnr] = self
        RailwayReservation.pnr_counter += 1
        print(f"""
            Ticket Booked Successfully!
            Name: {self.name}
            PNR: {self.pnr}
            Destination: {self.destination}
            Date: {self.date}
            Seats Booked: {self.seats}
            Remaining Seats: {RailwayReservation.available_seats}
        """)

    @classmethod
    def cancel_ticket(cls,pnr):
        if pnr not in cls.bookings:
            print("Invalid PNR. Cancellation failed.")

        booking = cls.bookings[pnr]
        cls.available_seats += booking.seats
        print(f"""
            Ticket Cancelled Successfully!
            PNR: {pnr}
            Seats Restored: {booking.seats}
            Available Seats: {cls.available_seats}
            """)


r1 = RailwayReservation("spoorthi","SK",2,"10/01/2027")
r2 = RailwayReservation("Spoo","SK",4,"10/01/2028")

r1.booking_ticket()
r2.booking_ticket()

# RailwayReservation.cancel_ticket(1001)