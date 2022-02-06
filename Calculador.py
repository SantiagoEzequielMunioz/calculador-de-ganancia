from tkinter import Frame,Tk,Label,Entry,Button,CENTER,BOTTOM,DoubleVar

raiz = Tk()
raiz.geometry('400x450')
raiz.title('CALCULADOR DE GANANCIA')

#instrucciones
impuestos=Label(raiz,text='Debes dejar Ganancia Bruta y 2 de las últimas 3 casillas vacías.',font=('Arial',10))
impuestos.grid(row=0,column=0,columnspan=2,padx=5,pady=3)
#impuestos
imp=DoubleVar()
impuestos=Label(raiz,text='Impuestos (%):',font=('Arial',14))
impuestos.grid(row=1,column=0,padx=5,pady=3)
entrada_impuestos=Entry(raiz,textvariable=imp,justify=CENTER,fg='red')
entrada_impuestos.grid(row=1,column=1,padx=5,pady=3)

#Costo del producto
op1 = DoubleVar()
costo_producto=Label(raiz,text='Costo del Producto:',font=('Arial',14))
costo_producto.grid(row=2,column=0,padx=5,pady=3)
entrada_costoProducto=Entry(raiz,textvariable=op1,justify=CENTER,fg='red')
entrada_costoProducto.grid(row=2,column=1,padx=5,pady=3)

#Costo del envío
op2=DoubleVar()
costo_envio=Label(raiz,text='Costo del Envío:',font=('Arial',14))
costo_envio.grid(row=3,column=0,padx=5,pady=3)
entrada_costoEnvio=Entry(raiz,textvariable=op2,justify=CENTER,fg='red')
entrada_costoEnvio.grid(row=3,column=1,padx=5,pady=3)

#Publicidad
op2bis=DoubleVar()
publicidad = Label(raiz,text='Gasto Publicitario:',font=('Arial',14))
publicidad.grid(row=4,column=0,padx=5,pady=3)
pub=Entry(raiz,textvariable=op2bis,justify=CENTER,fg='red')
pub.grid(row=4,column=1,padx=5,pady=3)

#Shipping (envío a cobrar)
op3=DoubleVar()
shipping=Label(raiz,text='Envío a cobrar (Shipping):',font=('Arial',14))
shipping.grid(row=5,column=0,padx=5,pady=3)
entrada_shipping=Entry(raiz,textvariable=op3,justify=CENTER,fg='green')
entrada_shipping.grid(row=5,column=1,padx=5,pady=3)

#Ganancia
op4=DoubleVar()
ganancia_bruta=Label(raiz,text='Ganancia Bruta:',font=('Arial',14))
ganancia_bruta.grid(row=6,column=0,padx=5,pady=3)
ganancia=Entry(raiz,textvariable=op4,justify=CENTER)
ganancia.grid(row=6,column=1,padx=5,pady=3)

#Precio de venta
op5=DoubleVar()
precio_venta=Label(raiz,text='Precio de Venta:',font=('Arial',14))
precio_venta.grid(row=7,column=0,padx=5,pady=3)
entrada_precioVenta=Entry(raiz,textvariable=op5,justify=CENTER)
entrada_precioVenta.grid(row=7,column=1,padx=5,pady=3)

#Porcentaje de ganancia
porcent=DoubleVar()
porcen_ganancia=Label(raiz,text='Porcentaje de ganancia (%):',font=('Arial',14))
porcen_ganancia.grid(row=8,column=0,padx=5,pady=3)
entrada_porGan=Entry(raiz,textvariable=porcent,justify=CENTER)
entrada_porGan.grid(row=8,column=1,padx=5,pady=3)

#Ganancia neta
gan_neto=DoubleVar()
ganan_neta=Label(raiz,text='Ganancia Neta:',font=('Arial',14))
ganan_neta.grid(row=9,column=0,padx=5,pady=3)
ganancia_posta=Entry(raiz,textvariable=gan_neto,justify=CENTER)
ganancia_posta.grid(row=9,column=1,padx=5,pady=3)

#BOTON CALCULAR
botonCalcular=Button(raiz,text='CALCULAR',command=lambda:verificacion(),bg='green',fg='white')
botonCalcular.grid(row=10,column=0,columnspan=2,padx=5,pady=3)
#BOTON LIMPIAR
botonLimpiar = Button(raiz,text='LIMPIAR',command=lambda:limpiar(),bg='red',fg='white')
botonLimpiar.grid(row=11,column=0,columnspan=2,padx=5,pady=3)

