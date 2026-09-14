---
title: '"xml.sax.saxutils" --- SAX Utilities'
source_url: https://docs.python.org/es/3
source_path: library/xml.sax.utils.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4640
---

# "xml.sax.saxutils" --- SAX Utilities

**Código fuente:** Lib/xml/sax/saxutils.py

======================================================================

The module "xml.sax.saxutils" contains a number of classes and
functions that are commonly useful when creating SAX applications,
either in direct use, or as base classes.

xml.sax.saxutils.escape(data, entities={})

   Escapar "'&'", "'<'" y "'>'" en una cadena de datos.

   Puede escapar otras cadenas de datos pasando un diccionario como el
   parámetro opcional *entities*. Las claves y los valores deben ser
   cadenas; cada clave será reemplazada por su valor correspondiente.
   Los caracteres "'&'", "'<'" y "'>'" siempre se escapan, incluso si
   se proporciona *entities*.

   Nota:

     Esta función debería ser usada únicamente para escapar caracteres
     que no pueden ser usados directamente en XML. No use esta función
     como una función general de traducción de cadenas de caracteres.

xml.sax.saxutils.unescape(data, entities={})

   Quitar el escape "'&amp;'", "'&lt;'", y "'&gt;'" en una cadena de
   datos.

   You can unescape other strings of data by passing a dictionary as
   the optional *entities* parameter.  The keys and values must all be
   strings; each key will be replaced with its corresponding value.
   "'&amp;'", "'&lt;'", and "'&gt;'" are always unescaped, even if
   *entities* is provided.

xml.sax.saxutils.quoteattr(data, entities={})

   Similar a "escape()", pero también prepara *data* para usarse como
   un valor de atributo. El valor devuelto es una versión
   entrecomillada de *data* con los reemplazos adicionales necesarios.
   "quoteattr()" seleccionará un carácter de comillas basado en el
   contenido de *data*, intentando evitar codificar los caracteres de
   comillas en la cadena. Si los caracteres de comillas simples y
   dobles ya están en *data*, los caracteres de comillas dobles se
   codificarán y *data* se envolverá entre comillas dobles. La cadena
   resultante se puede utilizar directamente como un valor de
   atributo:

      >>> print("<element attr=%s>" % quoteattr("ab ' cd \" ef"))
      <element attr="ab ' cd &quot; ef">

   Esta función es útil al generar valores de atributo para HTML o
   cualquier SGML utilizando la sintaxis concreta de referencia.

class xml.sax.saxutils.XMLGenerator(out=None, encoding='iso-8859-1', short_empty_elements=False)

   Esta clase implementa la interfaz "ContentHandler" escribiendo
   eventos SAX en un documento XML. En otras palabras, el uso de un
   "XMLGenerator" como controlador de contenido reproducirá el
   documento original que se está analizando. *out* debe ser un objeto
   similar a un archivo que por defecto sea *sys.stdout*. *encoding*
   es la codificación de la secuencia de salida que tiene como valor
   predeterminado "'iso-8859-1'". *short_empty_elements* controla el
   formato de los elementos que no contienen contenido: si "False"
   (valor predeterminado) se emiten como un par de etiquetas de
   inicio/fin, si se establece en "True" se emiten como una sola
   etiqueta autocerrada.

   Distinto en la versión 3.2: Added the *short_empty_elements*
   parameter.

class xml.sax.saxutils.XMLFilterBase(base)

   Esta clase está diseñada para situarse entre un "XMLReader" y los
   manejadores de eventos de la aplicación cliente. Por defecto, no
   hace más que pasar las peticiones al lector y los eventos a los
   manejadores sin modificar, pero las subclases pueden sobrescribir
   métodos específicos para modificar el flujo de eventos o las
   peticiones de configuración a medida que pasan.

xml.sax.saxutils.prepare_input_source(source, base='')

   Esta función toma una fuente de entrada y, opcionalmente, una URL
   base y retorna un objeto "InputSource" completamente resuelto y
   listo para ser leído. La fuente de entrada puede ser proporcionada
   como una cadena de caracteres, un objeto tipo archivo , o un objeto
   "InputSource"; los analizadores usarán esta función para
   implementar el argumento polimórfico *source* a su método
   "parse()".
