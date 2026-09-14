---
title: '"tkinter.scrolledtext" --- Scrolled text widget'
source_url: https://docs.python.org/es/3
source_path: library/tkinter.scrolledtext.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4220
---

# "tkinter.scrolledtext" --- Scrolled text widget

**Código fuente:** Lib/tkinter/scrolledtext.py

======================================================================

The "tkinter.scrolledtext" module provides a class of the same name
which implements a basic text widget which has a vertical scroll bar
configured to do the "right thing."  Using the "ScrolledText" class is
a lot easier than setting up a text widget and scroll bar directly.

The text widget and scrollbar are packed together in a "Frame", and
the methods of the "Pack", "Grid" and "Place" geometry managers are
acquired from the "Frame" object. This allows the "ScrolledText"
widget to be used directly to achieve most normal geometry management
behavior.

Si fuera necesario un control más específico, los siguientes atributos
están disponibles:

class tkinter.scrolledtext.ScrolledText(master=None, **kw)

   frame

      El marco que rodea el texto y los widgets de la barra de
      desplazamiento.

   vbar

      El widget de la barra de desplazamiento.
