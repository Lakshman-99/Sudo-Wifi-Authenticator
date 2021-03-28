# Sudo-Wifi-Authenticator

DESCRIPTION: 

This is an application which tackles the anonymous users in the domestic WiFi. This is a Linux based application.

PREREQUISITES: 

->Wi-fi router 

->Wi-fi adapter which supports monitor mode 

->Computer/Laptop 

HOW IT WILL HELP ?

This is an application which prevents the domestic WiFI from man in the middle (MITM) attacks.
Whenever a hacker tries to connect to the domestic WiFi ,
The super user (or the already connected user) gets a notification from this application. 
If you find the newly entering user anonymous or not genuine you can deny the connection and block that user.
If you find the user genuine or trustworthy you can accept the user. 
This gives a total security to the domestic WiFi. 

HOW IT WORKS:

Firstly the program asks for interface(default:wlan0). Then you have to select the wifi available near you. 
That's it, now the program completely monitor the selected network. Whenever someone connects your network, you
are notified with their MAC address, you allow or deny(1/0). If you allow he continues to stay in the network,
else you deny, he's blocked(deauthenticated) from that network. When you DENY someone, you can conclude that 
someone hacked your wifi password and its time to set a new strong password. This offers a complete security 
against MITM attacks.

INSTALLATION:

Go to the github repository and download the zip file or extract the file contents
using clone link.Then directly run the software(SudoAuth.py) on kali linux OS.

DEPENDENCIES: 

->This software runs on Kali Linux OS. 

->Air crack -ng tool is required for this software to run on other Linux operating systems.

->Make sure you have following python libraries such as subprocess,numpy,pandas,os,time etc.

LANGUAGES USED: 

->Front end - Python (Tkinter) 

->Back end – Python 3.8 

FUTURE PLANS ON THIS PROJECT:

The team code sploit is trying to connect this working application in a
GUI based application and will be released in later versions of the application. 
Next we try to implement this in every household which gives the security over the WiFi.
We're working on implementing this software in Windows os and Mac os.

TECHNOLOGIES USED: 

->Ethical hacking 

DEVELOPED BY:

TEAM : CODE SPLOIT
S.Lakshman - slakshman664@gmail.com
M.Kartik - muralikartik01@gmail.com
B.K.Nandha Kumar - awesomenandha@gmail.com
S.Shrinath - shrinathsrinivasan@gmail.com
