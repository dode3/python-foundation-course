import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for _ in range(36):
        for _ in range(4):
            brad.forward(100)
            brad.right(90)
        
        brad.left(10)

    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("arrow")
    angie.circle(100)

    jenni = turtle.Turtle()
    jenni.color("brown")
    jenni.shape("turtle")
    
    for _ in range(36):
        for _ in range(3):
            jenni.forward(100)
            jenni.left(120)
        jenni.left(10)
    jenni.forward(500)
        
       
    
    
    
    window.exitonclick()

draw_shapes()


