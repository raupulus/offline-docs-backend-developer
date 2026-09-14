---
title: '"tkinter.ttk" --- Tk themed widgets'
source_url: https://docs.python.org/es/3
source_path: library/tkinter.ttk.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4230
---

# "tkinter.ttk" --- Tk themed widgets

**Código fuente:** Lib/tkinter/ttk.py

======================================================================

The "tkinter.ttk" module provides access to the Tk themed widget set,
introduced in Tk 8.5. Its widgets adapt their appearance to the
platform's native theme, giving an application a better and more
consistent look and feel than the classic "tkinter" widgets, whose
appearance is fixed.

The basic idea for "tkinter.ttk" is to separate, to the extent
possible, the code implementing a widget's behavior from the code
implementing its appearance.

Ttk widgets are used just like the classic "tkinter" widgets and share
the same machinery: the widget hierarchy, the geometry managers,
variable coupling and event binding. Those foundational concepts are
covered in the "tkinter" documentation and are not repeated here.

Added in version 3.1.

Ver también:

  Tk Widget Styling Support (TIP #48)
     The Tcl Improvement Proposal that introduced the themed widget
     styling engine.

## Uso de Ttk

Para empezar a utilizar Ttk, hay que importar su módulo:

   from tkinter import ttk

Para anular los widgets Tk básicos, la importación debe seguir la
importación de Tk:

   from tkinter import *
   from tkinter.ttk import *

That code causes several "tkinter.ttk" widgets ("Button",
"Checkbutton", "Entry", "Frame", "Label", "LabelFrame", "Menubutton",
"OptionMenu", "PanedWindow", "Radiobutton", "Scale", "Scrollbar" and
"Spinbox") to automatically replace the Tk widgets.

Nota:

  Overriding the classic widgets with "from tkinter.ttk import *" is
  convenient for adapting existing code, but new code is usually
  clearer if it imports the module as "from tkinter import ttk" and
  refers to the themed widgets explicitly, such as "ttk.Button".

This has the direct benefit of using the new widgets which gives a
better look and feel across platforms; however, the replacement
widgets are not completely compatible. The main difference is that
widget options such as "fg", "bg" and others related to widget styling
are no longer present in Ttk widgets. Instead, use the "ttk.Style"
class for improved styling effects.

## Ttk widgets

Ttk comes with 18 widgets, twelve of which already existed in tkinter:
"Button", "Checkbutton", "Entry", "Frame", "Label", "LabelFrame",
"Menubutton", "PanedWindow", "Radiobutton", "Scale", "Scrollbar", and
"Spinbox". The other six are new: "Combobox", "Notebook",
"Progressbar", "Separator", "Sizegrip" and "Treeview". All of them are
subclasses of "Widget".

El uso de los widgets Ttk le da a la aplicación un aspecto mejorado.
Como se ha mencionado anteriormente, hay diferencias en cómo se
codifica el estilo.

Código Tk:

   l1 = tkinter.Label(text="Test", fg="black", bg="white")
   l2 = tkinter.Label(text="Test", fg="black", bg="white")

Código Ttk:

   style = ttk.Style()
   style.configure("BW.TLabel", foreground="black", background="white")

   l1 = ttk.Label(text="Test", style="BW.TLabel")
   l2 = ttk.Label(text="Test", style="BW.TLabel")

Para obtener más información acerca de TtkStyling, consulta la
documentación de la clase "Style".

## Widget

"ttk.Widget" defines standard options and methods supported by Tk
themed widgets and is not supposed to be directly instantiated.

### Standard options

All the "ttk" Widgets accept the following options:

+-------------+----------------------------------------------------------------+
| Opción      | Descripción                                                    |
|=============|================================================================|
| class       | Especifica la clase de ventana. La clase se usa cuando se      |
|             | consulta la base de datos de opciones para las otras opciones  |
|             | de la ventana, para determinar las etiquetas de enlace         |
|             | (*bindtags*) predeterminadas para la ventana y para            |
|             | seleccionar el diseño y estilo predeterminados del widget.     |
|             | Esta opción es de solo lectura y solo se puede especificar     |
## |             | cuando se crea la ventana.                                     |

| cursor      | Specifies the mouse cursor to be used for the widget.  See the |
|             | *cursor* option type under Tk option data types. If set to the |
|             | empty string (the default), the cursor is inherited from the   |
## |             | parent widget.                                                 |

| takefocus   | Determina si la ventana acepta el foco durante el recorrido    |
|             | del teclado. Se retorna 0, 1 o una cadena vacía. Si se retorna |
|             | 0, significa que la ventana debe omitirse por completo durante |
|             | el recorrido del teclado. Si es 1, significa que la ventana    |
|             | debe recibir el foco de entrada siempre que sea visible. Y una |
|             | cadena vacía significa que los scripts transversales toman la  |
## |             | decisión sobre si enfocarse o no en la ventana.                |

| style       | Se puede usar para especificar un estilo personalizado para el |
## |             | widget.                                                        |

### Scrollable widget options

Los widgets controlados por una barra deslizante presentan las
siguientes opciones.

+------------------+-----------------------------------------------------------+
| Opción           | Descripción                                               |
|==================|===========================================================|
| xscrollcommand   | Se usa para interactuar con las barras deslizantes        |
|                  | horizontales.  When the view in the widget's window       |
|                  | changes, the widget calls the *xscrollcommand* callback.  |
|                  | Usually this option consists of the method                |
|                  | "Scrollbar.set" of some scrollbar. This will cause the    |
|                  | scrollbar to be updated whenever the view in the window   |
## |                  | changes.                                                  |

| yscrollcommand   | Se utiliza para comunicarse con las barras deslizantes    |
|                  | verticales. Para obtener más información, consulta más    |
## |                  | arriba.                                                   |

### Label options

Las siguientes opciones son compatibles con etiquetas, botones y otros
widgets similares a botones.

+----------------+-------------------------------------------------------------+
| Opción         | Descripción                                                 |
|================|=============================================================|
| text           | Especifica una cadena de texto que se mostrará dentro del   |
## |                | widget.                                                     |

| textvariable   | Especifica un nombre cuyo valor se utilizará en lugar del   |
## |                | recurso de opción de texto.                                 |

| underline      | Si se activa, especifica el índice (empezando por 0) de un  |
|                | carácter que se va a subrayar en la cadena de texto. El     |
|                | carácter subrayado se utiliza para la activación            |
## |                | mnemotécnica.                                               |

| image          | Especifica una imagen que se va a mostrar. Es una lista de  |
|                | 1 o más elementos. El primer elemento es el nombre de       |
|                | imagen predeterminado. El resto de la lista es una          |
|                | secuencia de pares statespec/value según lo definido por    |
|                | "Style.map()", especificando diferentes imágenes para usar  |
|                | cuando el widget está en un estado determinado o una        |
|                | combinación de estados. Todas las imágenes de la lista      |
## |                | deben tener el mismo tamaño.                                |

| compound       | Especifica cómo mostrar la imagen en relación con el texto, |
|                | en el caso de que estén presentes las opciones de texto e   |
|                | imágenes. Los valores válidos son:  * text: mostrar solo    |
|                | texto  * image: mostrar solo la imagen  * top, bottom,      |
|                | left, right: muestra la imagen por encima, por debajo, a la |
|                | izquierda o a la derecha del texto, respectivamente.  *     |
|                | none: valor predeterminado. Mostrar la imagen si está       |
## |                | presente, de lo contrario el texto.                         |

| width          | Si es mayor que cero, especifica cuánto espacio, en ancho   |
|                | de caracteres, se debe asignar para la etiqueta de texto;   |
|                | si es menor que cero, especifica un ancho mínimo. Si es     |
|                | cero o no se especifica, se utiliza el ancho natural de la  |
## |                | etiqueta de texto.                                          |

### Compatibility options

+----------+------------------------------------------------------------------+
| Opción   | Descripción                                                      |
|==========|==================================================================|
| state    | Se puede establecer en "normal" o "deshabilitado" para controlar |
|          | el bit de estado "deshabilitado". Esta es una opción de solo     |
|          | escritura: establecerlo cambia el estado del widget, pero el     |
## |          | método "Widget.state()" no afecta a esta opción.                 |

### Widget states

El estado del widget es un mapa de bits de indicadores de estado
independientes.

+--------------+---------------------------------------------------------------+
| Indicador de | Descripción                                                   |
| estado       |                                                               |
|==============|===============================================================|
| active       | El puntero está sobre el widget y clickeando sobre él         |
## |              | producirá alguna acción                                       |

## | disabled     | El widget está desactivado bajo el control del programa       |

## | focus        | El widget tiene el enfoque del teclado                        |

## | pressed      | El widget está siendo pulsado                                 |

| selected     | "On", "true" o "current" para aspectos como Checkbuttons y    |
## |              | radiobuttons                                                  |

| background   | Windows y Mac tienen el concepto de ventana "activa" o en     |
|              | primer plano. El estado *background* se establece para los    |
|              | widgets en una ventana de fondo y se borra para los que están |
## |              | en la ventana en primer plano                                 |

## | readonly     | El widget no debe permitir la modificación del usuario        |

## | alternate    | Un formato de visualización alternativo específico del widget |

## | invalid      | El valor del widget no es válido                              |

Una especificación de estado es una secuencia de nombres de estado,
opcionalmente prefijados con un signo de exclamación que indica que el
bit está desactivado.

### ttk.Widget

Besides the methods described below, the "ttk.Widget" supports the
methods "tkinter.Widget.cget" and "tkinter.Widget.configure".

class tkinter.ttk.Widget

   identify(x, y)

      Retorna el nombre del elemento en la posición *x* *y* o la
      cadena vacía si el punto no se encuentra dentro de ningún
      elemento.

      *x* e *y* son coordenadas en píxeles relativas al widget.

   instate(statespec, callback=None, *args, **kw)

      Prueba el estado del widget. Si no se especifica una
      retrollamada, retorna "True" si el estado del widget coincide
      con *statespec* y "False" en caso contrario. Si se especifica la
      retrollamada, se llama con argumentos (*args*) si el estado del
      widget coincide con *statespec*.

   state(statespec=None)

      Modifica o pregunta el estado del widget. Si se especifica
      *statespec*, establece el estado del widget según éste y retorna
      un nuevo *statespec* informando cuales indicadores se han
      cambiado. Si no se especifica *statespec*, retorna los
      indicadores de estado habilitados actualmente.

      Not to be confused with "Wm.state".

   *statespec* es generalmente una lista o una tupla.

## Combobox

The "ttk.Combobox" widget combines a text field with a pop-down list
of values. This widget is a subclass of "Entry".

Besides the methods inherited from "Widget": "cget()", "configure()",
"identify()", "instate()" and "state()", and the following inherited
from "Entry": "bbox()", "delete()", "icursor()", "index()",
"insert()", "selection*", "xview*", it has some other methods,
described at "ttk.Combobox".

### Opciones

Este widget acepta las siguientes opciones específicas:

+-------------------+----------------------------------------------------------+
| Opción            | Descripción                                              |
|===================|==========================================================|
| exportselection   | Boolean value. If set, the widget selection is linked to |
|                   | the X selection (which can be returned by invoking       |
## |                   | Misc.selection_get, for example).                        |

| justify           | Especifica cómo el texto se alinea en el widget. Uno de  |
## |                   | "left", "center" o "right".                              |

| height            | Especifica el largo/altura del cuadro de la lista        |
## |                   | desplegable, en filas.                                   |

| postcommand       | Un script (posiblemente registrado con Misc.register)    |
|                   | que se llama inmediatamente antes de mostrar los         |
## |                   | valores. Puede especificar qué valores mostrar.          |

| state             | One of "normal", "readonly", or "disabled". In the       |
|                   | "readonly" state, the value may not be edited directly,  |
|                   | and the user can only select one of the values from the  |
|                   | dropdown list. In the "normal" state, the text field is  |
|                   | directly editable. In the "disabled" state, no           |
## |                   | interaction is possible.                                 |

| textvariable      | Especifica un nombre cuyo valor está vinculado al valor  |
|                   | del widget. Cada vez que cambia el valor asociado a ese  |
|                   | nombre, se actualiza el valor del widget y viceversa.    |
## |                   | Véase "tkinter.StringVar".                               |

| values            | Especifica la lista de valores que se mostrarán en el    |
## |                   | cuadro de lista desplegable.                             |

| width             | Especifica un valor entero que indica el ancho deseado   |
|                   | de la ventana de entrada, en caracteres de tamaño medio  |
## |                   | de la fuente del widget.                                 |

Nota:

  Tk 9.1 added the *locale* option, which selects the locale used to
  determine word and character boundaries within the text (""C"" by
  default).

### Eventos virtuales

Los widgets de cuadro combinado generan un evento virtual
**<<ComboboxSelected>>** cuando el usuario selecciona un elemento de
la lista de valores.

### ttk.Combobox

class tkinter.ttk.Combobox

   current(newindex=None)

      Si se especifica *newindex*, establece el valor del cuadro
      combinado en la posición del elemento *newindex*. De lo
      contrario, retorna el índice del valor actual o -1 si el valor
      actual no está en la lista de valores.

   get()

      Retorna el valor actual del cuadro combinado.

   set(value)

      Establece el valor del cuadro combinado a *value*.

## Spinbox

The "ttk.Spinbox" widget is a "ttk.Entry" enhanced with increment and
decrement arrows. It can be used for numbers or lists of string
values. This widget is a subclass of "Entry". Besides the methods
inherited from "Widget": "cget()", "configure()", "identify()",
"instate()" and "state()", and the following inherited from "Entry":
"bbox()", "delete()", "icursor()", "index()", "insert()", "xview*", it
has some other methods, described at "ttk.Spinbox".

### Opciones

Este widget acepta las siguientes opciones específicas:

+------------------------+--------------------------------------------------------+
| Opción                 | Descripción                                            |
|========================|========================================================|
| from                   | Valor flotante. Si se establece, este es el valor      |
|                        | mínimo al que se reducirá el botón de disminución.     |
|                        | Debe escribirse como "from_" cuando se usa como        |
|                        | argumento, ya que "from" es una palabra clave de       |
## |                        | Python.                                                |

| to                     | Valor flotante. Si se establece, este es el valor      |
## |                        | máximo al que se incrementará el botón de incremento.  |

| increment              | Valor flotante. Especifica la cantidad por la cual los |
|                        | botones de incremento/disminución cambian el valor.    |
## |                        | Por defecto la cantidad es de 1.0.                     |

| values                 | Secuencia de valores de cadena o flotantes. Si se      |
|                        | especifica, los botones de incremento/disminución      |
|                        | recorrerán los elementos de esta secuencia en lugar de |
## |                        | incrementar o disminuir los números.                   |

| wrap                   | Valor booleano. Si es "True", los botones de           |
|                        | incremento y disminución pasarán del valor "to" al     |
|                        | valor "from" o del valor "from" al valor "to",         |
## |                        | respectivamente.                                       |

| format                 | Valor de cadena. Especifica el formato de los números  |
|                        | establecidos por los botones de                        |
|                        | incremento/disminución. Debe tener la forma "%W.Pf",   |
|                        | donde W es el ancho de relleno del valor, P es la      |
## |                        | precisión, y '%' y 'f' son literales.                  |

| command                | Python invocable. Se llamará sin argumentos cada vez   |
|                        | que se presione alguno de los botones de incremento o  |
## |                        | disminución.                                           |

### Eventos virtuales

El widget spinbox genera un evento virtual **<<Increment>>** cuando el
usuario presiona <Up>, y un evento virtual **<<Decrement>>** cuando el
usuario presiona <Down>.

### ttk.Spinbox

class tkinter.ttk.Spinbox

   With a non-integer increment, see numeric values and the locale.

   Added in version 3.8.

   get()

      Retorna el valor actual del spinbox.

   set(value)

      Establece el valor del spinbox a *value*.

## Notebook

El widget Ttk Notebook administra una colección de ventanas y muestra
una sola a la vez. Cada ventana secundaria está asociada a una
pestaña, que el usuario puede seleccionar para cambiar la ventana que
se muestra actualmente.

### Opciones

Este widget acepta las siguientes opciones específicas:

+-----------+------------------------------------------------------------------+
| Opción    | Descripción                                                      |
|===========|==================================================================|
| height    | Si está presente y es mayor que cero, especifica la altura       |
|           | deseada del área del panel (sin incluir el relleno interno o las |
|           | pestañas). De lo contrario, se utiliza la altura máxima de todos |
## |           | los paneles.                                                     |

| padding   | Especifica la cantidad de espacio adicional que se va a agregar  |
|           | alrededor del exterior del bloc de notas. El relleno es una      |
|           | lista de hasta cuatro especificaciones de longitud izquierda     |
|           | superior derecha inferior. Si se especifican menos de cuatro     |
|           | elementos, el valor predeterminado inferior es el superior, el   |
|           | valor predeterminado de la derecha es el de la izquierda y el    |
## |           | valor predeterminado superior es el de la izquierda.             |

| width     | Si está presente y es mayor que cero, especifica el ancho        |
|           | deseado del área del panel (sin incluir el relleno interno). De  |
## |           | lo contrario, se utiliza el ancho máximo de todos los paneles.   |

### Tab options

Las opciones específicas para pestañas son:

+-------------+----------------------------------------------------------------+
| Opción      | Descripción                                                    |
|=============|================================================================|
| state       | O bien "normal", "disabled" o "hidden". Si es "disabled", la   |
|             | pestaña no se puede seleccionar. Si es "hidden", la pestaña no |
## |             | se muestra.                                                    |

| sticky      | Specifies how the child window is positioned within the pane   |
|             | area. Value is a string containing zero or more of the         |
|             | characters "n", "s", "e" or "w". Each letter refers to a side  |
|             | (north, south, east or west) that the child window will stick  |
## |             | to, as per the "grid" geometry manager.                        |

| padding     | Especifica la cantidad de espacio adicional que se va a        |
|             | agregar entre el notebook y este panel. La sintaxis es la      |
## |             | misma que para el relleno de opciones utilizado por Notebook.  |

## | text        | Especifica un texto que se muestra en la pestaña.              |

| image       | Especifica una imagen que se muestra en la pestaña. Consulta   |
## |             | la opción de imagen descrita en "Widget".                      |

| compound    | Especifica cómo mostrar la imagen en relación con el texto, en |
|             | el caso de que tanto el texto como la imagen estén presentes.  |
## |             | Consulta Label Options para obtener valores válidos.           |

| underline   | Especifica el índice (basado en 0) de un carácter que se va a  |
|             | subrayar en la cadena de texto. El carácter subrayado se       |
|             | utiliza para la activación mnemotécnica si se llama a          |
## |             | "Notebook.enable_traversal()".                                 |

### Tab identifiers

The tab_id present in several methods of "ttk.Notebook" may take any
of the following forms:

* Un entero entre cero y el número de pestañas

* El nombre de una ventana secundaria

* Un especificación de posición de la forma "@x,y" que identifique la
  pestaña

* El valor "current" el cual identifica la pestaña seleccionada
  actualmente

* El valor "end" que retorna el número de pestañas (válido solo para
  "Notebook.index()")

### Eventos virtuales

Este widget genera un evento virtual **<<NotebookTabChanged>>**
después de seleccionar una nueva pestaña.

### ttk.Notebook

class tkinter.ttk.Notebook

   add(child, **kw)

      Añade una nueva pestaña al notebook.

      Si la ventana está actualmente administrada por el notebook pero
      oculta, se restaura a su posición anterior.

      Consulta Tab Options para la lista de opciones disponibles.

   forget(tab_id)

      Quita la pestaña especificada por *tab_id*, desasigna y quita la
      ventana asociada.

      This shadows the inherited geometry-manager "forget()"; use
      "pack_forget()", "grid_forget()" or "place_forget()" to remove
      the widget itself from its manager.

   hide(tab_id)

      Oculta la pestaña especificada por *tab_id*.

      La pestaña no se mostrará, pero la ventana asociada permanece
      administrada por el notebook y se recordará su configuración.
      Las pestañas ocultas se pueden restaurar con el comando "add()".

   identify(x, y)

      Retorna el nombre del elemento de la pestaña en la posición *x*,
      *y* o cadena vacía si no hay ninguno.

   index(tab_id)

      Retorna el índice numérico de la pestaña especificada por
      *tab_id*, o el número total de pestañas si *tab_id* es la cadena
      "end".

   insert(pos, child, **kw)

      Añade un panel en la posición especificada.

      *pos* es la cadena "end", un índice entero o el nombre de un
      elemento secundario administrado. Si el bloc de notas ya
      administra *child*, lo mueve a la posición especificada.

      Consulta Tab Options para la lista de opciones disponibles.

   select(tab_id=None)

      Selecciona el *tab_id* especificado.

      Se mostrará la ventana secundaria asociada y la ventana
      previamente seleccionada (si es diferente) no se debe asignar.
      Si se omite *tab_id*, retorna el nombre del widget del panel
      seleccionado actualmente.

   tab(tab_id, option=None, **kw)

      Consultar o modificar las opciones del *tab_id* específico.

      Si no se proporciona *kw*, retorna un diccionario de los valores
      de las opciones de pestañas. Si se especifica *option*, retorna
      el valor de esa *option*. De lo contrario, establece las
      opciones en los valores correspondientes.

   tabs()

      Returns a tuple of windows managed by the notebook.

   enable_traversal()

      Habilita la tabulación para una ventana de nivel superior que
      contenga este notebook.

      Esto extenderá los enlaces para la ventana de nivel superior que
      contiene el notebook del siguiente modo:

      * "Control"-"Tab": selecciona la pestaña siguiente a la
        seleccionada actualmente.

      * "Shift"-"Control"-"Tab": selecciona la pestaña precedente a la
        seleccionada actualmente.

      * "Alt"-"K": donde *K* es el carácter mnemotécnico (subrayado)
        de cualquier pestaña, seleccionará esa pestaña.

      Multiple notebooks in a single toplevel may be enabled for
      traversal, including nested notebooks. However, notebook
      traversal only works properly if all panes are direct children
      of the notebook.

## Progressbar

The "ttk.Progressbar" widget shows the status of a long-running
operation. It can operate in two modes: 1) the determinate mode which
shows the amount completed relative to the total amount of work to be
done and 2) the indeterminate mode which provides an animated display
to let the user know that work is progressing.

