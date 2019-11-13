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
    - Can receive alerts
    - Can change status(`is_finished`) of object `consult` 
        - add a check mark via `form`
     - medicine inventory management
    
- Client Panel
    - For students that have not made a reservation previously
        - Problably safe to use similar code from the app `medline`
    - For students that have already made a reservation
        - <Probably isn't needed> Can scan QR Code containing a primaryKey of a consult object and show it on the panel

- Client notification to remind students to take medicine
    - HTML5 Notification
    - How to confirm that someone actually took the medicine?
        - Or simply make it so that students can respond to the notification (e.g. "Did you take the medicine?")
        
- Add feature to select date range of prescription inside consult

### Issues
- Add types of messages to bulma's popup message
    - e.g. `{% if tag == 'warning' %} is-warning {% elif ... %} {% endif%}`
- Make it so that only one `pending_consult` can be created
    - change the template accordingly to show only one object
    - throw an error if tries to make more than one appointment
        - possibly remove the button to `consultform` upon already having made one
