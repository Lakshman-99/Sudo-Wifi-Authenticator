#final

##Importing functions
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import askstring
import subprocess
import numpy as np
import pandas as pd
import time
import os
from multiprocessing import Process
import threading
from pandas import DataFrame



##========================================================================================================================================
# for deleting dump files

def dele():
	try:
		subprocess.run(['rm',' mon-01.csv'])
		subprocess.run(['rm',' mon-01.log.csv'])
		subprocess.run(['rm',' mon-01.kismet.csv'])
		subprocess.run(['rm',' mon-01.kismet.netxml'])
		subprocess.run(['rm',' mon-01.cap'])
	except:
		pass

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
	for i in range(x.shape[0]):
		print(l[i])
	return su_us,su_no,exc_val     

def de_auth(ap,tar,inter):         # pass ap= access point (wifi)  mac address, tar= target client (hacker) mac address, inter= interface wifi adaptor ( supporting monitor mode ).
	da= subprocess.Popen(['aireplay-ng', '--deauth', '10', '-a', ap ,'-c', tar, inter ], stdout=subprocess.PIPE)         # deauthentication attack.
	for j in range(0,1):
		dau={j:tar}
		black.update(dau)
	j=len(black)
	return black

def bruteforce_usercheck(a,b,c,pre_mac,pre_no,pre_ex,winame,ifc,ff,count):
	os.system('clear')
	if(count==6):
		ff.kill
		time.sleep(15)
		count=0
		return a,b,c,pre_mac,pre_no,pre_ex,count
	
	for i in range(4):
		time.sleep(7)
		try:
			df=pd.read_csv(" mon-01.csv", usecols=[0])
		except:
			print("excfkla;jflajfaskl;fjas;fjas;klfjask;fjask;dlfj;")
			ff.kill
			dele()
			time.sleep(10)
			return a,b,c,pre_mac,pre_no,pre_ex,count
		print(i)
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
		print(l[i])
		
	k=0

	temp =[]
		
	for i in a:
    		if(i in us): 
        		temp.append(i)
        		print("flagged")                #checking prupose
        		

                        #checking purpose
	a=np.array(temp)
	a=a.reshape(-1,1)
	b=a.shape[0]
	c=b+1
	print(b,c)
	
	new_bsid=[]
	for i in us:
    		if((i in pre_mac)): 
        		continue
    		else:
        		new_bsid.append(i)
        
	new_bsid=np.array(new_bsid)
	"""
       	if(no>pre_no):
            	#pop window
            	pop_action=False
            	if(pop_action):
         		a=np.append(a,new_bsid)
            	else:
              		de_auth(winame,new_bsid,ifc)
	
	"""

	for i in range(0, len(us)):    
		for j in range(i+1, len(us)):  
			if(us[i] == us[j]):  
				de_auth(winame,us[j],ifc)                                         #checking duplicate mac addresses
	ff.kill
	dele()
	time.sleep(2.5)
	return a,b,c,us,no,val,count


global uss           		# a copy of su_us
global noo			# a copy of su_no
global vaa			# a copy of exc_val
global d			# dictionary of corresponding ESSID:BSSID
global iface			# network interface
global mk			# temp value
global su_us			# Super user mac addresses
global su_no			# super user count
global exc_val			# super user count + 1
global bsid			# selected Ap(wifi name) mac address
global qq			# main process used in while(True)
global a			# a copy of su_us to bruteforce function
global b			# a copy of su_no to bruteforce function
global c			# a copy of exc_val to bruteforce function
global no			# a copy of current search list(no. of users) to calling function
global val			# a copy of current search list(no. of users + 1) to calling function
global us			# a copy of current search list(mac addresses) to calling function
global checkk
checkk=0

d={}
black={}                                      # black= dictionary of blocked users.
dele()


##========================================================================================================================================
##def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
##    canvas.create_text(x, y, text=text, font=('courier', 16, 'bold'), fill=strokecolor)
    # make regular text