### Opciones

Este widget acepta las siguientes opciones específicas:

+------------+-----------------------------------------------------------------+
| Opción     | Descripción                                                     |
|============|=================================================================|
| orient     | Puede ser "horizontal" o "vertical". Especifica la orientación  |
## |            | de la barra de progreso.                                        |

| length     | Especifica la longitud del eje largo de la barra de progreso    |
## |            | (ancho si horizontal, alto si es vertical).                     |

## | mode       | Puede ser "determinate" o "indeterminate".                      |

| maximum    | Número que especifica el valor máximo. Por defecto el valor es  |
## |            | 100.                                                            |

| value      | El valor actual de la barra de progreso. En el modo             |
|            | "determinado", representa la cantidad de trabajo completado. En |
|            | el modo "indeterminado", se interpreta como módulo *maximum*,   |
|            | es decir, la barra de progreso completa un "ciclo" cuando su    |
## |            | valor aumenta en *maximum*.                                     |

| variable   | Nombre vinculado al valor de la opción. Si se especifica, el    |
|            | valor de la barra de progreso se establece automáticamente en   |
## |            | el valor de este nombre cada vez que se modifica dicho valor.   |

| phase      | Variable de solo lectura. El widget incrementa periódicamente   |
|            | el valor de esta opción siempre que su valor sea mayor que 0 y, |
|            | en modo determinado, menor que el máximo. Esta opción puede ser |
|            | utilizada por el tema actual para proporcionar efectos de       |
## |            | animación adicionales.                                          |

