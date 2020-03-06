# Autonomous-Robo-Waiter

This is the circuit diagram of the waiter. Instead of wheels two LEDs are placed in the circuit diadram. You can replace them with wheels.

![Circuit](https://user-images.githubusercontent.com/33127885/63206556-67e26200-c0d4-11e9-938a-c6825f7719e3.PNG)

Depending on customer requirement ,the robot has to take order ,come back and   follow the same path again to serve the food in restaurants and hotels. <br/>
&nbsp;&nbsp; &nbsp;  ⦁	We have two attributes which differ for each restaurant these are:    <br/>
&nbsp;&nbsp; &nbsp;  ⦁	Number of tables. <br/>
&nbsp;&nbsp; &nbsp;  ⦁	Distance between the tables. <br/> <br/>
      2.     We have two different attributes while manufacturing the robot. <br/> 
&nbsp;&nbsp; &nbsp;   ⦁	Radius of the wheel. <br/>
&nbsp;&nbsp; &nbsp;  ⦁	Distance between the two motors or legs of the robot <br/>
&nbsp;&nbsp; &nbsp;  ⦁	RPM of the motor. <br/>

# Components 
&nbsp;&nbsp; &nbsp; ⦁	Pyboard <br/>
&nbsp;&nbsp; &nbsp; ⦁	5V DC Motors and wheels <br/>
&nbsp;&nbsp; &nbsp; ⦁	Ultrasonic Sensor <br/>
&nbsp;&nbsp; &nbsp; ⦁	Jumper wires <br/>
&nbsp;&nbsp; &nbsp; ⦁	Wheels <br/>


![image](https://user-images.githubusercontent.com/33127885/63206698-19829280-c0d7-11e9-95da-74decd855a9b.png)
# Math behind the logic
⦁	In the previous diagram the distance between the robo and X is d1 and distance between X and the table is d. So we need to  enter the X,Y beforehand. Similarly distances for all tables. <br/>
⦁	We know the rpm of the motor and we know the distance it has to travel so we can calculate the time of rotation. <br/>
⦁	We know that a circle travels a linear distance of 2r for a single rotation. <br/>
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; Time = Distance/(rpm*2r) <br/>
⦁	To rotate the robo or take a turn, one of the wheel is stopped and other is rotated in clockwise direction..Time taken to turn can be calculated as : <br/> 
 &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;  D = R𝜃 <br/>
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;Time = D/(rpm*2r) <br/>
Note: Here r is the radius of wheel. 𝜃 for the first rotation is 𝜋/2 and for the second rotation it is 𝜋

# Algorithm 
&nbsp;&nbsp; &nbsp;⦁	Firstly we enter the distance of the tables form the counter. <br/>
&nbsp;&nbsp; &nbsp;⦁	The robot goes to the desired table as requested by the owner. <br/>
&nbsp;&nbsp; &nbsp;⦁	Once the robo has reached the table it waits till a switch is pressed to take order or serve the customer. <br/>
&nbsp;&nbsp; &nbsp;⦁	When the switch is pressed it returns back to its initial state. <br/>
&nbsp;&nbsp; &nbsp;⦁	And the process is repeated to deliver the items required to the customers. <br/>
&nbsp;&nbsp; &nbsp;⦁	An ultrasonic sensor is used  to avoid any collision with any obstacle present in front of the robo. <br/>
&nbsp;&nbsp; &nbsp;⦁	The radius of the wheel is used to calculate the distance travelled. <br/>

<b> Led 1 is used to show the working of left leg of the robo(actually motor1) and led2 is taken for right leg of the robo (motor2) </b> <br/>

When table 1 is  to be served: <br/>
&nbsp;&nbsp; &nbsp;⦁	Both the wheel rotates in clockwise direction and the robo goes straight .<br/>
&nbsp;&nbsp; &nbsp;⦁	Then it takes a right angle turn when it has to turn by clockwise rotation of only left wheel .<br/>
&nbsp;&nbsp; &nbsp;⦁	When the robot reaches the table both the wheels stops rotating until it has taken order and served the customer .<br/>
&nbsp;&nbsp; &nbsp;⦁	Left wheel rotates by 180 degree turn when the switch is pressed.<br/>
&nbsp;&nbsp; &nbsp;⦁	After calculated delay taken to turn, both the motors are made to rotate in clockwise direction. <br/>
&nbsp;&nbsp; &nbsp;⦁	In similar manner it comes back to the counter. <br/> 
&nbsp;&nbsp; &nbsp;⦁	In the code pyb.millis() returns the time elapsed since the board was last reset. <br/> 
&nbsp;&nbsp; &nbsp;⦁	We should subtract the time which the robo has not moved. (See the code for detailed explanation). <br/>
&nbsp;&nbsp; &nbsp;⦁	We are using here so that we can know how much time we have to run the motor. <br/>

<b> It does the same thing to take order from customer on any table just the delay and the motor to rotate changes for different path. </b>

Note: <br/>
&nbsp;&nbsp; &nbsp;⦁	 This is done because giving the value high for the led is the same as giving high for a motor. <br/>
&nbsp;&nbsp; &nbsp;⦁	All the distances are in m. <br/>
&nbsp;&nbsp; &nbsp;⦁	Assumed rpm is 4000. <br/>
