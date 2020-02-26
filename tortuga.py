import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

def figura(lados):
   for i in range(lados):
      flecha.forward(100)
      flecha.left(360/lados)

cantidad = int(input('Hola : '))
figura(cantidad)
figura(4)
figura(5)


window.mainloop()