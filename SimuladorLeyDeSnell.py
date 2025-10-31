import tkinter as tk # Se importa la libreria tkinter para hacer la interfaz grafica
import customtkinter as ctk # Se importa la libreria customtkinter para mejorar la interfaz gráfica y hacerla as moderno
import math # Se importa la funcion math para

# ================================================================ # Comentario que inicia una sección decorativa con un separador visual para la descripción del simulador
# 🧪 SIMULADOR DE LA LEY DE SNELL # Comentario con el título del simulador, usando un emoji para decoración
# ------------------------------------------------ # Comentario con un separador horizontal
# Descripción: # Comentario que inicia la descripción del programa
#   Este simulador muestra gráficamente cómo se refracta y refleja # Continuación del comentario descriptivo, explicando la funcionalidad gráfica de refracción y reflexión de rayos de luz
#   un rayo de luz al pasar por distintas interfaces (materiales). # Continuación, especificando que simula el paso de luz por interfaces de materiales
#   Permite cambiar el número de interfaces, materiales y ángulo # Continuación, mencionando las opciones interactivas para el usuario
#   de incidencia. Se basa en la Ley de Snell: # Continuación, indicando la base física en la Ley de Snell
# # Línea vacía en el comentario para separación
#        n₁ * sin(θ₁) = n₂ * sin(θ₂) # Comentario que muestra la fórmula de la Ley de Snell, donde n1 y n2 son índices de refracción, θ1 y θ2 son ángulos respecto a la normal
# # Línea vacía en el comentario
#   Donde θ es el ángulo respecto a la normal (línea vertical). # Comentario explicando qué representa θ en la fórmula
# ================================================================ # Comentario que cierra la sección descriptiva con un separador visual

# Configuración inicial del tema de CustomTkinter # Comentario que indica el inicio de la configuración inicial de temas para customtkinter
ctk.set_appearance_mode("dark")  # Modo oscuro por defecto # Esta línea establece el modo de apariencia inicial de customtkinter en "dark" (oscuro), afectando los colores de todos los widgets
ctk.set_default_color_theme("blue")  # Tema azul # Esta línea establece el tema de color predeterminado en "blue", que define la paleta de colores base para los widgets

