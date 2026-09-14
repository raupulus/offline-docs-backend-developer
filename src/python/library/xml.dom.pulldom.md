---
title: '"xml.dom.pulldom" --- Support for building partial DOM trees'
source_url: https://docs.python.org/es/3
source_path: library/xml.dom.pulldom.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4580
---

# "xml.dom.pulldom" --- Support for building partial DOM trees

**Source code:** Lib/xml/dom/pulldom.py

======================================================================

The "xml.dom.pulldom" module provides a "pull parser" which can also
be asked to produce DOM-accessible fragments of the document where
necessary. The basic concept involves pulling "events" from a stream
of incoming XML and processing them. In contrast to SAX which also
employs an event-driven processing model together with callbacks, the
user of a pull parser is responsible for explicitly pulling events
from the stream, looping over those events until either processing is
finished or an error condition occurs.

Nota:

  If you need to parse untrusted or unauthenticated data, see XML
  security.

Distinto en la versión 3.7.1: El analizador SAX ya no procesa
entidades externas generales de forma predeterminada para aumentar la
seguridad de forma predeterminada. Para habilitar el procesamiento de
entidades externas, pase una instancia de analizador personalizada
(*custom parser instance in::*)

   from xml.dom.pulldom import parse
   from xml.sax import make_parser
   from xml.sax.handler import feature_external_ges

   parser = make_parser()
   parser.setFeature(feature_external_ges, True)
   parse(filename, parser=parser)

Ejemplo:

   from xml.dom import pulldom

   doc = pulldom.parse('sales_items.xml')
   for event, node in doc:
       if event == pulldom.START_ELEMENT and node.tagName == 'item':
           if int(node.getAttribute('price')) > 50:
               doc.expandNode(node)
               print(node.toxml())

"event" es una constante y puede ser uno de:

* "START_ELEMENT" (Iniciar elemento)

* "END_ELEMENT" (Finalizar elemento)

* "COMMENT" (comentario)

* "START_DOCUMENT" (Iniciar documento)

* "END_DOCUMENT" (finalizar documento)

* "CHARACTERS" (caracteres)

* "PROCESSING_INSTRUCTION" (instrucción de procesamiento)

* "IGNORABLE_WHITESPACE" (Espacio en blanco que puede ignorarse)

"node" es un objeto del tipo "xml.dom.minidom.Document",
"xml.dom.minidom.Element" ó "xml.dom.minidom.Text".

Puesto que el documento se trata como una secuencia "flat" (plana) de
eventos, el documento "tree" (árbol) se atraviesa implícitamente y los
elementos deseados se encuentran independientemente de su profundidad
en el árbol. En otras palabras, no es necesario tener en cuenta
cuestiones jerárquicas como la búsqueda recursiva de los nodos de
documento, aunque si el contexto de los elementos fuera importante, es
necesario mantener algún estado relacionado con el contexto (es decir,
recordar dónde se encuentra en el documento en un momento dado) o
hacer uso del método "DOMEventStream.expandNode()" y cambiar al
procesamiento relacionado con DOM.

class xml.dom.pulldom.PullDOM(documentFactory=None)

   Subclase de "xml.sax.handler.ContentHandler".

class xml.dom.pulldom.SAX2DOM(documentFactory=None)

   Subclase de "xml.sax.handler.ContentHandler".

xml.dom.pulldom.parse(stream_or_string, parser=None, bufsize=None)

   Retorna un "DOMEventStream" de la entrada dada. *stream_or_string*
   (secuencia o cadena) puede ser un nombre de archivo o un objeto
   similar a un archivo, *parser*, si se indica, debe ser un objeto
   "XMLReader". Esta función cambiará el controlador de documentos del
   analizador y activará el soporte de espacios de nombres; otra
   configuración del analizador (como establecer un solucionador de
   entidades) debe haberse realizado de antemano.

Si tiene XML en una cadena, puede usar en su lugar la función
"parseString()":

xml.dom.pulldom.parseString(string, parser=None)

   Retorna una: clase "DOMEventStream" que representa la cadena
   (Unicode) *strnig* (cadena)

xml.dom.pulldom.default_bufsize

   Valor predeterminado para el parámetro *bufsize* para "parse()".

   El valor de las variables puede ser cambiado antes de llamar a
   "parse()" y el nuevo valor tendrá efecto.

## Objetos DOMEventStream

class xml.dom.pulldom.DOMEventStream(stream, parser, bufsize)

   Distinto en la versión 3.11: Support for "__getitem__()" method has
   been removed.

   getEvent()

      Retorna el contenido de la tupla *event* y del *node* corriente
      como "xml.dom.minidom.Document" si el evento es igual a
      "START_DOCUMENT", "xml.dom.minidom.Element" si el evento es
      igual a "START_ELEMENT" o "END_ELEMENT" o "xml.dom.minidom.Text"
      si el evento es igual a "CHARACTERS". El nodo actual no es
      contiene información sobre sus hijos a menos que se llame a la
      función "expandNode()".

   expandNode(node)

      Expande todos los hijos de *node* en *node* (nodo en nodo).
      Ejemplo:

         from xml.dom import pulldom

         xml = '<html><title>Foo</title> <p>Some text <div>and more</div></p> </html>'
         doc = pulldom.parseString(xml)
         for event, node in doc:
             if event == pulldom.START_ELEMENT and node.tagName == 'p':
                 # Following statement only prints '<p/>'
                 print(node.toxml())
                 doc.expandNode(node)
                 # Following statement prints node with all its children '<p>Some text <div>and more</div></p>'
                 print(node.toxml())

   reset()
