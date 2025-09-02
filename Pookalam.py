import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

# Create a turtle object
pookkalam = turtle.Turtle()
pookkalam.speed(0)  # Fastest speed

# Function to draw a circle with specific radius and color
def draw_circle(radius, color):
    pookkalam.penup()
    pookkalam.goto(0, -radius)  # Start at bottom of circle
    pookkalam.setheading(0)     # Face right
    pookkalam.pendown()
    pookkalam.color(color)
    pookkalam.begin_fill()
    pookkalam.circle(radius)
    pookkalam.end_fill()

# Function to draw a petal
def draw_petal(radius, angle, color):
    pookkalam.color(color)
    pookkalam.begin_fill()
    pookkalam.circle(radius, angle)
    pookkalam.left(180 - angle)
    pookkalam.circle(radius, angle)
    pookkalam.end_fill()
    pookkalam.left(180 - angle)

# Function to draw flower pattern
def draw_flower(num_petals, outer_radius, inner_radius, outer_color, inner_color):
    # Draw outer petals
    pookkalam.goto(0, 0)
    for _ in range(num_petals):
        draw_petal(outer_radius, 60, outer_color)
        pookkalam.left(360 / num_petals)
    
    # Draw inner petals
    pookkalam.penup()
    pookkalam.goto(0, 0)
    pookkalam.pendown()
    
    for _ in range(num_petals):
        draw_petal(inner_radius, 60, inner_color)
        pookkalam.left(360 / num_petals)

# Function to draw decorative elements
def draw_decorative_elements():
    # Draw small circles around the center
    pookkalam.penup()
    pookkalam.goto(0, 0)
    pookkalam.pendown()
    
    for i in range(36):
        pookkalam.penup()
        pookkalam.goto(0, 0)
        pookkalam.setheading(i * 10)
        pookkalam.forward(125)
        pookkalam.pendown()
        
        # Alternate colors for small circles
        if i % 2 == 0:
            pookkalam.color("yellow")
        else:
            pookkalam.color("orange")
            
        pookkalam.begin_fill()
        pookkalam.circle(10)
        pookkalam.end_fill()

def draw_center_square():
    # Draw tilted squares around the center
    pookkalam.penup()
    pookkalam.goto(0, 0)
    
    for i in range(6):
        pookkalam.penup()
        pookkalam.goto(0, 0)
        pookkalam.setheading(i * 60 + 45)  # Add 45 degrees to tilt the squares
        pookkalam.forward(0)
        pookkalam.pendown()
        
        # Alternate colors for squares
        if i % 2 == 0:
            pookkalam.color("yellow")
        else:
            pookkalam.color("orange")
            
        pookkalam.begin_fill()
        # Draw a square (4 sides, 90 degree turns)
        for _ in range(4):
            pookkalam.forward(50)  # Size of the square
            pookkalam.right(90)
        pookkalam.end_fill()        
        
# Function to draw diamond shapes
def draw_diamonds(num_diamonds, distance, size, color):
    pookkalam.penup()
    pookkalam.goto(0, 0)
    
    for i in range(num_diamonds):
        pookkalam.penup()
        angle = i * (360 / num_diamonds)
        pookkalam.setheading(angle)
        pookkalam.forward(distance)
        
        # Draw diamond
        pookkalam.color(color)
        pookkalam.pendown()
        pookkalam.begin_fill()
        for _ in range(4):
            pookkalam.forward(size)
            pookkalam.left(90)
        pookkalam.end_fill()
        
        pookkalam.color(color)
        pookkalam.begin_fill()
        for _ in range(4):
            pookkalam.forward(size)
            pookkalam.right(90)
        pookkalam.end_fill()
        
        
        # Return to center
        pookkalam.penup()
        pookkalam.goto(0, 0)
        pookkalam.pendown()

# Main function to draw the complete pookkalam
def draw_pookkalam():
    # Draw the base circles (from largest to smallest)
    draw_circle(300, "#080808")   # Outer black ring
    draw_circle(280, "#FF7F00")   # Bright yellow base
    draw_circle(260, "#FFD700")   # Orange ring
    draw_circle(240, "#ffffaa")   # Red ring

    # Draw the main flower
    draw_flower(12, 280, 240, "#FF4500", "#FFFF00")  # Orange & yellow petals
    
    # Draw inner circles
    draw_circle(200, "#02b81a")   # Green ring
    draw_circle(180, "#e47037")   # Pink ring
    
    # Draw diamond patterns
    draw_diamonds(12, 180, 20, "#3a306f")  # Dark red diamonds
    
    # Draw center flower
    draw_flower(24, 180, 110, "#80010a", "#FFD700")  # Purple & yellow petals
    draw_circle(75, "#000080")   # Navy blue center

    # Draw decorative elements
    draw_decorative_elements()
    draw_center_square()

    # Add a final dot in the very center
    pookkalam.penup()
    pookkalam.goto(0, 0)
    pookkalam.pendown()
    draw_flower(10, 20, 10, "#FF0000", "#FFC0CB")  # Red & pink center

    # Hide the turtle
    pookkalam.hideturtle()

# Draw the pookkalam
draw_pookkalam()


# Keep the window open
turtle.done()