### ttk.Progressbar

class tkinter.ttk.Progressbar

   start(interval=None)

      Inicia el modo de incremento automático: programa un evento
      *timer* periódico que llama a "Progressbar.step()" cada
      *interval* milisegundos. Si se omite, *interval* tiene como
      valor predeterminado 50 milisegundos.

   step(amount=None)

      Incrementa el valor de la barra de progreso en *amount*.

      *amount* vale 1.0 por defecto si se omite.

   stop()

      Para el modo de incremento automático: cancela cualquier evento
      *timer* periódico iniciado por "Progressbar.start()" para la
      barra de progreso en cuestión.

## Separator

The "ttk.Separator" widget displays a horizontal or vertical separator
bar.

It has no other methods besides the ones inherited from "ttk.Widget".

### Opciones

Este widget acepta las opción específica siguiente:

+----------+------------------------------------------------------------------+
| Opción   | Descripción                                                      |
|==========|==================================================================|
| orient   | Puede ser "horizontal" o "vertical". Especifica la orientación   |
## |          | del separador.                                                   |

## Sizegrip

The "ttk.Sizegrip" widget (also known as a grow box) allows the user
to resize the containing toplevel window by pressing and dragging the
grip.

This widget has neither specific options nor specific methods, besides
the ones inherited from "ttk.Widget".

