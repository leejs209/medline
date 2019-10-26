### Todo

- Backend
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
    - Add feature for admin-side medicine inventory management

- Client-side Emergency Streaming
    - Utilizing OpenCV Library?
- Add client-side notification to remind students to take medicine and add a checkmark
    - Should be done with HTML5 Notification, client-side app, SMS, or Internet Messaging (Facebook Message / KakaoTalk)
    - How to confirm that someone actually took the medicine?
        - Possibly, add a Machine Learning algorithm to make sure that the medicine is actually eaten
        - Or simply make it so that students can respond to the notification (e.g. "Did you take the medicine?")

### Optional
- Localised form verification messages
     - In Korean
- CAPTCHA
     - Stop BruteForce
- Client Panel in the Infirmary for students that have not made a reservation previously
    - Problably safe to use similar code from the app `medline`
- Achieve DRY 


- Add Inventory system for cataloging medicine [admin]
   - `medicineType` - general info about medicine
      - Name
      - Inventory status (Number) - Non-Unique
      - Description (storage requirements)
   - `medicine` - info about individual packages of medicine that needs to be inventorized
      - added_date
      - expire_date
      - storage_location --> with zone codes or dropdown menu
   - `prescribed`
      - `ManyToOne` of `medicine` model
      - `ManyToOne` of `CustomUser` model
    - Option to alert automatically when certain medicine is not enough
    - Maybe add expiration date for each medicine as well?
        - Then, would need to label each medicine pack with barcode / qr code (wasteful)
        - Or maybe, a reusable sticker with a unique barcode can be matched with medicine itself
### Issues

-  Bulma's navbar burger doesn't work
    - May need to implement seperate `dropdown` for mobile devices using the tag `is-mobile`
- Add types of messages to bulma's popup message
   - Use the tag `{% include 'medline/messages.html'`
   - e.g. `{% if tag == 'warning' %} is-warning {% elif ... %} {% endif%}`
- Make it so that only a limited amount oof `pending_consult` can be created for one user's instance
    - change the template accordingly to show only one object
    - throw an error if tries to make more than one appointment 
        - possibly remove the button to `consultform` upon already having made one
- Error after submitting consultation... Should be immediately fixed
