## links :

 ## DRF : 
 ### https://www.django-rest-framework.org/

 ## simple-jwt-auth: 
 ### https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

### Note 01 : token is used to sign requests , HTTP requests are STATELESS => means u have to authenticate every single request ( generally in the frontend is: bearer token .. in the headers )

### Note 02 : login here changed .. from djago web browser default which is sessions based ... to token based which is more suitable for API server 

### NOTE 03 : Throttle is genereally good to avoid  server spamming HOWEVER i guess still there is a problem .. throttle policy prevent from getting views executed and response ...but they don't prevent from sending request.. 
### final NOTE : DRF can decode the token automatically so u only set the correct permissions in the views to protect critical sources
