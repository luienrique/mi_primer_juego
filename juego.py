from tkinter import*
import random
#----------------------------------------
#----------variables globales------------
#----------------------------------------

BASE = 760
ALTURA = 566

#----------------------------------------
#----------VENTANA PRINCIPAL-------------
#----------------------------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("800x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

#----------------------------------------
#----------frame de graficacion----------
#----------------------------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="red", width=780 , height=580 )
frame_graficacion.place(x=10 , y=10)

#creacion canvas

c = Canvas (frame_graficacion , width=BASE, height=ALTURA)
c.config(bg="white")
c.place(x=10,y=10)

# dibujar lineas
rect_1 = c. create_rectangle(BASE/2-280,ALTURA/2+170,BASE/2-200,30/2, fill="dark gray")
rect_2 = c. create_rectangle(BASE/2+280,ALTURA/2+170,BASE-20,30/2, fill="dark gray")
rect_3 = c. create_rectangle(BASE/2-200,ALTURA/2-160,BASE-100,ALTURA/2+90, fill="BLACK")
rect_4 = c. create_rectangle(BASE/2-180,ALTURA/2-30,BASE/2-80,ALTURA/2-60, fill="yellow")
rect_5 = c. create_rectangle(BASE/2-70,ALTURA/2-30,BASE/2+30,ALTURA/2-60, fill="yellow")
rect_6 = c. create_rectangle(BASE/2+40,ALTURA/2-30,BASE/2+140,ALTURA/2-60, fill="yellow")
rect_7 = c. create_rectangle(BASE/2+150,ALTURA/2-30,BASE/2+260,ALTURA/2-60, fill="yellow")

# agragar una imagen al canvas 
img_car1 = PhotoImage(file="img/car1.png")
car1 = c.create_image(BASE/4-60,ALTURA/4,image=img_car1)

img_car2 = PhotoImage(file="img/car2.png")
car2 = c.create_image(BASE/4-60,ALTURA/4*3,image=img_car2)


#desplegar ventana
ventana_principal.mainloop()