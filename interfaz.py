from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# Variables de la calculadora

operador = ''

def App():

    # Lista de productos
    lista_comidas = ['Pollo','Birria','Pescado','Menudo','Pozole',
                    'Carnitas','Tacos','Tamales']
    lista_bebidas = ['Agua','Coca-Cola','Mirinda','Jugo','Power',
                    'Gatorade','Cerveza','Michelada']
    lista_postres = ['Carlotta','Helado','Pastel','Chocoflan',
                    'Galetina','Flan','Pay','Churros']
    
    precios_comida = [1.32,1.65,2.31,3.22,1.22,1.99,2.05,2.65]
    precios_bebida = [0.25,2,1.21,1.54,1.08,1.10,2.00,1.58]
    precios_postre = [1.54,1.68,1.32,1.97,2.55,2.14,1.94,1.74]

    # Variables de los checkbuttons
    variables_comida = []
    variables_bebida = []
    variables_postre = []

    # Variables para la cantidad de comidas, bebidas y postres
    cuadros_comida = []
    texto_comida = []
    cuadros_bebida = []
    texto_bebida = []
    cuadros_postre = []
    texto_postre = []

    # Funcion llamada al oprimir boton de la calculadora

    def click_boton(boton):
        global operador
        visor_calculadora.delete(0, END)
        if boton == 'CE':
            operador = ''
        elif boton == '=':
            resultado = str(eval(operador))
            visor_calculadora.insert(END, resultado)
            operador = ''
        else:
            operador = operador + boton
            visor_calculadora.insert(END, operador)
    
    # Funcion para habilitar las cantidades con los checkbuttons

    def revisar_check():

        # Revision de variables comida
        for n, _ in enumerate(cuadros_comida):
            if variables_comida[n].get() == 1:
                cuadros_comida[n].config(state = NORMAL)
                if  texto_comida[n].get() == '0':       
                    cuadros_comida[n].delete(0, END)
                    cuadros_comida[n].focus()
            else:
                cuadros_comida[n].config(state = DISABLED)
                texto_comida[n].set('0') 

        # Revision de variables bebida
        for n, _ in enumerate(cuadros_bebida):
            if variables_bebida[n].get() == 1:
                cuadros_bebida[n].config(state = NORMAL)
                if  texto_bebida[n].get() == '0':       
                    cuadros_bebida[n].delete(0, END)
                    cuadros_bebida[n].focus()
            else:
                cuadros_bebida[n].config(state = DISABLED)
                texto_bebida[n].set('0') 

        # Revision de variables postre
        for n, _ in enumerate(cuadros_postre):
            if variables_postre[n].get() == 1:
                cuadros_postre[n].config(state = NORMAL)
                if  texto_postre[n].get() == '0':       
                    cuadros_postre[n].delete(0, END)
                    cuadros_postre[n].focus()
            else:
                cuadros_postre[n].config(state = DISABLED)
                texto_postre[n].set('0')     

    # Funcion que actua con los botones de totales y recibo
    def botones_totales(boton):

        # Si se presiona el boton total
        if boton == 'Total':

            # Cuenta de la comida
            sub_total_comida = 0
            for n, cantidad in enumerate(texto_comida):
                sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[n]) 

            # Cuenta de la bebida
            sub_total_bebida = 0
            for n, cantidad in enumerate(texto_bebida):
                sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[n]) 

            # Cuenta de la postre
            sub_total_postre = 0
            for n, cantidad in enumerate(texto_postre):
                sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[n]) 

            # Subtotal de las tres categorias
            subtotal = sub_total_comida + sub_total_bebida + sub_total_postre

            # Impuestos del 7%
            impuesto = subtotal * 0.1

            # Total de la cuenta
            total = subtotal + impuesto

            # Asignacion a los cuadros de texto
            var_costo_comida.set(f'$ {round(sub_total_comida,2)}')
            var_costo_bebida.set(f'$ {round(sub_total_bebida,2)}')
            var_costo_postre.set(f'$ {round(sub_total_postre,2)}')

            var_subtotal.set(f'$ {round(subtotal,2)}')
            var_impuesto.set(f'$ {round(impuesto,2)}')
            var_total.set(f'$ {round(total,2)}')
        
        # Si se presiona el boton recibo
        elif boton == 'Recibo':
            # Obtiene y agrega fecha hora y folio
            texto_recibo.delete(1.0, END)
            num_recibo = f'N# - {random.randint(1000, 9999)}'
            fecha = datetime.datetime.now()
            fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
            texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
            texto_recibo.insert(END, f'*' * 63 + '\n')

            # Agrega encabezados del recibo
            texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
            texto_recibo.insert(END, f'-' * 75 + '\n')

            # Agrega items de comida
            for n, comida in enumerate(texto_comida):
                if comida.get() != '0' and comida.get != '':
                    texto_recibo.insert(END, f'{lista_comidas[n]}\t\t'
                                             f'{comida.get()}\t'
                                             f'$ {int(comida.get()) * precios_comida[n]}\n')
                    
            # Agrega items de bebida
            for n, bebida in enumerate(texto_bebida):
                if bebida.get() != '0' and bebida.get != '':
                    texto_recibo.insert(END, f'{lista_bebidas[n]}\t\t'
                                             f'{bebida.get()}\t'
                                             f'$ {int(bebida.get()) * precios_bebida[n]}\n')
            
            # Agrega items de postre
            for n, postre in enumerate(texto_postre):
                if postre.get() != '0' and postre.get != '':
                    texto_recibo.insert(END, f'{lista_postres[n]}\t\t'
                                             f'{postre.get()}\t'
                                             f'$ {int(postre.get()) * precios_postre[n]}\n')

            # Agrega los subtotales
            texto_recibo.insert(END, f'-' * 75 + '\n')
            texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
            texto_recibo.insert(END, f' Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
            texto_recibo.insert(END, f' Costo del postre:   \t\t\t{var_costo_postre.get()}\n')

            # Agrega el total 
            texto_recibo.insert(END, f'-' * 75 + '\n')
            texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
            texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuesto.get()}\n')
            texto_recibo.insert(END, f' Total:   \t\t\t{var_total.get()}\n')

            # Cierre del recibo
            texto_recibo.insert(END, f'*' * 63 + '\n')
            texto_recibo.insert(END, f'Lo esperamos pronto')

        # Si se presiona el boton de Guardar
        elif boton == 'Guardar':
            info_recibo = texto_recibo.get(1.0, END)
            archivo = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
            archivo.write(info_recibo)
            archivo.close()
            messagebox.showinfo('Informacion', ' Su recibo ha sido guardado')

        # Si se presiona el boton de resetear
        elif boton == 'Resetear':
            texto_recibo.delete(0.1, END)

            for texto in texto_comida:
                texto.set('0')
            for texto in texto_bebida:
                texto.set('0')
            for texto in texto_postre:
                texto.set('0')

            for cuadro in cuadros_comida:
                cuadro.config(state=DISABLED)
            for cuadro in cuadros_bebida:
                cuadro.config(state=DISABLED)
            for cuadro in cuadros_postre:
                cuadro.config(state=DISABLED)

            for v in variables_comida:
                v.set(0)
            for v in variables_bebida:
                v.set(0)
            for v in variables_postre:
                v.set(0)

            var_costo_comida.set('')
            var_costo_bebida.set('')
            var_costo_postre.set('')
            var_subtotal.set('')
            var_impuesto.set('')
            var_total.set('')

    # Iniciar a tkinter
    ventana = Tk()

    # Tamaño de la ventana y evitar que se pueda maximizar
    ventana.geometry('1300x630+400+200')
    ventana.resizable(0, 0)

    # Titulo e icono de la ventana
    ventana.title("Roman Food - Sistema de Facturacion")

    # Configuracion de la ventana
    ventana.config(bg = "burlywood")

    # Configuracion y contenido del Panel superior
    panel_superior = Frame(ventana, bd = 1, relief = FLAT)
    panel_superior.pack(side = TOP)

    etiqueta_titulo = Label(panel_superior, 
                            text = 'Sistema de Facturacion',
                            fg = 'azure4',
                            font = ('Dosis', 58),
                            bg = 'burlywood',
                            width = 27)
    etiqueta_titulo.grid(row = 0, column = 0)

    # Configuracion y contenido del panel izquierdo
    panel_izquierdo = Frame(ventana, bd = 1, relief = FLAT)
    panel_izquierdo.pack(side = LEFT)

    # Panel izquierdo > panel costos
    panel_costos = Frame(panel_izquierdo,
                         bd = 1,
                         relief = FLAT,
                         bg = 'azure4',
                         padx = 50)
    panel_costos.pack(side = BOTTOM)

    # Etiquetas de costos y campos de entrada
    var_costo_comida = StringVar()
    var_costo_bebida = StringVar()
    var_costo_postre = StringVar()
    var_subtotal = StringVar()
    var_impuesto = StringVar()
    var_total = StringVar()

    # Comida
    etiqueta_costo_comida = Label(panel_costos,
                                  text = 'Costo Comida',
                                  font = ('Dosis',12,'bold'),
                                  bg = 'azure4',
                                  fg = 'white')
    etiqueta_costo_comida.grid(row = 0, column = 0, padx = 40)

    texto_costo_comida = Entry(panel_costos,
                               font = ('Dosis',12,'bold'),
                               bd = 1,
                               width = 10,
                               state = 'readonly',
                               textvariable = var_costo_comida)
    texto_costo_comida.grid(row = 0, column = 1, padx = 40)

    # Bebida
    etiqueta_costo_bebida = Label(panel_costos,
                                  text = 'Costo Bebida',
                                  font = ('Dosis',12,'bold'),
                                  bg = 'azure4',
                                  fg = 'white')
    etiqueta_costo_bebida.grid(row = 1, column = 0, padx = 40)

    texto_costo_bebida = Entry(panel_costos,
                               font = ('Dosis',12,'bold'),
                               bd = 1,
                               width = 10,
                               state = 'readonly',
                               textvariable = var_costo_bebida)
    texto_costo_bebida.grid(row = 1, column = 1, padx = 40)

    # Postres
    etiqueta_costo_postres = Label(panel_costos,
                                  text = 'Costo Postres',
                                  font = ('Dosis',12,'bold'),
                                  bg = 'azure4',
                                  fg = 'white')
    etiqueta_costo_postres.grid(row = 2, column = 0, padx = 40)

    texto_costo_postres = Entry(panel_costos,
                               font = ('Dosis',12,'bold'),
                               bd = 1,
                               width = 10,
                               state = 'readonly',
                               textvariable = var_costo_postre)
    texto_costo_postres.grid(row = 2, column = 1, padx = 40)

    # Subtotal
    etiqueta_subtotal = Label(panel_costos,
                                  text = 'Subtotal',
                                  font = ('Dosis',12,'bold'),
                                  bg = 'azure4',
                                  fg = 'white')
    etiqueta_subtotal.grid(row = 0, column = 2, padx = 40)

    texto_subtotal = Entry(panel_costos,
                               font = ('Dosis',12,'bold'),
                               bd = 1,
                               width = 10,
                               state = 'readonly',
                               textvariable = var_subtotal)
    texto_subtotal.grid(row = 0, column = 3, padx = 40)

    # Impuesto
    etiqueta_impuesto = Label(panel_costos,
                                  text = 'Impuesto',
                                  font = ('Dosis',12,'bold'),
                                  bg = 'azure4',
                                  fg = 'white')
    etiqueta_impuesto.grid(row = 1, column = 2, padx = 40)

    texto_impuesto = Entry(panel_costos,
                               font = ('Dosis',12,'bold'),
                               bd = 1,
                               width = 10,
                               state = 'readonly',
                               textvariable = var_impuesto)
    texto_impuesto.grid(row = 1, column = 3, padx = 40)

    # Total
    etiqueta_total = Label(panel_costos,
                                  text = 'Total',
                                  font = ('Dosis',12,'bold'),
                                  bg = 'azure4',
                                  fg = 'white')
    etiqueta_total.grid(row = 2, column = 2, padx = 40)

    texto_total = Entry(panel_costos,
                               font = ('Dosis',12,'bold'),
                               bd = 1,
                               width = 10,
                               state = 'readonly',
                               textvariable = var_total)
    texto_total.grid(row = 2, column = 3, padx = 40)

    # Panel izquierdo > panel comidas
    panel_comidas = LabelFrame(panel_izquierdo,
                               text = 'Comida',
                               font = ('Dosis', 19, 'bold'),
                               bd = 1,
                               relief = FLAT,
                               fg = 'azure4',)
    panel_comidas.pack(side = LEFT)

    # Genera los items de las comidas
    for n, comida in enumerate(lista_comidas):
        # Crear los checkbutton
        variables_comida.append('')
        variables_comida[n] = IntVar()
        comida = Checkbutton(panel_comidas,
                             text = comida,
                             font = ('Dosis', 19, 'bold'),
                             onvalue = 1,
                             offvalue = 0,
                             variable = variables_comida[n],
                             command = revisar_check)
        comida.grid(row = n, column = 0, sticky = W)

        # Crear los cuadros de entrada
        cuadros_comida.append('')
        texto_comida.append('')
        texto_comida[n] = StringVar()
        texto_comida[n].set('0')
        cuadros_comida[n] = Entry(panel_comidas,
                                  font = ('Dosis', 18, 'bold'),
                                  bd = 1,
                                  width = 6,
                                  state = DISABLED,
                                  textvariable = texto_comida[n])
        cuadros_comida[n].grid(row = n, column = 1)

    # Panel izquierdo > panel bebidas
    panel_bebidas = LabelFrame(panel_izquierdo,
                               text = 'Bebidas',
                               font = ('Dosis', 19, 'bold'),
                               bd = 1,
                               relief = FLAT,
                               fg = 'azure4',)
    panel_bebidas.pack(side = LEFT)

     # Genera los items de las bebidas
    for n, bebida in enumerate(lista_bebidas):
        
        # Crear los checkbutton
        variables_bebida.append('')
        variables_bebida[n] = IntVar()
        bebida = Checkbutton(panel_bebidas,
                             text = bebida,
                             font = ('Dosis', 19, 'bold'),
                             onvalue = 1,
                             offvalue = 0,
                             variable = variables_bebida[n],
                             command = revisar_check)
        bebida.grid(row = n, column = 0, sticky = W)

        # Crear los cuadros de entrada
        cuadros_bebida.append('')
        texto_bebida.append('')
        texto_bebida[n] = StringVar()
        texto_bebida[n].set('0')
        cuadros_bebida[n] = Entry(panel_bebidas,
                                  font = ('Dosis', 18, 'bold'),
                                  bd = 1,
                                  width = 6,
                                  state = DISABLED,
                                  textvariable = texto_bebida[n])
        cuadros_bebida[n].grid(row = n, column = 1)

    # Panel izquierdo > panel postres
    panel_postres = LabelFrame(panel_izquierdo,
                               text = 'Postres',
                               font = ('Dosis', 19, 'bold'),
                               bd = 1,
                               relief = FLAT,
                               fg = 'azure4',)
    panel_postres.pack(side = LEFT)

     # Genera los items de las postres
    for n, postre in enumerate(lista_postres):

        #Crear los checkbuttons
        variables_postre.append('')
        variables_postre[n] = IntVar()
        postre = Checkbutton(panel_postres,
                             text = postre,
                             font = ('Dosis', 19, 'bold'),
                             onvalue = 1,
                             offvalue = 0,
                             variable = variables_postre[n],
                             command = revisar_check)
        postre.grid(row = n, column = 0, sticky = W)

        # Crear los cuadros de entrada
        cuadros_postre.append('')
        texto_postre.append('')
        texto_postre[n] = StringVar()
        texto_postre[n].set('0')
        cuadros_postre[n] = Entry(panel_postres,
                                  font = ('Dosis', 18, 'bold'),
                                  bd = 1,
                                  width = 6,
                                  state = DISABLED,
                                  textvariable = texto_postre[n])
        cuadros_postre[n].grid(row = n, column = 1)

    # Configuracion y contenido del panel derecho
    panel_derecho = Frame(ventana, bd = 1, relief = FLAT)
    panel_derecho.pack(side = RIGHT)

    # Panel derecho > panel calculadora
    panel_calculadora = Frame(panel_derecho, 
                              bd = 1, 
                              relief = FLAT, 
                              bg = 'burlywood')
    panel_calculadora.pack()

    # Calculadora
    visor_calculadora = Entry(panel_calculadora,
                              font = ('Dosis', 16, 'bold'),
                              width = 32,
                              bd = 1)
    visor_calculadora.grid(row = 0,
                           column = 0,
                           columnspan = 4)
    
    botones_calculadora = ['7','8','9','+',
                           '4','5','6','-',
                           '1','2','3','*',
                           '=','CE','0','/']
    
    fila = 1
    columna = 0

    for boton in botones_calculadora:
        boton = Button(panel_calculadora,
                       text = boton,
                       font = ('Dosis', 16, 'bold'),
                       fg = 'white',
                       bg = 'azure4',
                       bd = 1,
                       width = 8,
                       command = lambda valor=boton: click_boton(valor))
        boton.grid(row = fila,
                   column = columna)
        
        if columna == 3:
            fila += 1
        
        columna += 1

        if columna == 4:
            columna = 0
    
    # Panel drecho > panel recibo
    panel_recibo = Frame(panel_derecho, 
                         bd = 1, 
                         relief = FLAT, 
                         bg = 'burlywood')
    panel_recibo.pack()

    # Area de recibo
    texto_recibo = Text(panel_recibo,
                        font = ('Dosis', 12, 'bold'),
                        bd = 1,
                        width = 42,
                        height = 10)
    texto_recibo.grid(row = 0,
                      column = 0)

    # Panel drecho > panel botones
    panel_botones = Frame(panel_derecho, 
                         bd = 1, 
                         relief = FLAT, 
                         bg = 'burlywood')
    panel_botones.pack()

    # Botones
    botones = ['Total','Recibo','Guardar','Resetear']
    for n, boton in enumerate(botones):
        boton = Button(panel_botones,
                       text = boton,
                       font = ('Dosis',14,'bold'),
                       fg = 'white',
                       bg = 'azure4',
                       bd = 1,
                       width = 9,
                       command = lambda valor = boton: botones_totales(valor))
        boton.grid(row = 0,
                   column = n)

    # Main loop de la pantalla
    ventana.mainloop()
