### Todo

- Custom user creation form for:
   - CAPTCHA
        - Stop BruteForce
   - Student Verifiation -> Possible solutions
        - __Barcode matching with School Library DB__
        - Manual checking by Infirmary T 
        - Automatic sign-up via default ID/PW
            - PW would need to be unique --> birthday, etc.
        - Phone number verification
        
- Admin Panel
    - Can receive alerts and play Emergency Sound
    - Can change status(`is_finished`) of object `consult` 
        - add a check mark via `form`
     - medicine inventory management

- Client-side Emergency Streaming
    - Utilizing OpenCV Library?
    
- Client Panel
    - For students that have not made a reservation previously
        - Problably safe to use similar code from the app `medline`
    - For students that have already made a reservation
        - <Probably isn't needed> Can scan QR Code containing a primaryKey of a consult object and show it on the panel

- Add model for prescribed medicine

- Client notification to remind students to take medicine
    - HTML5 Notification
    - How to confirm that someone actually took the medicine?
        - Possibly, add a Machine Learning algorithm to make sure that the medicine is actually eaten
        - Or simply make it so that students can respond to the notification (e.g. "Did you take the medicine?")
- Add Inventory system for cataloging medicine [admin]
    - medicineType
        - Name
        - description
        - Barcode
    - medicinePackage
        - number
        - location            
    - Option to alert automatically when certain medicine is not enough
    - Maybe add expiration date for each medicine as well?
        - Then, would need to label each medicine pack with barcode / qr code (wasteful)
        - Or maybe, a reusable sticker with a unique barcode can be matched with medicine 
        
- Add option to delete user to protect personal information
    - Show a message that all their `consult` and `prescription` data will be gone
    - data export option if enough time (as PDF)
    
- Add option to print `consult` and `prescription`
    - https://docs.djangoproject.com/en/2.2/howto/outputting-pdf/
    

### Issues
- Need to add `edit_consult` feature on clicked
- Add types of messages to bulma's popup message
    - e.g. `{% if tag == 'warning` %} is-warning {% elif ... %} {% endif%}`
- Make it so that only one `pending_consult` can be created
    - change the template accordingly to show only one object
    - throw an error if tries to make more than one appointment
        - possibly remove the button to `consultform` upon already having made one
