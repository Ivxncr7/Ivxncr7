from turtle import Turtle, exitonclick



def myfunction():
    print ("hello world")

    bob = Turtle()
    bob .shape("turtle")

    bob .color("black")
    bob .fillcolor("gold")
    bob .pensize(5)

    bob.forward(50)
    bob.right(90)
    bob.forward(50)



def mifunction():
    bob = Turtle()
    bob.begin_fill()
    bob.setheading(0)
    bob.forward(30)
    bob.left(120)S
    bob.forward(30)
    bob.left(120)
    bob.forward(30)
    bob.end_fill()

    bob.setheading(90)
    bob.forward(30)
    bob.right(45)
    bob.forward(30)
    bob.right(45)
    bob.forward(30)
    bob.right(45)


                  





if __name__ == "__main__":
    myfunction()
    mifunction()
    myfunction()
    exitonclick()
