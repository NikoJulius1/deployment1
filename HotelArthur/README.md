# Booking API
## Projektoversigt

Denne Booking API er en Flask-baseret applikation til administration af hotelværelsesbookinger. Den gør det muligt for brugere at oprette, liste og eksportere bookinger samt integrere med en faktureringsservice til håndtering af tilknyttede omkostninger. API’en tjekker også tilgængelighed på værelser, inden en booking bekræftes, for at undgå overlap i reservationer.

**Funktioner**
Liste over Bookinger: Hent en liste over alle bookinger i JSON-format.
Opret Bookin: Tilføj en ny booking, hvis værelset er tilgængeligt, og send detaljer til faktureringsservicen.
Tjek Tilgængelighed: Bekræfter værelsets tilgængelighed ud fra bookingdatoer.
Eksporter Bookinger i CSV: Eksporter alle bookingsdata i CSV-format til ekstern behandling.
Endpoints
1. GET /bookings
Beskrivelse: Henter en liste over alle bookinger.
Respons: Returnerer en JSON-array med bookingoplysninger.

2. POST /bookings
Beskrivelse: Opretter en ny booking, hvis det ønskede værelse er tilgængeligt.
Request Body:
json
Kopier kode
{
    "roomnumber": 101,
    "category": "Standard single room",
    "checkin": "2024-11-01T14:00:00",
    "checkout": "2024-11-05T12:00:00"
}
Respons:
201 Created hvis bookingen blev oprettet.
409 Conflict hvis værelset ikke er tilgængeligt.
400 Bad Request hvis nødvendige felter mangler.

Integration med Faktureringsservice: Ved en succesfuld booking sendes en notifikation til faktureringsservicen med bookingdetaljer.

3. GET /bookings/export/csv
Beskrivelse: Eksporterer alle bookingsdata i CSV-format.
Respons: En downloadbar CSV-fil med bookingdata.
Eksempel: CSV’en inkluderer kolonner som id, roomnumber, category, isbooking, checkin, og checkout.
Vigtige Komponenter
Databaseforbindelse
Funktion: get_db_connection()
Formål: Styrer forbindelsen til SQLite-databasen reservation_database.db, som gemmer bookingsdata.

# Notifikation til Faktureringsservice
Funktion: notify_billing_service(booking_id, room_type, checkin, checkout)
Formål: Sender en POST-forespørgsel til en ekstern faktureringsservice (http://billing-service:5002/bills/update/{booking_id}) for at opdatere faktureringen i forbindelse med en ny booking.
Data der Sendes: room_type, checkin, og checkout
