def _4000k(wave_lenth):
	if(wave_lenth<400):
		return 0
	elif(wave_lenth>800):
		return 0
	elif(wave_lenth>=400 and wave_lenth<450):
		return (wave_lenth-400)**3/125000
	elif(wave_lenth>=450 and wave_lenth<460):
		return 1-(wave_lenth-450)*(0.5/10)
	elif(wave_lenth>=460 and wave_lenth<475):
		return 0.5-(wave_lenth-460)*(0.25/15)
	elif(wave_lenth>=475 and wave_lenth<520):
		return 0.25+(wave_lenth-475)*(0.35/45)
	elif(wave_lenth>=520 and wave_lenth<600):
		return 0.6+(wave_lenth-520)*(0.3/80)
	elif(wave_lenth>=600 and wave_lenth<650):
		return 0.9-(wave_lenth-600)*(0.5/50)
	elif(wave_lenth>=650 and wave_lenth<=800):
		return (800-wave_lenth)**3/3375000*0.4

def _3000k(wave_lenth):
	if(wave_lenth<400):
		return 0
	elif(wave_lenth>800):
		return 0
	elif(wave_lenth>=400 and wave_lenth<450):
		return (wave_lenth-400)**3/125000*0.55
	elif(wave_lenth>=450 and wave_lenth<460):
		return 0.55-(wave_lenth-450)*(0.5/10)
	elif(wave_lenth>=460 and wave_lenth<480):
		return 0.5-(wave_lenth-460)*(0.25/15)
	elif(wave_lenth>=480 and wave_lenth<520):
		return 0.25+(wave_lenth-480)*(0.35/45)
	elif(wave_lenth>=520 and wave_lenth<600):
		return 0.6+(wave_lenth-520)*(0.3/80)
	elif(wave_lenth>=600 and wave_lenth<650):
		return 0.9-(wave_lenth-600)*(0.5/50)
	elif(wave_lenth>=650 and wave_lenth<=800):
		return (800-wave_lenth)**3/3375000*0.4

