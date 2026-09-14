---
title: IDLE --- Python editor and shell
source_url: https://docs.python.org/es/3
source_path: library/idle.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2910
---

# IDLE --- Python editor and shell

**Código fuente:** Lib/idlelib/

======================================================================

IDLE es el entorno de desarrollo integrado de Python.

IDLE tiene las siguientes características:

* multiplataforma: funciona en su mayoría igual en Windows, Unix y
  macOS

* La ventana del shell de Python (interprete interactivo) con
  coloreado de código de entrada, salida y mensajes de error

* editor de texto multiventana con deshacer múltiple, coloreación
  Python, indentado inteligente, sugerencias de llamadas a funciones,
  autocompletado y otras características

* búsqueda dentro de cualquier ventana, reemplazo dentro de las
  ventanas del editor, y búsqueda a través de múltiples archivos
  (grep)

* depurador con breakpoints persistentes, por pasos y visualización de
  espacios de nombres globales y locales

* configuración, navegadores y otros cuadros de diálogo

The IDLE application is implemented in the "idlelib" package.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

## Menús

IDLE tiene dos tipos de ventana principales, la ventana del shell y la
ventana del editor.  Es posible tener múltiples ventanas de edición
simultáneamente.  En Windows y Linux, cada una tiene su propio menú
principal.  Cada menú documentado abajo indica con cuál tipo de
ventana está asociada esta.

Las ventanas de salida, como las que se usan para Editar => Encontrar
en archivos, son un subtipo de la ventana de edición.  Actualmente
tienen el mismo menú principal pero un título predeterminado y un menú
contextual diferente.

En macOS, hay un menú de aplicación.  Este cambia dinámicamente de
acuerdo la ventana actualmente seleccionada.  Tiene un menú IDLE y
algunas de las entradas descritas a continuación se mueven de acuerdo
con las pautas de Apple.

### Menú de archivo (Shell y Editor)

Nuevo archivo
   Crea una nueva ventana de edición de archivos.

Abrir...
   Abre un archivo existente con un cuadro de dialogo para abrir.

Abrir módulo...
   Abre un módulo existente (buscar en sys.path).

Archivos recientes
   Abre una lista de archivos recientes.  Haga click en alguno para
   abrirlo.

Navegador de módulo
   Muestra las funciones, clases y métodos en estructura de árbol en
   el archivo actual del Editor.  En el shell, primero abra un módulo.

Navegador de ruta
   Muestra directorios, módulos, funciones, clases y métodos de
   sys.path en una estructura de árbol.

Guardar
   Guarda la ventana actual en el archivo asociado, si existe alguno.
   Las ventanas que han sido modificadas desde que se abrieron o se
   guardaron por última vez tienen un * antes y después del título de
   la ventana.  Si no hay un archivo asociado, ejecute Guardar como en
   su lugar.

Guardar como...
   Save the current window with a Save As dialog.  The file saved
   becomes the new associated file for the window. (If your file
   manager is set to hide extensions, the current extension will be
   omitted in the file name box. If the new filename has no '.', '.py'
   and '.txt' will be added for Python and text files, except that on
   macOS Aqua,'.py' is added for all files.)

Guardar copia como...
   Guarda la ventana actual en un archivo diferente sin cambiar el
   archivo asociado. (Consultar la nota anterior Guardar como sobre
   las extensiones de nombre de archivo.)

Imprimir ventana
   Imprime la ventana actual en la impresora predeterminada.

Cerrar ventana
   Cierra la ventana actual (si es un editor no guardado, solicita
   guardar; si es un Shell no guardado, solicita salir de la
   ejecución). Llamar a "exit()" o "close()" en la ventana de Shell
   también cierra el Shell. Si esta es la única ventana, también sale
   del IDLE.

Salir del IDLE
   Cierra todas las ventanas y sale del IDLE (solicita guardar
   ventanas de edición no guardadas).

### Menú editar (Shell y Editor)

Deshacer
   Deshace el último cambio a la ventana actual.  Se puede deshacer un
   máximo de 1000 cambios.

Rehacer
   Vuelve a aplicar el último cambio deshecho a la ventana actual.

Seleccionar todo
   Selecciona el contenido completo de la ventana actual.

Cortar
   Copia la selección en el portapapeles global; después elimina la
   selección.

Copiar
   Copia la selección en el portapapeles global.

Pegar
   Inserta el contenido del portapapeles global en la ventana actual.

Las funciones del portapapeles también están disponibles en los menús
contextuales.

Encontrar...
   Abre un cuadro de diálogo de búsqueda con muchas opciones

Buscar de nuevo
   Repite la última búsqueda, si hay alguna.

Encontrar selección
   Busca la cadena de caracteres seleccionada actualmente, si hay
   alguna.

Encontrar en Archivos...
   Abre un cuadro de diálogo de búsqueda de archivos.  Presenta los
   resultados en una nueva ventana de salida.

Reemplazar...
   Abre un cuadro de diálogo de búsqueda y reemplazo.

Ir a la línea
   Mueve el cursor al inicio de la línea solicitada y hace que esa
   línea sea visible.  Una solicitud a partir del final del archivo lo
   lleva al final. Borra cualquier selección y actualiza el estado de
   la línea y la columna.

Mostrar complementos
   Open a scrollable list allowing selection of existing names. See
   Completions in the Editing and Navigation section below.

Expandir palabra
   Completa un prefijo que se ha escrito para que coincida con una
   palabra completa en la misma ventana; intente nuevamente para
   obtener un complemento diferente.

Mostrar sugerencias de llamada
   After an unclosed parenthesis for a function, open a small window
   with function parameter hints.  See Calltips in the Editing and
   Navigation section below.

