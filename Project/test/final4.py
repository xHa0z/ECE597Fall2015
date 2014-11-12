#!/usr/bin/env python

'''
change send pixel

'''


import opc
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.io import wavfile # get the api
from scipy.fftpack import fft

# pixel map
pixels_map = [[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)],[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0),(0,255,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)]]

pixel_off = [(0,0,0)]*100
#print np.shape(pixels_map)
#print pixels_map[2][2]

# connect to beagle
ADDRESS = '192.168.7.2:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print 'connected to %s' % ADDRESS
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print 'WARNING: could not connect to %s' % ADDRESS


#print send_pixel	
# data analyze

formal_fft = []
grid = []
col = [0,0,0,0,0,0,0,0,0,0]
colNormalize = [0,0,0,0,0,0,0,0,0,0]
col_rfft = [0,0,0,0,0,0,0,0,0,0]
fs, data = wavfile.read('mario.wav') # load the data
a = data.T[0]
a_downsize = a.reshape(-1,4).mean(axis=1)
number = int( math.floor(len(a_downsize)/(fs/4)))
for i in range(0,number):
	send_pixel = [(0,0,0)]*100
        tmp_arr = a_downsize[(fs/4)*i : ((fs/4)*(i+1)-1)]
        tmp_pre_fft = [(ele/2**8.)*2-1 for ele in tmp_arr]
        tmp_fft = fft(tmp_pre_fft)
	fftlength = fs/4;
	tmp_fft_right = abs(tmp_fft[:(fftlength-1)])
        #formal_fft = np.append(formal_fft,tmp_fft_right)
	
	#find max in fft
	maxfft = max(tmp_fft_right);
#	print maxfft;
#	print len(tmp_fft_right)
	x_segment= int(math.floor(len(tmp_fft_right)/10))
#	print x_segment;
	for j in range (0,10):
#		print j*x_segment
#		print (j+1)*x_segment-1
		col[j] = np.mean(tmp_fft_right[j*x_segment:x_segment*(j+1)-1])
	fftmax = max(col[1:9]);
#	print fftmax;
	for k in range (1,9):
		col_avg = np.mean(col[1:9])
		if(col[k] < col_avg):
			colNormalize[k] = 5 - math.floor(((abs(col[k]-col_avg)/col_avg)*50/10))
		else:
			colNormalize[k] = 5 + math.floor(((abs(col[k]-col_avg)/col_avg)*50/10))
	
#		colNormalize[k] = math.floor(col[k]/fftmax*10)
#	print col;
	print colNormalize;
	
# send pixel
	x = 0
	for n in range(0,10):
		for m in range(0,int(colNormalize[n])):
			send_pixel[n*10+m] = pixels_map[n][m]
	
#	print send_pixel	
	client.put_pixels(send_pixel, channel=0)

#	time.sleep(0.2)
#	client.put_pixels(pixel_off, channel=0)	
			



'''



# connect to beagle
ADDRESS = '192.168.7.2:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print 'connected to %s' % ADDRESS
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print 'WARNING: could not connect to %s' % ADDRESS

# Send pixels forever
while True:
	for 
	
    my_pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255),(255,255,255)]*5*5
    random.shuffle(my_pixels)
    if client.put_pixels(my_pixels, channel=0):
        print 'sent'
    else:
        print 'not connected'
    time.sleep(0.3)
'''

