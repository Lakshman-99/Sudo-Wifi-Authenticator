import subprocess
import numpy as np
import pandas as pd
import time
import os
import requests
from pandas import DataFrame
import sys, select


# for deleting dump files

def dele():
	try:
		subprocess.run(['rm',' mon-01.csv'])
		subprocess.run(['rm',' mon-01.log.csv'])
		subprocess.run(['rm',' mon-01.kismet.csv'])
		subprocess.run(['rm',' mon-01.kismet.netxml'])
		subprocess.run(['rm',' mon-01.cap'])
	except:
		print(" ")


print(" ")
print(" ")


print("  . '   .        __        .   ' .        >> Sudo Wifi Authenticator 1.0         ")
print(" :     :   '    (||)   '    :     :       >> A wifi adminstrator.                ")
print(" :     :   '    /--\   '    :     :       >> Maintained by Code Sploit.          ")
print("  ' .   '      /----\      '    .'                                               ")


print(" ")
print(" ")


# step-1 : enabling monitor mode!
global iface

print("[+] Enter your wifi adapter name[1-4] : ")
print("[+] 1.wlan0 ")
print("[+] 2.wlan0mon ")
print("[+] 3.wlan1 ")
print("[+] 4.wlan2 ")
print("[+] 5.wlan3 ")        
cc= int(input())
if(cc==1):
	iface= 'wlan0' 
elif(cc==2):
	iface= 'wlan1' 
elif(cc==3):
	iface= 'wlan2'    
elif(cc==4):
	iface= 'wlan3'    
else:
	print("Select a valid interface!! (default=wlan0) ")                                                                            #input interface supporting monitor mode    
subprocess.call(f'airmon-ng start {iface}', shell=True)                                                                            #changing to mode monitor         


##################################
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()
   
   
# Driver's code
# Printing CWD before
current_path()
##################################
print(" ")
print("[+]   **************************Loading************************ ")


# step-2 : Displaying Wifi names


p = subprocess.Popen(['airodump-ng','-w hi', iface], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)       # line-1.1
time.sleep(10)                                                                                                                    # line-1.2
p.kill()                                                                                                                          # line-1.3 running airodump-ng



df=pd.read_csv(" hi-01.csv", usecols=[0,13,3])                                                                 
data=df.dropna()
y=np.array(data)
z=y.shape[0]
c=y[:,2]
ch=y[:,1]
v=y[:,0]
d={}
cd={}
for i in range(z):
	di={c[i]:v[i]}
	dp={c[i]:ch[i]}
	d.update(di)
	cd.update(dp)
	
os.system('clear')
print(" ")
print("[+] Available wifi networks : ")
print(" ")

for i in range(c.size):                                                                                              # printing available wifi
	print(f"[+] {i+1}.", c[i])


op= int(input("[+] Select a wifi to start protection[options] : "))
global wifi
global bsid
wifi= c[op-1]
bsid= d.get(wifi) 
bsid=str(bsid)
bsid= bsid.strip() 
channel= cd.get(wifi)
channel=str(channel)
global cha
cha=channel.strip()

subprocess.run(['rm',' hi-01.csv'])
subprocess.run(['rm',' hi-01.log.csv'])
subprocess.run(['rm',' hi-01.kismet.csv'])
subprocess.run(['rm',' hi-01.kismet.netxml'])
subprocess.run(['rm',' hi-01.cap'])                                                                                                               # getting AP mac address( selecting wifi )





# step-3: connected user code



def myPeriodicFunction():
	os.system('clear')
	df=pd.read_csv(" mon-01.csv", usecols=[0])
	f= DataFrame(df)
	x=df.drop(0,0)
	x=x.drop(1,0)
	ij=np.array(x)
	su_us=ij
	su_no=x.shape[0]
	exc_val=su_no+1
	l=np.unique(ij)
	print("[+] ***********************Loading, please wait******************************* ")
	return su_us,su_no,exc_val                                                                            # Displaying devices connected to the selected AP (wifi) 


    
dele()