Mostrar los paréntesis alrededor
   Resalta los paréntesis.

### Menú de formato (solo ventana del Editor)

Formatear párrafo
   Rewrap the text block containing the text insert cursor. Avoid code
   lines.  See Format block in the Editing and Navigation section
   below.

Zona de indentación
   Desplaza las líneas seleccionadas a la derecha en un nivel de
   indentación (por defecto 4 espacios).

Zona de deindentación
   Desplaza las líneas seleccionadas hacia la izquierda en un nivel de
   indentación (por defecto 4 espacios).

Zona comentada
   Inserta ## delante de las líneas seleccionadas.

Zona descomentada
   Elimina los # o ## al inicio de las líneas seleccionadas.

Zona tabulada
   Transforma los tramos de espacios *iniciales* en tabs. (Nota:
   Recomendamos usar 4 bloques de espacio para indentar el código de
   Python).

Zona destabulada
   Transforma *todos* los tabs en el número correcto de espacios.

Alternar tabs
   Abre un cuadro de diálogo para cambiar entre indentado con espacios
   y tabs.

Nuevo tamaño de indentación
   Abre un cuadro de diálogo para cambiar el tamaño de indentación. El
   valor predeterminado aceptado por la comunidad de Python es de 4
   espacios.

Strip Trailing Whitespace
   Remove trailing space and other whitespace characters after the
   last non-whitespace character of a line by applying "str.rstrip()"
   to each line, including lines within multiline strings.  Except for
   Shell windows, remove extra newlines at the end of the file.

### Menú ejecutar (solo ventana Editor)

Módulo ejecutar
   Hace lo que dice en Verificar módulo.  Si no hay errores, reinicia
   el shell para limpiar el entorno, luego ejecuta el módulo.  La
   salida es mostrada en la ventana de shell.  Tener en cuenta que la
   visualización requiere el uso de "print" o "write". Cuando finaliza
   la ejecución, el shell permanece activo y muestra un mensaje. En
   este punto, se puede explorar interactivamente el resultado de la
   ejecución. Esto es similar a ejecutar un archivo con "python -i
   file" en una línea de comando.

Ejecutar... Personalizado
   Igual que Módulo ejecutar, pero ejecuta el módulo con parámetros
   personalizados.  *Los argumentos de la línea de comandos* extienden
   "sys.argv" como si se pasaran por una línea de comando. El módulo
   se puede ejecutar en el shell sin reiniciar.

Verificar módulo
   Comprueba la sintaxis del módulo actualmente abierto en la ventana
   de edición. Si el módulo no ha sido guardado IDLE solicitará al
   usuario que guarde o guarde automáticamente, como se seleccionó en
   la pestaña General del cuadro de diálogo Configuración de
   inactividad.  Si hay algún error de sintaxis, la ubicación
   aproximada será indicada en la ventana del Editor.

Shell de Python
   Abrir o activar la ventana del shell de Python.

### Menú de shell (solo ventana de shell)

Ver el último reinicio
   Navega la ventana del shell hasta el último reinicio del mismo.

Reiniciar shell
   Reinicia el shell para limpiar el entorno.

Historial anterior
   Recorre los comandos anteriores en el historial que coinciden con
   la entrada actual.

Historial siguiente
   Recorre los comandos posteriores en el historial que coinciden con
   la entrada actual.

Ejecución de interrupción
   Detiene un programa en ejecución.

### Menú de depuración (solo ventana de shell)

Ir al Archivo/Línea
   Busca en la línea actual, con el cursor y la línea de arriba para
   un nombre de archivo y número de línea.  Si lo encuentra, abre el
   archivo si aún no está abierto y muestra la línea.  Usa esto para
   ver las líneas de origen referenciadas en un rastreo de excepción y
   las líneas encontradas por Buscar en archivos. También disponible
   en el menú contextual de la ventana del shell y las ventanas de
   salida.

Depurador (alternar)
   Cuando esta función está habilitada, el código ingresado en el
   shell o ejecutado desde el editor se ejecutará con el depurador.
   En el editor, los breakpoints se pueden establecer con el menú
   contextual.  Esta funcionalidad aún está incompleta y es en cierto
   modo experimental.

Visualizador de pila
   Muestra el seguimiento de la pila de la última excepción en un
   complemento de árbol, con acceso a locales y globales.

Auto-abrir visualizador de pila
   Activa/desactiva automáticamente el visualizador de pila en una
   excepción no controlada.

### Menú de opciones (Shell y editor)

Configurar IDLE
   Abre un cuadro de diálogo de configuración y cambia las
   preferencias por lo siguiente: fuentes, indentación, combinaciones
   de teclas, temas de color de texto, ventanas y tamaño de inicio,
   fuentes de ayuda adicionales y extensiones.  En macOS, abre el
   cuadro de diálogo de configuración seleccionando Preferencias en el
   menú de la aplicación. Para obtener más detalles, consultar
   Configurar preferencias en Ayuda y preferencias.

La mayoría de los ajustes de configuración se aplican a todas las
ventanas, abiertas o no. Los siguientes elementos de opción se aplican
solo a la ventana activa.

Mostrar/Ocultar el contexto del código (solo ventana del Editor)
   Abre un panel en la parte superior de la ventana de edición el cual
   muestra el contexto de bloque de código que se ha desplazado sobre
   la parte superior de la ventana.  Consultar Contexto de código en
   la sección Edición y Navegación a continuación.

Mostrar/Ocultar números de línea (solo ventana del Editor)
   Abre una columna a la izquierda de la ventana de edición que
   muestra el número de cada línea de texto.  El valor por defecto de
   esta característica es desactivado, este puede modificarse en las
   preferencias (consultar Configuración de preferencias).