##    canvas.create_text(x, y, text=text, font=('courier', 16), fill=textcolor)

root = Tk()
root.title("Sudo Authenticator");
##global list for connected list and block list 
global val
global block_list #here you define block list in a array or list
block_list = list()
global connected_list #here you have to define connected list in array or list
connected_list = list()
global x#**
x=1 #**
global counter #**
count=5  #**
global y
y=1000
global connected_frame
global connected_user   #THIS  LIST IS FOR ALREADY CONNECTED USERS 
global blocked_user
global connected_list1 ##THIS LIST FOR USERS ENTER USING POPUP WINDOW USE IT PROPERLY ELSE OP WILL NOT COME
connected_list1  =list()
global counter  ##For timer
counter = 15
##========================================================================================================================================

#CODE THE DEAUTH FUNCTION HERE
def deauth_func(connected_user):
	global block_list
	global conected_list
	global connected_list1
	print("Deauthenticated")
	try:
		values1 = connected_user.curselection() #**
		index = values1[0]      #**
		block = connected_user.get(index)
		if block in connected_list:
			connected_list.remove(block)   #FOR DEAUTH FUNCTION REMOVE FROM CONNECTED LIST
			block_list.append(block)      #AND ADD TO BLOCK LIST
		else:
			connected_list1.remove(block)
			block_list.append(block)      #AND ADD TO BLOCK LIST       
		for i in block_list:
			print(i)
		for i in connected_list:     #WRITE YOUR CODE HERE
			connected_user.insert(1,i)   #PRINTING THE BLOCKED USERS HERE
		for i in connected_list1:
			connected_user.insert(1,i)
	except IndexError:
		print(showwarning("Alert" , "Please select a User first"))
	except ValueError:
		print(showwarning("Alert" , "Please select a User first"))        

##========================================================================================================================================

#CODE THE UNBLOCK FUNCTION HERE
def Unblock_user(blocked_user):
	global connected_list    
	global block_list
	try:
		print("Unblocked")
		unblock1 = blocked_user.curselection()   #**
		index = unblock1[0]    #**
		unblock = blocked_user.get(index)    #**
		block_list.remove(unblock)     #REMOVING FROM BLOCK LIST AND
		connected_list.append(unblock)   #ADDING TO CONNECTED LIST
	except ValueError:
		print(showwarning("Alert" , "User already unblocked"))  #EXCEPTION ARISES IF USER TRIES TO REMOVE A USER TWO TIMES
	except IndexError:
		print(showwarning("Alert" , "Please select a user first"))
##========================================================================================================================================
def popup(): ##POPUP FUNCTION
	global connected_user
	global blocked_user
	global connected_list #**
	global connected_list1 #**
	global block_list #**
	window = Toplevel()
	window.geometry("380x100")
	label = Label(window )
	label.config(text = "New User named " + str(y) + " has entered , do you want to accept?")  ##IN STR(Y) PLACE ENTER THE USER OR MAC ADDRESS NAME
	label.pack(fill='x')
	window.resizable(0,0)

	def deny():
		print("Denied")
		block_list.append(y)   ##IF DENIED USER WILL DIRECTLY GO TO BLOCK LIST
		window.destroy()
	def accept():
		print("Accept")
		connected_list1.append(y) ##***IF ACCEPTED USER WILL DIRECTLY GO TO CONNECTED LIST1 LIST NOT CONNECTED LIST PLEASE USE IT ACCORDINGLY***
		window.destroy()

	def counter_label(label):
		def count():
			global counter
			if(counter > 0):
				counter-=1
				label.config(text=str(counter))
				label.after(1000, count)
			else:
				block_list.append(y)
				window.destroy()
		count()

	label = Label(window, fg="green")
	label.pack()
	counter_label(label)

	button_deny = Button(window, text="Deny", command=lambda :deny())
	button_deny.place(relx = 0.6 , rely = 0.4, relheight = 0.2 , relwidth = 0.2)

	button_accept = Button(window  ,text = "Accept" , command = lambda :accept())
	button_accept.place(relx = 0.2 , rely = 0.4, relheight = 0.2 , relwidth = 0.2)
    
