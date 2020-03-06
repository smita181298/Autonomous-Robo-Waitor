import pyb

led1 = pyb.Pin('X1',pyb.Pin.OUT_PP)
led2 = pyb.Pin('X2',pyb.Pin.OUT_PP)
sw = pyb.switch()
y = int(input())
r = 2.54 /100
R = 2 * r 
rpm = 4000 
d=1
d1=1
d2=1
d3=3
d4=3
while True:
	if y==1:
		led1.on()
		led2.on()
		delay(((d1/(2*rpm*r)))*60*1000)
		led2.off()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led1.on()
		led2.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led1.off()
		led2.off()
		while True:
			if sw.value():
				break
		led1.on()
		led2.off()
		delay(((2*((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led1.on()
		led2.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led1.off()
		led2.on()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led1.on()
		led2.on()
		delay(((d1/(2*rpm*r)))*60*1000)
		led1.off()
		led2.off()
		break
	elif y==2:
		led2.on()
		led1.on()
		delay(((d2/(2*rpm*r)))*60*1000)
		led1.off()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led2.on()
		led1.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led2.off()
		led1.off()
		while True:
			if sw.value():
				break
		led2.on()
		led1.off()
		delay(((2*((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led2.on()
		led1.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led2.off()
		led1.on()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led2.on()
		led1.on()
		delay(((d2/(2*rpm*r)))*60*1000)
		led2.off()
		led1.off()
		break
	elif y==3:
		led2.on()
		led1.on()
		delay(((d3/(2*rpm*r)))*60*1000)
		led1.off()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led2.on()
		led1.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led2.off()
		led1.off()
		while True:
			if sw.value():
				break
		led2.on()
		led1.off()
		delay(((2*((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led2.on()
		led1.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led2.off()
		led1.on()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led2.on()
		led1.on()
		delay(((d3/(2*rpm*r)))*60*1000)
		led2.off()
		led1.off()
		break
	elif y==4:
		led1.on()
		led2.on()
		delay(((d4/(2*rpm*r)))*60*1000)
		led2.off()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led1.on()
		led2.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led1.off()
		led2.off()
		while True:
			if sw.value():
				break
		led1.on()
		led2.off()
		delay(((2*((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led1.on()
		led2.on()
		delay(((d/(2*rpm*r)))*60*1000)
		led1.off()
		led2.on()
		delay(((((R*3.14)/2)/(2*rpm*r)))*60*1000)
		led1.on()
		led2.on()
		delay(((d4/(2*rpm*r)))*60*1000)
		led1.off()
		led2.off()
		break
	
	
		
		
				
		
		
	