import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    andy = turtle.Turtle()
    andy.shape("turtle")
    andy.color("blue")
    andy.speed(1)
    andy.forward(100)
    andy.right(90)
    andy.forward(100)
    andy.right(90)
    andy.forward(100)
    andy.right(90)
    andy.forward(100)

    bob = turtle.Turtle()
    bob.shape("arrow")
    bob.circle(100)
    bob.color("yellow")

    window.exitonclick()

draw_square()