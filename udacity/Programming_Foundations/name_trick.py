import turtle


def draw_circle(circle, radius, color):
    circle.circle(radius)
    circle.color(color)


def A(annick):
    annick.pu()
    annick.setpos(10, 0)
    annick.pd()


def alphabet():
    window = turtle.Screen()
    window.bgcolor("blue")

    annick = turtle.Turtle()
    annick.speed(200)
    annick.shape("turtle")
    annick.right(45)

    for i in range(1, 50):
        for j in range(1, 5):
            draw_circle(annick, i, "green")
            annick.left(90)
    annick.right(45)
    annick.color("purple")
    annick.forward(200)

    A(annick)

    window.exitonclick()

alphabet()