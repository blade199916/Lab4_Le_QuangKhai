Name: Quang Khai Le 
Class: EE 104 
Professor: Christopher Pham 


Lab 4: Modeling


Github link: https://github.com/blade199916/Lab4_Le_QuangKhai.git


Youtube link: https://youtu.be/QWBciGcjdyM




Part 1: 
Part 1: The average acceleration across the most important deceleration period is calculated to determine the Head Injury Criterion (HIC). The acceleration function with respect to time must be integrated across the period from t1 to t2, where D stands for the time difference.
Depending on whether an airbag is present or not, the HIC value changes since the acceleration functions are different in each situation. The acceleration is very strong in the absence of an airbag (as depicted in plot 1). But when an airbag is present, the HIC value considerably drops (as seen in plot 2).
When d is close to 60 in plot 2, the HIC achieves its maximum value of roughly 310, which is close to the HIC value seen in Mercedes Benz automobiles.


  
  

Part 2: 
This section requires us to create a production capacity model using four different cases.
I created two Python files in total.
The first Python file displays 1.Neither the ERU nor the ICU are saturated
The overall number of beds, the number of beds in ERU, the rate at which individuals are migrating into ERU, and the rate at which they are leaving ERU are among the constants we announce.
These variables include qin, the number of persons arriving at the ERU, quot1, the pace at which patients are going to the ICU, and qout2, the number of beds required in the ERU.
To determine the inflow and outflow over the entire bed as well as the bed of ERU, we use differential equations.
Just ERU is saturated.
In a similar manner, we will plot the number of physicians entering and exiting ERU. In this situation, we get scenario 2, which is a saturated ERU. 


  
  
  
  
  

The first py file shows that just the ICU is saturated.
We solve the differential equations, take into account the nurse entering and exiting the ICU room, and plot the nursing rate/number of nurses in the ICU with time in this scenario. A saturated ICU in scenario three is depicted.
2. ERU and ICU are both saturated
In the last scenario, we take into account how much equipment enters and exits the ICU room. It will display scenario 4, which is a saturated ERU and ICU.




Part 3: 
  
  

  

Part 4: 
The game is shown by adjusting one more function of the other color dot and setting the attempt to one time only.