pp= subprocess.Popen([f'airodump-ng', iface , '--bssid', bsid , '--channel', cha ,'-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)              # monitoring specific AP (wifi)

for i in range(2):
	time.sleep(8)
	su_us,su_no,exc_val = myPeriodicFunction()



pp.kill()    
dele()
###############################################################
#sms function


def msg(mess):

	url = "https://www.fast2sms.com/dev/bulk"



	payload = f"sender_id=FSTSMS&message={mess}&language=english&route=p&numbers=6381675281,8667688729,9092269687,9498063020"

	headers = {
		'authorization': "B7UXClFIymn8MfJrzSD4ERs0Qd935WYT2NiVoHGhLbat1ucwAKno2XEcK8GIyTuh6Zlq3MUvHxYpFDm0",
		'Content-Type': "application/x-www-form-urlencoded",
		'Cache-Control': "no-cache",
		}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)
################################################################

#step-4: main functions


def bruteforce_usercheck(a,b,c,pre_mac,pre_no,pre_ex,count):
	qq=subprocess.Popen([f'airodump-ng', iface , '--bssid', bsid ,'--channel' , cha , '-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) 

	os.system('clear')
	print("                                                                  >>  Wi-Fi is under protection <<                              ")     
	print(" ")               
	print(" ") 
	print(" *********please wait, loading*********")
	print("[+] Connected Users in the Wi-Fi are, ")
	print(" ")
	
	if(count==6):
		ff.kill                                                                                       # this lines of code help the wifi adaptor to rest for 15 seconds after every 6 checks
		time.sleep(15)
		count=0
		return a,b,c,pre_mac,pre_no,pre_ex,count
	
	for i in range(2):
		time.sleep(7)
		try:
			df=pd.read_csv(" mon-01.csv", usecols=[0])                                           # this lines of code reads values of the captures data of a wifi
		except:
			qq.kill
			dele()
			time.sleep(10)
			return a,b,c,pre_mac,pre_no,pre_ex,count
	
	qq.kill()
	f= DataFrame(df)
	x=df.drop(0,0)
	x=x.drop(1,0)
	ij=np.array(x)
	us=ij
	no=x.shape[0]
	val=no+1
	l=np.unique(ij)
	for i in range(x.shape[0]):
		print(f"[+] {i+1})",l[i])                                                                     # this prints the connected users of a wifi
		
	k=0

	temp =[]
		
	for i in a:
    		if(i in us): 
        		temp.append(i)                                                                         # checking the current user with the previous iteration users
        		
	a=np.array(temp)
	a=a.reshape(-1,1)
	b=a.shape[0]
	c=b+1
	
	new_bsid=[]
	for i in us:
    		if((i in pre_mac)): 
        		continue                                                                              # checking new devices connecting to the wifi
    		else:
        		new_bsid.append(i)
        
	new_bsid=np.array(new_bsid)
	us=np.unique(us)
	pre_mac=np.unique(pre_mac)
	
	for i in us:
		if((i in pre_mac or no<pre_no)): 
			continue
		else:
			print("[+] New user detected: ",i)
			print("[+] (1/0) ")                                                                   # here the new user is put forword the screen
			ss= int(input())
			print(ss)
			oi=str(i)
			print(oi)
			if(ss==1):
				pass
			else:
				mess="SOMEONE ENTERED YOUR WIFI"
				msg(mess)
				os.system(f"python3 rem.py {oi} {iface}")
							               # you can allow or deny, if denied they are removed from the wifi network

	for i in range(0, len(us)):    
		for j in range(i+1, len(us)):  
			if(us[i] == us[j]): 
				mess="YOUR WIFI IS HACKED"
				msg(mess) 
				os.system(f"python3 rem.py {oi} {iface}")                                       # if found duplicate devices, tthe duplicate device is automatically removed from the network

	dele()
	time.sleep(2.5)
	return a,b,c,us,no,val,count



uss=su_us
noo=su_no
vaa=exc_val
mk=0

global qq
while (True):
	
	time.sleep(3)
	
	su_us,su_no,exc_val,uss,noo,vaa,mk = bruteforce_usercheck(su_us,su_no,exc_val,uss,noo,vaa,mk)                     # this will check infinitely, thus ensureing security to a wifi network.

	
	
	
	
	
