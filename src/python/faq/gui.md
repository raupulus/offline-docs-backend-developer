---
title: Preguntas frecuentes sobre la Interfaz Gráfica de Usuario (*GUI*)
source_url: https://docs.python.org/es/3
source_path: faq/gui.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: faq
order: 1070
---

# Preguntas frecuentes sobre la Interfaz Gráfica de Usuario (*GUI*)

## Preguntas generales de la GUI

## ¿Qué conjuntos de herramientas de GUI existen para Python?

Los empaquetados estándar de Python incluyen una interfaz orientada a
objetos para el conjunto de widgets de Tcl/Tk, llamada tkinter. Esta
es probablemente la más fácil de instalar (ya que viene incluida con
la mayoría de distribuciones binarias de Python) y usar. Para obtener
más información sobre Tk, incluyendo referencias a la fuente, ver la
Página de inicio Tcl/Tk. Tcl/Tk es totalmente portable a macOS,
Windows y plataformas Unix.

Dependiendo de a que plataforma(s) estés apuntando, hay también
múltiples alternativas. Una lista de conjuntos de herramientas
multiplataforma y de plataforma específica puede ser encontrada en la
wiki de Python.

## Preguntas de Tkinter

### ¿Cómo congelo las aplicaciones de Tkinter?

Freeze es una herramienta para crear aplicaciones independientes. Al
congelar aplicaciones Tkinter, las aplicaciones no serán realmente
independientes, ya que la aplicación seguirá necesitando las
bibliotecas Tcl y Tk.

Una solución es enviar la aplicación con las bibliotecas Tcl y Tk, y
apuntarlas en tiempo de ejecución utilizando las variables de entorno
"TCL_LIBRARY" y "TK_LIBRARY".

Varias bibliotecas de terceros para congelar como py2exe y cx_Freeze
tienen soporte integrado para aplicaciones Tkinter.

### ¿Puedo tener eventos Tk manejados mientras espero por *I/O*?

En plataformas que no sean Windows, sí, ¡y ni siquiera necesitas
hilos! Pero tendrá que reestructurar un poco su código de
entrada/salida. Tk tiene un equivalente de la llamada "XtAddInput()"
de Xt, que permite registrar una función de retorno que será llamada
desde el bucle principal de Tk cuando sea posible entrada/salida en un
descriptor de archivo. Ver File handlers.

### No puedo hacer que los atajos de teclado funcionen en Tkinter: ¿por qué?

Una queja frecuente que se escucha es que los controladores de eventos
vinculados con el método "bind()" no se ejecutan incluso cuando se
presiona la tecla correspondiente.

La causa más común es que el widget al que se aplica el atajo no tiene
enfoque de teclado. Consulte la documentación de Tk para el comando de
*focus*. Por lo general, un *widget* recibe el foco del teclado
haciendo clic en él (pero no para las etiquetas; consulte la opción
*takefocus*).
