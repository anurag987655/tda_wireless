import matplotlib.pyplot as plt 
import numpy as np 

class  Signal:
    def __init__(self,x,t,name):
        self.x = np.asarray(x)
        self.t = np.asarray(t)
        self.name = name

    @property
    def sampling_frequency(self): 
         
         if len(self.t)<2: 
              return None
         
         return 1/(self.t[1]-self.t[0])
    
    @property
    def duration(self):
         return self.t[1]-self.t[0]

    def __len__(self):
        return len(self.x)
    
    def __repr__(self):
            return f"{self.name}(samples={len(self.x)})"

    def plot(self):
         plt.figure(figsize=(10,10))
         plt.plot(self.t,self.x)
         plt.title(self.name)
         plt.xlabel("Time")
         plt.ylabel("Amplitude")
         plt.grid(True)
         plt.show()

    def add_awgn(self,snr_db):
         power_signal = np.mean(self.x**2)
         power_noise = power_signal / (10 ** (snr_db/10))
         noise = np.sqrt(power_noise) * np.random.randn(len(self.x))
         return Signal(self.x+noise, self.t, f"{self.name}_{snr_db}dB")