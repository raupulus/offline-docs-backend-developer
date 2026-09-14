---
title: '"tkinter.dnd" --- Drag and drop support'
source_url: https://docs.python.org/es/3
source_path: library/tkinter.dnd.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4190
---

# "tkinter.dnd" --- Drag and drop support

**Código fuente:** Lib/tkinter/dnd.py

======================================================================

Nota:

  Esto es experimental y quedará obsoleto cuando se sustituya por el
  Tk DND.

The "tkinter.dnd" module provides drag-and-drop support for objects
within a single application, within the same window or between
windows. To enable an object to be dragged, you must create an event
binding for it that starts the drag-and-drop process. Typically, you
bind a ButtonPress event to a callback function that you write (see
Bindings and events). The function should call "dnd_start()", where
*source* is the object to be dragged, and *event* is the event that
invoked the call (the argument to your callback function).

La selección de un objeto de destino ocurre de la siguiente manera:

1. Top-down search of the area under the mouse for a target widget:

   * the target widget should have a callable *dnd_accept* attribute;

   * if *dnd_accept* is not present or returns "None", the search
     moves to the parent widget;

   * if no target widget is found, the target object is "None".

2. Call to "<old_target>.dnd_leave(source, event)".

3. Call to "<new_target>.dnd_enter(source, event)".

4. Call to "<target>.dnd_commit(source, event)" to notify of the drop.

5. Call to "<source>.dnd_end(target, event)" to signal the end of
   drag-and-drop.

class tkinter.dnd.DndHandler(source, event)

   La clase *DndHandler* maneja los eventos de arrastrar y soltar que
   rastrean los eventos Motion y ButtonRelease en la raíz del widget
   de eventos.

   cancel(event=None)

      Cancela el proceso de arrastrar y soltar.

   finish(event, commit=0)

      Ejecuta el fin de las funciones de arrastrar y soltar.

   on_motion(event)

      Inspect area below mouse for target objects while a drag is
      performed.

   on_release(event)

      Señal de fin de arrastre cuando se activa el patrón de
      liberación.

tkinter.dnd.dnd_start(source, event)

   Factory function for the drag-and-drop process. Return the
   "DndHandler" instance managing the drag, or "None" if a drag could
   not be started.

Ver también: Bindings and events
