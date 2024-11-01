import requests

# Fetch and print room bookings
def fetch_bookings():
    try:
        response = requests.get("http://booking-service:5001/bookings")
            #Tjekker for fejl, og "raiser" en status ved fejl
        response.raise_for_status()
        #Parser det til en liste af bookings. Parser JSON til Python object
        bookings = response.json()
        
        print("Rooms that need cleaning or preparation:")
        for booking in bookings:
            print("Booking data:", booking)  # Debugging. Display alt data for hver booking
            # Display vigtigste elementer ved hver booking
            print(f"ID: {booking[0]}, Room: {booking[1]}, Check-In: {booking[4]}, Check-Out: {booking[5]}")
            
            # Prompt til at markere done, ved hver booking
            mark_done = input("Mark this room as done? (y/n): ").strip().lower()
            if mark_done == 'y':
                mark_booking_done(booking[0])
     # Except i try-except. Error handling så den ikke crasher           
    except requests.exceptions.RequestException as e:
        print("Error fetching bookings:", e)

# PUT til at markere booking rengjort
def mark_booking_done(booking_id):
    try:
        #booking_id vælger specifikke værelse
        response = requests.put(f"http://booking-service:5001/bookings/{booking_id}/mark_done")
        #Tjekker for fejl, og "raiser" en status ved fejl
        response.raise_for_status()
        print("Booking marked as done.")
    except requests.exceptions.RequestException as e:
        print("Error marking booking as done:", e)

if __name__ == "__main__":
    fetch_bookings()