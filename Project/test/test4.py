import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
formal_fft = []
fs, data = wavfile.read('mario.wav') # load the data
a = data.T[0] # this is a two channel soundtrack, I get the first track
#b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
#c = fft(b) # create a list of complex number
#d = len(c)/2  # you only need half of the fft list
#nu = np.fft.fftfreq(d,10)
a_downsize = a.reshape(-1,4).mean(axis=1)
#plt.plot(a_downsize,'r') 
#plt.plot( abs(c[:(d-1)]),'r')
#plt.show()
number = int( math.floor(len(a_downsize)/(fs/4)))
#print number

for i in range(0,number):
	tmp_arr = a_downsize[(fs/4)*i : ((fs/4)*(i+1)-1)]
	tmp_pre_fft = [(ele/2**8.)*2-1 for ele in tmp_arr]
	tmp_fft = fft(tmp_pre_fft)
	fftlength = fs/4;
	tmp_fft_right = abs(tmp_fft[:(fftlength-1)])
	formal_fft = np.append(formal_fft,tmp_fft_right)

print len(tmp_fft_right)
print len(formal_fft)
	


#e = len(a)
#print a_downsize
#print b
#print c
#print e
#print fs
#print d
np.savetxt("fft.txt",formal_fft);
#np.savetxt("fft.txt", abs(c[:(d-1)]))
