from tkinter import *
from logica import *

def App():

    # Iniciar a tkinter
    ventana = Tk()

    # Tamaño de la ventana y evitar que se pueda maximizar
    ventana.geometry('1020x630+400+200')
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
    
    # Panel drecho > panel recibo
    panel_recibo = Frame(panel_derecho, 
                         bd = 1, 
                         relief = FLAT, 
                         bg = 'burlywood')
    panel_recibo.pack()

    # Panel drecho > panel botones
    panel_botones = Frame(panel_derecho, 
                         bd = 1, 
                         relief = FLAT, 
                         bg = 'burlywood')
    panel_botones.pack()

    # Main loop de la pantalla
    ventana.mainloop()
