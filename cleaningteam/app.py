import requests

# Fetch and print room bookings
def fetch_bookings():
    try:
        response = requests.get("http://host.docker.internal:5001/bookings")
        response.raise_for_status()
        bookings = response.json()
        
        print("Rooms that need cleaning or preparation:")
        for booking in bookings:
            print("Booking data:", booking)  # Debugging line to check each booking
            # Display bookings as they are since we don't have `is_cleaned`
            print(f"ID: {booking[0]}, Room: {booking[1]}, Check-In: {booking[4]}, Check-Out: {booking[5]}")
            
            # Prompt to mark the room as done
            mark_done = input("Mark this room as done? (y/n): ").strip().lower()
            if mark_done == 'y':
                mark_booking_done(booking[0])
                
    except requests.exceptions.RequestException as e:
        print("Error fetching bookings:", e)

# Mark a booking as done
def mark_booking_done(booking_id):
    try:
        response = requests.put(f"http://host.docker.internal:5001/bookings/{booking_id}/mark_done")
        response.raise_for_status()
        print("Booking marked as done.")
    except requests.exceptions.RequestException as e:
        print("Error marking booking as done:", e)

if __name__ == "__main__":
    fetch_bookings()