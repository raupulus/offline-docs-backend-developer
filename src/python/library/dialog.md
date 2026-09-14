---
title: Tkinter dialogs
source_url: https://docs.python.org/es/3
source_path: library/dialog.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2320
---

# Tkinter dialogs

## "tkinter.simpledialog" --- Standard Tkinter input dialogs

**Código fuente:** Lib/tkinter/simpledialog.py

======================================================================

The "tkinter.simpledialog" module contains convenience classes and
functions for creating simple modal dialogs to get a value from the
user.

tkinter.simpledialog.askfloat(title, prompt, *, initialvalue=None, minvalue=None, maxvalue=None, parent=None)
tkinter.simpledialog.askinteger(title, prompt, *, initialvalue=None, minvalue=None, maxvalue=None, parent=None)
tkinter.simpledialog.askstring(title, prompt, *, initialvalue=None, show=None, parent=None)

   Prompt the user to enter a value of the desired type and return it,
   or "None" if the dialog is cancelled.

   *title* is the dialog title and *prompt* the message shown above
   the entry. *initialvalue* is the value initially placed in the
   entry. *parent* is the window over which the dialog is shown.
   "askinteger()" and "askfloat()" also accept *minvalue* and
   *maxvalue*, which bound the accepted value. "askstring()" also
   accepts *show*, a character used to mask the entered text, for
   example "'*'" to hide a password.

class tkinter.simpledialog.Dialog(parent, title=None)

   The base class for custom dialogs. Instantiating it shows the
   dialog modally and returns once the user closes it; the entered
   value is then available in the "result" attribute.

   result

      The value produced by "apply()", or "None" if the dialog was
      cancelled.

   body(master)

      Sobrescribir para construir la interfaz del dialogo y retornar
      el widget que debe tener el foco inicial.

   buttonbox()

      El comportamiento por defecto añade los botones OK y Cancelar.
      Sobrescribir para diseños de botones personalizados.

   validate()

      Validate the data entered by the user. Return true if it is
      valid, in which case the dialog proceeds to "apply()"; return
      false to keep the dialog open. The default implementation always
      returns true; override it to check the input.

   apply()

      Process the data entered by the user, for example by storing it
      in the "result" attribute. Called after "validate()" succeeds
      and just before the dialog is destroyed. The default
      implementation does nothing; override it to act on or store the
      result.

   destroy()

      Destroy the dialog window, clearing the reference to the widget
      that had the initial focus.

class tkinter.simpledialog.SimpleDialog(master, text='', buttons=[], default=None, cancel=None, title=None, class_=None)

   A simple modal dialog that displays the message *text* above a row
   of push buttons whose labels are given by *buttons*, and returns
   the index of the button the user presses. *default* is the index of
   the button activated by the Return key, *cancel* the index returned
   when the window is closed through the window manager, *title* the
   window title, and *class_* the Tk class name of the window.

   go()

      Display the dialog, wait until the user presses a button or
      closes the window, and return the index of the chosen button.

## "tkinter.filedialog" --- File selection dialogs

**Código fuente:** Lib/tkinter/filedialog.py

======================================================================

The "tkinter.filedialog" module provides classes and factory functions
for creating file/directory selection windows.

### Native load/save dialogs

Las siguientes clases y funciones proporcionan ventanas de diálogo de
archivos que combinan un aspecto nativo con opciones de configuración
para personalizar el comportamiento. Los siguientes argumentos son
aplicables a las clases y funciones enumeradas a continuación:

      *parent* - la ventana sobre la que se situará el diálogo

      *title* - el título de la ventana

      *initialdir* - el directorio en el que inicia el diálogo

      *initialfile* - el archivo seleccionado al abrir el diálogo

      *filetypes* - una secuencia de tuplas (label, pattern), se permite el comodín '*'

      *defaultextension* - extensión por defecto para añadir al archivo (diálogos de guardado)

      *multiple* - cuando es verdadero, se permite la selección de múltiples elementos

**Funciones estáticas de factoría**

The below functions when called create a modal, native look-and-feel
dialog, wait for the user's selection, and return it. The exact return
value depends on the function (see below); when the dialog is
cancelled it is an empty string, an empty tuple or "None". The precise
type of this empty value may vary between platforms and Tk versions,
so test the result for truth rather than comparing it with a specific
value.

tkinter.filedialog.askopenfile(mode='r', **options)
tkinter.filedialog.askopenfiles(mode='r', **options)

   Create an "Open" dialog. "askopenfile()" returns the opened file
   object, or "None" if the dialog is cancelled. "askopenfiles()"
   returns a list of the opened file objects, or an empty tuple if
   cancelled. The files are opened in mode *mode* (read-only "'r'" by
   default).

tkinter.filedialog.asksaveasfile(mode='w', **options)

   Create a "SaveAs" dialog and return the opened file object, or
   "None" if the dialog is cancelled. The file is opened in mode
   *mode* ("'w'" by default).