##========================================================================================================================================
#CONNECTED FRAME DISPLAY CODE
def connected(print_val):
	global connected_frame
	global connected_user
	global blocked_user
	print("hello")
	global connected_list
	global connected_list1
	global x
	#global uss
	global uss           		# a copy of su_us
	global noo			# a copy of su_no
	global vaa			# a copy of exc_val
	global d			# dictionary of corresponding ESSID:BSSID
	global iface			# network interface
	global mk			# temp value
	global su_us			# Super user mac addresses
	global su_no			# super user count
	global exc_val			# super user count + 1
	global bsid			# selected Ap(wifi name) mac address
	global qq			# main process used in while(True)
	global a			# a copy of su_us to bruteforce function
	global b			# a copy of su_no to bruteforce function
	global c			# a copy of exc_val to bruteforce function
	global no			# a copy of current search list(no. of users) to calling function
	global val			# a copy of current search list(no. of users + 1) to calling function
	global us
	
	
	connected_user = Listbox(connected_frame , bg = "#ffcc66")  #**
	connected_user.place(relx = 0 ,rely = 0, relheight = 1 , relwidth = 0.7)  #**
   
	scrollbar1 = Scrollbar(connected_user , bg = "#66fcf1")  #**
	scrollbar1.pack(side=RIGHT, fill=Y)   #**
	connected_user.config(yscrollcommand = scrollbar1.set)    #**
	scrollbar1.config(command = connected_user.yview)  #**
	
	for i in print_val:
		connected_user.insert(1,i)
		
	"""
	if(x<2):            ##STORE THE USERS IN THE ARRAY AND PRINT THEM
		for i in range(145):
			connected_list.append(i)   #WRITE THE CODE HERE TO PRINT THE CONNECTED USERS HERE  (ALREADY CONNECTED USERS)
		for i in connected_list:
			connected_user.insert(1,i) #**
		for i in connected_list1:      ##***FOR USERS WHO CAME THROUGH POPUP USE IT ACCORDINGLY****
			connected_user.insert(1,i)
		x+=1
	else:
		for i in connected_list:
			connected_user.insert(1,i)  #WRITE THE CODE HERE TO PRINT THE CONNECTED USERS HERE AGAIN
		for i in connected_list1:
			connected_user.insert(1,i)
 	"""
	"""
	def calc():
		for i in print_val:
			connected_user.insert(1,i)
	calc()
	connected_user.after(2000, calc())
	"""
##========================================================================================================================================
	
	try:
		deauth = Button(connected_frame , text = "BLOCK" , command = lambda:deauth_func(connected_user) ,bg = "#ffcc66")  #**
		deauth.place(relx= 0.73 , rely =0.35 , relwidth = 0.25 , relheight = 0.1)  #**
	except IndexError:
		print(showwarning("Alert" , "Please select a User first"))
	connected_frame.lift()
	"""
	while (True):

		
		qq= subprocess.Popen(['airodump-ng', iface , '--bssid', bsid ,'-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) 
	
		time.sleep(3)
		
		print("asdasdasfmszsdfasrfmkq2krwe")
		
		
			
		su_us,su_no,exc_val,uss,noo,vaa,mk = bruteforce_usercheck(su_us,su_no,exc_val,uss,noo,vaa,bsid,iface,qq,mk)
	"""
	main1()
