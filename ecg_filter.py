import numpy as np
import matplotlib.pyplot as plt
 
#------------------------Bandstop Filter Function------------------------
def bandstop(M,low,high,Fs):
    #50Hz removal
    k1 = int( (low/Fs)*M) # index 22
    k2 = int( (high/Fs)*M) # index 27
    #DC removal
    k0 = int( (1/Fs)*M) # index 0

    #Creating the desired frequency response X for the bandstop filter
    X = np.ones(M)  # Frequency response
    #DC removal
    X[0:k0+1]=0 # from index 0 to 0
    #50Hz removal
    X[k1:k2+1]=0 # from index 22 to 27
    #Mirror of the 50Hz removal
    X[M-k2:M-k1+1] = 0 # from index 492 to 477
    
    #Passing the created frequency response to ifft to get impulse response signal
    x = np.real(np.fft.ifft(X)) # signal x - impulse response of system
    return x

#-----------------------------FIR Filter Function---------------------------
def FIR_filter(ecg,h):
    M = len(ecg) # length of ecg
    N = len(h) #length of coefficients h
    filtered = np.zeros( M + N - 1 ) # list of zeros of length M+N-1
    for n in range( M+N ): #iterates from 0 to M+N
        for k in range(N): #iterates from 0 to N
            if 0 <= n-k <= M-1 :  #allows only possible index numbers for ecg
                filtered[n] = filtered[n] + ecg[n-k]*h[k] # convolution formula
    filtered = filtered[int(N/2):] #removing first 250 values
    filtered = filtered[: int(len(filtered) - N/2)] #removing last 250 values
    return filtered 

#----------Importing and preparing the signal before filtering-----------       
data= np.loadtxt('ecg_data.dat')
xval = data[:,0]
ecg = data[:,1]

ampGain = 500; # Amplitude Gain
Fs = 1000; # Sampling Frequency

# Reducing the signal to remove amplitude gain 
ecg = ecg/ampGain #ecg amplitude in mVs
midval =  min(ecg) + (max(ecg)-min(ecg))/2
ecg = ecg-midval #normalising

#---------------------------------Filtering-----------------------------
# Designing a FIR filter using Window method


# Bandstop filter
M = 500 #length/order of filter
x = bandstop(M,45,55,Fs)

# Positioning first half in second half and second half in first half
# making the 45-55hz removal around midpoint
# which accordingly denoise the signal
h = np.zeros(M)
h[0:int(M/2)] = x[int(M/2):M] # 250 to 499
h[int(M/2):M] = x[0:int(M/2)] # 0 to 249

# Hamming window (Taper formed by weighted cosine)
# Maximum value normalised to one
h = np.hamming(M)*h 

#Filtering the whole signal
Filtered_signal = FIR_filter(ecg,h)

#-------------------------------Plotting---------------------------------
plt.figure(1)
plt.plot(xval,ecg)
plt.title('Unfiltered ECG [time domain]')
plt.xlabel('Time [mS]')
plt.ylabel('Amplitude')
plt.grid()

plt.figure(2) 
plt.plot(Filtered_signal)
plt.title("Filtered ECG [time domain]")
plt.xlabel("Time [ms]")
plt.ylabel("Amplitude")
plt.grid()

plt.figure(3)
plt.plot(xval[5000:6000],ecg[5000:6000])
plt.xlabel("Time [ms]")
plt.ylabel("Amplitude")
plt.title("Unfiltered ECG [Momentary]")
plt.grid()

plt.figure(4)
plt.plot(xval[5000:6000],Filtered_signal[5000:6000])
plt.xlabel("Time [ms]")
plt.ylabel("Amplitude")
plt.title("Filtered ECG [Momentary]")    
plt.grid()

#Frequency response for the ECG
fftdata = np.fft.fft(ecg)
faxis = np.linspace(0,Fs, len(fftdata))

plt.figure(5)
plt.plot(faxis, np.abs(fftdata))
plt.title("Unfiltered ECG [frequency domain]")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid()

#Frequency response for the filtered ECG
fftdata1 = np.fft.fft(Filtered_signal)
faxis1 = np.linspace(0,Fs, len(fftdata1))

plt.figure(6)
plt.plot(faxis1, np.abs(fftdata1))
plt.title('Filtered ECG [frequency domain]')
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid()
