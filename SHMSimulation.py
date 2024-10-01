Web VPython 3.2

################################################################################
# CONSTANTS AND VARIABLES
################################################################################

g = 9.81 # acceleration due to gravity (m/s^2)

theta0 = 15.0 # Initial angular displacement (degrees)
theta = radians(theta0) # Initial angular displacement (radians)
omega = 0.0 # Initial angular velocity

################################################################################
# SET UP DISPLAY
################################################################################

canvas(center = vector(0, -0.6, 0), background = color.white)

################################################################################
# SET UP VISUAL OBJECTS
################################################################################

# Set up the support as a compound object
box1 = box(pos = vector(0, 0.025, 0), size = vector(0.05, 0.05 ,0.6),
           color = color.green)
box2 = box(pos = vector(0, 0.025, 0.25), size = vector(1.0, 0.05, 0.2),
           color = color.green)
box3 = box(pos = vector(0, 0.025, -0.25), size = vector(1.0, 0.05, 0.2),
           color = color.green)

support = compound([box1,box2,box3])

# length of pendulum (m)
l = 0.5
dl = 0.1

# Set up the bob
bob = sphere(pos = vector(l*sin(theta), -l*cos(theta), 0),
             radius = 0.05, color = color.blue)

# Set up the rod
rod = cylinder(pos = vector(0.0, 0.0, 0.0),
               axis = bob.pos,
               radius = 0.01,
               color = color.red)



# Define timesteps
t = 0.0         # Intitial time
dt = 0.000001       # Time step
t_max = 15.0     # End time

dtheta0 = 0.1

# Create a graph object
graph1 = graph(xtitle = 'time (seconds)', ytitle = 'displacement angle (rads)')

graph2 = graph(xtitle = 'theta (degrees)', ytitle = 'time period (seconds)')

# small angle approx curve
function1 = gdots(graph = graph2, color = color.red)

while theta0 < 20:
    theta = radians(theta0)
    bob.pos = vector(l*sin(theta), -l*cos(theta), 0)
    rod.axis = bob.pos
    T = 0
    count = True
    while count:
        omegaOld = omega
        rate(1/dt)


    #Calculate acceleration
        alpha = (-g/l)*sin(theta)

    #Update angular velocity
        omega = omega + alpha*dt

    #Update angular displacement
        theta = theta + omega*dt

    #Update bob position
        bob.pos = vector(l*sin(theta), -l*cos(theta), 0)

    #Update rod position
        rod.axis = bob.pos

    #Update Time
        t = t + dt
        T = T + dt

    #Displacement as it should look
        AnalyticalSol = theta0*cos((sqrt(g/l))*t)


        if omegaOld * omega < 0 and theta > 0:
            count = False
            print ("Angular Displacement (rad):", theta, "Time Period (s):", T)
            function1.plot(degrees(theta), T)
            T = 0

    theta0 = theta0 + dtheta0
