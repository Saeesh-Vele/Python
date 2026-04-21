probablity={'rain':0.2,'no rain':0.8,'wet_g|rain':0.9,'wet_g|no rain':0.1}
p_wet_g=(probablity['rain']*probablity['wet_g|rain'])+(probablity['no rain']*probablity['wet_g|no rain'])
p_rain_wet_g=(probablity['wet_g|rain']*probablity['rain'])/p_wet_g
print(f"Total Probablity of grass being wet:{p_wet_g: .2f}")
print(f"Probablity that the grass is wet because of rain:{p_rain_wet_g: .2f}")