### Notas específicas por plataforma

* En macOS, las ventanas de nivel superior incluyen automáticamente un
  control de tamaño integrado de forma predeterminada. Agregar un
  "Sizegrip" es inofensivo, ya que el agarre integrado solo enmascara
  el widget.

### Errores detectados

* If the containing toplevel's position was specified relative to the
  right or bottom of the screen (for example, ....), the "Sizegrip"
  widget will not resize the window.

* El widget solo soporta el cambio de tamaño desde la esquina inferior
  derecha.

## Treeview

The "ttk.Treeview" widget displays a hierarchical collection of items.
Each item has a textual label, an optional image, and an optional list
of data values. The data values are displayed in successive columns
after the tree label.

El orden en que se muestran los valores de datos se puede controlar
estableciendo la opción de widget "displaycolumns". El Treeview
también puede mostrar encabezados. Se puede acceder a las columnas por
número o nombres simbólicos enumerados en las columnas de opciones del
widget. Consulte Column Identifiers.

Cada elemento se identifica con un nombre único. El widget genera IDs
para los elementos si no se proporcionan en la declaración. Hay un
elemento raíz distinguido, denominado "{}". El elemento raíz en sí no
se muestra; sus hijos aparecen en el nivel superior de la jerarquía.

Cada elemento también tiene una lista de etiquetas que se pueden usar
para asociar enlaces de eventos con elementos individuales y controlar
la apariencia del elemento.

El widget Treeview admite el deslizamiento horizontal y vertical,
según las opciones descritas en Scrollable Widget Options y los
métodos "Treeview.xview()" y "Treeview.yview()".

### Opciones

Este widget acepta las siguientes opciones específicas:

+------------------+----------------------------------------------------------+
| Opción           | Descripción                                              |
|==================|==========================================================|
| columns          | Una lista de identificadores de columna, que especifican |
## |                  | el número de columnas y sus nombres.                     |

| displaycolumns   | Una lista de identificadores de columna (índices         |
|                  | simbólicos o enteros) que especifican qué columnas de    |
|                  | datos se muestran y el orden en que aparecen, o la       |
## |                  | cadena "#all".                                           |

| height           | Especifica el número de filas que deben estar visibles.  |
|                  | Nota: el ancho solicitado se determina a partir de la    |
## |                  | suma de los anchos de columna.                           |

| padding          | Especifica el relleno interno del widget. El relleno es  |
## |                  | una lista de hasta cuatro especificaciones de longitud.  |

| selectmode       | Controla cómo los enlaces de clase integrados            |
|                  | administran la selección. Puede ser "extended", "browse" |
|                  | o "none". Si se establece en "extended" (valor           |
|                  | predeterminado), se pueden seleccionar varios elementos. |
|                  | Si se elige "browse", se seleccionará un solo elemento a |
|                  | la vez. Si se elige "none", la selección no se cambiará. |
|                  | Tenga en cuenta que el código de la aplicación y los     |
|                  | enlaces de etiqueta pueden establecer la selección como  |
## |                  | deseen, independientemente del valor de esta opción.     |

| show             | Una lista que contiene cero o más de los siguientes      |
|                  | valores, especificando qué elementos del árbol se van a  |
|                  | mostrar.  * tree: muestra las etiquetas del árbol en la  |
|                  | columna #0.  * headings: muestra la fila de encabezado.  |
|                  | The default is "tree headings", that is, show all        |
|                  | elements.  **Nota**: la columna #0 siempre hace          |
|                  | referencia a la columna del árbol, incluso si no se      |
## |                  | especifica show="tree".                                  |

Nota:

  Tk 9.0 added several "Treeview" features. The *selectmode* option
  gained the values ""single"" and ""multiple""; the new widget
  options *selecttype* (""item"" or ""cell"" selection), *striped*
  (zebra-striped rows), and *titlecolumns* / *titleitems* (columns or
  rows frozen against scrolling) were introduced; the column
  *separator* option was added; and items gained a *hidden* option. Tk
  9.1 added the *rowheight* and *headingheight* options.

### Item options

Las siguientes opciones de elemento se pueden especificar para los
elementos de los comandos de inserción y de elementos del widget.

+----------+-----------------------------------------------------------------+
| Opción   | Descripción                                                     |
|==========|=================================================================|
## | text     | La etiqueta textual que se va a mostrar para el elemento.       |

## | image    | Una imagen Tk, que se muestra a la izquierda de la etiqueta.    |

| values   | La lista de valores asociados al elemento.  Cada elemento debe  |
|          | tener el mismo número de valores que las columnas de opciones   |
|          | del widget. Si hay menos valores que columnas, los valores      |
|          | restantes se asumen vacíos. Si hay más valores que columnas, se |
## |          | omiten los valores adicionales.                                 |

| open     | Valor "True"/"False" que indica si los elementos secundarios    |
## |          | deben mostrarse u ocultarse.                                    |

## | tags     | La lista de etiquetas asociadas al elemento.                    |

