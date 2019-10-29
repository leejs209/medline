### Todo

- Custom user creation form for:
   - Localised form verification messages
        - In Korean
   - CAPTCHA
        - Stop BruteForce
   - Student Verifiation -> Possible solutions
        - __Barcode matching with School Library DB__
        - Manual checking by Infirmary T 
        - Automatic sign-up via default ID/PW
            - PW would need to be unique --> bithday, etc.
- Admin Panel
    - Should be easy to use
    - Can receive alerts and play Emergency Sound
    - <Probably isn't needed> Can scan QR Code containing a primaryKey of a consult object and show it on the panel
    - Can change status(`is_finished`) of object `consult` 
- Client-side Emergency Streaming
    - Utilizing OpenCV Library?
- Client Panel in the Infirmary for students that have not made a reservation previously
    - Problably safe to use similar code from the app `medline`
- Achieve DRY 
    - by making `pending_consult`, `finished_consult`, and `expired_consult` into one with context with a boolean value
        - mostly finished with `/medline/consult_column.html`
        
- Add feature for admin-side medicine inventory management

- Add model for prescribed medicine

- Add client-side notification to remind students to take medicine and add a checkmark
    - Should be done with HTML5 Notification, client-side app, SMS, or Internet Messaging (Facebook Message / KakaoTalk)
    - How to confirm that someone actually took the medicine?
        - Possibly, add a Machine Learning algorithm to make sure that the medicine is actually eaten
        - Or simply make it so that students can respond to the notification (e.g. "Did you take the medicine?")
        -  
- Add Inventory system for cataloging medicine [admin]
    - Option to add & delete medicine types
        - Not just medicine's amount, but also other associated metadata
        - Properties
            - Name
            - Inventory status (Number)
                - For whom it was prescribed for
            - 
            
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

-  Bulma's navbar burger doesn't work
    - may need to implement seperate menu for mobile devices using the tag `is-mobile`
- Add types of messages to bulma's popup message
    - e.g. `{% if tag == 'warning` %} is-warning {% elif ... %} {% endif%}`
- Make it so that only one `pending_consult` can be created
    - change the template accordingly to show only one object
    - throw an error if tries to make more than one appointment
        - possibly remove the button to `consultform` upon already having made one
