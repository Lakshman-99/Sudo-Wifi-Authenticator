import subprocess
import numpy as np
import pandas as pd
import time
import os
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
print(" :     :   '    /--\   '    :     :       >> Maintained by code sploit.          ")
print("  ' .   '      /----\      '    .'                                               ")


print(" ")
print(" ")


# step-1 : enabling monitor mode!

print("[+] Enter your wifi adapter name[1-4] : ")
print("[+] 1.wlan0 ")
print("[+] 2.wlan1 ")
print("[+] 3.wlan2 ")
print("[+] 4.wlan3 ")        
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
subprocess.call(['airmon-ng', 'start' , iface ])                                                                  #changing to mode monitor         




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
wifi= c[op-1]
bsid= d.get(wifi)  
channel= cd.get(wifi)
channel=str(channel)


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
	#for i in range(x.shape[0]):
	#	print(l[i])
	print("[+] ***********************Loading, please wait******************************* ")
	return su_us,su_no,exc_val                                                                            # Displaying devices connected to the selected AP (wifi) 


    
dele()
pp= subprocess.Popen(['airodump-ng', iface , '--bssid', bsid ,'-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)             # monitoring specific AP (wifi)

for i in range(2):
	time.sleep(8)
	su_us,su_no,exc_val = myPeriodicFunction()


pp.kill()    
dele()

# su-us= super user mac addresses( genuine users/ existing users )
# su_no= no.of super user 
# exc_val= conditional value. ( for if condition ) 




# step 4: deauthentication



def de_auth(ap,tar,inter):         # pass ap= access point (wifi)  mac address, tar= target client (hacker) mac address, inter= interface wifi adaptor ( supporting monitor mode ).
	da= subprocess.Popen(['aireplay-ng', '--deauth', '10', '-a', ap ,'-c', tar, inter ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)         # deauthentication attack.
    



# step-5 increment
"""
def counter():
	ss,o,p = select.select( [sys.stdin], [],[], 15 )

	if (ss=='y'):
		ss='y'
	else:
		ss='n'
	return ss
"""

def bruteforce_usercheck(a,b,c,pre_mac,pre_no,pre_ex,winame,ifc,count):
	os.system('clear')
	print("                             >>  Wi-Fi is under protection <<                              ")     
	print(" ")               
	print(" ") 
	print(" *********please wait, loading*********")
	print("[+] Connected Users in the Wi-Fi are, ")
	print(" ")
	
	if(count==6):
		ff.kill
		time.sleep(15)
		count=0
		return a,b,c,pre_mac,pre_no,pre_ex,count
	
	for i in range(2):
		time.sleep(7)
		try:
			df=pd.read_csv(" mon-01.csv", usecols=[0])
		except:
			#print("excfkla;jflajfaskl;fjas;fjas;klfjask;fjask;dlfj;")     #checking
			qq.kill
			dele()
			time.sleep(10)
			return a,b,c,pre_mac,pre_no,pre_ex,count
		#print(i)
	qq.kill()
	f= DataFrame(df)
	x=df.drop(0,0)
	x=x.drop(1,0)
            #checking purpose
	ij=np.array(x)
	us=ij
	no=x.shape[0]
	val=no+1
	l=np.unique(ij)
	for i in range(x.shape[0]):
		print(f"[+] {i+1})",l[i])
		
	k=0

	temp =[]
		
	for i in a:
    		if(i in us): 
        		temp.append(i)
        		#print("flagged")                #checking prupose
        		

                        #checking purpose
	a=np.array(temp)
	a=a.reshape(-1,1)
	b=a.shape[0]
	c=b+1
	#print(b,c)
	
	new_bsid=[]
	for i in us:
    		if((i in pre_mac)): 
        		continue
    		else:
        		new_bsid.append(i)
        
	new_bsid=np.array(new_bsid)
	#new_bsid= np.unique(new_bsid)
	us=np.unique(us)
	pre_mac=np.unique(pre_mac)
	
	for i in us:
		if((i in pre_mac or no<pre_no)): 
			continue
		else:
			print("[+] New user detected: ",i)
			print("[+] (1/0) ")
			#ss,o,p = select.select( [sys.stdin], [],[], 15 )
			ss= int(input())
			print(ss)
			oi=str(i)
			print(oi)
			if(ss==1):
				pass
			else:
			
				subprocess.run([f" aireplay-ng -0 15 -e {wifi} -a {winame} -c {oi} {ifc} "],shell=True) 
				
				
				

	for i in range(0, len(us)):    
		for j in range(i+1, len(us)):  
			if(us[i] == us[j]):  
				subprocess.Popen(['aireplay-ng', '--deauth 100', '-a', winame ,'-c', us[j], ifc ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
	dele()
	time.sleep(2.5)
	return a,b,c,us,no,val,count,

subprocess.call(f'ifconfig {iface} down', shell=True)
subprocess.call(f'iwconfig {iface} channel {channel}', shell=True)
subprocess.call(f'ifconfig {iface} up', shell=True)
#subprocess.run([f'iwconfig {iface} channel {channel}'])
uss=su_us
noo=su_no
vaa=exc_val
mk=0

global qq
while (True):
	qq= subprocess.Popen([f'airodump-ng', iface , '--bssid', bsid ,'-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) 
	
	time.sleep(3)
	
	su_us,su_no,exc_val,uss,noo,vaa,mk = bruteforce_usercheck(su_us,su_no,exc_val,uss,noo,vaa,bsid,iface,mk)

	
	
	
	
	




    