### Tag options

Se pueden especificar las opciones siguientes para etiquetas:

+--------------+-------------------------------------------------------------+
| Opción       | Descripción                                                 |
|==============|=============================================================|
## | foreground   | Especifica el color de primer plano del texto.              |

## | background   | Especifica el color de fondo de la celda o elemento.        |

## | font         | Especifica la fuente que se utilizará al añadir texto.      |

| image        | Especifica la imagen del elemento, en caso de que la opción |
## |              | de imagen del elemento esté vacía.                          |

### Column identifiers

Los identificadores de columna toman cualquiera de los siguientes
formas:

* Un nombre simbólico de la lista de opciones de columna.

* Un entero n, especificando la enésima columna de datos.

* Una cadena de la forma #n, donde n es un entero, especificando la
  enésima columna mostrada.

Notas:

* Los valores de opciones del elemento se pueden mostrar en un orden
  diferente al orden en el que se almacenan.

* La columna #0 siempre hace referencia a la columna del árbol,
  incluso si no se especifica show="tree".

Un número de columna de datos es un índice en la lista de valores de
opciones de un elemento; el número de columna se visualiza en el árbol
donde se muestran los valores. Las etiquetas de árbol se muestran en
la columna #0. Si no se establece la opción displaycolumns, la columna
de datos n se muestra en la columna #n+1. Una vez más, **la columna #0
siempre hace referencia a la columna del árbol**.

### Eventos virtuales

El widget Treeview genera los siguientes eventos virtuales.

+----------------------+----------------------------------------------------+
| Evento               | Descripción                                        |
|======================|====================================================|
## | <<TreeviewSelect>>   | Se genera cada vez que cambia la selección.        |

| <<TreeviewOpen>>     | Generado justo antes configurar el elemento de     |
## |                      | resalto a open=True.                               |

| <<TreeviewClose>>    | Generado justo después de establecer el elemento   |
## |                      | de resalto a open=False.                           |

Los métodos "Treeview.focus()" y "Treeview.selection()" se pueden
utilizar para determinar el elemento o elementos afectados.

### ttk.Treeview

class tkinter.ttk.Treeview

   bbox(item, column=None)

      Retorna el cuadro delimitador (en relación con la ventana del
      widget de Treeview) del *item* especificado con el formato (x,
      y, ancho, alto).

      If *column* is specified, returns the bounding box of that cell.
      If the *item* is not visible (that is, if it is a descendant of
      a closed item or is scrolled offscreen), returns an empty
      string.

      This shadows the inherited "Misc.bbox()"; use "grid_bbox()" for
      the grid bounding box.

   get_children(item=None)

      Returns a tuple of children belonging to *item*.

      Si no se especifica *item*, retorna la raíz.

   set_children(item, *newchildren)

      Replaces *item*'s children with *newchildren*.

      Los elementos secundarios presentes en *item* que no están
      presentes en *newchildren* se separan del árbol. Ningún elemento
      de *newchildren* puede ser un antecesor de *item*. Tenga en
      cuenta que si no se especifica *newchildren* se desasocian los
      elementos secundarios de *item*.

   column(column, option=None, **kw)

      Consultar o modificar las opciones para la *columna*
      especificada.

      Si no se proporciona *kw*, retorna un diccionario de los valores
      de opciones de columna. Si se especifica *option*, se retorna el
      valor de esa *option*. De lo contrario, establece las opciones
      en los valores correspondientes.

      Las opciones/valores válidos son:

      *id*
         Retorna el nombre de la columna. Esta es una opción de solo
         lectura.

      *anchor*: One of the standard Tk anchor values.
         Especifica cómo se debe alinear el texto de esta columna con
         respecto a la celda.

      *minwidth*: width
         El ancho mínimo de la columna en píxeles. El widget Treeview
         no hará que la columna sea más pequeña de lo especificado por
         esta opción cuando se cambie el tamaño del widget o el
         usuario arrastre una columna.

      *separator*: "True"/"False"
         Specifies whether a column separator should be drawn to the
         right of the column.

      *stretch*: "True"/"False"
         Especifica si el ancho de la columna debe ajustarse cuando se
         cambia el tamaño del widget.

      *width*: width
         El ancho de la columna en píxeles.

      Se puede establecer *column = "#0"* para configurar el árbol de
      la columna.

   delete(*items)

      Elimina todos los *items* especificados y todos sus
      descendientes.

      El elemento raíz no se elimina.

   detach(*items)

      Desvincula todos los *items* especificados del árbol.

      Los objetos y todos sus descendientes todavía existen, y pueden
      ser reinsertados en otro punto del árbol, pero no se mostrarán.

      El elemento raíz no se desvincula.

   exists(item)

      Returns "True" if the specified *item* is present in the tree,
      "False" otherwise.

   focus(item=None)

      Si se especifica *item*, establece el elemento de foco en
      *item*. De lo contrario, retorna el elemento de foco actual o ''
      si no hay ninguno.

      This shadows the inherited "Misc.focus()"; use "focus_set()" to
      focus the widget itself.

   heading(column, option=None, **kw)

      Consulta o modifica las opciones de encabezado para la *column*
      especificada.

      Si no se proporciona *kw*, retorna un diccionario de los valores
      de opciones de encabezado. Si se especifica *option*, se retorna
      el valor de esa *option*. De lo contrario, establece las
      opciones en los valores correspondientes.

      Las opciones/valores válidos son:

      *text*: text
         El texto se muestra en el encabezado de la columna.

      *image*: imageName
         Especifica una imagen para mostrar en la parte derecha del
         encabezado de la columna.

      *anchor*: anchor
         Especifica el alineamiento del texto del encabezado. Es uno
         de los valores estándar de Tk anchor.

      *command*: callback
         Una retrollamada que se ejecutará cuando se presione la
         etiqueta de encabezado.

      Se especifica *column ="#0"* para configurar el encabezado de la
      columna de árbol.

   identify(component, x, y)

      Retorna una descripción del *component* especificado bajo el
      punto dado por *x* e *y*, o la cadena vacía si no existe dicho
      *component* en esa posición.

   identify_row(y)

      Retorna el identificador del elemento en la posición *y*.

   identify_column(x)

      Returns the display column identifier of the cell at position
      *x*.

      La columna del árbol tiene ID #0.

   identify_region(x, y)

      Retorna uno de:

      +-------------+----------------------------------------+
      | zona        | significado                            |
      |=============|========================================|
      | heading     | Zona de encabezado del árbol.          |
      +-------------+----------------------------------------+
      | separator   | Espacio entre dos encabezados de       |
      |             | columna.                               |
      +-------------+----------------------------------------+
      | tree        | La zona del árbol.                     |
      +-------------+----------------------------------------+
      | cell        | Datos de celda.                        |
      +-------------+----------------------------------------+

      Disponibilidad: Tk 8.6.

   identify_element(x, y)

      Retorna el elemento en la posición *x*, *y*.

      Disponibilidad: Tk 8.6.

   index(item)

      Retorna el índice entero de *item* dentro de la lista de
      elementos secundarios de su elemento primario.

   insert(parent, index, iid=None, **kw)

      Crea un nuevo elemento y retorna el identificador del elemento
      recién creado.

      *parent* es el identificador del elemento primario o la cadena
      vacía para crear un nuevo elemento de nivel superior. *index* es
      un entero, o el valor "end", especificando dónde insertar el
      nuevo elemento en la lista de elementos secundarios del elemento
      primario. Si *index* es menor o igual que cero, el nuevo nodo se
      inserta al principio; si *index* es mayor o igual que el número
      actual de elementos secundarios, se inserta al final. Si se
      especifica *iid*, se utiliza como identificador de elemento;
      *iid* no debe existir en el árbol previamente. De lo contrario,
      se genera un nuevo identificador único.

      See Item Options for the list of available options.

   item(item, option=None, **kw)

      Consulta o modifica las opciones para el *item* especificado.

      Si no se proporciona ninguna opción, se retorna un diccionario
      con opciones/valores para el elemento. Si se especifica
      *option*, se retorna el valor de esa opción. De lo contrario,
      establece las opciones en los valores correspondientes según
      *kw*.

   move(item, parent, index)

      Mueve *item* a la posición *index* en la lista de elementos
      secundarios de *parent*.

      No se permite mover un elemento bajo uno de sus descendientes.
      Si *index* es menor o igual que cero, *item* se mueve al
      principio; si es mayor o igual que el número de hijos, se mueve
      hasta el final. Si *item* se desvincula, se vuelve a conectar.

      "reattach()" is an alias of "move()".

   next(item)

      Retorna el identificador del siguiente elemento de *item*, o ''
      si *item* es el último elemento secundario de su elemento
      primario.

   parent(item)

      Retorna el identificador del elemento primario de *item* o '' si
      *item* está en el nivel superior de la jerarquía.

   prev(item)

      Retorna el identificador del elemento anterior de *item*, o ''
      si *item* es el primer elemento secundario de su elemento
      primario.

   see(item)

      Garantiza que *item* está visible.

      Establece todas las opciones modificables de los antecesores de
      *item* a "True" y desplaza el widget si es necesario para que
      *item* esté dentro de la parte visible del árbol.

   selection()

      Retorna una tupla de los elementos seleccionados.

      Distinto en la versión 3.8: "selection()" ya no toma argumentos.
      Para cambiar el estado de selección, utiliza los siguientes
      métodos de selección.

   selection_set(*items)

      *items* se convierte en la nueva selección.

      Distinto en la versión 3.6: *items* se pueden pasar como
      argumentos separados, no solo como una sola tupla.

   selection_add(*items)

      Añade *items* a la selección.

      Distinto en la versión 3.6: *items* se pueden pasar como
      argumentos separados, no solo como una sola tupla.

   selection_remove(*items)

      Elimina *elementos* de la selección.

      Distinto en la versión 3.6: *items* se pueden pasar como
      argumentos separados, no solo como una sola tupla.

   selection_toggle(*items)

      Alterna el estado de selección de cada elemento en *items*.

      Distinto en la versión 3.6: *items* se pueden pasar como
      argumentos separados, no solo como una sola tupla.

   set(item, column=None, value=None)

      Con un argumento, retorna un diccionario de pares columna/valor
      para el *item* especificado. Con dos argumentos, retorna el
      valor actual de la *columna* especificada. Con tres argumentos,
      establece el valor de determinado *column* en un *item*
      determinado en el *value* especificado.

   tag_bind(tagname, sequence=None, callback=None)

      Enlaza una retrollamada para el evento *sequence* a la etiqueta
      *tagname*. Cuando se entrega un evento a un elemento, se llama a
      las retrollamadas de cada una de las etiquetas del elemento.

   tag_configure(tagname, option=None, **kw)

      Consulta o modifica las opciones para el *tagname* especificado.

      Si no se proporciona *kw*, retorna un diccionario de la
      configuración de opciones para *tagname*. Si se especifica
      *option*, retorna el valor de esa *option* para el *tagname*
      especificado. De lo contrario, establece las opciones en los
      valores correspondientes para el *tagname* dado.

   tag_has(tagname, item=None)

      If *item* is specified, returns "True" if the specified *item*
      has the given *tagname* and "False" otherwise. Otherwise,
      returns a tuple of all items that have the specified tag.

      Disponibilidad: Tk 8.6

   xview(*args)

      Consulta o modifica la posición horizontal de la vista de árbol.

   yview(*args)

      Consulta o modifica la posición vertical de la vista de árbol.

