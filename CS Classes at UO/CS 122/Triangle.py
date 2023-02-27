import turtle

def draw_triangle(t, size):
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)

morla = turtle.Turtle()

draw_triangle(morla, 100)