##========================================================================================================================================
#CODE OF BLOCKED USER HERE
def blocked(blocked_frame):
	global connected_user
	global blocked_user
	global block_list
    
	print("hello") 
	blocked_user = Listbox(blocked_frame , bg = "#ffcc66") #**
	blocked_user.place(relx = 0 ,rely = 0, relheight = 1 , relwidth = 0.7)  #**

	scrollbar2 = Scrollbar(blocked_user , bg = "#66fcf1")  #**
	scrollbar2.pack(side=RIGHT, fill=Y)  #** 
	blocked_user.config(yscrollcommand = scrollbar2.set)  #**
	scrollbar2.config(command = blocked_user.yview) #**

	unblock = Button(blocked_frame , text = "UNBLOCK", command = lambda : Unblock_user(blocked_user))   #**
	unblock.place(relx = 0.73 , rely = 0.3 , relwidth = 0.25 , relheight = 0.1)  #**
	print(block_list)
	for i in block_list:
		blocked_user.insert(1,i) ##CODE THE FUNCTION OF PRINTING BLOCKED USERS HERE 
	blocked_frame.lift()
##========================================================================================================================================
#DISPLAYING THE LIST OF NETWORKS FUNCTION
def getSelection(network_list):
	global val
	global connected_frame
	global connected_list
	global mk
	global jkl
	global uss
	global bsid
	global uss           		# a copy of su_us
	global noo			# a copy of su_no
	global vaa			# a copy of exc_val
	global d			# dictionary of corresponding ESSID:BSSID
	global iface			# network interface
	global mk			# temp value
	global su_us			# Super user mac addresses
	global su_no			# super user count
	global exc_val			# super user count + 1
	global bsid			# selected Ap(wifi name) mac address
	global qq			# main process used in while(True)
	global a			# a copy of su_us to bruteforce function
	global b			# a copy of su_no to bruteforce function
	global c			# a copy of exc_val to bruteforce function
	global no			# a copy of current search list(no. of users) to calling function
	global val			# a copy of current search list(no. of users + 1) to calling function
	global us
	jkl=2
	mk=0
	connected_list = list()

	try:
		values = network_list.curselection() #**
		index = values[0]   #** 
		val = network_list.get(index) #**
		
		
		##############
		wifi= val
		bsid= d.get(wifi) 
		subprocess.run(['rm',' hi-01.csv'])
		subprocess.run(['rm',' hi-01.log.csv'])
		subprocess.run(['rm',' hi-01.kismet.csv'])
		subprocess.run(['rm',' hi-01.kismet.netxml'])
		subprocess.run(['rm',' hi-01.cap']) 
		
		pp= subprocess.Popen(['airodump-ng', iface , '--bssid', bsid ,'-w mon' ], stdout=subprocess.PIPE)             # monitoring specific AP (wifi)
		for i in range(3):
			time.sleep(12)
			su_us,su_no,exc_val = myPeriodicFunction()
		pp.kill()    
		dele()
		uss=su_us
		noo=su_no
		vaa=exc_val
		print(uss)
		
		
		##############

	except IndexError:
		print(showwarning("ALert" , "Please select a network"))

	print(val)
	changing_frame3 = Frame( height = 500 , width= 700 , bg = "#FF0000" ) #**
	changing_frame3.place(relx = 0 , rely = 0.2 , relheight = 0.8 , relwidth = 1)  #**

	monitoring = Label(changing_frame3 , bg= "#ffcc66" ,  font = ("Helvetica" , "16" ,"bold")) #**
	monitoring.place(relx = 0 , rely = 0 , relheight = 0.15 , relwidth = 1) #**
	monitoring.config(text = "Monitoring network  >>"+ str(val) + "<<")#**
	
	
##========================================================================================================================================
#BLOCKED FRAME GUI CODE
	blocked_frame = Frame(changing_frame3 , bg = "#ffcc66")  #**
	blocked_frame.place(relx = 0 , rely = 0.3 , relheight = 0.7 , relwidth = 1) #**
  
	blocked_users = Button(changing_frame3 , text = "Blocked users" , command = lambda : blocked(blocked_frame)) #**
	blocked_users.place(relx = 0.5 , rely = 0.15 , relheight = 0.15 , relwidth = 0.5) #**

	select_label = Label(changing_frame3 , bg = "#ffcc66" , text = "Select any one tab"  ,font = ("Helvetcia" , "14" , "bold")) #**
	select_label.configure(underline = 1)
	select_label.place(relx = 0.3 , rely = 0.1, relwidth = 0.4 , relheight = 0.05)  #**

    