## Ttk styling

Each widget in "ttk" is assigned a style, which specifies the set of
elements making up the widget and how they are arranged, along with
dynamic and default settings for element options. By default the style
name is the same as the widget's class name, but it may be overridden
by the widget's style option. If you don't know the class name of a
widget, use the method "Misc.winfo_class" (somewidget.winfo_class()).

Ver también:

  Introduction to the Tk theme engine
     The "ttk::intro" man page explains how the theme engine works.

  The Tile Widget Set
     Joe English's 2004 paper introducing the theme engine (then the
     separate *Tile* extension), with diagrams of how elements and
     layouts make up a widget's appearance.

class tkinter.ttk.Style

   Esta clase se utiliza para manipular la base de datos de estilos.

   configure(style, query_opt=None, **kw)

      Consulta o establece el valor predeterminado de las opciones
      especificadas en *style*.

      Cada clave en *kw* es una opción y cada valor es una cadena que
      identifica el valor de esa opción.

      Por ejemplo, para cambiar cualquier botón por defecto a un botón
      plano con borde interno y un color de fondo distinto:

         from tkinter import ttk
         import tkinter

         root = tkinter.Tk()

         ttk.Style().configure("TButton", padding=6, relief="flat",
            background="#ccc")

         btn = ttk.Button(text="Sample")
         btn.pack()

         root.mainloop()

   map(style, query_opt=None, **kw)

      Consulta o establece valores dinámicos de opciones específicas
      en *style*.

      Cada clave en *kw* es una opción y cada valor es una lista o
      tupla (generalmente) que contiene *statespecs* agrupados en
      tuplas, listas o alguna otra preferencia. Una *statespec* es un
      compuesto de uno o más estados y un valor.

      Un ejemplo puede hacerlo más comprensible:

         import tkinter
         from tkinter import ttk

         root = tkinter.Tk()

         style = ttk.Style()
         style.map("C.TButton",
             foreground=[('pressed', 'red'), ('active', 'blue')],
             background=[('pressed', '!disabled', 'black'), ('active', 'white')]
             )

         colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

         root.mainloop()

      Ten en cuenta que el orden de las secuencias (estado, valor)
      para una opción es importante, si se cambia el orden a
      "[('active', 'blue'), ('pressed', 'red')]" en la opción en
      primer plano, por ejemplo, el resultado sería un primer plano
      azul cuando el widget se encuentre en los estados *active* o
      *pressed*.

      When called to query the map (without specifying values to set),
      it returns a dictionary mapping each option to its list of
      statespecs.

      Distinto en la versión 3.10: The value returned when querying
      the map was corrected.

   lookup(style, option, state=None, default=None)

      Retorna el valor especificado para *option* en *style*.

      Si *state* se especifica, se espera que sea una secuencia de uno
      o más estados. Si se establece el argumento *default*, se usa
      como valor de reserva en caso de que no se especifique una
      opción.

      Para verificar qué fuente usa un Button por defecto:

         from tkinter import ttk

         print(ttk.Style().lookup("TButton", "font"))

   layout(style, layoutspec=None)

      Define el diseño del widget para un *estilo* dado. Si se omite
      *layoutspec*, retorna la especificación de diseño para un estilo
      determinado.

      *layoutspec*, si se especifica, se espera que sea una lista o
      algún otro tipo de secuencia (excluyendo cadenas), donde cada
      elemento debe ser una tupla y el primer elemento es el nombre de
      diseño y el segundo elemento debe tener el formato descrito en
      Layouts.

      Para entender el formato, consulta el siguiente ejemplo (no está
      pensado para hacer nada útil):

         from tkinter import ttk
         import tkinter

         root = tkinter.Tk()

         style = ttk.Style()
         style.layout("TMenubutton", [
            ("Menubutton.background", None),
            ("Menubutton.button", {"children":
                [("Menubutton.focus", {"children":
                    [("Menubutton.padding", {"children":
                        [("Menubutton.label", {"side": "left", "expand": 1})]
                    })]
                })]
            }),
         ])

         mbtn = ttk.Menubutton(text='Text')
         mbtn.pack()
         root.mainloop()

   element_create(elementname, etype, *args, **kw)

      Create a new element in the current theme, of the given *etype*
      which is expected to be either "image", "from" or "vsapi". The
      latter is only available in Tk 8.6 on Windows.

      Si se utiliza "image", *args* debe contener el nombre de imagen
      predeterminado seguido de pares statespec/value (esta es
      imagespec), y *kw* puede tener las siguientes opciones:

      border=padding
         el relleno interno es una lista de hasta cuatro enteros,
         especificando los bordes izquierdo, superior, derecho e
         inferior, respectivamente.

      height=height
         Especifica una altura mínima para el elemento. Si es menor
         que cero, la altura de la imagen base se utiliza como valor
         predeterminado.

      padding=padding
         Especifica el relleno interior del elemento. El valor
         predeterminado es el valor del borde si no se especifica.

      sticky=spec
         Especifica cómo se coloca la imagen dentro de la sección.
         *spec* contiene cero o más caracteres "n", "s", "w" o "e".

      width=width
         Especifica un ancho mínimo para el elemento. Si es menor que
         cero, el ancho de la imagen base se utiliza como valor
         predeterminado.

      Example:

         img1 = tkinter.PhotoImage(master=root, file='button.png')
         img1 = tkinter.PhotoImage(master=root, file='button-pressed.png')
         img1 = tkinter.PhotoImage(master=root, file='button-active.png')
         style = ttk.Style(root)
         style.element_create('Button.button', 'image',
                              img1, ('pressed', img2), ('active', img3),
                              border=(2, 4), sticky='we')

      Si se utiliza "from" como valor de *etype*, "element_create()"
      clonará un elemento existente. *args* contiene un themename,
      desde el que se clonará el elemento y, opcionalmente, un
      elemento desde el que clonar. Si no se especifica este elemento
      para clonar, se usará un elemento vacío. *kw* se descarta.

      Example:

         style = ttk.Style(root)
         style.element_create('plain.background', 'from', 'default')

      If "vsapi" is used as the value of *etype*, "element_create()"
      will create a new element in the current theme whose visual
      appearance is drawn using the Microsoft Visual Styles API which
      is responsible for the themed styles on Windows XP and Vista.
      *args* is expected to contain the Visual Styles class and part
      as given in the Microsoft documentation followed by an optional
      sequence of tuples of ttk states and the corresponding Visual
      Styles API state value. *kw* may have the following options:

      padding=padding
         Specify the element's interior padding. *padding* is a list
         of up to four integers specifying the left, top, right and
         bottom padding quantities respectively. If fewer than four
         elements are specified, bottom defaults to top, right
         defaults to left, and top defaults to left. In other words, a
         list of three numbers specify the left, vertical, and right
         padding; a list of two numbers specify the horizontal and the
         vertical padding; a single number specifies the same padding
         all the way around the widget. This option may not be mixed
         with any other options.

      margins=padding
         Specifies the elements exterior padding. *padding* is a list
         of up to four integers specifying the left, top, right and
         bottom padding quantities respectively. This option may not
         be mixed with any other options.

      width=width
         Specifies the width for the element. If this option is set
         then the Visual Styles API will not be queried for the
         recommended size or the part. If this option is set then
         *height* should also be set. The *width* and *height* options
         cannot be mixed with the *padding* or *margins* options.

      height=height
         Specifies the height of the element. See the comments for
         *width*.

      Example:

         style = ttk.Style(root)
         style.element_create('pin', 'vsapi', 'EXPLORERBAR', 3, [
                              ('pressed', '!selected', 3),
                              ('active', '!selected', 2),
                              ('pressed', 'selected', 6),
                              ('active', 'selected', 5),
                              ('selected', 4),
                              ('', 1)])
         style.layout('Explorer.Pin',
                      [('Explorer.Pin.pin', {'sticky': 'news'})])
         pin = ttk.Checkbutton(style='Explorer.Pin')
         pin.pack(expand=True, fill='both')

      Distinto en la versión 3.13: Added support of the "vsapi"
      element factory.

   element_names()

      Returns a tuple of elements defined in the current theme.

   element_options(elementname)

      Returns a tuple of *elementname*'s options.

   theme_create(themename, parent=None, settings=None)

      Crea un tema nuevo.

      Es un error si *themename* ya existe. Si se especifica *parent*,
      el nuevo tema heredará estilos, elementos y diseños del tema
      primario. Si se especifica *settings*, se espera que tengan la
      misma sintaxis utilizada para "theme_settings()".

   theme_settings(themename, settings)

      Establece temporalmente el tema actual en *themename*, aplica
      los *settings* especificados y, a continuación, restaura el tema
      anterior.

      Cada clave en *settings* es un estilo y cada valor puede
      contener las teclas 'configure', 'map', 'layout' y 'element
      create' y se espera que tengan el mismo formato especificado por
      los métodos "Style.configure()", "Style.map()", "Style.layout()"
      y "Style.element_create()" respectivamente.

      Como ejemplo, vamos a cambiar un poco el Combobox por el tema
      predeterminado:

         from tkinter import ttk
         import tkinter

         root = tkinter.Tk()

         style = ttk.Style()
         style.theme_settings("default", {
            "TCombobox": {
                "configure": {"padding": 5},
                "map": {
                    "background": [("active", "green2"),
                                   ("!disabled", "green4")],
                    "fieldbackground": [("!disabled", "green3")],
                    "foreground": [("focus", "OliveDrab1"),
                                   ("!disabled", "OliveDrab2")]
                }
            }
         })

         combo = ttk.Combobox().pack()

         root.mainloop()

   theme_names()

      Returns a tuple of all known themes.

   theme_use(themename=None)

      Si no se proporciona *themename*, retorna el tema en uso. De lo
      contrario, establece el tema actual en *themename*, actualiza
      todos los widgets y emite un evento <<ThemeChanged>>.

