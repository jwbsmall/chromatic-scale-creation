duration = 0.5 

# Import pysox library 
import sox
t = sox.Transform() 

# Create and play the list of frequencies  
freqs_list = [440, 880, 1320, 1760, 2200]  

# Use loop to play each frequency in order 
for freq in freqs_list:   
    # Generate tone and playtone        
	t.tone(freq, duration)
	t.play()