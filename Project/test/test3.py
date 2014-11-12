from pylab import*
from scipy.io import wavfile
sampFreq, snd = wavfile.read('440_sine.wav')

snd = snd / (2.**15)
s1 = snd[:,0] 
timeArray = arange(0, 5060.0, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds
plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
print(snd)
print(s1)
