"""from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.fd(100)
timmy.color("red")

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()"""

import prettytable

from prettytable import PrettyTable
table  = PrettyTable()
print(table)
#table.add_row(["Name",1,2])
table.add_column("age",[11,22])
table.add_column("Name",[11,22])
table.align ="r"
print(table)