tkinter.filedialog.askopenfilename(**options)
tkinter.filedialog.askopenfilenames(**options)

   Create an "Open" dialog. "askopenfilename()" returns the selected
   filename as a string, or an empty string if the dialog is
   cancelled. "askopenfilenames()" returns a tuple of the selected
   filenames, or an empty tuple if cancelled.

tkinter.filedialog.asksaveasfilename(**options)

   Create a "SaveAs" dialog and return the selected filename as a
   string, or an empty string if the dialog is cancelled.

tkinter.filedialog.askdirectory(**options)

   Prompt the user to select a directory, and return its path as a
   string, or an empty string if the dialog is cancelled. Additional
   keyword option: *mustexist* - if true, the user may only select an
   existing directory (false by default).

class tkinter.filedialog.Open(master=None, **options)
class tkinter.filedialog.SaveAs(master=None, **options)
class tkinter.filedialog.Directory(master=None, **options)

   The above three classes provide native dialog windows for loading
   and saving files and for selecting a directory.

**Clases de conveniencia**

Las siguientes clases se utilizan para crear ventanas de
archivos/directorios desde cero. Estas no emulan el aspecto nativo de
la plataforma.

Nota:

  La clase *FileDialog* debe ser subclasificada para el manejo de
  eventos y comportamiento personalizados.

class tkinter.filedialog.FileDialog(master, title=None)

   Crear un diálogo básico de selección de archivos.

   cancel_command(event=None)

      Activa la terminación de la ventana de diálogo.

   dirs_double_event(event)

      Manejador de eventos para el evento de doble clic sobre un
      directorio.

   dirs_select_event(event)

      Manejador de eventos para el evento de clic sobre un directorio.

   files_double_event(event)

      Manejador de eventos para el evento de doble clic sobre un
      archivo.

   files_select_event(event)

      Manejador de eventos para el evento de un solo clic sobre un
      archivo.

   filter_command(event=None)

      Filtra los archivos por directorio.

   get_filter()

      Recupera el filtro de archivos que se está utilizando
      actualmente.

   get_selection()

      Recupera el elemento seleccionado actualmente.

   go(dir_or_file=os.curdir, pattern='*', default='', key=None)

      Renderiza el diálogo e inicia el bucle de eventos.

   ok_event(event)

      Salir del diálogo retornando la selección actual.

   ok_command()

      Called when the user confirms the current selection. The base
      implementation accepts the selection and closes the dialog;
      "LoadFileDialog" and "SaveFileDialog" override it to check the
      selection first.

   quit(how=None)

      Salir del diálogo retornando el nombre del archivo, si lo hay.

   set_filter(dir, pat)

      Establece el filtro de archivos.

   set_selection(file)

      Actualiza la selección de archivos actual a *archivo*.

class tkinter.filedialog.LoadFileDialog(master, title=None)

   Una subclase de FileDialog que crea una ventana de diálogo para
   seleccionar un archivo existente.

   ok_command()

      Comprueba que se proporciona un archivo y que la selección
      indica un archivo ya existente.

class tkinter.filedialog.SaveFileDialog(master, title=None)

   Una subclase de FileDialog que crea una ventana de diálogo para
   seleccionar un archivo de destino.

   ok_command()

      Comprueba si la selección apunta a un archivo válido que no es
      un directorio. Se requiere confirmación si se selecciona un
      archivo ya existente.

## "tkinter.commondialog" --- Dialog window templates

**Código fuente:** Lib/tkinter/commondialog.py

======================================================================

The "tkinter.commondialog" module provides the "Dialog" class that is
the base class for dialogs defined in other supporting modules.

class tkinter.commondialog.Dialog(master=None, **options)

   show(**options)

      Renderiza la ventana de diálogo.

## "tkinter.dialog" --- Classic Tk dialog boxes

**Source code:** Lib/tkinter/dialog.py

======================================================================

The "tkinter.dialog" module provides a simple modal dialog box built
on the classic (non-themed) Tk widgets.

tkinter.dialog.DIALOG_ICON

   The name of a bitmap ("'questhead'") suitable for use as the
   *bitmap* of a "Dialog".

class tkinter.dialog.Dialog(master=None, cnf={}, **kw)

   Display a modal dialog box built from the classic (non-themed) Tk
   widgets and wait for the user to press one of its buttons. The
   options, given through *cnf* or as keyword arguments, are all
   required: *title* (the window title), *text* (the message),
   *bitmap* (the name of a bitmap icon, such as "DIALOG_ICON"),
   *default* (the index of the default button) and *strings* (the
   sequence of button labels). After construction, the "num" attribute
   holds the index of the button the user pressed.

   destroy()

      Do nothing. The dialog window is destroyed automatically before
      the constructor returns, so there is nothing left for this
      method to do.

Ver también:

  Módulos "tkinter.messagebox", Leyendo y escribiendo archivos
