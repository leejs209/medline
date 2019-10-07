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
    - Can scan QR Code containing a primaryKey of a consult object and show it on the panel
- Client-side Emergency Streaming
    - Utilizing OpenCV Library
- seperate consult into reserved, expired, and completed
    - use F to compare dates (https://stackoverflow.com/questions/12380448/how-to-create-a-django-queryset-filter-comparing-two-date-fields-in-the-same-mod)
    - add flag to `consult` to partition into categories
        - fiture out how to update status when date passes
- Client Panel in the Infirmary for students that have not made a reservation previously
    - Problably safe to use similar code from the app `medline`

### Issues

-  Bulma's navbar burger doesn't work
    - may need to implement seperate menu for mobile devices using the tag `is-mobile`
- Add types of messages to bulma's popup message
    - e.g. `{% if tag == 'warning` %} is-warning {% elif ... %} {% endif%}`