### Diseños

A layout can be just "None", if it takes no options, or a dict of
options specifying how to arrange the element. The layout mechanism
uses a simplified version of the pack geometry manager: given an
initial cavity, each element is allocated a parcel.

Las opciones/valores válidos son:

*side*: whichside
   Especifica en qué lado de la cavidad colocar el elemento; sea
   arriba, derecha, abajo o izquierda. Si se omite, el elemento ocupa
   toda la cavidad.

*sticky*: nswe
   Especifica dónde se coloca el elemento dentro de su sección
   asignada.

*unit*: 0 or 1
   Si se establece en 1, hace que el elemento y todos sus
   descendientes sean tratados como un único elemento en métodos como
   "Widget.identify()" y otros. Se utiliza para cosas como los
   *thumbs* de la barra de desplazamiento.

*children*: [sublayout... ]
   Especifica una lista de elementos para colocar dentro del elemento.
   Cada elemento es una tupla (u otro tipo de secuencia) donde el
   primer elemento es el nombre de diseño y el otro es un Layout.

## Additional widgets

The following themed widgets complete the "tkinter.ttk" widget set.
Each is the themed counterpart of the like-named classic "tkinter"
widget and inherits the common methods of "Widget".

class tkinter.ttk.Button(master=None, **kw)

   Ttk "Button" widget, displays a textual label and/or image, and
   evaluates a command when pressed. It is the themed counterpart of
   "tkinter.Button" and inherits the common widget methods from
   "Widget".

   invoke()

      Invoke the command associated with the button and return its
      result.

