

## Challenge 1 ##
### Skill ###
Learning how to explore a webpage with the inspect editor

### Solution ###
Password hidden in HTML comment.


## Challenge 2 ##
### Skill ###
Learning to edit rendered page with the inspect editor.

### Solution ###
Remove disabled attributes from input fields, remove `visibiliy: hidden` from submit button.


## Challenge 3 ##
### Skill ###
Viewing Javascript console.

### Solution ###
Username and password printed to JS console.


## Challenge 4 ##
### Skill ###
Running code in Javascript console.

### Solution ###
Open console and run: `atob(login_details());`


## Challenge 5 ##
### Skill ###
Using a web proxy to view headers on requests.

### Solution ###
Flag is sent as header in response.


## Challenge 6 ##
### Skill ###
Intercepting and editing requests from the browser en-route to the web-server.

### Solution ###
Edit cookie `access-level`'s value from `user` to `admin`.


## Challenge 7 ##
### Skill ###
Using Burp interceptor and being able to send data to decoder.

### Solution ###
Inspect page response in burp interceptor, find cookie `super-secret-cookie`, send it's base64 contents to decoder.
Decoded text contains username and password.


## Challenge 8 ##
### Skill ###
Using Burp interceptor to capture traffic, sending to repeater and using repeater, sending to decoder and using decoder to edit and encode.

### Solution ###
Login to challenge 8 with user `user` and password `password`.
Inspect traffic with burp interceptor HTTP history and see `session-cookie` being set.
Send base64 session cookie to decoder, decond and realise it has the user in the cookie and the cookie is unencrypted.
Send inspected request to burp repeater, then send base64 cookie to decoder.
Decode base64 cookie in decoder, change `user` to `admin` and re-encode the cookie.
Copy and paste cookie into request in repeater, hit send.
See flag from admin login page sent back to user in response window.

## Challenge 9 ##
### Skill ###
Using Burp intruder to brute force logins using a wordlist of users and a wordlist of passwords.

### Solution ###
Use wordlists provided on the challenges list page.
First perform attack on usernames looking for a change in error - `user_wordlist.txt`.
Second put found username into username location and change attack to password field, again looking for error change - `password_wordlist.txt`.
Put in correct user and password into form and flag is show.


## Challenge 10 ##
### Skill ###
Using `dirb` to enumerate file and directories on a webserver.
