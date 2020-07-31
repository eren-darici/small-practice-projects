import random
from math import sqrt

def estimate_pi(n):
    counter = 0
    circle_counter = 0
    

    for i in range(n):
    # I'm generating x and y values between -1 and 1 because 0 is we assumed 0 is our origin and R = 2.
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Distance is the distance from the origin.
        distance = sqrt((x ** 2) + (y ** 2))
        # If distance lower than or equal to distance, that means our point is on the circle.
        if distance <= 1:
            circle_counter += 1

        counter += 1
    
    # Since we got circle with r = 1 our equation becomes ( (circle_counter/counter) / (pi/4) )
    return (circle_counter * 4) / counter
    


print(estimate_pi(100000))