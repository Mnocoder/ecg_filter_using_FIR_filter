# ecg_filter_using_FIR_filter
# Abstract :
       Noise reduction in ECG signal using Finite Impulse Response(FIR) filter
             The electrocardiogram (ECG) signal is non-stationary electrical signals from the heart characteristically 
             precede the normal mechanical function and monitoring of these signals has great clinical significance.
# Motivation:
             The heart rate analysis from an ECG is crucial in assessing the health condition of an individual. 
             But the measured ECG tend to have noises such as the 50Hz interference and the DC.  
             These noises make the detection of peaks inaccurate which in turn make the detection of heartrate inaccurate.
             Thus, removing the noises from the ECG is pertinent for the proper analysis of the ECG signal.
             We have used FIR filter to achieve filtration of ECG signal.
# System description with application :
             The Electrocardiogram (ECG) machine with 4 terminal wires is an electrogram of the heart which is a graph of voltage versus time of the electrical activity of the heart using electrodes placed on the skin. These electrodes detect the small electrical changes.
             But the signal have power line interference which have 50Hz frequency and DC which make the detection of heartrate inaccurate.
             The ﬁnite impulse response (FIR) ﬁlter is created to remove the 50Hz interference as well as the DC from the signal. 
             We used bandpass filter  for the calculation of impulse response of the desired frequency response created and Hamming window for normalising the impulse response which is used for convolution of ECG signal and impulse response. 

For the values of ECG signal passed to the system -> Filtered signal values that can be displayed is returned

# Methodology :

            FIR filters are digital filters with finite impulse response.
            They are also known as non-recursive digital filters because of their inherent stability when implement in non-recursive form, the ease with which one can attain linear phase and more stable which cant be achieved in IIR filter.
            This filter doesn’t depend on past samples of input along with past output like the IIR filter.
            Bandstop filter is a combination of lowpass and highpass filter which can block or at least severely attenuate a band of frequencies within the two cut-off frequency points specified and allow frequencies other than that.  
            The Hamming window is a taper formed by using a weighted cosine which reduces the ripple on either side of the peak.
            Then, the ECG signal and impulse response is passed to a function that does convolution and returns the filtered signal.


