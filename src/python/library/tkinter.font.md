---
title: '"tkinter.font" --- Tkinter font wrapper'
source_url: https://docs.python.org/es/3
source_path: library/tkinter.font.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4200
---

# "tkinter.font" --- Tkinter font wrapper

**Código fuente:** Lib/tkinter/font.py

======================================================================

The "tkinter.font" module provides the "Font" class for creating and
using named fonts.

Los diferentes pesos e inclinaciones de la fuente son:

tkinter.font.NORMAL
tkinter.font.BOLD
tkinter.font.ITALIC
tkinter.font.ROMAN

class tkinter.font.Font(root=None, font=None, name=None, exists=False, **options)

   La clase "Font" representa una fuente con nombre. Las instancias
   *Font* reciben nombres únicos y se pueden especificar por su
   configuración de familia, tamaño y estilo. Las fuentes con nombre
   son el método de Tk para crear e identificar fuentes como un solo
   objeto, en lugar de especificar una fuente por sus atributos con
   cada aparición.

   Distinto en la versión 3.10: Two fonts now compare equal ("==")
   only when both are "Font"   instances with the same name belonging
   to the same Tcl interpreter.argumentos:

         *font* - tupla de especificador de fuente (familia, tamaño, opciones)
         *name* - nombre de fuente único
         *exists* - self apunta a la fuente con nombre existente si es verdadera

   opciones de palabras clave adicionales (ignoradas si se especifica
   *font*):

         *family* - font family, for example, Courier, Times
         *size* - tamaño de fuente
            Si *size* es positivo, se interpreta como tamaño en puntos.
            Si *size* es un número negativo, se trata su valor absoluto
            como tamaño en píxeles.
         *weight* - énfasis de fuente (NORMAL, BOLD)
         *slant* - ROMAN, ITALIC
         *underline* - subrayado de fuente (0 - ninguno, 1 - subrayado)
         *overstrike* - tachado de fuente (0 - ninguno, 1 - tachado)

   actual(option=None, displayof=None)

      Return the actual attributes of the font, which may differ from
      the requested ones because of platform limitations. With no
      *option*, return a dictionary of all the attributes; if *option*
      is given, return the value of that single attribute. The
      attributes are resolved on the display of the *displayof*
      widget, or the main application window if it is not specified.

   cget(option)

      Recupera un atributo de la fuente.

   configure(**options)

      Modify one or more attributes of the font. With no arguments,
      return a dictionary of the current attributes.

      "config()" is an alias of "configure()".

   copy()

      Return a distinct copy of the current font: a new named font
      with the same attributes but a different name, which can be
      reconfigured independently of the original. If the current font
      wraps a font description, the copy is instead a named font with
      its resolved attributes.

   measure(text, displayof=None)

      Return amount of space the text would occupy on the specified
      display when formatted in the current font, as an integer number
      of pixels. If no display is specified then the main application
      window is assumed.

   metrics(*options, **kw)

      Return font-specific data. With no options, return a dictionary
      mapping each metric name to its integer value; if one option
      name is given, return that metric's value as an integer. Options
      include:

      *ascent* - distancia entre la línea de base y el punto más alto
      que un
         el carácter de la fuente puede ocupar

      *descent* - distancia entre la línea de base y el punto más bajo
      que un
         el carácter de la fuente puede ocupar

      *linespace* - separación vertical mínima necesaria entre dos
         caracteres de la fuente que aseguran que no haya
         superposición vertical entre líneas.

      *fixed* - 1 si la fuente es de ancho fijo en caso contrario 0

tkinter.font.families(root=None, displayof=None)

   Return a tuple of the names of the available font families.

tkinter.font.names(root=None)

   Return a tuple of the names of all the defined fonts.

tkinter.font.nametofont(name, root=None)

   Return a "Font" representation of the existing named font *name*.
   *root* is the widget whose Tcl interpreter owns the font; if
   omitted, the default root window is used.

   Distinto en la versión 3.10: Se agregó el parámetro *root*.
