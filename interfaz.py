from tkinter import *
from logica import *

# Variables de la calculadora

operador = ''

def App():

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
    var_costo_postres = StringVar()
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
                               textvariable = var_costo_postres)
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
                             variable = variables_comida[n])
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
                             variable = variables_bebida[n])
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
                             variable = variables_postre[n])
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

     # Genera los items de las comidas
    for n, comida in enumerate(lista_comidas):
        variables_comida.append('')
        variables_comida[n] = IntVar()
        comida = Checkbutton(panel_comidas,
                             text = comida,
                             font = ('Dosis', 19, 'bold'),
                             onvalue = 1,
                             offvalue = 0,
                             variable = variables_comida[n])
        comida.grid(row = n, column = 0, sticky = W)

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
                       width = 9)
        boton.grid(row = 0,
                   column = n)

    # Main loop de la pantalla
    ventana.mainloop()
