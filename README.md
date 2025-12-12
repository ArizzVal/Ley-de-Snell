<div align="center">

# ⚡ Simulador Interactivo de Campo Eléctrico - Dipolo

💡 **Visualiza en tiempo real cómo dos cargas eléctricas generan un campo eléctrico dipolar.**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Compatible-Windows%20|%20macOS%20|%20Linux-green)
![Status](https://img.shields.io/badge/Estado-Activo-success)

---

</div>

## 📋 Datos Generales

**👤 Nombres del equipo:** Lopez Barrera Gustavo Aristoteles, Martinez Valenzuela Fernando, Vega Mendoza Aldo Salvador, Caracosa Birrueta Silver Naim.  
**📚 Grupo:** Equipo Fisica
**🏫 Institución:** INSTITUTO TECNOLOGICO SUPERIOR DE APATZINGAN  
**📅 Fecha:** Diciembre 2025  
**📖 Materia:** Física - Electrostática - Unidad 5 

**🎯 Título del proyecto:** *Modelado del Campo Eléctrico de un Dipolo con Python - Simulador Interactivo*

---

## 🌟 ¿Qué es un Campo Eléctrico?

El campo eléctrico es una región del espacio donde una carga eléctrica experimenta una fuerza.  
Para una carga puntual, se describe mediante la **Ley de Coulomb**:

$$ \vec{E} = k \frac{q}{r^2} \hat{r} $$

Donde:
- **k** = Constante de Coulomb (8.99 × 10⁹ N·m²/C²)
- **q** = Magnitud de la carga
- **r** = Distancia desde la carga

---

## 🧠 Descripción del Proyecto

Este proyecto es un **simulador gráfico interactivo** del campo eléctrico producido por un **dipolo eléctrico**, desarrollado en **Python**. Permite visualizar cómo dos cargas de igual magnitud pero signo opuesto generan patrones característicos de campo eléctrico.

⚡ **Características principales:**
- Visualización en **tiempo real** del campo eléctrico
- Control de **posición** de ambas cargas mediante sliders interactivos
- **Mapa de colores** que representa la intensidad del campo
- **Vectores direccionales** que muestran la dirección del campo
- Interfaz **moderna** con modo **claro/oscuro**
- Cálculo dinámico de la **separación** entre cargas
- Información física **educativa** integrada

El código principal se encuentra en el archivo **`dipolo_interactivo.py`**.

---

## 🔬 Descripción Física del Modelo Elegido

### Distribución de Carga Utilizada

Se eligió modelar un **dipolo eléctrico**, que consiste en:

- **🔴 Carga positiva:** +q = +1.00 C
- **🔵 Carga negativa:** -q = -1.00 C

Las cargas están separadas por una distancia variable controlable mediante la interfaz.

### Justificación de la Elección

El dipolo eléctrico es fundamental en electrostática por:

1. **📱 Relevancia Natural:** Muchas moléculas (como H₂O) son dipolos permanentes
2. **🔬 Aplicaciones:** Antenas, análisis molecular, materiales dieléctricos
3. **📊 Complejidad Intermedia:** Paso natural después de cargas puntuales individuales
4. **🎨 Simetría Única:** Exhibe patrones simétricos fascinantes
5. **➕ Superposición:** Demuestra claramente la suma vectorial de campos

---

## 📐 Modelo Matemático

### Campo Eléctrico para una Carga Puntual

En componentes cartesianas (x, y):

$$E_x = k \cdot q \cdot \frac{x - x_0}{[(x - x_0)^2 + (y - y_0)^2]^{3/2}}$$

$$E_y = k \cdot q \cdot \frac{y - y_0}{[(x - x_0)^2 + (y - y_0)^2]^{3/2}}$$

### Principio de Superposición

Para el **dipolo**, el campo total en cualquier punto es:

$$\vec{E}_{total} = \vec{E}_{+q} + \vec{E}_{-q}$$

**Proceso:**
1. Se calcula el campo de la carga positiva en cada punto
2. Se calcula el campo de la carga negativa en cada punto
3. Se suman vectorialmente ambas contribuciones
4. Se obtiene la magnitud: $|\vec{E}| = \sqrt{E_x^2 + E_y^2}$

---

## 💻 Descripción del Código

### Estructura del Programa

```
📁 Proyecto
├── 📄 dipolo_interactivo.py    # Código principal
├── 📄 README.md                 # Este archivo
├── 📸 figura1_dipolo_horizontal.png
└── 📸 figura2_dipolo_vertical.png
```

### Componentes Principales

#### 1️⃣ **Definición de Cargas**
```python
self.q = 1.0  # Magnitud de la carga
cargas = [
    (self.q, x1_val, y1_val),   # Carga positiva
    (-self.q, x2_val, y2_val)   # Carga negativa
]
```

#### 2️⃣ **Generación de Malla**
```python
self.rango = 5        # De -5 a +5 metros
self.resolucion = 20  # 20×20 = 400 puntos
x = np.linspace(-self.rango, self.rango, self.resolucion)
y = np.linspace(-self.rango, self.rango, self.resolucion)
self.X, self.Y = np.meshgrid(x, y)
```

#### 3️⃣ **Cálculo del Campo**
```python
def campo_electrico(self, x, y, cargas):
    Ex = np.zeros_like(x)
    Ey = np.zeros_like(y)
    
    for q_i, x_i, y_i in cargas:
        dx = x - x_i
        dy = y - y_i
        r_cuadrado = dx**2 + dy**2 + 1e-10
        r = np.sqrt(r_cuadrado)
        
        Ex += self.k * q_i * dx / (r_cuadrado * r)
        Ey += self.k * q_i * dy / (r_cuadrado * r)
    
    return Ex, Ey
```

#### 4️⃣ **Visualización**
- **Mapa de colores:** Representa la magnitud del campo
- **Flechas vectoriales:** Muestran dirección y sentido
- **Actualización en tiempo real:** Cada movimiento del slider recalcula todo

---

## ⚙️ Requisitos Previos

🖥️ **Sistema Operativo:** Windows, macOS o Linux  
🐍 **Python:** Versión 3.8 o superior  
📥 Puedes descargar Python desde aquí:  
[![Descargar Python](https://img.shields.io/badge/Python.org-Descargar-blue?logo=python)](https://python.org)

---

## 📦 Dependencias

El simulador requiere las siguientes bibliotecas:

| Librería | Descripción | Instalación |
|-----------|-------------|--------------|
| **tkinter** | Biblioteca estándar para interfaces gráficas | Incluida por defecto |
| **customtkinter** | Widgets modernos con temas claro/oscuro | `pip install customtkinter` |
| **numpy** | Cálculos numéricos y arrays | `pip install numpy` |
| **matplotlib** | Visualización científica | `pip install matplotlib` |

💡 *Se recomienda usar un entorno virtual para evitar conflictos.*

---

## 🚀 Instalación

1. **Clona o descarga** el repositorio:  
   ```bash
   git clone https://github.com/[tu-usuario]/simulador-campo-electrico.git
   ```

2. **Entra al directorio** del proyecto:
    ```bash
   cd simulador-campo-electrico
   ```

3. **Instala las dependencias** necesarias:
   ```bash
   pip install customtkinter numpy matplotlib
   ```

---

## ▶️ Cómo Ejecutar

Ejecuta el simulador con:

```bash
python dipolo_interactivo.py
```

### 🎮 Controles

- **🔴 Sliders X₁, Y₁:** Controlan la posición de la carga positiva
- **🔵 Sliders X₂, Y₂:** Controlan la posición de la carga negativa
- **🌓 Botón de tema:** Alterna entre modo claro y oscuro
- **📊 Panel de información:** Muestra separación y propiedades en tiempo real

---

## 📸 Resultados y Gráficas

### Figura 1: Dipolo en Configuración Horizontal

![Dipolo Horizontal](figura1_dipolo_horizontal.png)

**Configuración:**
- Carga positiva: (-1.0, 0.0)
- Carga negativa: (+1.0, 0.0)
- Separación: 2.0 metros

**🔍 Observaciones:**

1. **Simetría Bilateral:** Perfecta simetría respecto al eje Y vertical

2. **Intensidad del Campo:**
   - **Colores brillantes (amarillo/verde):** Campo intenso cerca de las cargas
   - **Colores oscuros (azul/morado):** Campo débil en regiones lejanas
   - La intensidad disminuye según 1/r²

3. **Dirección de las Líneas:**
   - Las flechas **emergen** de la carga positiva (🔴)
   - Las flechas **convergen** hacia la carga negativa (🔵)
   - En la zona central, el campo apunta horizontalmente de + hacia -

4. **Campo Intenso:** Entre las cargas existe una zona de campo muy intenso debido a la superposición

5. **Comportamiento Asintótico:** A grandes distancias, el campo se debilita y las líneas se vuelven paralelas

---

### Figura 2: Dipolo en Configuración Vertical

![Dipolo Vertical](figura2_dipolo_vertical.png)

**Configuración:**
- Carga positiva: (0.0, -1.5)
- Carga negativa: (0.0, +1.5)
- Separación: 3.0 metros

**🔍 Observaciones:**

1. **Rotación de Simetría:** El patrón se rotó 90°. Ahora la simetría es respecto al eje X

2. **Mayor Separación:**
   - Campo central más "alargado" verticalmente
   - Transición más gradual entre influencias

3. **Invariancia:** La magnitud del campo en puntos equidistantes es idéntica, solo cambió la orientación

4. **Patrón Vectorial:** Las flechas apuntan verticalmente en la región central

---

### 📊 Comparación Entre Configuraciones

| Aspecto | Horizontal (2.0m) | Vertical (3.0m) |
|---------|-------------------|-----------------|
| **Simetría** | Respecto eje Y | Respecto eje X |
| **Separación** | 2.0 metros | 3.0 metros |
| **Campo central** | Compacto | Alargado |
| **Orientación** | Horizontal | Vertical |
| **Intensidad máxima** | Igual | Igual |

---

## 🎓 Conclusiones

### 📚 Aprendizajes Obtenidos

1. **✅ Principio de Superposición en Acción**
   - El campo total es la suma vectorial correcta de los campos individuales
   - Se observó claramente cómo ambas cargas contribuyen al patrón resultante

2. **📉 Comportamiento del Campo Eléctrico**
   - Disminuye con 1/r² (visible en el degradado de colores)
   - Las líneas van de + a - sin cruzarse
   - La densidad de líneas indica intensidad

3. **🖼️ Importancia de la Visualización**
   - Los gráficos permiten entender conceptos abstractos intuitivamente
   - La combinación de colores + vectores da información completa

4. **💻 Programación Científica**
   - NumPy para cálculos vectoriales eficientes
   - Matplotlib para visualización científica
   - CustomTkinter para interfaces modernas

---

### ✅ Validación Teórica

**¿El comportamiento coincidió con lo esperado?**

**SÍ, completamente.**

✅ **Dirección:** Líneas de + a - según teoría  
✅ **Intensidad:** Decae con 1/r² (Ley de Coulomb)  
✅ **Simetría:** Dipolo con simetría bilateral  
✅ **Superposición:** Suma vectorial correcta  
✅ **Continuidad:** Sin discontinuidades ni cruces  

---

### 🎮 Comportamiento del Dipolo Móvil (Puntos Extra)

Gracias a los **sliders interactivos**, observamos en tiempo real:

#### **🔍 Al acercar las cargas (separación menor):**
- ✅ Campo central más intenso y compacto
- ✅ Líneas más "apretadas" entre cargas
- ✅ A grandes distancias, comportamiento casi puntual
- ✅ Patrón concentrado en el centro

#### **🔍 Al alejar las cargas (separación mayor):**
- ✅ Campo central "estirado" y menos intenso
- ✅ Zonas de influencia mejor distinguidas
- ✅ Transición más amplia y gradual
- ✅ Patrón dipolar más evidente

#### **🔄 Al rotar el dipolo (cambiar orientación):**
- ✅ Todo el patrón rota con las cargas
- ✅ Simetría se mantiene pero cambia de eje
- ✅ Propiedades invariantes bajo rotación
- ✅ La orientación determina la dirección del campo

#### **🎯 Al mover cargas independientemente:**
- ✅ Se pueden crear configuraciones asimétricas
- ✅ El código sigue funcionando correctamente
- ✅ Demuestra flexibilidad basada en superposición

---

### 💡 Reflexión Final

Este proyecto combinó exitosamente:
- **⚛️ Física teórica** (Ley de Coulomb, superposición)
- **📐 Matemáticas** (cálculo vectorial)
- **💻 Programación** (Python, NumPy)
- **🎨 Diseño** (interfaz interactiva)

El resultado fue un **simulador educativo** que no solo calcula correctamente, sino que permite **explorar interactivamente** cómo las cargas afectan el campo, facilitando una comprensión profunda de la electrostática.

Ver en **tiempo real** cómo responde el campo a los cambios reforzó significativamente nuestra comprensión intuitiva de estos fenómenos físicos fundamentales.

---

## 🧰 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Lenguaje principal |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) | Cálculos numéricos |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge) | Visualización científica |
| ![Tkinter](https://img.shields.io/badge/Tkinter-2c3e50?style=for-the-badge) | Interfaz gráfica |

---

## 📚 Referencias

1. Serway, R. A., & Jewett, J. W. (2018). *Physics for Scientists and Engineers*. Cengage Learning.
2. Griffiths, D. J. (2017). *Introduction to Electrodynamics*. Cambridge University Press.
3. Halliday, D., Resnick, R., & Walker, J. (2013). *Fundamentals of Physics*. Wiley.
4. Documentación de NumPy: https://numpy.org/doc/
5. Documentación de Matplotlib: https://matplotlib.org/
6. Documentación de CustomTkinter: https://github.com/TomSchimansky/CustomTkinter

---

## 🙌 Hecho por:

<table align="center">
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/0" width="110" height="110" style="border-radius:50%; border: 3px solid #4CAF50;">
      <br>
      <strong>[Tu nombre]</strong>
      <br>
      Desarrollador principal
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/0" width="110" height="110" style="border-radius:50%; border: 3px solid #2196F3;">
      <br>
      <strong>[Tu profesor]</strong>
      <br>
      Asesor del proyecto
    </td>
  </tr>
</table>

---

## 🪪 Licencia

Este proyecto fue desarrollado con fines educativos para la materia de **Electrostática**.  
Universidad: ITSA - Diciembre 2025

---

<div align="center">

**⚡ Hecho con pasión por la física y la programación ⚡**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Fercho36)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ArizzVal)

</div>