class tkinter.ttk.Checkbutton(master=None, **kw)

   Ttk "Checkbutton" widget, used to control a boolean variable that
   is toggled on and off. It is the themed counterpart of
   "tkinter.Checkbutton" and inherits the common widget methods from
   "Widget".

   invoke()

      Toggle the button between its selected and deselected states,
      invoke the command associated with the button, and return its
      result.

class tkinter.ttk.Entry(master=None, widget=None, **kw)

   Ttk "Entry" widget, displays a one-line text string and allows the
   user to edit it. It is the themed counterpart of "tkinter.Entry"
   and inherits the common widget methods from "Widget" as well as the
   editing methods from "tkinter.Entry".

   bbox(index)

      Return a tuple "(x, y, width, height)" giving the bounding box
      of the character at the given *index*.

      This shadows the inherited "Misc.bbox()"; use "grid_bbox()" for
      the grid bounding box.

   identify(x, y)

      Return the name of the element under the point given by *x* and
      *y*, or the empty string if no element is present at that
      location.

   validate()

      Force validation of the entry and return "True" if validation
      succeeded, and "False" otherwise.

class tkinter.ttk.Frame(master=None, **kw)

   Ttk "Frame" widget, a container used to group and lay out other
   widgets. It is the themed counterpart of "tkinter.Frame" and
   inherits the common widget methods from "Widget".

class tkinter.ttk.Label(master=None, **kw)

   Ttk "Label" widget, displays a textual label and/or image. It is
   the themed counterpart of "tkinter.Label" and inherits the common
   widget methods from "Widget".

class tkinter.ttk.Labelframe(master=None, **kw)

   Ttk "Labelframe" widget, a container that draws a border and a
   title label around its contents. It is the themed counterpart of
   "tkinter.LabelFrame" and inherits the common widget methods from
   "Widget".

class tkinter.ttk.Menubutton(master=None, **kw)

   Ttk "Menubutton" widget, displays a textual label and/or image, and
   pops up a menu when pressed. It is the themed counterpart of
   "tkinter.Menubutton" and inherits the common widget methods from
   "Widget".

class tkinter.ttk.OptionMenu(master, variable, default=None, *values, **kwargs)

   Ttk "OptionMenu" widget, a "Menubutton" that pops up a menu of
   mutually exclusive choices. *variable* is the variable that tracks
   the currently selected value, *default* is the value to set
   initially, and *values* are the entries to display in the menu. A
   *command* keyword argument may be given to specify a callable that
   is invoked with the selected value whenever the selection changes;
   the *style* keyword argument sets the style used by the underlying
   menubutton; the *direction* keyword argument sets where the menu is
   posted relative to the menubutton (one of "'above'", "'below'" (the
   default), "'left'", "'right'" or "'flush'"); and the *name* keyword
   argument sets the Tk widget name.

   set_menu(default=None, *values)

      Replace the entries of the menu with *values*. If *default* is
      given, also set it as the current value of the *variable*.

   destroy()

      Destroy this widget and its associated menu.

   Distinto en la versión 3.14: Added support for the *name* keyword
   argument.

class tkinter.ttk.Panedwindow(master=None, **kw)

   Ttk "Panedwindow" widget, displays a number of subwindows stacked
   either vertically or horizontally. The user may adjust the relative
   sizes of the subwindows by dragging the sash between panes. It is
   the themed counterpart of "tkinter.PanedWindow" and inherits the
   common widget methods from "Widget", as well as the "add()" and
   "panes()" methods from "tkinter.PanedWindow".

   insert(pos, child, **kw)

      Insert a pane containing *child* at the position *pos*. *pos* is
      either the string "'end'", an integer index, or the name of a
      managed subwindow. If *child* is already managed by the paned
      window, move it to the specified position. Any keyword arguments
      set pane options.

   forget(child)

      Remove *child*, which may be either an integer index or the name
      of a managed subwindow, from the panes.

      This shadows the inherited geometry-manager "forget()"; use
      "pack_forget()", "grid_forget()" or "place_forget()" to remove
      the widget itself from its manager.

   pane(pane, option=None, **kw)

      Query or modify the options of the specified *pane*, where
      *pane* is either an integer index or the name of a managed
      subwindow. If no arguments are given, return a dictionary of the
      pane option values. If *option* is specified, return the value
      of that option. Otherwise, set the options given as keyword
      arguments to their corresponding values.

   sashpos(index, newpos=None)

      If *newpos* is specified, set the position of sash number
      *index* and return its new position. This may adjust the
      positions of adjacent sashes to ensure that positions are
      monotonically increasing; positions are also constrained to be
      between 0 and the total size of the widget. If *newpos* is
      omitted, return the current position of the sash.

class tkinter.ttk.Radiobutton(master=None, **kw)

   Ttk "Radiobutton" widget, used as part of a group to control a
   single shared variable by selecting one of several mutually
   exclusive values. It is the themed counterpart of
   "tkinter.Radiobutton" and inherits the common widget methods from
   "Widget".

   invoke()

      Set the option variable to the button's value, select the
      button, invoke the command associated with the button, and
      return its result.

class tkinter.ttk.Scale(master=None, **kw)

   Ttk "Scale" widget, displays a slider that lets the user select a
   numeric value from a range by moving the slider along a trough. It
   is the themed counterpart of "tkinter.Scale" and inherits the
   common widget methods from "Widget".

   configure(cnf=None, **kw)

      Modify or query the widget options, like "Widget.configure". In
      addition, this method clips the "from" and "to" values so that
      the current value stays within the range defined by them.

      Distinto en la versión 3.9: Now returns the configuration value,
      like "Widget.configure".

   get(x=None, y=None)

      Return the current value of the scale. If *x* and *y* are given,
      return the value corresponding to the pixel coordinate *x*, *y*
      instead.

class tkinter.ttk.Scrollbar(master=None, **kw)

   Ttk "Scrollbar" widget, controls the viewport of an associated
   scrollable widget such as a "Treeview", "Entry" or "tkinter.Text".
   It is the themed counterpart of "tkinter.Scrollbar" and inherits
   the common widget methods from "Widget", as well as the "set()" and
   "get()" methods from "tkinter.Scrollbar".

class tkinter.ttk.Separator(master=None, **kw)

   Ttk "Separator" widget, displays a horizontal or vertical separator
   line. It has no direct counterpart in "tkinter" and inherits the
   common widget methods from "Widget".

class tkinter.ttk.Sizegrip(master=None, **kw)

   Ttk "Sizegrip" widget, displays a grip that allows the user to
   resize the containing toplevel window by pressing and dragging the
   grip, typically placed in the bottom-right corner. It has no direct
   counterpart in "tkinter" and inherits the common widget methods
   from "Widget".

class tkinter.ttk.LabeledScale(master=None, variable=None, from_=0, to=10, **kw)

   A "Frame" containing a "Scale" and a "Label" that shows the scale's
   current value. *variable* is the "IntVar" tracked by the scale (one
   is created if it is not given), and *from_* and *to* define the
   range of the scale.

   destroy()

      Destroy this widget and remove the trace callback registered on
      the associated variable.

class tkinter.ttk.LabelFrame(master=None, **kw)

   Alias of "Labelframe", kept for naming compatibility with
   "tkinter.LabelFrame".

class tkinter.ttk.PanedWindow(master=None, **kw)

   Alias of "Panedwindow", kept for naming compatibility with
   "tkinter.PanedWindow".