#Cuadro de Error
errorLabel=Label(raiz,text='DATOS NO VÁLIDOS INFANTE, VUELVA A INTENTARLO',fg='red')
errorLabel.grid(row=12,column=0,columnspan=2,pady=3)
errorLabel.grid_remove()


def verificacion():
        try:
            imp = float(entrada_impuestos.get())
            op1 = float(entrada_costoProducto.get())
            op2 = float(entrada_costoEnvio.get())
            op2bis = float(pub.get())
            op3 = float(entrada_shipping.get())
            op5 = float(entrada_precioVenta.get())
            porcent = float(entrada_porGan.get())
            gan_neto = float(ganancia_posta.get())
            error2()                
        except:
            try:
                if entrada_precioVenta.get() == '' and entrada_porGan.get() == '':
                    gan_neto = float(ganancia_posta.get())
                    situ1()
                elif entrada_precioVenta.get() == ''and ganancia_posta.get() == '':
                    porcent = float(entrada_porGan.get())
                    situ1()
                elif entrada_porGan.get() == '' and ganancia_posta.get() == '':
                    x_op4()
                else:
                    error3()
            except:
                error1()
   
def limpiar():

    entrada_impuestos.delete(0,'end')
    entrada_costoProducto.delete(0,'end')
    pub.delete(0,'end')
    entrada_costoEnvio.delete(0,'end')
    entrada_shipping.delete(0,'end')
    ganancia.delete(0,'end')
    entrada_precioVenta.delete(0,'end')
    entrada_porGan.delete(0,'end')
    ganancia_posta.delete(0,'end')
    entrada_impuestos.focus()
    errorLabel.grid_remove()
    
    ganancia ['fg'] = 'black'
    entrada_precioVenta ['fg'] = 'black'
    entrada_porGan ['fg'] = 'black'
    ganancia_posta ['fg'] = 'black'

#MÉTODOS
#   op4 = op5 + op3 - op1 - op2 - op2bis

def x_op4():
    x = op5.get() + op3.get() - op1.get() - op2.get() - op2bis.get()
    if x > 0:
        ganancia ['fg'] = 'green'
    else:
        ganancia ['fg'] = 'red'
    op4.set(round(x,3))
    taxes_porcent()

def x_op5():
    x = op1.get() + op4.get() + op2.get() + op2bis.get() - op3.get()
    if x > op1.get():
        entrada_precioVenta ['fg'] = 'green'
    else:
        entrada_precioVenta ['fg'] = 'red'
    op5.set(round(x,3))
   
def taxes_porcent():
    z = float(op4.get()-(op4.get() * (imp.get()/100)))
    if z > 0:
        ganancia_posta ['fg'] = 'green'
    else:
        ganancia_posta ['fg'] = 'red'
    gan_neto.set(round(z,3))
    costo = op1.get()+op2.get()+op2bis.get()
    y= gan_neto.get()*100/costo
    if y > 0:
        entrada_porGan ['fg'] = 'green'
    else:
        entrada_porGan ['fg'] = 'red'
    porcent.set(round(y,3))

def situ1():
    costo = op1.get()+op2.get()+op2bis.get()
    if entrada_porGan.get() == '':
        z = gan_neto.get()*100/costo
        if z > 0:
            entrada_porGan ['fg'] = 'green'
        else:
            entrada_porGan ['fg'] = 'red'
        porcent.set(round(z,3))
    else:
        z = porcent.get()*costo/100
        if z > 0:
            ganancia_posta ['fg'] = 'green'
        else:
            ganancia_posta ['fg'] = 'red'
        gan_neto.set(round(z,3))
    i = float(((gan_neto.get()*100)/(100-imp.get())))
    if i > 0:
        ganancia ['fg'] = 'green'
    else:
        ganancia ['fg'] = 'red'
    op4.set(round(i,3))
    x_op5() 

#ERRORES

def error1():
    errorLabel.grid()

def error2():
    errorLabel['text'] = 'DEJAME UN CAMPO LIBRE AUNQUE SEA MAESTRO'
    errorLabel.grid()

def error3():
    errorLabel['text'] = 'TENÉS QUE DEJAR 2 CAMPOS VACÍOS'
    errorLabel.grid()

# prueba de git


raiz.mainloop()