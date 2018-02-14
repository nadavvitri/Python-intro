import turtle

def draw_petal():
    """this method draw only one petal"""
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)

def draw_flower():
    """this method draw one flower"""
    turtle.right(45)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(135)
    turtle.forward(150)

def draw_advanced_flower():
    """this method draw one flower and move the turtle
    to allow draw another flower"""
    draw_flower()
    turtle.left(90)
    turtle.up()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()

def draw_flower_bed():
    """this method draw three flowers"""
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.down()
    draw_advanced_flower()
    draw_advanced_flower()
    draw_advanced_flower()