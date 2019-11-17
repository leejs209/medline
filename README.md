# Django를 이용한 보건실 플랫폼
# Infirmary consulting platform using Django
- Any Feedback is Welcome - While I already submitted the project with commmit `2853018` it doesn't mean that I'm not still interested in what I did right and what I did wrong! After all, this is my first time trying to develop a Django applications.

2019년 11월 17일
# 개발 계획서
## 프로젝트 요약
### 목적
  학교에서 보건실은 매일 일반적인 병원보다 많은 학생들의 건강을 책임지지만, 그에 맞먹는 체계적인 시스템을 갖추지 못하고 있다. A4용지를 자른 종이로 상담카드를 쓰고 그에 대해 상담과 처방받는 것이 그 대표적인 예이다. 이러한 시스템은 학생의 상태에 따른 체계적인 분석이 힘들고, 학생의 관점에서도 불편하다는 단점을 가진다. 따라서 나는 보건실의 상담신청과 간단한 약의 처방, 그리고 학생 건강 기록까지 관리할 수 있는 하나의 플랫폼을 만들고자 하였다.
### 목표
  이 프로젝트를 진행함으로써 나는
	(1) 보건실 상담·처방 절차를 단순화하는 것
	(2) 관리자(보건 선생님)의 관리는 단순하게 하는 것
	(3) 상담 및 건강 기록을 체계적으로 관리할 수 있는 시스템을 만드는 것
을 성취하는 것을 목표로 한다.
### 해결책
  앞서 설명한 이러한 시스템을 “대륜고등학교 Medline”이라 이름짓고, Django와 Python을 이용한 Web App으로 플랫폼을 구현하였다. 

# 개요
## 프로젝트 구성
  나는 학생과 앱 사이의 상호작용에 이용되는 앱인 medline 과 관리자의 사용을 위한 앱인 medicalhub로 프로젝트를 나누어 설정하였다. 또한 user앱을 통해 Django에서 기본적으로 제공되는 사용자 모델을 확장하였다. 
  Django는 MVC(Model-View-Controller) 모델을 변환하여 MTV (Model-Template-View)를 이용하는데 그에 따라 나누어 설명하겠다.
### DB 구조 (Model)
  우선 medline 앱의 모델로는 상담 내역을 저장하는 모델인 consult와 처방된 약을 저장하는 PrescribedMedicine이 있다. 다음으로 medicalhub에는 처방할 수 있는 약의 종류를 저장하는 MedicineType가 있고, user 앱에는 Django의 AbstractUser를 계승해 CustomUser를 만들어 학년, 학반, 번호, 이름, 생년월일을 저장하였다.
  또한 일부 논리를 Model 안에 넣었다. 예를 들어 상담 내역에서 표시하는 짧을 메시지 (shortened_message)는 django의 @property를 이용해 저장하였다.
### HTML/CSS 디자인 (Template)
  나는 UI/UX 디자인을 위해 널리 알려지지는 않았지만 손쉬운 HTML/CSS 구성이 가능한 bulma를 사용하였다. 이를 위해 CDN(Content Delivery Network)로부터 .css 파일을 받았다. 또한 같은 스타일의 form을 구현하기 위해 django-bulma라는 이름의 module을 pip3를 통해 설치하였다.
### Python (View)
  주로 View에서 필요한 대부분의 논리를 구현하였다. 이들을 urls.py파일에 링크하여 필요한 파일을 클라이언트에게 전송한다.
### PWA
  django-pwa 패키지를 활용하여 PWA(Progressive Web App)를 만들었다. 그럼으로써 사용자가 자신의 스마트폰에 앱 형태로 웹 앱을 설치할 수 있게 하여 사용하기 쉽도록 하였다. 이 기능을 프로젝트 디렉토리에서 ‘python3 manage.py runserver 0.0.0.0:8000’ 을 실행한 이후 같은 네트워크상의 디바이스로 서버의 IP로 접속하면 확인할 수 있다.
### 기타 사항
  관리자 ID는 ‘admin’이고 비밀번호는 ‘rhksflwk’입니다.

### 참고문헌
https://docs.djangoproject.com/en/2.2/
https://bulma.io/documentation/
https://wsvincent.com/django-custom-user-model-tutorial/


# Ideas
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