Ampliar/Restaurar altura
   Alterna la ventana entre el tamaño normal y la altura máxima. El
   tamaño inicial predeterminado es 40 líneas por 80 caracteres a
   menos que se cambie en la pestaña General del cuadro de diálogo
   Configurar IDLE.  La altura máxima para una pantalla es determinada
   maximizando momentáneamente una ventana la primera vez que se
   acerca la pantalla. Cambiar la configuración de la pantalla puede
   invalidar la altura guardada.  Este alternado no tiene efecto
   cuando se maximiza una ventana.

### Menú de ventana (shell y editor)

Enumera los nombres de todas las ventanas abiertas; seleccione uno
para ponerlo en primer plano (deiconificándolo si es necesario).

### Menú de ayuda (shell y editor)

Acerca de IDLE
   Muestra la versión, derechos de autor, licencia, créditos y más.

Ayuda de IDLE
   Muestra este documento IDLE, que detalla las opciones del menú,
   edición y navegación básica y otros consejos.

Documentación de Python
   Accede a la documentación local de Python, si está instalada, o
   inicia un navegador web y abre docs.python.org mostrando la última
   documentación de Python.

Demostración Turtle
   Ejecuta el módulo turtledemo con ejemplos de código Python y
   dibujos de tortugas.

Se pueden agregar fuentes de ayuda adicionales aquí con el cuadro de
diálogo Configurar IDLE en la pestaña General. Consultar la subsección
Fuentes de ayuda a continuación para obtener más información sobre las
opciones del menú Ayuda.

### Menús contextuales

Se abre un menú contextual haciendo click derecho en una ventana
(Control-click en macOS). Los menús contextuales tienen las funciones
estándar del portapapeles también en el menú Editar.

Cortar
   Copia la selección en el portapapeles global; después elimina la
   selección.

Copiar
   Copia la selección en el portapapeles global.

Pegar
   Inserta el contenido del portapapeles global en la ventana actual.

Las ventanas del editor también tienen funciones de breakpoint.  Las
líneas con un conjunto de breakpoints están especialmente marcadas.
Los breakpoints solo tienen efecto cuando se ejecutan bajo el
depurador.  Los breakpoints para un archivo se guardan en el
directorio ".idlerc" del usuario.

Establecer breakpoint
   Establecer un breakpoint en la línea actual.

Eliminar breakpoint
   Eliminar el breakpoint en esa línea.

Las ventanas de shell y de salida también tienen los siguientes
elementos.

Ir a archivo/línea
   Hace lo mismo que el menú depurar.

La ventana de shell también tiene una función de *squeezing* de salida
explicada en la subsección *ventana de shell de Python* a
continuación.

Exprimir
   Si el cursor está sobre una línea de salida, comprime toda la
   salida entre el código de arriba y el mensaje de abajo hasta la
   etiqueta 'Texto *squeezed*'.

## Edición y navegación

### Ventana del editor

IDLE puede abrir ventanas del editor cuando se inicia, dependiendo de
la configuración y de cómo inicies el IDLE.  A partir de ahí, usar el
menú Archivo.  Solo puede haber una ventana de editor abierta para un
archivo determinado.

La barra de título contiene el nombre del archivo, la ruta completa y
la versión de Python e IDLE que ejecuta la ventana.  La barra de
estado contiene el número de línea ('Ln') y el número de columna
('Col').  Los números de línea comienzan con 1; los números de columna
con 0.

El IDLE supone que los archivos con una extensión .py* conocida
contienen código Python y que los otros archivos no. Ejecuta el código
Python con el menú Ejecutar.

### Atajos de teclado

The IDLE insertion cursor is a thin vertical bar between character
positions.  When characters are entered, the insertion cursor and
everything to its right moves right one character and the new
character is entered in the new space.

Several non-character keys move the cursor and possibly delete
characters.  Deletion does not puts text on the clipboard, but IDLE
has an undo list.  Wherever this doc discusses keys, 'C' refers to the
"Control" key on Windows and Unix and the "Command" key on macOS.
(And all such discussions assume that the keys have not been re-bound
to something else.)

* Arrow keys move the cursor one character or line.

* "C"-"LeftArrow" and "C"-"RightArrow" moves left or right one word.

* "Home" and "End" go to the beginning or end of the line.

* "Page Up" and "Page Down" go up or down one screen.

* "C"-"Home" and "C"-"End" go to beginning or end of the file.

* "Backspace" and "Del" (or "C"-"d") delete the previous or next
  character.

* "C"-"Backspace" and "C"-"Del" delete one word left or right.

* "C"-"k" deletes ('kills') everything to the right.

Las combinaciones de teclas estándar (como "C"-"c" para copiar y
"C"-"v" para pegar) pueden funcionar. Las combinaciones de teclas se
seleccionan en el cuadro de diálogo Configurar IDLE.

### Indentación automática

Después de una declaración de apertura de bloque, la siguiente línea
está indentada por 4 espacios (en la ventana del shell de Python por
un tab).  Después de ciertas palabras clave (saltar, retornar, etc.),
la siguiente línea se deindenta.  En la indentación principal,
"Backspace" elimina hasta 4 espacios si están allí. "Tab" inserta
espacios (en la ventana del shell de Python un tab), el número depende
del tamaño de la indentación. Actualmente, los tabs están restringidos
a cuatro espacios debido a las limitaciones de Tcl/Tk.

Consulte también los comandos de zona de indexación/deindentación en
Menú de formato.

### Buscar y reemplazar

Cualquier selección se convierte en un objetivo de búsqueda. Sin
embargo, solo funcionan las selecciones dentro de una línea porque las
búsquedas solo se realizan dentro de las líneas con la nueva línea de
terminal eliminada. Si se marca la "[x] Expresión regular", el
objetivo se interpreta de acuerdo al módulo *re* de Python.

