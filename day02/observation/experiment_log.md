# Day 02 : Experimental log 

## Experiment 01 : FFT of pure sine wave (5hz)
- time domain :  a clean continous signal 
- frequency domain : a spike at 5 hz else 0 freq 

## Experiment 02 : FFT of mixed sine wave (5hz + 20hz)
- time domain : a continuous signal yet seemed like a a 20 hz frequency embeded per each cycle of 5hz
- frequency domain : a clean spike at 5hz and 20 hz frequency 

## Experiment 03 : FFT of noisy sine wave (5hz + noise (gaussian))
- time domain : random fluctuation all over the sine wave shape retained due to 0.5  scaling 
- frequency domain : a spike at 5 hz along with small frequencies all over sample space

## Experiment 04 : FFT of square wave 
- frequency domain : a high spike at 5hz and then gradual drop in spike across different odd multiple frequencies(15,25,35...)