##========================================================================================================================================
#CONNECTED USERS FRAME GUI CODE
	connected_frame = Frame(changing_frame3 , bg = "#ffcc66") #**
	connected_frame.place(relx=0,rely=0.3 , relheight = 0.7 , relwidth = 1)  #**
    
	connected_users = Button(changing_frame3, text = "Connected users" , command = lambda : connected(uss)   ) #**
	connected_users.place(relx = 0 , rely = 0.15 , relheight= 0.15 , relwidth = 0.5)  #**
	
    
##========================================================================================================================================

	


##SECOND PAGE GUI
def changing_frame2():
	global d
	global iface
	global clicked
	a=clicked.get()
	if(a=="--Select--"):
		print(showwarning("Alert" , "Select a valid Interface"))
    
	else:

        ##########
		iface= a
		subprocess.call(['airmon-ng', 'start' , iface ]) 
		p = subprocess.Popen(['airodump-ng','-w hi', iface], stdout=subprocess.PIPE)       # line-1.1
		time.sleep(10)                                                                                                                    # line-1.2
		p.kill()                                                                                                                          # line-1.3 running airodump-ng



		df=pd.read_csv(" hi-01.csv", usecols=[0,13])                                                                 
		data=df.dropna()
		y=np.array(data)
		z=y.shape[0]
		c=y[:,1]
		v=y[:,0]
		d={}
		for i in range(z):
			di={c[i]:v[i]}
			d.update(di)
        
        
        
        ############
        
		changing_frame2 = Frame(first_page ,bg="#111111")
		changing_frame2.place(relx = 0 , rely = 0.2 , relheight = 0.8 , relwidth = 1)
##GRADIENT FRAMES CODE
		gradient_frame6 = Frame(changing_frame2 , bg = "#ffb31a")#ffb31a
		gradient_frame6.place(relx= 0,rely = 0 , relwidth = 1 , relheight = 0.2)

		gradient_frame7 = Frame(changing_frame2 , bg = "#ffbb33")#ffbb33
		gradient_frame7.place(relx= 0,rely = 0.2 , relwidth = 1 , relheight = 0.2)

		gradient_frame8 = Frame(changing_frame2 , bg = "#ffc34d")
		gradient_frame8.place(relx= 0,rely = 0.4 , relwidth = 1 , relheight = 0.2)

		gradient_frame9 = Frame(changing_frame2 , bg = "#ffcc66")#ffcc66
		gradient_frame9.place(relx= 0,rely = 0.6 , relwidth = 1 , relheight = 0.2)

		gradient_frame10 = Frame(changing_frame2 , bg = "#ffd480")#ffd480
		gradient_frame10.place(relx= 0,rely = 0.8 , relwidth = 1 , relheight = 0.2)
        
		available_networks_label = Label(changing_frame2 , text = "Available networks" , bg = "#ffbb33" ,  font = ("Helvetica" , "16" ,"bold"))
		available_networks_label.place(relx = 0.27 , rely = 0.3 , relwidth= 0.4 , relheight = 0.1)

		network_list = Listbox(changing_frame2,  bg = "#ffd480")
		network_list.place(relx = 0.27 , rely = 0.4 , relwidth = 0.4 , relheight = 0.4)
    
		scrollbar = Scrollbar(network_list , bg = "#000428") #**
		scrollbar.pack(side=RIGHT, fill=Y) #**
		network_list.config(yscrollcommand = scrollbar.set) #**
		scrollbar.config(command = network_list.yview) #**

		for i in range(c.size):                                                                                              # printing available wifi
			network_list.insert(1,c[i])

        
		try:
			scan_network = Button(changing_frame2 , text = "Scan this network" , command = lambda: getSelection(network_list))
			scan_network.place(relx=0.4 , rely = 0.85 , relheight = 0.1 , relwidth = 0.2)
		except:
			print(showwarning("ALert" , "Please select a network")) 
