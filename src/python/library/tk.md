---
title: Graphical user interfaces with Tk
source_url: https://docs.python.org/es/3
source_path: library/tk.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4170
---

# Graphical user interfaces with Tk

Tk/Tcl has long been an integral part of Python.  It provides a robust
and platform independent windowing toolkit, that is available to
Python programmers using the "tkinter" package, and its extension, the
"tkinter.ttk" module.

El paquete "tkinter" es una fina capa orientada a objetos encima de
Tcl/Tk. Para usar "tkinter", no necesita escribir código Tcl, pero
deberá consultar la documentación de Tk y, ocasionalmente, la
documentación de Tcl. "tkinter" es un conjunto de envoltorios que
implementan los widgets Tk como clases de Python.

Las principales virtudes de "tkinter" son que es rápido y que
generalmente viene incluido con Python. Aunque su documentación
estándar es débil, se dispone de buen material, que incluye:
referencias, tutoriales, un libro y otros. "tkinter" también es famoso
por tener un aspecto y una sensación obsoletos, que se ha mejorado
enormemente en Tk 8.5. Sin embargo, hay muchas otras bibliotecas GUI
en las que podría estar interesado. La wiki de Python enumera varias
GUI frameworks and tools alternativas.

* "tkinter" --- Python interface to Tcl/Tk

  * Arquitectura

  * Tkinter modules

  * Tkinter life preserver

    * A Hello World program

    * Important Tk concepts

    * Understanding how Tkinter wraps Tcl/Tk

    * ¿Cómo lo hago?, ¿Cómo funciona?

    * Navigating the Tcl/Tk reference manual

  * Modelo de subprocesamiento

  * Handy reference

    * Setting options

    * Geometry management

    * Coupling widget variables

    * The window manager

    * Tk option data types

    * Bindings and events

    * The index parameter

    * Imágenes

  * Reference

    * Base and mixin classes

    * Toplevel widgets

    * Widget classes

    * Variable classes

    * Image classes

    * Other classes

    * Module-level functions

    * File handlers

    * Constants

* "tkinter.colorchooser" --- Color choosing dialog

* "tkinter.font" --- Tkinter font wrapper

* Tkinter dialogs

  * "tkinter.simpledialog" --- Standard Tkinter input dialogs

  * "tkinter.filedialog" --- File selection dialogs

    * Native load/save dialogs

  * "tkinter.commondialog" --- Dialog window templates

  * "tkinter.dialog" --- Classic Tk dialog boxes

* "tkinter.messagebox" --- Tkinter message prompts

* "tkinter.scrolledtext" --- Scrolled text widget

* "tkinter.dnd" --- Drag and drop support

* "tkinter.ttk" --- Tk themed widgets

  * Uso de Ttk

  * Ttk widgets

  * Widget

    * Standard options

    * Scrollable widget options

    * Label options

    * Compatibility options

    * Widget states

    * ttk.Widget

  * Combobox

    * Opciones

    * Eventos virtuales

    * ttk.Combobox

  * Spinbox

    * Opciones

    * Eventos virtuales

    * ttk.Spinbox

  * Notebook

    * Opciones

    * Tab options

    * Tab identifiers

    * Eventos virtuales

    * ttk.Notebook

  * Progressbar

    * Opciones

    * ttk.Progressbar

  * Separator

    * Opciones

  * Sizegrip

    * Notas específicas por plataforma

    * Errores detectados

  * Treeview

    * Opciones

    * Item options

    * Tag options

    * Column identifiers

    * Eventos virtuales

    * ttk.Treeview

  * Ttk styling

    * Diseños

  * Additional widgets

* IDLE --- Python editor and shell

  * Menús

    * Menú de archivo (Shell y Editor)

    * Menú editar (Shell y Editor)

    * Menú de formato (solo ventana del Editor)

    * Menú ejecutar (solo ventana Editor)

    * Menú de shell (solo ventana de shell)

    * Menú de depuración (solo ventana de shell)

    * Menú de opciones (Shell y editor)

    * Menú de ventana (shell y editor)

    * Menú de ayuda (shell y editor)

    * Menús contextuales

  * Edición y navegación

    * Ventana del editor

    * Atajos de teclado

    * Indentación automática

    * Buscar y reemplazar

    * Terminaciones

    * Sugerencias de llamada

    * Format block

    * Contexto del código

    * Ventana de Shell

    * Colores del texto

  * Inicio y ejecución de código

    * Command-line usage

    * Error de inicio

    * Ejecutando código del usuario

    * Salida del usuario en consola

    * Desarrollando aplicaciones tkinter

    * Ejecutando sin un subproceso

  * Ayuda y preferencias

    * Recursos de ayuda

    * Preferencias de configuración

    * IDLE en macOS

    * Extensiones

  * idlelib --- implementation of IDLE application

* "turtle" --- Turtle graphics

  * Introducción

  * Empezar

  * Tutorial

    * Iniciando un entorno para tortugas

    * Dibujo básico

      * Control del lápiz

      * La posición de la tortuga

    * Creando patrones algorítmicos

  * Cómo...

    * Empiece lo antes posible

    * Automatically begin and end filling

    * Utilice el espacio de nombres del módulo "turtle"

    * Utilice gráficos de tortugas en un guión

    * Utilice gráficos de tortuga orientados a objetos

  * Referencia gráficos de tortugas

    * Métodos Turtle

    * Métodos de TurtleScreen/Screen

  * Métodos de *RawTurtle/Turtle* Y sus correspondientes funciones

    * Movimiento de Turtle

    * Mostrar el estado de la tortuga

    * Configuración de las medidas

    * Control del lápiz

      * Estado de dibujo

      * Control del color

      * Relleno

      * Más controles de dibujo

    * Estado de la Tortuga

      * Visibilidad

      * Apariencia

    * Usando eventos

    * Métodos especiales de *Turtle*

    * Formas compuestas

  * Métodos de *TurtleScreen/Screen* y sus correspondientes funciones

    * Control de ventana

    * Control de animación

    * Usando eventos de pantalla

    * Métodos de entrada

    * Configuración y métodos especiales

    * Métodos específicos de *Screen*, no heredados de *TurtleScreen*

  * Clases públicas

  * Explicación

  * Ayuda y configuración

    * Cómo usar la ayuda

    * Traducción de cadenas de documentos a diferentes idiomas

    * Cómo configurar Screen and Turtles

  * "turtledemo" --- Demo scripts

  * Cambios desde Python 2.6

  * Cambios desde Python 3.0
