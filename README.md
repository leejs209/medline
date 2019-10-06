### Todo

- Custom user creation form for:
   - Localised form verification
        - In Korean
   - CAPTCHA
        - Stop BruteForce
   - Student Verifiation -> Possible solutions
        - Barcode matching with School Library DB
        - Manual checking by Infirmary T
        - Automatic sign-up via default ID/PW
            - PW would need to be unique --> bithday, etc.
        

- Create Modal Login Form
- Do something about the Login Form and Signup Form's CSS
    - possibly django-crispy-forms with bootstrap

### Issues

- `medline.views.consulthistory` linked with template `medline.consulthistory` keeps logging out when accessed.
-  