##========================================================================================================================================
global clicked
global first_page
global Title_frame
global p
global p1
global Title_label
global changing_frame1, gradient_frame1, gradient_frame2, gradient_frame3, gradient_frame4, gradient_frame5, team_name, select_interface_frame, select_interface, interface_label, scan_wifibutton


def changing_frame1():
	global clicked
	global first_page
	global Title_frame
	global p
	global p1
	global Title_label
	global changing_frame1, gradient_frame1, gradient_frame2, gradient_frame3, gradient_frame4, gradient_frame5, team_name, select_interface_frame, select_interface, interface_label, scan_wifibutton
	clicked = StringVar()
	clicked.set("--Select--")
	##STARTING PAGE GUI
	first_page = Canvas(root, height = 500 , width = 700)
	first_page.pack()

	Title_frame = Frame(first_page, bg= "#000428")
	Title_frame.place(relx=0,rely=0,relwidth=1,relheight=0.2)
	#LOGO 
	p= PhotoImage(file="LOGO.png" , width = 140 , height = 85)
	bglabel=Label(Title_frame, image=p , padx = 0 ,pady =0)
	bglabel.place(relx = 0.02 , rely = 0.04 )
	#TITLE FRAME
	p1= PhotoImage(file="title.png" , width = 540 , height = 25)
	Title_label=Label(Title_frame, image=p1 ,bg = "#000428" ,padx = 0 ,pady =0)
	Title_label.place(relx= 0.29 , rely = 0.2 , relheight = 0.7 , relwidth = 0.73 )
	##Title_label = Label(Title_frame )##, text = "Sudo wifi authenticator" , bg = "#000428" , fg = "#80ffff" , font=("Rockwell",23))
	##Title_label.place(relx= 0.33 , rely = 0.2 , relheight = 0.5 , relwidth = 0.4)

	##canvas = Canvas(Title_label, bg='#000428')
	##canvas.pack()
	##stroke_text(105, 30, "Sudo Wi-Fi authenticator", '#80ffff', 'red')


	#FIRST PAGE FRAME
	changing_frame1 = Frame(first_page, bg= "#d1d1e0")
	changing_frame1.place(relx = 0 , rely = 0.2 , relheight = 0.8 , relwidth = 1)
	#GRADIENT FRAMES
	gradient_frame1 = Frame(changing_frame1 , bg="#ffd480")
	gradient_frame1.place(relx=0 , rely = 0 , relheight = 0.2 , relwidth = 1)

	gradient_frame2 = Frame(changing_frame1 , bg="#ffcc66")
	gradient_frame2.place(relx=0 , rely = 0.2 , relheight = 0.2 , relwidth = 1)

	gradient_frame3 = Frame(changing_frame1 , bg="#ffc34d")
	gradient_frame3.place(relx=0 , rely = 0.4 , relheight = 0.2 , relwidth = 1)

	gradient_frame4 = Frame(changing_frame1 , bg="#ffbb33")
	gradient_frame4.place(relx=0 , rely = 0.6 , relheight = 0.2 , relwidth = 1)

	gradient_frame5 = Frame(changing_frame1 , bg="#ffb31a")
	gradient_frame5.place(relx=0 , rely = 0.8 , relheight = 0.2 , relwidth = 1)

	team_name = Label(gradient_frame5 ,text = "Team : Code Sploit" , bg= "#ffb31a" , font = ("Helvetica" , "16" ,"bold"))
	team_name.place(relx = 0.15 , rely = 0.1 , relheight = 0.8 , relwidth = 0.7)

	select_interface_frame = Frame(changing_frame1 , bg="#ffc34d")
	select_interface_frame.place(relx=0.33 , rely= 0.3 , relheight = 0.1 , relwidth =  0.34)

	select_interface = OptionMenu(select_interface_frame , clicked , "wlan0","wlan1","wlan2","wlan3","wlan4","wlan5")
	select_interface.place(relx = 0.03 , rely = 0.08 , relheight = 0.8 , relwidth = 0.6)

	interface_label = Label(select_interface_frame , text = "Interface" )
	interface_label.place(relx = 0.67 , rely = 0.065 , relheight = 0.8 , relwidth = 0.3)
	#SCAN WIFI BUTTON FIRST PAGE
	scan_wifibutton = Button(changing_frame1, text = "Scan Wifi" , command = lambda: changing_frame2() , activebackground="#05386B",activeforeground="#80ffff", relief = "raise" )
	scan_wifibutton.place(relx  = 0.42 , rely = 0.48 , relwidth = 0.15 , relheight = 0.07)

	"""
	#################
	if(checkk==1):
		while (True):
			connected(uss)
			
			qq= subprocess.Popen(['airodump-ng', iface , '--bssid', bsid ,'-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) 
	
			time.sleep(3)
		
			print("asdasdasfmszsdfasrfmkq2krwe")
		
		
			
			su_us,su_no,exc_val,uss,noo,vaa,mk = bruteforce_usercheck(su_us,su_no,exc_val,uss,noo,vaa,bsid,iface,qq,mk)
	
	#################
	"""

	##Write YOUR CONDITION HERE WHEN THE POPUP SHOULD APPEAR