class SimuladorSnell: # Se crea una clase para hacer el simulador # Esta línea define la clase SimuladorSnell, que encapsula toda la lógica y elementos del simulador de la Ley de Snell

    def __init__(self, ventana_principal): # Definición del constructor de la clase, que recibe ventana_principal como parámetro (la ventana raíz de la GUI)
        """ Se crea el constructor de la clase para inicializar la ventana principal del simulador, # Docstring que describe el propósito del constructor: inicializar la ventana, variables y controles
            las variables globales y los controles de usuario.""" # Continuación del docstring

        self.ventana_principal = ventana_principal # Le asigna la ventana que llega como parametro a la ventana de la clase # Esta línea asigna el parámetro ventana_principal a un atributo de instancia self.ventana_principal para acceso dentro de la clase
        self.ventana_principal.title("SIMULADOR DE LA LEY DE SNELL") # Se le asigna el titulo a la ventana # Esta línea establece el título de la ventana principal como "SIMULADOR DE LA LEY DE SNELL"
        self.ventana_principal.geometry("1600x900") # Se definen sus dimensiones # Esta línea configura el tamaño inicial de la ventana a 1600 píxeles de ancho por 900 de alto

        # Personaliza el color de fondo general con un degradado desde #E8EDF2 (gris azulado claro) hasta #1a1a2e (azul muy oscuro) # Comentario explicando la personalización del fondo
        self.ventana_principal.configure(fg_color=("#E8EDF2", "#1a1a2e")) # Esta línea configura el color de foreground (fondo) de la ventana como una tupla para modos claro y oscuro, creando un efecto de degradado

        # Se crea un diccionario de materiales disponibles para las interfaces, con sus índices de refracción # Comentario describiendo el diccionario de materiales
        self.materiales_disponibles = { # Inicio de la definición del atributo self.materiales_disponibles como un diccionario
            "Vacío": 1.0, # Clave "Vacío" con valor 1.0 (índice de refracción del vacío)
            "Aire": 1.0003, # Clave "Aire" con valor 1.0003 (índice aproximado del aire)
            "Agua": 1.333, # Clave "Agua" con valor 1.333 (índice del agua)
            "Vidrio": 1.5, # Clave "Vidrio" con valor 1.5 (índice típico del vidrio)
            "Diamante": 2.417, # Clave "Diamante" con valor 2.417 (índice del diamante)
            "Personalizado": 1.5 # Clave "Personalizado" con valor predeterminado 1.5 para índices personalizados
        } # Cierre del diccionario

        # Se personalizan los colores para cada medio (interfaz) # Comentario describiendo la lista de colores para las capas
        # Azul muy oscuro, Azul noche oscuro, Azul medianamente oscuro, Púrpura oscuro, Lila # Comentario detallando los colores
        self.colores_capas = ["#1a1a2e", "#16213e", "#0f3460", "#533483", "#94618e"] # Esta línea define self.colores_capas como una lista de códigos hexadecimales de colores para representar visualmente cada capa en el canvas

        # Variables de configuración inicial # Comentario indicando el inicio de variables de configuración
        self.numero_interfaces = tk.IntVar(value=1)  # Número de interfaces por defecto al iniciar la ejecución # Esta línea crea self.numero_interfaces como una variable entera de tkinter inicializada en 1, para rastrear el número de interfaces activas
        self.angulo_incidente = tk.DoubleVar(value=30.0)  # Inicializa el ángulo con respecto al eje X (horizontal) en 30° # Esta línea crea self.angulo_incidente como una variable flotante de tkinter inicializada en 30.0 grados

        # Lista de materiales seleccionados por el usuario # Comentario describiendo la lista de materiales seleccionados
        self.materiales_seleccionados = [tk.StringVar(value="Vacío")] # Se crea una lista que contiene una variable de texto de Tkinter y se inicializa en "Vacío" # Esta línea inicializa self.materiales_seleccionados como una lista con una StringVar de tkinter set en "Vacío" para la primera capa
        self.indices_personalizados = [tk.DoubleVar(value=1.0)] # Se crea una lista que contiene una variable decimal de Tkinter y se inicializa en 1.0 # Esta línea inicializa self.indices_personalizados como una lista con una DoubleVar set en 1.0 para índices personalizados

        # Inicializa los materiales por defecto para las 4 capas adicionales, respectivamente # Comentario explicando la inicialización de materiales predeterminados
        materiales_predeterminados = ["Aire", "Agua", "Vidrio", "Diamante"] # Esta línea define una lista local con materiales predeterminados para las capas adicionales
        for i in range(4): # Recorre la lista anterior con un ciclo for # Esta línea inicia un bucle for que itera 4 veces (i de 0 a 3)
            self.materiales_seleccionados.append(tk.StringVar(value=materiales_predeterminados[i])) # Agrega a la lista de materiales_seleccionados los materiales predeterminados # Esta línea agrega una nueva StringVar con el material predeterminado correspondiente a la lista self.materiales_seleccionados
            self.indices_personalizados.append(tk.DoubleVar(value=1.5)) # Agrega a la lista de indices_personalizados un índice personalizado de 1.5 por defecto # Esta línea agrega una nueva DoubleVar con valor 1.5 a self.indices_personalizados

        # Inicializar la interfaz gráfica # Comentario indicando la inicialización de la GUI
        self.crear_interfaz_usuario() # Llama a la funcion crear_interfaz_usuario() # Esta línea llama al método self.crear_interfaz_usuario() para construir los elementos de la interfaz
        self.actualizar_simulacion() # Llama a la funcion actualizar_simulacion() # Esta línea llama al método self.actualizar_simulacion() para dibujar la simulación inicial en el canvas

    def crear_interfaz_usuario(self): # Definición del método crear_interfaz_usuario, que no recibe parámetros adicionales además de self
        """Se crea el metodo para crear todos los controles de la interfaz del simulador.""" # Docstring describiendo el propósito del método: crear todos los controles de la interfaz

        # Crea un frame para usarlo como marco principal para almacenar dentro de el todos los elementos, # Comentario explicando la creación del frame principal
        # se coloca en la venta principal, y se hace tranparente para que no se note # Continuación del comentario
        marco_principal = ctk.CTkFrame(self.ventana_principal, fg_color="transparent") # Esta línea crea un CTkFrame (frame personalizado) en la ventana principal, con color de fondo transparente
        # Se indica que el frame se extiende a toda la ventana, y si la ventana crece, el frame también # Comentario explicando el packing del frame
        # además deja un margen de 15px alrededor del frame # Continuación
        marco_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=15) # Esta línea empaqueta el frame para que llene ambos ejes, se expanda con la ventana, y agregue padding de 15 píxeles

        # Se crea un frame para contener el título (header), dentro del frame anterior, con una altura de 60px, # Comentario describiendo la creación del header_frame
        # se redondean las esquinas con un radio de 12px # Continuación
        header_frame = ctk.CTkFrame(marco_principal, height=60, corner_radius=12, fg_color=("#2b5797", "#0f3460")) # Esta línea crea un CTkFrame para el header con altura fija, esquinas redondeadas y colores para modos claro/oscuro
        # El frame se muestra en el marco principal, se extiende por toda la horizontal del marco # Comentario explicando el packing
        # y se deja un espacio de 10px arriba y abajo de este # Continuación
        header_frame.pack(fill=tk.X, pady=(0, 10)) # Esta línea empaqueta el header_frame para que llene horizontalmente y agregue padding vertical

        titulo_label = ctk.CTkLabel( # Se crea un label para mostrar el titulo # Esta línea inicia la creación de un CTkLabel para el título
            header_frame, # Se almacena en el frame del header # Parámetro: parent widget es header_frame
            text="🧪 SIMULADOR DE LA LEY DE SNELL", # Se le agrega el texto al label # Parámetro: texto con emoji y título
            font=("Roboto", 22, "bold"), # Se especifican la fuente del texto (Roboto), el tamaño (22) y el grosor (bold o en negrita) # Parámetro: fuente como tupla
                text_color=("#ffffff", "#ffffff") # Se indica el color del label (blanco) # Parámetro: color de texto para modos claro/oscuro, ambos blanco
        ) # Cierre de la creación del label
        # Se muestra el label, se coloca a la izquierda del header_frame, se deja un espacio de 20px a la derecha y a la izquierda, # Comentario explicando el packing
        # y un espacio de 15px arriba y abajo # Continuación
        titulo_label.pack(side=tk.LEFT, padx=20, pady=15) # Esta línea empaqueta el label a la izquierda con padding

        # Se crea un boton para cambiar el tema de la interfaz # Comentario describiendo la creación del botón de tema
        self.boton_tema = ctk.CTkButton( # Esta línea inicia la creación de un CTkButton para cambiar el tema
            header_frame, # Se almacena en el header_frame (donde mismo que el label anterior) # Parámetro: parent es header_frame
            text="☀️ Modo Claro", # Se le agrega el texto al botón # Parámetro: texto inicial con emoji
            width=140, # Se le asigna un ancho de 140px # Parámetro: ancho fijo
            height=35, # Se le asigna una altura de 35px # Parámetro: altura fija
            corner_radius=8, # Se redondean las esquinas con un radio de 8px # Parámetro: radio de esquinas
            font=("Roboto", 12, "bold"), # Se especifican la fuente del texto (Roboto), el tamaño (12) y el grosor (bold o en negrita) # Parámetro: fuente
            fg_color=("#3a7ebf", "#1f538d"), # Se indica el color del botón # Parámetro: color de fondo para modos claro/oscuro
            hover_color=("#5a9edf", "#2a6bad"), # Se le agrega un efecto de color cuando el mouse está sobre él # Parámetro: color al hover
            command=self.cambiar_tema # Se le asiga en comando de cambiar el tema cuando se le da clic # Parámetro: función a llamar al clic
        ) # Cierre de la creación del botón
        # Se muestra el botón, se coloca a la derecha del header_frame, se deja un espacio de 20px a la derecha y a la izquierda, # Comentario explicando el packing
        # y un espacio de 12px arriba y abajo # Continuación
        self.boton_tema.pack(side=tk.RIGHT, padx=20, pady=12) # Esta línea empaqueta el botón a la derecha con padding

        # Se crea un frame contenedor para contener el panel de control, se almacena en el marco principal y se le da u color transparente # Comentario describiendo la creación del contenedor_inferior
        contenedor_inferior = ctk.CTkFrame(marco_principal, fg_color="transparent") # Esta línea crea un CTkFrame transparente en marco_principal
        # Se muestra en el marco principal, se extiende por todo el marco, y si el marco crece, el contenedor también # Comentario explicando el packing
        contenedor_inferior.pack(fill=tk.BOTH, expand=True) # Esta línea empaqueta el frame para que llene y se expanda

        # Se crea un frame con scroll para el panel de control # Comentario describiendo la creación del panel_control
        panel_control = ctk.CTkScrollableFrame( # Esta línea inicia la creación de un CTkScrollableFrame para scroll
            contenedor_inferior, # Se almacena en el frame anterior # Parámetro: parent es contenedor_inferior
            width=350, # Le establece un ancho de 350px # Parámetro: ancho fijo
            corner_radius=12, # Redondeo las esquinas con un radio de 12px # Parámetro: radio de esquinas
            fg_color=("#D1DBE6", "#16213e"), # Se establecen los colores del frame (azul grisáceo muy claro, y azul marino oscuro con tono violeta) # Parámetro: colores para modos
            border_width=2, # Se establece un borde de 2px alrededor el frame # Parámetro: ancho de borde
            border_color=("#3a7ebf", "#2b5797") # Se establecen los colores del borde (azul medio brillante y azul oscuro elegante) # Parámetro: colores de borde
        ) # Cierre de la creación
        # Se muestra el panel de control en el contenedor inferior, se coloca a la izquierda, se extiende verticalmente # Comentario explicando el packing
        # y se deja un espacio de 10px a la derecha # Continuación
        panel_control.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10), expand=False) # Esta línea empaqueta a la izquierda, llenando verticalmente, con padding

        # Se crea un label para agregar un título # Comentario describiendo el título del panel
        titulo_panel = ctk.CTkLabel( # Esta línea inicia la creación de un CTkLabel para el título del panel
            panel_control, # Se almacena en el frame con scroll anterior # Parámetro: parent
            text="💡 Panel de Control", # Se le agrega el texto al label # Parámetro: texto
            font=("Roboto", 18, "bold"), # Se especifican la fuente del texto (Roboto), el tamaño (18) y el grosor (bold o en negrita) # Parámetro: fuente
            text_color=("#1a1a2e", "#ffffff") # Se indica el color del botón # Parámetro: color de texto (nota: dice "botón" pero es label)
        ) # Cierre
        # Se muestra el label en el frame del panel de control, agregando un espacio de 15px arriba y abajo, # Comentario
        # y 10px a la derecha y a la izquierda # Continuación
        titulo_panel.pack(pady=15, padx=10) # Empaqueta con padding

        # Se crea un label para agregar un título # Comentario para el label de interfaces
        label_interfaces = ctk.CTkLabel( # Inicio creación
            panel_control,  # Se almacena en el frame con scroll anterior # Parent
            text="Número de Interfaces Activas:",  # Se le agrega el texto al label # Texto
            font=("Roboto", 13, "bold"), # Se especifican la fuente del texto (Roboto), el tamaño (13) y el grosor (bold o en negrita) # Fuente
            text_color=("#2c3e50", "#e0e0e0")# Se indica el color del botón # Color de texto
        ) # Cierre
        # Se muestra el label en el frame del panel de control, agregando un espacio de 10px arriba y 5px abajo, # Comentario
        # y 10px a la derecha y a la izquierda # Continuación
        label_interfaces.pack(pady=(10, 5), padx=10) # Empaqueta

        # Se crea un frame para almacenar los sliders para el ángulo y el número de interfaces # Comentario para marco_slider_interfaces
        # y se almacena en el frame del panel del control # Continuación
        marco_slider_interfaces = ctk.CTkFrame(panel_control, fg_color=("#D1DBE6", "#16213e")) # Crea frame con colores
        # Se muestra en el frame del panel del control, se deja un espacio de 15px a la derecha e izquierda, # Comentario
        # y deja un espacio de 5px arriba y abajo # Continuación
        marco_slider_interfaces.pack(fill=tk.X, padx=15, pady=5) # Empaqueta

        # Se crea un slider para seleccionar el número de interfaces # Comentario para slider_interfaces
        slider_interfaces = ctk.CTkSlider( # Inicio creación
            marco_slider_interfaces, # Se almacena en el frame para almacenar los sliders # Parent
            from_=1, # Indica el valor minimo del slider # Parámetro: valor inicial
            to=4, # Indica el valor maximo del slider # Parámetro: valor final
            number_of_steps=3, # Divide el rango en 3 pasos o partes # Parámetro: pasos
            variable=self.numero_interfaces, # Asocia el valor del slider con el del número de interfaces # Variable vinculada
            orientation="horizontal", # Indica la orientación del slider # Orientación
            command=self.al_cambiar_interfaces, # Ejecuta la función al mover el slider # Comando al cambio
            button_color=("#3a7ebf", "#2b5797"), # Indica el color del botón del deslizador # Color botón
            button_hover_color=("#5a9edf", "#3a7ebf"), # Indica el color del botón del slider cuando el mouse está sobre él # Hover botón
            progress_color=("#5a9edf", "#0f3460"), # Indica el color del slider lleno # Color progreso
            fg_color=("#b8c5d6", "#2c3e50"), # Indica el color del slider vacio # Color fondo
            width=200 # Define un ancho de 200px del botón # Ancho
        ) # Cierre
        # Se muestra el slider, se coloca a la izquierda, se expande por toda la horizontal del frame, # Comentario
        # si el frame se expande, el slider también, y se deja un espacio de 5px a la izquierda y 10px a la derecha # Continuación
        slider_interfaces.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10)) # Empaqueta

        self.etiqueta_interfaces = ctk.CTkLabel( # Crea label para mostrar el valor del slider de interfaces
            marco_slider_interfaces, # Parent
            text="1", # Texto inicial
            font=("Roboto", 14, "bold"), # Fuente
            width=40, # Ancho
            fg_color=("#3a7ebf", "#0f3460"), # Color fondo
            corner_radius=6, # Radio esquinas
            text_color=("#ffffff", "#ffffff") # Color texto
        ) # Cierre
        self.etiqueta_interfaces.pack(side=tk.LEFT, padx=5) # Empaqueta a la izquierda con padding

        separador1 = ctk.CTkFrame(panel_control, height=2, fg_color=("#a0aec0", "#34495e")) # Crea un frame como separador horizontal de 2px de alto con colores
        separador1.pack(fill=tk.X, pady=15, padx=15) # Empaqueta llenando horizontalmente con padding

        # Ángulo de incidencia # Comentario sección para ángulo
        label_angulo = ctk.CTkLabel( # Crea label para título del ángulo
            panel_control, # Parent
            text="📦 Ángulo de Incidencia", # Texto
            font=("Roboto", 13, "bold"), # Fuente
            text_color=("#2c3e50", "#e0e0e0") # Color
        ) # Cierre
        label_angulo.pack(pady=5, padx=10) # Empaqueta

        label_angulo_desc = ctk.CTkLabel( # Crea label para descripción del ángulo
            panel_control, # Parent
            text="(Medido desde el eje X horizontal, rayo incidente)", # Texto
            font=("Roboto", 9, "italic"), # Fuente
            text_color=("#5a6c7d", "#95a5a6") # Color
        ) # Cierre
        label_angulo_desc.pack(padx=10) # Empaqueta con padding horizontal

        marco_slider_angulo = ctk.CTkFrame(panel_control, fg_color=("#D1DBE6", "#16213e")) # Crea frame para el slider de ángulo con colores
        marco_slider_angulo.pack(fill=tk.X, padx=15, pady=5) # Empaqueta

        slider_angulo = ctk.CTkSlider( # Crea slider para ángulo
            marco_slider_angulo, # Parent
            from_=0, # Mínimo 0
            to=90, # Máximo 90
            variable=self.angulo_incidente, # Variable vinculada
            orientation="horizontal", # Orientación
            command=lambda x: self.actualizar_simulacion(), # Comando: lambda que llama a actualizar_simulacion al cambio, parámetro x es el valor actual (ignorado)
            button_color=("#3a7ebf", "#2b5797"), # Color botón
            button_hover_color=("#5a9edf", "#3a7ebf"), # Hover
            progress_color=("#5a9edf", "#0f3460"), # Progreso
            fg_color=("#b8c5d6", "#2c3e50"), # Fondo
            width=200 # Ancho
        ) # Cierre
        slider_angulo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10)) # Empaqueta

        self.etiqueta_angulo = ctk.CTkLabel( # Crea label para mostrar valor del ángulo
            marco_slider_angulo, # Parent
            text="30°", # Texto inicial
            font=("Roboto", 14, "bold"), # Fuente
            width=60, # Ancho
            fg_color=("#3a7ebf", "#0f3460"), # Fondo
            corner_radius=6, # Radio
            text_color=("#ffffff", "#ffffff") # Color
        ) # Cierre
        self.etiqueta_angulo.pack(side=tk.LEFT, padx=5) # Empaqueta

        self.info_angulo = ctk.CTkLabel( # Crea label para info adicional del ángulo (inicial vacío)
            panel_control, # Parent
            text="", # Texto inicial vacío
            font=("Roboto", 10), # Fuente
            text_color=("#5a6c7d", "#95a5a6") # Color
        ) # Cierre
        self.info_angulo.pack(pady=5, padx=10) # Empaqueta
        separador2 = ctk.CTkFrame(panel_control, height=2, fg_color=("#a0aec0", "#34495e")) # Crea segundo separador
        separador2.pack(fill=tk.X, pady=15, padx=15) # Empaqueta

        # ---------------- Selección de materiales y controles por capa ---------------- # # Comentario sección para selección de materiales
        label_materiales = ctk.CTkLabel( # Crea label para título de materiales
            panel_control, # Parent
            text="🔬 Materiales por Capa:", # Texto
            font=("Roboto", 14, "bold"), # Fuente
            text_color=("#2c3e50", "#e0e0e0") # Color
        ) # Cierre
        label_materiales.pack(pady=5, padx=10) # Empaqueta

        # Primera capa fija: Vacío (no editable) # Comentario para capa fija
        marco_capa0 = ctk.CTkFrame( # Crea frame para capa 1
            panel_control, # Parent
            corner_radius=10, # Radio
            fg_color=("#e8f0f7", "#1a2332"), # Colores
            border_width=2, # Borde
            border_color=("#3a7ebf", "#2b5797") # Color borde
        ) # Cierre
        marco_capa0.pack(fill=tk.X, padx=15, pady=8) # Empaqueta

        label_capa0_titulo = ctk.CTkLabel( # Label título capa 1
            marco_capa0, # Parent
            text="Capa 1 - Vacío (fijo)", # Texto
            font=("Roboto", 11, "bold"), # Fuente
            text_color=("#2c3e50", "#ffffff") # Color
        ) # Cierre
        label_capa0_titulo.pack(pady=(8, 2)) # Empaqueta

        label_capa0_material = ctk.CTkLabel( # Label material
            marco_capa0, # Parent
            text="Material: Vacío", # Texto
            font=("Roboto", 10), # Fuente
            text_color=("#34495e", "#bdc3c7") # Color
        ) # Cierre
        label_capa0_material.pack(pady=2) # Empaqueta

        label_capa0_indice = ctk.CTkLabel( # Label índice
            marco_capa0, # Parent
            text="n = 1.0000", # Texto
            font=("Roboto", 10, "italic"), # Fuente
            text_color=("#5a6c7d", "#95a5a6") # Color
        ) # Cierre
        label_capa0_indice.pack(pady=(2, 8)) # Empaqueta

        # Crear controles para las 4 capas seleccionables # Comentario para bucle de capas
        self.marcos_materiales = [] # Inicializa lista vacía para marcos de materiales
        for i in range(4): # Bucle for i de 0 a 3 para crear controles de 4 capas
            marco = ctk.CTkFrame( # Crea frame para cada capa
                panel_control, # Parent
                corner_radius=10, # Radio
                fg_color=("#e8f0f7", "#1a2332"), # Colores
                border_width=2, # Borde
                border_color=("#3a7ebf", "#2b5797") # Color borde
            ) # Cierre
            marco.pack(fill=tk.X, padx=15, pady=8) # Empaqueta

            # Título de la capa # Comentario
            label_titulo_capa = ctk.CTkLabel( # Crea label título
                marco, # Parent
                text=f"Capa {i + 2}", # Texto dinámico (Capa 2 a 5)
                font=("Roboto", 11, "bold"), # Fuente
                text_color=("#2c3e50", "#ffffff") # Color
            ) # Cierre
            label_titulo_capa.pack(pady=(8, 5)) # Empaqueta

            # Fila con menú de opciones para elegir material # Comentario para fila de combo
            fila_combo = ctk.CTkFrame(marco, fg_color=("#e8f0f7", "#1a2332")) # Crea frame para la fila del combo de materiales
            fila_combo.pack(fill=tk.X, padx=10, pady=5) # Empaqueta

            label_material = ctk.CTkLabel( # Crea label "Material:"
                fila_combo, # Parent
                text="Material:", # Texto
                font=("Roboto", 10), # Fuente
                text_color=("#34495e", "#bdc3c7") # Color
            ) # Cierre
            label_material.pack(side=tk.LEFT, padx=(0, 8)) # Empaqueta a la izquierda

            combo = ctk.CTkOptionMenu( # Crea menú desplegable (CTkOptionMenu) con materiales, vinculado a la variable correspondiente, y llama a actualizar_simulacion al cambiar
                fila_combo, # Parent
                variable=self.materiales_seleccionados[i + 1], # Variable vinculada
                values=list(self.materiales_disponibles.keys()), # Valores del menú desde las claves del diccionario
                width=180, # Ancho
                height=28, # Altura
                corner_radius=8, # Radio
                font=("Roboto", 10), # Fuente
                dropdown_font=("Roboto", 10), # Fuente del desplegable
                fg_color=("#3a7ebf", "#2b5797"), # Color fondo
                button_color=("#2b5797", "#1f538d"), # Color botón
                button_hover_color=("#3a7ebf", "#2b5797"), # Hover botón
                command=lambda x: self.actualizar_simulacion() # Comando al cambio
            ) # Cierre
            combo.pack(side=tk.LEFT, padx=5) # Empaqueta a la izquierda

            # Fila para índice personalizado # Comentario para fila personalizada
            fila_personalizado = ctk.CTkFrame(marco, fg_color=("#e8f0f7", "#1a2332")) # Crea frame para entrada de índice personalizado
            fila_personalizado.pack(fill=tk.X, padx=10, pady=(5, 8)) # Empaqueta

            label_personalizado = ctk.CTkLabel( # Crea label "n personalizado:"
                fila_personalizado, # Parent
                text="n personalizado:", # Texto
                font=("Roboto", 9), # Fuente
                text_color=("#5a6c7d", "#95a5a6") # Color
            ) # Cierre
            label_personalizado.pack(side=tk.LEFT, padx=(0, 8)) # Empaqueta

            spin_n = ctk.CTkEntry( # Crea entrada de texto para índice personalizado, vinculada a la variable correspondiente
                fila_personalizado, # Parent
                textvariable=self.indices_personalizados[i + 1], # Variable vinculada
                width=100, # Ancho
                height=28, # Altura
                corner_radius=6, # Radio
                font=("Roboto", 10), # Fuente
                fg_color=("#ffffff", "#2c3e50"), # Fondo
                border_color=("#3a7ebf", "#2b5797"), # Color borde
                border_width=2 # Ancho borde
            ) # Cierre
            spin_n.pack(side=tk.LEFT, padx=5) # Empaqueta
            spin_n.bind("<KeyRelease>", lambda e, idx=i + 1: self.cambiar_personalizado(idx)) # Bind evento KeyRelease a lambda que llama cambiar_personalizado con idx

            self.marcos_materiales.append(marco) # Agrega el marco de la capa actual a la lista self.marcos_materiales para poder referenciarlo más adelante si es necesario

        # ---------------- Canvas para dibujo ---------------- # # Comentario que marca la sección donde se crea el área de dibujo (canvas) para la simulación gráfica
        marco_canvas = ctk.CTkFrame( # Se crea un frame contenedor para el canvas, se almacena dentro del contenedor_inferior
            contenedor_inferior, # Se almacena en el frame contenedor_inferior que está al lado del panel de control
            corner_radius=12, # Se redondean las esquinas del frame con un radio de 12px para mantener el estilo moderno
            fg_color=("#f7f9fc", "#0d1117"), # Se establecen los colores de fondo del frame: claro (#f7f9fc) y oscuro (#0d1117)
            border_width=2, # Se establece un borde de 2px alrededor del frame
            border_color=("#3a7ebf", "#2b5797") # Se establecen los colores del borde para modos claro y oscuro
        ) # Cierre de la creación del frame
        marco_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) # Se muestra el frame en el contenedor_inferior, se coloca a la izquierda, se extiende en ambos direcciones y se expande si el contenedor crece

        self.canvas = tk.Canvas( # Se crea el canvas para dibujar la simulación gráfica
            marco_canvas, # Se almacena en el frame marco_canvas
            bg="#f0f0f0", # Se establece el color de fondo del canvas en gris claro
            highlightthickness=0 # Se quita el borde de resalte del canvas para que no se vea
        ) # Cierre de la creación del canvas
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=3, pady=3) # Se muestra el canvas, se extiende en ambos direcciones, se expande si el frame crece, y se deja un margen de 3px alrededor
        # Redibujar cuando la ventana cambie de tamaño # Comentario que explica el propósito del bind siguiente
        self.canvas.bind("<Configure>", lambda e: self.actualizar_simulacion()) # Se vincula el evento de cambio de tamaño del canvas a una lambda que llama a actualizar_simulacion, parámetro e es el evento (ignorado)

    def cambiar_tema(self): # Definición del método cambiar_tema, que no recibe parámetros adicionales además de self
        """ Se crea este método para alterna entre modo oscuro y claro""" # Docstring describiendo el propósito del método: alternar entre modos claro y oscuro
        modo_actual = ctk.get_appearance_mode() # Obtiene el modo de apariencia actual de customtkinter ("Dark" o "Light")
        if modo_actual == "Dark": # Verifica si el modo actual es oscuro
            ctk.set_appearance_mode("light") # Cambia el modo de apariencia a claro
            self.boton_tema.configure(text="🌙 Modo Oscuro") # Actualiza el texto del botón de tema para reflejar el cambio a modo oscuro
        else: # Caso contrario (modo claro)
            ctk.set_appearance_mode("dark") # Cambia el modo de apariencia a oscuro
            self.boton_tema.configure(text="☀️ Modo Claro") # Actualiza el texto del botón de tema para reflejar el cambio a modo claro

    # ---------------- Funciones auxiliares (lógica física) ---------------- # # Comentario que marca la sección de funciones auxiliares para la lógica física
    def al_cambiar_interfaces(self, valor): # Definición del método al_cambiar_interfaces, que recibe el parámetro valor (el valor actual del slider)
        """ Callback para el slider de número de interfaces. # Docstring describiendo el propósito: callback para el slider de interfaces
        Convertimos el valor a entero y forzamos la actualización.""" # Continuación del docstring
        valor_entero = int(float(valor)) # Convierte el valor (flotante) a entero para asegurarse de que sea un número entero
        self.numero_interfaces.set(valor_entero) # Actualiza la variable de tkinter self.numero_interfaces con el valor entero
        self.etiqueta_interfaces.configure(text=str(valor_entero)) # Actualiza el texto de la etiqueta self.etiqueta_interfaces para mostrar el nuevo valor
        self.actualizar_simulacion() # Llama al método actualizar_simulacion para redibujar la simulación con el nuevo número de interfaces

    def cambiar_personalizado(self, indice_capa): # Definición del método cambiar_personalizado, que recibe el parámetro indice_capa (el índice de la capa modificada)
        """ Se crea este método para el caso en que la capa está en modo 'Personalizado', # Docstring describiendo el propósito: actualizar si se modifica el índice personalizado
         actualizamos la simulación cuando el usuario modifica el spinbox del índice n.""" # Continuación del docstring
        if self.materiales_seleccionados[indice_capa].get() == "Personalizado": # Verifica si el material seleccionado para la capa es "Personalizado"
            self.actualizar_simulacion() # Llama al método actualizar_simulacion para redibujar con el nuevo índice personalizado

    def obtener_indice_refraccion(self, indice_capa): # Definición del método obtener_indice_refraccion, que recibe el parámetro indice_capa (el índice de la capa)
        """ Se crea este método para devolver el índice de refracción para la capa indicada. # Docstring describiendo el propósito: obtener el índice de refracción de una capa
        Si el material es 'Personalizado', devuelve el valor del spinbox asociado. # Continuación del docstring
        """
        material = self.materiales_seleccionados[indice_capa].get() # Obtiene el nombre del material seleccionado para la capa desde la variable de tkinter
        if material == "Personalizado": # Verifica si el material es "Personalizado"
            try: # Intenta ejecutar el bloque siguiente
                return float(self.indices_personalizados[indice_capa].get()) # Convierte y retorna el valor del índice personalizado desde la variable de tkinter
            except: # Captura cualquier excepción (como valor no numérico)
                return 1.5 # Retorna el valor por defecto 1.5 si hay error
        return self.materiales_disponibles[material] # Retorna el índice del diccionario de materiales disponibles para el material seleccionado

    def calcular_angulo_refraccion(self, angulo_horizontal_deg, n1, n2): # Definición del método calcular_angulo_refraccion, que recibe parámetros angulo_horizontal_deg (ángulo horizontal en grados), n1 (índice incidente), n2 (índice transmisor)
        """
        Se crea este método para calcular el ángulo refractado usando la Ley de Snell. # Docstring describiendo el propósito: calcular ángulo refractado con Ley de Snell
        Entrada: # Inicio de descripción de entrada
            angulo_horizontal_deg: ángulo medido respecto al eje X (horizontal) # Parámetro descrito
            n1: índice del medio incidente # Parámetro descrito
            n2: índice del medio transmisor # Parámetro descrito
        Salida: # Inicio de descripción de salida
            ángulo horizontal refractado (grados) o None si ocurre TIR (sin solución real) # Salida descrita
        Nota: # Nota adicional
            Internamente convertimos a ángulo respecto a la normal (vertical): # Explicación interna
                theta_normal = 90° - theta_horizontal # Fórmula de conversión
        """
        # Convertir a ángulo respecto a la normal (grados) # Comentario explicando la conversión
        theta_n1 = 90.0 - angulo_horizontal_deg # Calcula el ángulo respecto a la normal en grados
        # Convertir a radianes para trigonometría # Comentario explicando la conversión a radianes
        theta_n1_rad = math.radians(theta_n1) # Convierte el ángulo normal a radianes usando math.radians

        try: # Intenta ejecutar el bloque de cálculo
            # Ley de Snell: n1 * sin(theta_n1) = n2 * sin(theta_n2) # Comentario con la fórmula de Snell
            sin_theta2 = (n1 / n2) * math.sin(theta_n1_rad) # Calcula el seno del ángulo refractado usando math.sin
            # Si el valor absoluto excede 1 -> asin no tiene solución real -> TIR # Comentario explicando la condición de TIR
            if abs(sin_theta2) > 1.0: # Verifica si el seno excede 1 en valor absoluto
                return None # Retorna None indicando reflexión interna total (TIR)
            theta_n2_rad = math.asin(sin_theta2) # Calcula el ángulo refractado en radianes usando math.asin
            theta_n2_deg = math.degrees(theta_n2_rad) # Convierte el ángulo refractado a grados usando math.degrees
            # Convertir de nuevo a ángulo respecto a la horizontal # Comentario explicando la reconversión
            angulo_horizontal_refractado = 90.0 - theta_n2_deg # Calcula el ángulo horizontal refractado
            return angulo_horizontal_refractado # Retorna el ángulo refractado en grados
        except Exception: # Captura cualquier excepción durante el cálculo
            # En caso de error numérico, devolver None para indicar fallo # Comentario explicando el manejo de error
            return None # Retorna None en caso de error numérico

    # ---------------- Funciones de dibujo de rayos ---------------- # # Comentario que marca la sección de funciones para dibujar rayos en el canvas
    def dibujar_rayo_incidente(self, x0, y0, angulo_horizontal_deg, largo, color="#ff4444", grosor=4): # Definición del método dibujar_rayo_incidente, que recibe parámetros x0 y y0 (punto de impacto), angulo_horizontal_deg (ángulo), largo (longitud), color (por defecto rojo), grosor (por defecto 4)
        """
        Dibuja el rayo incidente que llega al punto (x0, y0). # Docstring describiendo el propósito: dibujar rayo incidente
        El rayo parte lejos a la izquierda y apunta al punto de impacto. # Continuación
        Fórmulas: # Inicio de fórmulas
            x_inicio = x0 - L * cos(theta) # Fórmula para x inicial
            y_inicio = y0 - L * sin(theta) # Fórmula para y inicial
        """
        theta_rad = math.radians(angulo_horizontal_deg) # Convierte el ángulo horizontal a radianes usando math.radians
        x_inicio = x0 - largo * math.cos(theta_rad) # Calcula la coordenada x inicial del rayo usando math.cos
        y_inicio = y0 - largo * math.sin(theta_rad) # Calcula la coordenada y inicial del rayo usando math.sin

        # Línea con flecha que termina en (x0, y0) # Comentario explicando la creación de la línea
        self.canvas.create_line(x_inicio, y_inicio, x0, y0, # Crea una línea en el canvas desde (x_inicio, y_inicio) hasta (x0, y0)
                                fill=color, width=grosor, # Parámetros: color de relleno y ancho de línea
                                arrow=tk.LAST, arrowshape=(12, 15, 6)) # Parámetros: flecha al final con forma especificada
        return (x_inicio, y_inicio) # Retorna la tupla con las coordenadas iniciales del rayo

    def dibujar_rayo_reflejado(self, x0, y0, angulo_horizontal_deg, largo, color="#ffaaaa", grosor=3): # Definición del método dibujar_rayo_reflejado, que recibe parámetros x0 y y0 (punto de impacto), angulo_horizontal_deg, largo, color (por defecto rosa claro), grosor (por defecto 3)
        """ Se crea el método para dibujar el rayo reflejado que sale del punto (x0, y0). # Docstring describiendo el propósito: dibujar rayo reflejado
        El rayo reflejado mantiene el mismo ángulo (simetría respecto a la normal). # Continuación
        Se dibuja hacia arriba-derecha desde el punto de impacto. """ # Continuación
        theta_rad = math.radians(angulo_horizontal_deg) # Convierte el ángulo a radianes usando math.radians
        x_fin = x0 + largo * math.cos(theta_rad) # Calcula la coordenada x final del rayo usando math.cos
        y_fin = y0 - largo * math.sin(theta_rad) # Calcula la coordenada y final del rayo (hacia arriba) usando math.sin

        # Línea punteada para indicar reflexión parcial # Comentario explicando la creación de la línea punteada
        self.canvas.create_line(x0, y0, x_fin, y_fin, # Crea una línea en el canvas desde (x0, y0) hasta (x_fin, y_fin)
                                fill=color, width=grosor, dash=(8, 4)) # Parámetros: color, ancho y patrón de dashes para punteado
        return (x_fin, y_fin) # Retorna la tupla con las coordenadas finales del rayo

    def dibujar_rayo_refractado(self, x0, y0, angulo_horizontal_deg, largo, color="#00ccff", grosor=4): # Definición del método dibujar_rayo_refractado, que recibe parámetros x0 y y0, angulo_horizontal_deg, largo, color (por defecto cian), grosor (por defecto 4)
        """ Se crea el método para dibujar el rayo refractado que sale del punto (x0, y0) hacia abajo/derecha # Docstring describiendo el propósito: dibujar rayo refractado
        según el ángulo horizontal refractado calculado. """ # Continuación
        theta_rad = math.radians(angulo_horizontal_deg) # Convierte el ángulo a radianes usando math.radians
        x_fin = x0 + largo * math.cos(theta_rad) # Calcula la coordenada x final usando math.cos
        y_fin = y0 + largo * math.sin(theta_rad) # Calcula la coordenada y final (hacia abajo) usando math.sin

        # Línea con flecha que indica el rayo transmitido a la siguiente capa # Comentario explicando la creación de la línea
        self.canvas.create_line(x0, y0, x_fin, y_fin, # Crea una línea desde (x0, y0) hasta (x_fin, y_fin)
                                fill=color, width=grosor, # Parámetros: color y ancho
                                arrow=tk.LAST, arrowshape=(12, 15, 6)) # Parámetros: flecha al final con forma
        return (x_fin, y_fin) # Retorna la tupla con las coordenadas finales

    # ---------------- Función principal: recalcular y dibujar ---------------- # # Comentario que marca la sección de la función principal de actualización
    def actualizar_simulacion(self): # Definición del método actualizar_simulacion, que no recibe parámetros adicionales
        """ Se crea la función central que borra el canvas y redibuja: # Docstring describiendo el propósito: borrar y redibujar la simulación
         - las capas (rectángulos horizontales), # Elemento redibujado
         - la posición del punto de impacto, # Elemento redibujado
         - los rayos incidente, refractados y reflejados, # Elemento redibujado
         - etiquetas de ángulos y leyenda. """ # Elemento redibujado
        # Limpiar canvas # Comentario explicando la limpieza
        self.canvas.delete("all") # Borra todos los elementos dibujados en el canvas

        ancho = self.canvas.winfo_width() # Obtiene el ancho actual del canvas usando winfo_width
        alto = self.canvas.winfo_height() # Obtiene el alto actual del canvas usando winfo_height
        if ancho < 2 or alto < 2: # Verifica si el canvas tiene un tamaño mínimo válido
            return  # canvas no inicializado aún # Retorna temprano si el canvas no está inicializado para evitar errores

        # Obtener ángulos actuales # Comentario explicando obtención de ángulos
        ang_h = self.angulo_incidente.get() # Obtiene el valor actual del ángulo incidente de la variable de tkinter
        ang_n = 90.0 - ang_h # Calcula el ángulo respecto a la normal restando de 90 grados
        self.etiqueta_angulo.configure(text=f"{ang_h:.1f}°") # Actualiza el texto de la etiqueta del ángulo horizontal con formato de 1 decimal
        self.info_angulo.configure(text=f"θ normal = {ang_n:.1f}°") # Actualiza el texto de la etiqueta del ángulo normal con formato

        # Número total de capas (incluye la capa inicial de vacío) # Comentario explicando cálculo de capas
        total_capas = self.numero_interfaces.get() + 1 # Obtiene el número de interfaces y suma 1 para incluir la capa inicial
        altura_capa = alto / total_capas # Calcula la altura de cada capa dividiendo el alto total por el número de capas

        # Punto de incidencia horizontal fijo (30% ancho del canvas) # Comentario explicando posición fija
        x_impacto = ancho * 0.3 # Calcula la posición x del punto de impacto como el 30% del ancho del canvas
        largo_base_rayo = min(ancho * 0.18, altura_capa * 0.75) # Calcula la longitud base del rayo tomando el mínimo entre el 18% del ancho y el 75% de la altura de capa

        # Dibujar cada capa como rectángulo horizontal y su recuadro informativo # Comentario explicando el bucle de dibujo de capas
        for i in range(total_capas): # Recorre cada capa desde 0 hasta total_capas - 1
            y_arriba = i * altura_capa # Calcula la coordenada y superior de la capa multiplicando i por altura_capa
            y_abajo = (i + 1) * altura_capa # Calcula la coordenada y inferior sumando una altura_capa

            color = self.colores_capas[i % len(self.colores_capas)] # Selecciona el color de la capa usando módulo para ciclar la lista de colores
            self.canvas.create_rectangle(0, y_arriba, ancho, y_abajo, # Dibuja un rectángulo en el canvas desde (0, y_arriba) hasta (ancho, y_abajo)
                                         fill=color, outline="white", width=3) # Parámetros: relleno con color, borde blanco de 3px

            # Información de la capa (material + índice n) # Comentario explicando dibujo de info
            material = self.materiales_seleccionados[i].get() # Obtiene el material seleccionado de la variable de tkinter
            n = self.obtener_indice_refraccion(i) # Llama al método para obtener el índice de refracción de la capa
            texto_info = f"Capa {i + 1}: {material}\nn = {n:.4f}" # Formatea el texto con el número de capa, material e índice con 4 decimales
            self.canvas.create_rectangle(10, y_arriba + 10, 150, y_arriba + 65, # Dibuja un rectángulo blanco para el info desde (10, y_arriba+10) hasta (150, y_arriba+65)
                                         fill="white", outline="black", width=2) # Parámetros: relleno blanco, borde negro de 2px
            self.canvas.create_text(80, y_arriba + 37, text=texto_info, # Dibuja el texto en el centro del rectángulo
                                    font=("Arial", 10, "bold"), justify=tk.CENTER) # Parámetros: fuente Arial 10 bold, justificación centrada

        # ---------------- Trazado de rayos a través de las interfaces ---------------- # # Comentario que marca la sección de trazado de rayos
        angulo_actual_h = ang_h  # empezamos con el ángulo incidente horizontal # Inicializa el ángulo actual con el incidente
        x_actual = x_impacto # Inicializa la posición x actual con la del impacto inicial

        for indice_interfaz in range(total_capas): # Recorre cada interfaz desde 0 hasta total_capas - 1
            # Coordenada vertical de la línea que separa la capa i de la siguiente # Comentario explicando cálculo de y
            y_linea_inferior = (indice_interfaz + 1) * altura_capa # Calcula la y de la interfaz inferior multiplicando por altura_capa

            if indice_interfaz == 0: # Verifica si es la primera interfaz
                # Primera interfaz: dibujar rayo incidente que llega al primer límite # Comentario
                self.dibujar_rayo_incidente(x_actual, y_linea_inferior, angulo_actual_h, largo_base_rayo) # Llama al método para dibujar el rayo incidente

                # Dibujar la normal (línea vertical punteada) alrededor del punto de impacto # Comentario
                self.canvas.create_line(x_actual, y_linea_inferior - 60, x_actual, y_linea_inferior + 60, # Dibuja línea vertical desde 60px arriba hasta 60px abajo
                                        fill="yellow", dash=(5, 3), width=2) # Parámetros: color amarillo, dashes para punteado, ancho 2px

                # Punto de impacto como un círculo amarillo # Comentario
                r = 6 # Define el radio del círculo como 6px
                self.canvas.create_oval(x_actual - r, y_linea_inferior - r, x_actual + r, y_linea_inferior + r, # Dibuja óvalo (círculo) alrededor del punto de impacto
                                        fill="yellow", outline="white", width=2) # Parámetros: relleno amarillo, borde blanco de 2px

                # Etiqueta con ángulos del rayo incidente (horizontal y normal) # Comentario
                self.canvas.create_text(x_actual - 100, y_linea_inferior - 30, # Dibuja texto 100px a la izquierda y 30px arriba del impacto
                                        text=f"Incidente\nθ={angulo_actual_h:.1f}° (horiz)\nθ={90 - angulo_actual_h:.1f}° (normal)", # Texto formateado con ángulos
                                        font=("Arial", 9, "bold"), fill="white", anchor="e") # Parámetros: fuente Arial 9 bold, color blanco, anclado al este

                # Dibujar rayo reflejado parcial hacia arriba # Comentario
                self.dibujar_rayo_reflejado(x_actual, y_linea_inferior, angulo_actual_h, largo_base_rayo * 0.6) # Llama al método para dibujar reflejo parcial con 60% de longitud

            # Si existe siguiente capa, calcular refracción entre capa actual y la siguiente # Comentario
            if indice_interfaz < total_capas - 1: # Verifica si hay una capa siguiente
                n1 = self.obtener_indice_refraccion(indice_interfaz) # Obtiene el índice de la capa actual llamando al método
                n2 = self.obtener_indice_refraccion(indice_interfaz + 1) # Obtiene el índice de la siguiente capa

                angulo_refractado_h = self.calcular_angulo_refraccion(angulo_actual_h, n1, n2) # Calcula el ángulo refractado llamando al método

                if angulo_refractado_h is None: # Verifica si hay reflexión interna total (None)
                    # REFLEXIÓN INTERNA TOTAL (TIR): dibujar reflejo fuerte y notificar # Comentario
                    self.dibujar_rayo_reflejado(x_actual, y_linea_inferior, angulo_actual_h, # Llama al método para dibujar reflejo fuerte
                                               largo_base_rayo, color="#ff8800", grosor=5) # Con color naranja y grosor 5

                    # Aviso visual de TIR # Comentario
                    self.canvas.create_rectangle(x_actual + 40, y_linea_inferior - 50, # Dibuja rectángulo naranja para aviso 40px a la derecha y 50px arriba
                                                 x_actual + 240, y_linea_inferior - 10, # Hasta 240px a la derecha y 10px arriba
                                                 fill="orange", outline="black", width=2) # Parámetros: relleno naranja, borde negro de 2px
                    self.canvas.create_text(x_actual + 140, y_linea_inferior - 30, # Dibuja texto centrado en el rectángulo
                                            text="⚠ REFLEXIÓN INTERNA TOTAL", # Texto de aviso con emoji
                                            font=("Arial", 10, "bold"), fill="black") # Parámetros: fuente Arial 10 bold, color negro
                    # Detener trazado ya que no hay transmisión # Comentario
                    break # Sale del bucle for para detener el trazado de rayos
                else: # Caso de refracción normal
                    # Hay refracción: dibujar rayo refractado en la siguiente capa # Comentario
                    largo_siguiente = min(largo_base_rayo, altura_capa * 0.7) # Calcula la longitud del rayo refractado limitada por el 70% de la altura de capa
                    x_fin, y_fin = self.dibujar_rayo_refractado(x_actual, y_linea_inferior, # Llama al método para dibujar el rayo refractado
                                                                angulo_refractado_h, largo_siguiente) # Con el ángulo calculado y longitud

                    # Dibujar normal y punto de impacto (decorativo) # Comentario
                    self.canvas.create_line(x_actual, y_linea_inferior - 60, x_actual, y_linea_inferior + 60, # Dibuja línea normal vertical punteada
                                            fill="yellow", dash=(5, 3), width=2) # Parámetros: amarillo, dashes, ancho 2
                    r = 6 # Define radio 6px
                    self.canvas.create_oval(x_actual - r, y_linea_inferior - r, x_actual + r, y_linea_inferior + r, # Dibuja círculo amarillo en impacto
                                            fill="yellow", outline="white", width=2) # Parámetros: relleno, borde

                    # Etiqueta con ángulos en la interfaz para el rayo refractado # Comentario
                    self.canvas.create_text(x_actual + 100, y_linea_inferior + 30, # Dibuja texto 100px a la derecha y 30px abajo
                                            text=f"Refractado\nθ={angulo_refractado_h:.1f}° (horiz)\nθ={90-angulo_refractado_h:.1f}° (normal)", # Texto formateado
                                            font=("Arial", 9, "bold"), fill="white", anchor="w") # Parámetros: fuente, color blanco, anclado al oeste

                    # Dibujar rayo reflejado parcial # Comentario
                    self.dibujar_rayo_reflejado(x_actual, y_linea_inferior, angulo_actual_h, largo_base_rayo * 0.5) # Llama al método para reflejo parcial con 50% longitud

                    # Actualizar variables para la siguiente interfaz: # Comentario
                    # el rayo transmitido se convierte en el incidente para la interfaz siguiente # Continuación
                    angulo_actual_h = angulo_refractado_h # Actualiza el ángulo actual al refractado para la siguiente iteración
                    x_actual = x_fin # Actualiza la posición x actual al final del rayo refractado

        # Dibujar leyenda explicativa en la esquina superior derecha # Comentario
        self.dibujar_leyenda(ancho, alto) # Llama al método dibujar_leyenda pasando ancho y alto del canvas

    # ---------------- Función para dibujar la leyenda ---------------- # # Comentario que marca la sección de la función para dibujar la leyenda
    def dibujar_leyenda(self, ancho_canvas, alto_canvas): # Definición del método dibujar_leyenda, que recibe parámetros ancho_canvas y alto_canvas (dimensiones del canvas)
        """ Este método dibuja un recuadro explicativo con el significado de colores y tipos de rayos. """ # Docstring describiendo el propósito: dibujar recuadro con leyenda de rayos
        x_leyenda = ancho_canvas - 220 # Calcula la posición x de la leyenda restando 220 del ancho para colocarla a la derecha
        y_leyenda = 20 # Establece la posición y fija en 20px desde arriba

        self.canvas.create_rectangle(x_leyenda - 15, y_leyenda - 10, # Dibuja rectángulo para la leyenda desde (x-15, y-10)
                                     x_leyenda + 205, y_leyenda + 150, # Hasta (x+205, y+150)
                                     fill="white", outline="black", width=2) # Parámetros: relleno blanco, borde negro de 2px
        self.canvas.create_text(x_leyenda + 95, y_leyenda + 5, text="📖 Leyenda", # Dibuja texto "Leyenda" centrado arriba
                                font=("Arial", 12, "bold"), anchor="n") # Parámetros: fuente Arial 12 bold, anclado al norte

        y_offset = y_leyenda + 30 # Inicializa el offset vertical para los elementos de la leyenda en y_leyenda + 30

        # Rayo incidente # Comentario para el rayo incidente en la leyenda
        self.canvas.create_line(x_leyenda, y_offset, x_leyenda + 50, y_offset, # Dibuja línea horizontal de 50px
                                fill="#ff4444", width=4, arrow=tk.LAST) # Parámetros: color rojo, ancho 4, flecha al final
        self.canvas.create_text(x_leyenda + 60, y_offset, text="Rayo Incidente", # Dibuja texto al lado de la línea
                                font=("Arial", 10), anchor="w") # Parámetros: fuente Arial 10, anclado al oeste

        y_offset += 30 # Incrementa el offset en 30px para el siguiente elemento

        # Rayo refractado # Comentario para el rayo refractado
        self.canvas.create_line(x_leyenda, y_offset, x_leyenda + 50, y_offset, # Dibuja línea horizontal
                                fill="#00ccff", width=4, arrow=tk.LAST) # Color cian, ancho 4, flecha
        self.canvas.create_text(x_leyenda + 60, y_offset, text="Rayo Refractado", # Texto al lado
                                font=("Arial", 10), anchor="w") # Fuente y anclaje

        y_offset += 30 # Incrementa offset

        # Rayo reflejado # Comentario para el rayo reflejado
        self.canvas.create_line(x_leyenda, y_offset, x_leyenda + 50, y_offset, # Dibuja línea horizontal
                                fill="#ffaaaa", width=3, dash=(8, 4)) # Color rosa, ancho 3, dashes para punteado
        self.canvas.create_text(x_leyenda + 60, y_offset, text="Rayo Reflejado", # Texto al lado
                                font=("Arial", 10), anchor="w") # Fuente y anclaje


# ---------------- Bloque principal (ejecución) ---------------- # # Comentario que marca el bloque principal de ejecución
if __name__ == "__main__": # Verifica si el archivo se está ejecutando directamente (no importado como módulo)
    ventana = ctk.CTk() # Crea la ventana principal usando ctk.CTk() como instancia de la ventana raíz
    app = SimuladorSnell(ventana) # Crea una instancia de SimuladorSnell pasando la ventana como parámetro, inicializando la app
    ventana.mainloop() # Inicia el bucle principal de eventos de tkinter para mantener la ventana abierta y responsive