### Terminaciones

Cuando se solicitan y están disponibles, se suministran complementos
para los nombres de los módulos, los atributos de las clases o las
funciones, o los nombres de los archivos.  Cada método de solicitud
muestra un cuadro para completar con los nombres existentes.  (Para
cualquier cuadro, cambie el nombre que se está completando y el
elemento resaltado en el cuadro escribiendo y borrando caracteres;
pulsando las teclas "Up", "Down", "PageUp", "PageDown", "Home", y
"End"; y con un solo clic dentro del cuadro.  Cierra la caja con las
teclas "Escape", "Enter" y doble "Tab" o con clics fuera de la caja.
Un doble clic dentro de la caja selecciona y cierra.

Una forma de abrir una caja es escribir un carácter clave y esperar un
intervalo predefinido.  Este intervalo es por defecto de 2 segundos;
se puede modificar en el diálogo de configuración.  (Para evitar las
ventanas emergentes automáticas, establezca el retardo a un número
grande de milisegundos, como 100000000). Para nombres de módulos
importados o atributos de clases o funciones, escriba '.'. Para
nombres de archivos en el directorio raíz, escriba "os.sep" o
"os.altsep" inmediatamente después de una comilla de apertura.  (En
Windows, se puede especificar una unidad de disco primero.) Muévase a
los subdirectorios escribiendo un nombre de directorio y un separador.

En lugar de esperar, o después de cerrar una caja, abra una caja de
finalización inmediatamente con Mostrar finalizaciones en el menú
Edición.  La tecla rápida por defecto es "C"-"espacio".  Si se teclea
un prefijo para el nombre deseado antes de abrir el cuadro, la primera
coincidencia o casi coincidencia se hace visible. El resultado es el
mismo que si se introduce un prefijo después de mostrar la caja.
Mostrar las terminaciones después de una cita completa de los nombres
de archivo en el directorio actual en lugar de un directorio raíz.

Pulsar "Tab" después de un prefijo suele tener el mismo efecto que el
de mostrar las terminaciones.  (Sin prefijo, se indenta.) Sin embargo,
si solo hay una coincidencia con el prefijo, esa coincidencia se añade
inmediatamente al texto del editor sin abrir una caja.

Al invocar 'Mostrar las terminaciones', o al pulsar "Tab" después de
un prefijo, fuera de una cadena y sin un '.' precedente, se abre un
cuadro con las palabras clave, los nombres incorporados y los nombres
disponibles a nivel de módulo.

Cuando se edita el código en un editor (a diferencia de Shell),
aumentar los nombres disponibles a nivel de módulo mediante la
ejecución de su código y no reiniciar el Shell después.  Esto es
especialmente útil después de añadir importaciones en la parte
superior de un archivo.  Esto también aumenta las posibles
terminaciones de atributos.

Los cuadros de  excluyen inicialmente los valores que empiezan por '_'
o, en el caso de los módulos, no incluidos en '__all__'.  Se puede
acceder a los nombres ocultos escribiendo '_' después de '.', ya sea
antes o después de abrir la caja.

### Sugerencias de llamada

Se muestra una sugerencia de llamada cuando se escribe "(" después del
nombre de una función *accesible*.  Una expresión de nombre puede
incluir puntos y subíndices.  Una sugerencia permanece hasta que se
hace click, el cursor se mueve fuera del área de argumento o es
escrito ")".  Cada vez que el cursor está en la parte del argumento de
una definición, el menú o acceso directo muestra una sugerencia de
llamada.

La sugerencia de llamada consiste en la firma de la función y el
docstring hasta la primera línea en blanco de este último o la quinta
línea no en blanco.  (Algunas funciones incorporadas carecen de una
firma accesible.) Un '/' o '*' en la firma indica que los argumentos
anteriores o posteriores se pasan solo por posición o por nombre
(palabra clave).  Los detalles están sujetos a cambios.

En Shell, las funciones accesibles dependen de los módulos que se
hayan importado en el proceso del usuario, incluidos los importados
por el propio Idle, y de las definiciones que se hayan ejecutado, todo
ello desde el último reinicio.

Por ejemplo, reinicie el Shell e ingrese "itertools.count(".  Una
sugerencia de llamada aparece porque el Idle importa itertools en el
proceso del usuario para su propio uso. (Esto puede cambiar.)  Al
ingresar "turtle.write(" nada aparece.  El Idle no importa turtle.  El
menú o el acceso directo tampoco hace nada.  Al ingresar "import
turtle" y luego "turtle.write(" funcionará.

En un editor, las declaraciones de importación no tienen efecto hasta
que se ejecuta el archivo.  Es posible que desee ejecutar un archivo
después de escribir las declaraciones de importación en la parte
superior o ejecutar inmediatamente un archivo existente antes de
editarlo.

### Format block

Reformat Paragraph rewraps a block ('paragraph') of contiguous equally
indented non-blank comments, a similar block of text within a
multiline string, or a selected subset of either. If needed, add a
blank line to separate string from code. Partial lines in a selection
expand to complete lines. The resulting lines have the same indent as
before but have maximum total length of N columns (characters). Change
the default N of 72 on the Window tab of IDLE Settings.

### Contexto del código

Dentro de una ventana del editor que contiene código Python, el
contexto del código se puede alternar para mostrar u ocultar un panel
en la parte superior de la ventana.  Cuando se muestra, este panel
congela las líneas de apertura por bloques de código, como aquellos
que comienzan con las palabras clave "class", "def", o "if", que de
otro modo se habrían desplazado fuera de la vista.  El tamaño del
panel se expandirá y contraerá según sea necesario para mostrar todos
los niveles actuales de contexto, hasta el número máximo de líneas
definidas en el cuadro de diálogo Configurar IDLE (que por defecto es
15).  Si no hay líneas de contexto actuales y la función está
activada, se visualizará una sola línea en blanco.  Al hacer click en
una línea en el panel de contexto, esa línea se moverá a la parte
superior del editor.

El texto y los colores de fondo para el panel de contexto se pueden
configurar en la pestaña destacados en el cuadro de diálogo Configurar
IDLE.

### Ventana de Shell

Con el Shell del IDLE, se ingresa, edita y recupera declaraciones
completas. (La mayoría de consolas y terminales solo funcionan con una
sola línea física a la vez).

Envía una declaración de una sola línea para su ejecución al presionar
"Return" con el cursor en cualquier parte de la línea. Si una línea se
extiende con una barra invertida ("\"), el cursor debe estar en la
última línea física. Envía una declaración compuesta de varias líneas
al ingresar una línea vacía después de la declaración.

Cuando se pega código en el Shell, este no se compila y posiblemente
se ejecuta hasta que se teclea "Return", como se especifica arriba. Se
puede editar el código pegado primero. Si se pega más de una
declaración en el Shell, el resultado será un "SyntaxError" cuando se
compilan varias declaraciones como si fueran una sola.

Las líneas que contienen "RESTART" significan que el proceso de
ejecución del usuario se ha reiniciado. Esto ocurre cuando falla el
proceso de ejecución del usuario, solicita un reinicio en el menú del
Shell o ejecuta código en una ventana del editor.

The editing features described in previous subsections work when
entering code interactively.  IDLE's Shell window also responds to the
following:

* "C"-"c" attempts to interrupt statement execution (but may fail).

* "C"-"d" closes Shell if typed at a ">>>" prompt.

* "Alt"-"p" and "Alt"-"n" ("C"-"p" and "C"-"n" on macOS) retrieve to
  the current prompt the previous or next previously entered statement
  that matches anything already typed.

* "Return" while the cursor is on any previous statement appends the
  latter to anything already typed at the prompt.

### Colores del texto

El idle por defecto es negro sobre texto blanco, pero colorea el texto
con significados especiales. Para el shell, estos son: la salida del
shell, error del shell, salida del usuario y error del usuario.  Para
el código Python, en el indicador de comandos de shell o en un editor,
estos son: palabras clave, nombres de funciones y clases incorporadas,
los siguientes nombres "class" and "def", cadenas de caracteres y
comentarios. Para cualquier ventana de texto, estos son: el cursor
(cuando está presente), el texto encontrado (cuando sea posible) y el
texto seleccionado.

IDLE también resalta las palabras claves ligeras "match", "case", y
"_" en sentencias de patrones coincidentes. Sin embargo, este
resaltado no es perfecto y será incorrecto en algunos raras ocasiones,
incluyendo algunos "_"-s en patrones "case".

La coloración del texto se realiza en segundo plano, por lo que
ocasionalmente se puede ver el texto sin colorear.  Para cambiar la
combinación de colores, use la pestaña Resaltar en el cuadro de
diálogo Configurar IDLE.  El marcado de líneas de breakpoint del
depurador en el editor y el texto en ventanas emergentes y cuadros de
diálogo no es configurable por el usuario.

## Inicio y ejecución de código

Al iniciar con la opción "-s", el IDLE ejecutará el archivo al que
hacen referencia las variables de entorno  "IDLESTARTUP" o
"PYTHONSTARTUP". El IDLE primero verifica "IDLESTARTUP"; si
"IDLESTARTUP" está presente, se ejecuta el archivo al que se hace
referencia.  Si "IDLESTARTUP" no está presente, IDLE verifica
"PYTHONSTARTUP".  Los archivos referenciados por estas variables de
entorno son lugares convenientes para almacenar funciones que son
usadas con frecuencia desde el shell del IDLE o para ejecutar
declaraciones importadas para importar módulos comunes.

Además, "Tk" también carga un archivo de inicio si este está presente.
Tenga en cuenta que el archivo Tk se carga incondicionalmente.  Este
archivo adicional es ".Idle.py" y es buscado en el directorio de
inicio del usuario.  Las declaraciones en este archivo se ejecutarán
en el espacio de nombres Tk, por lo que este archivo no es útil para
importar funciones que se utilizarán desde el shell de Python del
IDLE.

### Command-line usage

IDLE can be invoked from the command line with various options. The
general syntax is:

   python -m idlelib [options] [file ...]

The following options are available:

-c <command>

   Run the specified Python command in the shell window. For example,
   pass "-c "print('Hello, World!')"". On Windows, the outer quotes
   must be double quotes as shown.

-d

   Enable the debugger and open the shell window.

-e

   Open an editor window.

-h

   Print a help message with legal combinations of options and exit.

-i

   Open a shell window.

-r <file>

   Run the specified file in the shell window.

-s

   Run the startup file (as defined by the environment variables
   "IDLESTARTUP" or "PYTHONSTARTUP") before opening the shell window.

-t <title>

   Set the title of the shell window.

-

   Read and execute standard input in the shell window. This option
   must be the last one before any arguments.

If arguments are provided:

* If "-", "-c", or "-r" is used, all arguments are placed in
  "sys.argv[1:]", and "sys.argv[0]" is set to "''", "'-c'", or "'-r'"
  respectively. No editor window is opened, even if that is the
  default set in the *Options* dialog.

* Otherwise, arguments are treated as files to be opened for editing,
  and "sys.argv" reflects the arguments passed to IDLE itself.

### Error de inicio

El IDLE usa un socket para comunicarse entre el proceso del GUI de
IDLE y el proceso de ejecución del código de usuario.  Se debe
establecer una conexión cada vez que el Shell se inicia o reinicia.
(Esto último se indica mediante una línea divisoria que dice
'REINICIAR' (*RESTART*)). Si el proceso del usuario no se conecta al
proceso de la GUI, muestra un cuadro de error "Tk" con un mensaje de
'no se puede conectar' que dirige al usuario aquí. Y después se
detiene.

Una falla de conexión específica en sistemas Unix es el resultado de
una mala configuración de las reglas de enmascarado en algún lugar de
la configuración del sistema de red. Cuando el IDLE inicia desde la
terminal, puede verse un mensaje que comienza con **``** Invalid
host:". The valid value is ``127.0.0.1 (idlelib.rpc.LOCALHOST)``**. Se
puede diagnosticar con ``tcpconnect -irv 127.0.0.1 6543" en una
ventana de la terminal y "tcplisten <same args>" en otra.

Una causa común de falla se da cuando un archivo escrito por el
usuario tiene el mismo nombre de un módulo de biblioteca estándar,
como *random.py* y *tkinter.py*. Cuando dicho archivo se encuentra en
el mismo directorio que un archivo que está por ejecutarse, el IDLE no
puede importar el archivo stdlib.  La solución actual es cambiar el
nombre del archivo del usuario.

Aunque es menos común que en el pasado, un programa de antivirus o
firewall puede detener la conexión.  Si el programa no se puede
configurar para permitir la conexión, debe estar apagado para que
funcione el IDLE.  Es seguro permitir esta conexión interna porque no
hay datos visibles en puertos externos.  Un problema similar es una
configuración incorrecta de la red que bloquea las conexiones.

Los problemas de instalación de Python ocasionalmente detienen el
IDLE: puede darse un conflicto entre versiones o una sola instalación
puede requerir privilegios de administrador.  Si se soluciona el
conflicto o no se puede o quiere ejecutar como administrador, puede
ser más fácil desinstalar completamente Python y comenzar de nuevo.

Un proceso zombie pythonw.exe podría ser un problema.  En Windows, use
el Administrador de tareas para buscar uno y detenerlo si lo hay.  A
veces, un reinicio iniciado por un bloqueo del programa o una
interrupción del teclado (control-C) puede fallar al conectarse.
Descartar el cuadro de error o usar Reiniciar Shell en el menú del
Shell puede solucionar un problema temporal.

Cuando el IDLE se inicia por primera vez, intenta leer los archivos de
configuración de usuario en "~/.idlerc/" (~ este es el directorio
principal).  Si hay un problema, se mostrará un mensaje de error.
Dejando de lado los fallos aleatorios del disco, esto se puede evitar
si nunca se editan los archivos a mano.  En su lugar, utilice el
cuadro de diálogo de configuración, en Opciones.  Una vez que hay un
error en un archivo de configuración de usuario, la mejor solución
puede ser eliminarlo y empezar de nuevo con el cuadro de diálogo de
configuración.

Si el IDLE se cierra sin mensaje y este no fue iniciado desde una
consola, intente iniciarlo desde una consola o terminal ("python -m
idlelib") y observe si esto genera un mensaje de error.

En sistemas basados en Unix con tcl/tk más antiguos que "8.6.11" (ver
"About IDLE") ciertos caracteres de ciertas fuentes pueden causar un
fallo a tk con un mensaje hacia la terminal. Esto puede pasar cuando
se inicia el IDLE para editar un archivo con dicho carácter o luego
cuando se ingresa ese carácter. Si no se puede actualizar tcl/tk,
entonces re configurar el IDLE para usar una fuente que funcione
mejor.

### Ejecutando código del usuario

Con raras excepciones, el resultado de ejecutar el código de Python
con el IDLE se supone es el mismo que al ejecutar el mismo código por
el método predeterminado, directamente con Python en una consola de
sistema en modo de texto o una ventana de terminal. Sin embargo, las
diferentes interfaces y operaciones ocasionalmente afectan los
resultados visibles.  Por ejemplo, "sys.modules" comienza con más
entradas y "threading.activeCount()" retorna 2 en lugar de 1.

De forma predeterminada, el IDLE ejecuta el código de usuario en un
proceso separado del sistema operativo en lugar de hacerlo en el
proceso de la interfaz de usuario que ejecuta el shell y el editor.
En el proceso de ejecución, este reemplaza "sys.stdin", "sys.stdout",
y "sys.stderr" con objetos que recuperan las entradas desde y envían
las salidas hacia la ventana de la consola. Los valores originales
almacenados en "sys.__stdin__", "sys.__stdout__", y "sys.__stderr__"
no se ven afectados, pero pueden ser "None".

El envío de la salida de impresión de un proceso a un widget de texto
en otro es más lento que la impresión a un terminal del sistema en el
mismo proceso. Esto tiene el mayor efecto cuando se imprimen múltiples
argumentos, ya que la cadena de cada argumento, cada separador y la
nueva línea se envían por separado. Para el desarrollo, esto no suele
ser un problema, pero si uno quiere imprimir más rápido en IDLE,
formatea y une todo lo que quiere mostrar junto y luego imprime una
sola cadena.  Tanto las cadenas de formato como "str.join()" pueden
ayudar a combinar campos y líneas.

Las sustituciones de flujo estándar del IDLE no son heredadas por
subprocesos creados en el proceso de ejecución, siendo directamente
por código de usuario o por módulos como el multiprocesamiento.  Si
tal subproceso usa "input" desde sys.stdin o "print" o "write" hacia
sys.stdout o sys.stderr, el IDLE debe ser iniciado en una ventana de
línea de comando. (En Windows, utilice "python" o "py" en lugar de
"pythonw" o "pyw".) El subproceso secundario será adjuntado a esa
ventana para entrada y salida.

Si "sys" es restablecido mediante un código de usuario, tal como
"importlib.reload(sys)", los cambios del IDLE se perderán y la entrada
del teclado y la salida de la pantalla no funcionarán correctamente.

Cuando el shell está en primer plano, controla el teclado y la
pantalla.  Este es transparente normalmente, pero las funciones que
acceden directamente al teclado y la pantalla no funcionarán.  Estas
incluyen funciones específicas del sistema que determinan si se ha
presionado una tecla y de ser así, cuál.

La ejecución de código del IDLE en el proceso de ejecución agrega
marcos a la pila de llamadas que de otro modo no estarían allí.  el
IDLE encapsula "sys.getrecursionlimit" y "sys.setrecursionlimit" para
reducir el efecto de los marcos de pila adicionales.

Cuando el código de usuario genera SystemExit directamente o llamando
a sys.exit, el IDLE regresa al visualizador del Shell en lugar de
salir.

### Salida del usuario en consola

Cuando un programa muestra texto, el resultado está determinado por el
dispositivo de salida correspondiente.  Cuando el IDLE ejecuta el
código de usuario "sys.stdout" y "sys.stderr" se conectan al área de
visualización del Shell del IDLE.  Algunas de estas características
son heredadas de los widgets de texto Tk subyacentes.  Otras son
adiciones programadas.  Donde es importante, el shell está diseñado
para el desarrollo en lugar de la ejecución de producción.

Por ejemplo, el Shell nunca elimina la salida. Un programa que envía
salidas ilimitadas al Shell eventualmente llenará la memoria, lo que
resultará en un error de memoria. Por el contrario, algunas ventanas
de texto del sistema solo conservan las últimas n líneas de salida.
Una consola de Windows, por ejemplo, mantiene una línea configurable
por el usuario de 1 a 9999, con 300 por defecto.

Un widget de texto de Tk, y por lo tanto el Shell de IDLE, muestra
caracteres (puntos de código) en el subconjunto BMP (plano
multilingual básico) de Unicode.  Aquellos caracteres que se muestran
con un glifo adecuado y los cuales con una caja de reemplazo depende
del sistema operativo y las fuentes instaladas.  Los caracteres de
tabulación hacen que el texto siguiente comience después de la
siguiente tabulación. (Ocurre cada 8 'caracteres').  Los caracteres de
nueva línea hacen que el texto siguiente aparezca en una nueva línea.
Otros caracteres de control se omiten o se muestran como un espacio,
cuadro u otra cosa, dependiendo del sistema operativo y la fuente.
(Mover el cursor del texto a través de esa salida con las teclas de
flecha puede mostrar algún comportamiento de espaciado sorpresivo.)

   >>> s = 'a\tb\a<\x02><\r>\bc\nd'  # Enter 22 chars.
   >>> len(s)
   14
   >>> s  # Display repr(s)
   'a\tb\x07<\x02><\r>\x08c\nd'
   >>> print(s, end='')  # Display s as is.
   # Result varies by OS and font.  Try it.

La función "repr" es usada para la visualización interactiva del valor
de las expresiones.  Esta retorna una versión modificada de la cadena
de caracteres de entrada en la que los códigos de control, algunos
puntos de código BMP y todos los puntos de código que no son BMP son
reemplazados con caracteres de escape. Como se demostró anteriormente,
esto permite identificar los caracteres en una cadena de caracteres,
independientemente de cómo sean mostrados.

La salida normal y de error generalmente se mantienen separadas (en
líneas separadas) de la entrada de código y entre sí. Cada una obtiene
diferentes colores de resaltado.

Para el *traceback* de SyntaxError, el marcado normal '^' dónde se
detectó el error se reemplaza coloreando el texto con un resaltado de
error. Cuando el código ejecutado desde un archivo causa otras
excepciones, se puede hacer click derecho en un *traceback* para
saltar a la línea correspondiente en un editor del IDLE. El archivo se
abrirá si es necesario.

El Shell tiene una funcionalidad especial para exprimir las líneas de
salida hasta una etiqueta de 'Texto *Squeezed*'.  Esto se hace
automáticamente para una salida sobre N líneas (N = 50 por defecto). N
se puede cambiar en la sección PyShell de la página General del cuadro
de diálogo Configuración.  La salida con menos líneas puede ser
*squeezed* haciendo click derecho en la salida.  Esto puede ser útil
en líneas suficientemente largas para bajar el tiempo de
desplazamiento.

La salida *squeezed* se expande en su lugar haciendo doble click en la
etiqueta. También se puede enviar al portapapeles o a una ventana de
vista separada haciendo click derecho en la etiqueta.

### Desarrollando aplicaciones tkinter

El IDLE es intencionalmente diferente de Python estándar para
facilitar el desarrollo de programas tkinter.  Ingrese "import tkinter
as tk; root = tk.Tk()" en Python estándar y no aparecerá nada. Ingrese
lo mismo en el IDLE y aparecerá una ventana tk.  En Python estándar,
también se debe ingresar "root.update()" para ver la ventana.  El IDLE
hace el equivalente en segundo plano, aproximadamente 20 veces por
segundo, lo que es aproximadamente cada 50 milisegundos. Luego ingrese
"b = tk.Button(root, text='button'); b.pack()".  Del mismo modo, no
hay cambios visibles en Python estándar hasta que ingrese
"root.update()".

La mayoría de los programas tkinter ejecutan "root.mainloop()", que
generalmente no retorna hasta que se destruye la aplicación tk.  Si el
programa se ejecuta con "python -i" o desde un editor del IDLE, no
aparecerá un mensaje ">>>" del shell hasta que retorne "mainloop()",
momento en el cual no queda nada con lo que interactuar.

Al ejecutar un programa tkinter desde un editor IDLE, se puede
comentar la llamada de bucle principal.  Luego se recibe un aviso del
shell inmediatamente y se puede interactuar con la aplicación en vivo.
Solo se debe recordar reactivar la llamada al bucle principal cuando
se ejecuta en Python estándar.

### Ejecutando sin un subproceso

Por defecto, el IDLE ejecuta el código de usuario en un subproceso
separado a través de un socket, el cual utiliza la interfaz de bucle
interno.  Esta conexión no es visible externamente y no son enviados
ni recibidos datos de Internet. Si el software de cortafuego sigue
presentando problemas, puede ignorarlo.

Si el intento de conexión del socket falla, IDLE lo notificará. Este
tipo de falla a veces es temporal, pero si persiste, el problema puede
provenir de un cortafuego que bloquea la conexión o de una mala
configuración en un sistema en particular.  Hasta que se solucione el
problema, se puede ejecutar el Idle con el modificador de línea de
comandos -n.

Si el IDLE se inicia con el modificador de línea de comandos -n, se
ejecutará en un único proceso y no creará el subproceso que ejecuta el
servidor de ejecución de Python RPC.  Esto puede ser útil si Python no
puede crear el subproceso o la interfaz de socket RPC en su
plataforma.  Sin embargo, en este modo el código de usuario no está
aislado en sí del IDLE.  Además, el entorno no se reinicia cuando se
selecciona Ejecutar/Ejecutar módulo (F5).  Si el código se ha
modificado, se debe volver a cargar() los módulos afectados y volver a
importar cualquier elemento específico (por ejemplo, desde *foo*
importar *baz*) para que los cambios surtan efecto.  Por estas
razones, es preferible ejecutar el IDLE con el subproceso
predeterminado si es posible.

Obsoleto desde la versión 3.4.

## Ayuda y preferencias

### Recursos de ayuda

La entrada del menú Ayuda "Ayuda IDLE" muestra una versión HTML
formateada del capítulo IDLE de la Referencia de la biblioteca.  El
resultado, en una ventana de texto tkinter de solo lectura, está cerca
de lo que se ve en un navegador web. Navegue por el texto con la rueda
del ratón, la barra de desplazamiento o presionando las teclas de
flecha arriba y abajo. O haga click en el botón TDC (Tabla de
contenido) y seleccione un encabezado de sección en el cuadro abierto.

La entrada del menú de ayuda "Documentos de Python" abre amplias
fuentes de ayuda, incluyendo tutoriales, disponibles en
"docs.python.org/x.y", donde 'x.y' es la versión de Python actualmente
en ejecución.  Si su sistema tiene una copia fuera de línea de los
documentos (esta puede ser una opción de instalación), esta se abrirá
en su lugar.

Las URL seleccionadas se pueden agregar o eliminar del menú de ayuda
en cualquier momento utilizando la pestaña General del cuadro de
diálogo Configurar IDLE.

### Preferencias de configuración

Las preferencias de fuente, resaltado, teclas y preferencias generales
se pueden cambiar en Configurar IDLE en el menú opción. Las
configuraciones de usuario no predeterminadas se guardan en un
directorio ".idlerc" en el directorio de inicio del usuario.  Los
problemas causados por archivos de configuración de usuario
incorrectos se resuelven editando o eliminando uno o más de los
archivos en ".idlerc".

En la pestaña Fuentes (*Font*), consulte la muestra de texto para ver
el efecto de la fuente y el tamaño de la fuente en varios caracteres
en varios idiomas.  Edite la muestra para agregar otros caracteres de
interés personal.  Use la muestra para seleccionar fuentes
monoespaciadas.  Si determinados caracteres tienen problemas en el
shell o en el editor, agréguelos a la parte inicial de la muestra e
intente cambiar primero el tamaño y luego la fuente.

En la pestaña Resaltado y Teclas (*Highlights and Keys*), seleccione
un tema de color integrado o personalizado y un conjunto de teclas.
Para utilizar un nuevo tema de color integrado o un conjunto de teclas
con IDLE más antiguos, guárdelo como un nuevo tema personalizado o
conjunto de teclas y será accesible para los IDLE más antiguos.

### IDLE en macOS

En Preferencias del sistema: Dock, puede establecer "Preferencias de
pestañas al abrir documentos" en el valor "Siempre".  Este parámetro
no es compatible con la interfaz gráfica de usuario del framework
tk/tkinter utilizado por IDLE y rompe algunas funcionalidades del
IDLE.

### Extensiones

IDLE incluye una herramienta de extensiones.  Las preferencias para
las extensiones se pueden cambiar con la pestaña Extensiones de la
ventana de preferencias. Lea el inicio de config-extensions.def en la
carpeta idlelib para obtener más información.  La única extensión
utilizada actualmente por defecto es zzdummy, un ejemplo que también
se utiliza para realizar pruebas.

## idlelib --- implementation of IDLE application

**Código fuente:** Lib/idlelib

======================================================================

El paquete Lib/idlelib implementa la aplicación del IDLE. Consultar el
resto de esta página para saber cómo utilizar el IDLE.

Los archivos en idlelib se describen en idlelib/README.txt. Accede a
él en idlelib o haga clic en Ayuda => Acerca del IDLE en el menú del
IDLE. Este archivo también asigna elementos del menú del IDLE al
código que implementa el elemento. Excepto para archivos enumerados en
'Inicio', el código de idlelib es 'privado' en el sentido de que los
cambios de características pueden ser portados (consultar **PEP
434**).
