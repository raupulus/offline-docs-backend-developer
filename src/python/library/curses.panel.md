---
title: '"curses.panel" --- A panel stack extension for curses'
source_url: https://docs.python.org/es/3
source_path: library/curses.panel.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2210
---

# "curses.panel" --- A panel stack extension for curses

======================================================================

Los paneles son ventanas con la característica de profundidad añadida,
por lo que se pueden apilar una encima de la otra, y solo se mostrarán
las partes visibles de cada ventana. Los paneles se pueden agregar,
mover hacia arriba o hacia abajo en la pila y eliminarse.

## Funciones

The module "curses.panel" defines the following exception:

exception curses.panel.error

   Exception raised when a curses panel library function returns an
   error.

The module "curses.panel" defines the following functions:

curses.panel.bottom_panel()

   Retorna el panel inferior en la pila del panel.

curses.panel.new_panel(win)

   Returns a panel object, associating it with the given window *win*
   and placing the new panel on top of the panel stack.  Be aware that
   you need to keep the returned panel object referenced explicitly.
   If you don't, the panel object is garbage collected and removed
   from the panel stack.

curses.panel.top_panel()

   Retorna el panel superior de la pila de paneles.

curses.panel.update_panels()

   Actualiza la pantalla virtual después de los cambios en la pila del
   panel. Esto no llama a "curses.doupdate()", por lo que tendrás que
   hacerlo tú mismo.

## Panel objects

class curses.panel.panel

   Panel objects, as returned by "new_panel()" above, are windows with
   a stacking order.  There's always a window associated with a panel
   which determines the content, while the panel methods are
   responsible for the window's depth in the panel stack.

   Los objetos de panel tienen los siguientes métodos:

panel.above()

   Retorna el panel situado encima del panel actual.

panel.below()

   Retorna el panel debajo del panel actual.

panel.bottom()

   Empuja el panel hasta la parte inferior de la pila.

panel.hidden()

   Retorna "True" si el panel está oculto (no visible), "False" en
   caso contrario.

panel.hide()

   Ocultar el panel. Esto no elimina el objeto, solo hace que la
   ventana en la pantalla sea invisible.

panel.move(y, x)

   Mueve el panel a las coordenadas de pantalla "(y, x)".

panel.replace(win)

   Cambia la ventana asociada con el panel a la ventana *win*.

panel.set_userptr(obj)

   Establece el puntero de usuario del panel en *obj*. Esto se usa
   para asociar un dato arbitrario con el panel y puede ser cualquier
   objeto de Python.

panel.show()

   Display the panel (which might have been hidden), placing it on top
   of the panel stack.

panel.top()

   Empuja el panel hacia la parte superior de la pila.

panel.userptr()

   Retorna el puntero del usuario para el panel. Puede ser cualquier
   objeto de Python.

panel.window()

   Retorna el objeto de ventana asociado con el panel.
