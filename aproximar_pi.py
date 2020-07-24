from tkinter import *

#-------------Funciones--------------------

def serieLeibniz(n):
	if(n==-1):
		return 0;
	else:
		return 4*pow(-1,n)/float(2*n+1)+serieLeibniz(n-1)

def serieNilakantha(n):
	if(n==-1):
		return float(3)
	else:
		return float(4*(pow(-1,n)/float(pow(2*n+3,3)-(2*n+3)))+serieNilakantha(n-1))

def obtenerPI():
    n=int(cuadroTex.get())
    PI1 = "Aproximacion a PI: " + str(serieLeibniz(n))
    PI2 = "Aproximacion a PI: " + str(serieNilakantha(n))

    var1.set(PI1)
    var2.set(PI2)


rous=Tk()
rous.iconbitmap("pi.ico")
rous.title("Calcular PI")

#-----------------Frame------------------------
miFrame=Frame(rous,borderwidth=2, relief="solid")
miFrame.pack()
miFrame.config(background="dark turquoise")

var1=StringVar()
var2=StringVar()

#---------------IngresarDato-------------------
miLabel=Label(miFrame,text="Ingrese Dato:",font=2,borderwidth=2, relief="groove")
miLabel.grid(row=0,column=0,padx=10,pady=10)
miLabel.config(background="DarkSlateGray1")

cuadroTex=Entry(miFrame,width=35)
cuadroTex.grid(row=0,column=1,padx=10,pady=10)
cuadroTex.config(background="black",fg="#03f943",justify="right")

boton=Button(miFrame,text="Enviar",command=obtenerPI)
boton.grid(row=1,column=1)
boton.config(background="blue2",fg="white")

#boton2=Button(miFrame,text="Imprimir",command=serieLeibniz)
#boton2.grid(row=1,column=2,padx=10,pady=10)
#boton2.config(background="blue2",fg="white")

#---------------Leibniz----------------------------
miLabelLebn=Label(miFrame,text="Leibniz:",font=2,borderwidth=2, relief="groove")
miLabelLebn.grid(row=2,column=0,padx=10,pady=10)
miLabelLebn.config(background="DarkSlateGray1")

cuadroLebn=Entry(miFrame,textvariable=var1,width=35)
cuadroLebn.grid(row=2,column=1,padx=10,pady=10)
cuadroLebn.config(background="black",fg="#03f943",justify="right")

#----------------Nilakantha-------------------------
miLabelNila=Label(miFrame,text="Nilakantha:",font=2,borderwidth=2, relief="groove")
miLabelNila.grid(row=3,column=0,padx=10,pady=10)
miLabelNila.config(background="DarkSlateGray1")

cuadroNila=Entry(miFrame, textvariable=var2,width=35)
cuadroNila.grid(row=3,column=1,padx=10,pady=10)
cuadroNila.config(background="black",fg="#03f943",justify="right")


rous.mainloop()