def while_func():
	global uss           		# a copy of su_us
	global noo			# a copy of su_no
	global vaa			# a copy of exc_val
	global d			# dictionary of corresponding ESSID:BSSID
	global iface			# network interface
	global mk			# temp value
	global su_us			# Super user mac addresses
	global su_no			# super user count
	global exc_val			# super user count + 1
	global bsid			# selected Ap(wifi name) mac address
	global qq			# main process used in while(True)
	global a			# a copy of su_us to bruteforce function
	global b			# a copy of su_no to bruteforce function
	global c			# a copy of exc_val to bruteforce function
	global no			# a copy of current search list(no. of users) to calling function
	global val			# a copy of current search list(no. of users + 1) to calling function
	global us			# a copy of current search list(mac addresses) to calling function
	global checkk

	while (True):
		qq= subprocess.Popen(['airodump-ng', iface , '--bssid', bsid ,'-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) 
		time.sleep(3)
		print("asdasdasfmszsdfasrfmkq2krwe")
		su_us,su_no,exc_val,uss,noo,vaa,mk = bruteforce_usercheck(su_us,su_no,exc_val,uss,noo,vaa,bsid,iface,qq,mk)	
		
	
def main1():
	if(jkl==2):
		while_func()
def main():
	global uss           		# a copy of su_us
	global noo			# a copy of su_no
	global vaa			# a copy of exc_val
	global d			# dictionary of corresponding ESSID:BSSID
	global iface			# network interface
	global mk			# temp value
	global su_us			# Super user mac addresses
	global su_no			# super user count
	global exc_val			# super user count + 1
	global bsid			# selected Ap(wifi name) mac address
	global qq			# main process used in while(True)
	global a			# a copy of su_us to bruteforce function
	global b			# a copy of su_no to bruteforce function
	global c			# a copy of exc_val to bruteforce function
	global no			# a copy of current search list(no. of users) to calling function
	global val			# a copy of current search list(no. of users + 1) to calling function
	global us			# a copy of current search list(mac addresses) to calling function
	global checkk	
	#if(y==1000):
	#	popup()
	
	if(jkl==1):
		changing_frame1()
		#jkl
	if(jkl==2):
		while_func()
	#while_func()

	

global jkl
jkl=1

main()




root.resizable(0,0)
root.mainloop()
