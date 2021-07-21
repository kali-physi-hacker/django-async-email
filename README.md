### Django Async Email Sending

##### Description 
A simple app written to demonstrate how to send emails
asynchronously on **pythonanywhere.com**.  
Currently, **pythonanywhere.com** doesn't support sending of emails asynchronously using threads
this example makes use of **django-rq**, a package that uses **rq**, a redis based task queuing package to send the email.


##### Usage 
The app doesn't include an interface. It basically makes use of django's management command extensions.
There is management command ---> send_email which can just be called:   
`python manage.py send_email`  to send a sample email