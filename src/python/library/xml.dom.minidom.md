---
title: '"xml.dom.minidom" --- Minimal DOM implementation'
source_url: https://docs.python.org/es/3
source_path: library/xml.dom.minidom.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4570
---

# "xml.dom.minidom" --- Minimal DOM implementation

**Código fuente:** Lib/xml/dom/minidom.py

======================================================================

"xml.dom.minidom" is a minimal implementation of the Document Object
Model interface, with an API similar to that in other languages.  It
is intended to be simpler than the full DOM and also significantly
smaller.  Users who are not already proficient with the DOM should
consider using the "xml.etree.ElementTree" module for their XML
processing instead.

Nota:

  If you need to parse untrusted or unauthenticated data, see XML
  security.

DOM applications typically start by parsing some XML into a DOM.  With
"xml.dom.minidom", this is done through the parse functions:

   from xml.dom.minidom import parse, parseString

   dom1 = parse('c:\\temp\\mydata.xml')  # parse an XML file by name

   datasource = open('c:\\temp\\mydata.xml')
   dom2 = parse(datasource)  # parse an open file

   dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')

La función "parse()" puede tomar un nombre de archivo o un objeto de
archivo previamente abierto.

xml.dom.minidom.parse(filename_or_file, parser=None, bufsize=None)

   Retorna un "Document" a partir de la entrada dada.
   *filename_or_file* puede ser un nombre de archivo o un objeto
   similar a un archivo. *parser*, si se proporciona, debe ser un
   objeto de un analizador sintáctico SAX2. Esta función intercambiará
   el controlador de documentos del analizador sintáctico y activará
   el soporte con el espacio de nombres. Otras configuraciones del
   analizador sintáctico (como configurar un solucionador de
   entidades) deben haberse realizado de antemano.

Si tienes XML en una cadena de caracteres, puedes usar la función
"parseString()" en su lugar:

xml.dom.minidom.parseString(string, parser=None)

   Retorna un objeto "Document" que representa a *string*. Este método
   crea un objeto "io.StringIO" para la cadena de caracteres y lo pasa
   a "parse()".

Ambas funciones retornan un objeto "Document" que representa el
contenido del documento.

What the "parse()" and "parseString()" functions do is connect an XML
parser with a "DOM builder" that can accept parse events from any SAX
parser and convert them into a DOM tree.  The names of the functions
are perhaps misleading, but are easy to grasp when learning the
interfaces.  The parsing of the document will be completed before
these functions return; it's simply that these functions do not
provide a parser implementation themselves.

You can also create a "Document" by calling a method on a "DOM
Implementation" object.  You can get this object either by calling the
"getDOMImplementation()" function in the "xml.dom" package or the
"xml.dom.minidom" module.  Once you have a "Document", you can add
child nodes to it to populate the DOM:

   from xml.dom.minidom import getDOMImplementation

   impl = getDOMImplementation()

   newdoc = impl.createDocument(None, "some_tag", None)
   top_element = newdoc.documentElement
   text = newdoc.createTextNode('Some textual content.')
   top_element.appendChild(text)

Una vez que tengas un objeto del documento DOM, puedes acceder a las
partes de tu documento XML a través de sus propiedades y métodos.
Estas propiedades se definen en la especificación DOM. La propiedad
principal del objeto del documento es "documentElement". Te
proporciona el elemento principal en el documento XML: el que contiene
a todos los demás. Aquí hay un programa de ejemplo:

   dom3 = parseString("<myxml>Some data</myxml>")
   assert dom3.documentElement.tagName == "myxml"

When you are finished with a DOM tree, you may optionally call the
"unlink()" method to encourage early cleanup of the now-unneeded
objects.  "unlink()" is an "xml.dom.minidom"-specific extension to the
DOM API that renders the node and its descendants essentially useless.
Otherwise, Python's garbage collector will eventually take care of the
objects in the tree.

Ver también:

  Document Object Model (DOM) Level 1 Specification
     The W3C recommendation for the DOM supported by
     "xml.dom.minidom".

## Objetos del DOM

The definition of the DOM API for Python is given as part of the
"xml.dom" module documentation.  This section lists the differences
between the API and "xml.dom.minidom".

Node.unlink()

   Rompe las referencias internas dentro del DOM para recolectarlo
   como basura en las versiones de Python sin recolector de basura
   cíclico. Incluso cuando se dispone del mismo, su uso puede hacer
   que grandes cantidades de memoria estén disponibles antes, por lo
   que es una buena práctica invocar este método en objetos DOM, tan
   pronto como ya no se necesiten. Solo necesita ser invocado en el
   objeto "Document", pero se puede llamar en los nodos hijos para
   descartar los hijos de ese nodo concreto.

   Puedes evitar invocar este método explícitamente utilizando la
   declaración "with". El siguiente código desvinculará
   automáticamente *dom* cuando se salga del bloque "with":

      with xml.dom.minidom.parse(datasource) as dom:
          ... # Work with dom.

Node.writexml(writer, indent='', addindent='', newl='', encoding=None, standalone=None)

   Escribe XML en el objeto escritor. El escritor recibe texto pero no
   bytes como entrada, debe tener un método "write()" que coincida con
   el de la interfaz del objeto de archivo. El parámetro *indent* es
   la sangría del nodo actual. El parámetro *addindent* es la sangría
   incremental que se utilizará para los subnodos del nodo actual. El
   parámetro *newl* especifica la cadena que se utilizará como
   terminación de las nuevas líneas.

   Para el nodo "Document", se puede usar el argumento por palabra
   clave adicional *encoding* para especificar el valor del campo de
   codificación del encabezado XML.

   De manera similar, al indicar explícitamente el argumento
   *standalone*, las declaraciones del documento independiente se
   agregan al prólogo del documento XML. Si el valor se establece en
   "True", se agrega "standalone="yes""; de lo contrario, se establece
   en ""no"". No declarar el argumento omitirá la declaración del
   documento.

   Distinto en la versión 3.8: El método "writexml()" ahora conserva
   el orden de los atributos especificado por el usuario.

   Distinto en la versión 3.9: Se agregó el parámetro *standalone*.

Node.toxml(encoding=None, standalone=None)

   Retorna una cadena de caracteres o una cadena de bytes que contiene
   el XML representado por el nodo DOM.

   Si se proporciona de forma explícita un valor para el argumento
   *encoding* [1], el resultado es una cadena de bytes con la
   codificación especificada. Si no se proporciona el argumento
   *encoding*, el resultado es una cadena Unicode y la declaración XML
   en la cadena resultante no especifica una codificación. Codificar
   esta cadena en una codificación que no sea UTF-8 probablemente sea
   una práctica incorrecta, ya que UTF-8 es la codificación
   predeterminada para XML.

   El argumento *standalone* se comporta exactamente como en
   "writexml()".

   Distinto en la versión 3.8: El método "toxml()" ahora conserva el
   orden de los atributos especificado por el usuario.

   Distinto en la versión 3.9: Se agregó el parámetro *standalone*.

Node.toprettyxml(indent='\t', newl='\n', encoding=None, standalone=None)

   Retorna una versión impresa elegante del documento. *indent*
   especifica la cadena de caracteres a usar como sangría y es una
   tabulación por defecto; *newl* especifica la cadena de caracteres
   emitida al final de cada línea y es "\n" por defecto.

   El argumento *encoding* se comporta como el argumento
   correspondiente del método "toxml()".

   El argumento *standalone* se comporta exactamente como en
   "writexml()".

   Distinto en la versión 3.8: El método "toprettyxml()" ahora
   conserva el orden de los atributos especificado por el usuario.

   Distinto en la versión 3.9: Se agregó el parámetro *standalone*.

## Ejemplo de DOM

Este programa de ejemplo es una demostración bastante realista de un
programa simple. En este caso particular, no aprovechamos mucho la
flexibilidad del DOM.

   import xml.dom.minidom

   document = """\
   <slideshow>
   <title>Demo slideshow</title>
   <slide><title>Slide title</title>
   <point>This is a demo</point>
   <point>Of a program for processing slides</point>
   </slide>

   <slide><title>Another demo slide</title>
   <point>It is important</point>
   <point>To have more than</point>
   <point>one slide</point>
   </slide>
   </slideshow>
   """

   dom = xml.dom.minidom.parseString(document)

   def getText(nodelist):
       rc = []
       for node in nodelist:
           if node.nodeType == node.TEXT_NODE:
               rc.append(node.data)
       return ''.join(rc)

   def handleSlideshow(slideshow):
       print("<html>")
       handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
       slides = slideshow.getElementsByTagName("slide")
       handleToc(slides)
       handleSlides(slides)
       print("</html>")

   def handleSlides(slides):
       for slide in slides:
           handleSlide(slide)

   def handleSlide(slide):
       handleSlideTitle(slide.getElementsByTagName("title")[0])
       handlePoints(slide.getElementsByTagName("point"))

   def handleSlideshowTitle(title):
       print(f"<title>{getText(title.childNodes)}</title>")

   def handleSlideTitle(title):
       print(f"<h2>{getText(title.childNodes)}</h2>")

   def handlePoints(points):
       print("<ul>")
       for point in points:
           handlePoint(point)
       print("</ul>")

   def handlePoint(point):
       print(f"<li>{getText(point.childNodes)}</li>")

   def handleToc(slides):
       for slide in slides:
           title = slide.getElementsByTagName("title")[0]
           print(f"<p>{getText(title.childNodes)}</p>")

   handleSlideshow(dom)

## minidom y el estándar DOM

The "xml.dom.minidom" module is essentially a DOM 1.0-compatible DOM
with some DOM 2 features (primarily namespace features).

El uso de la interfaz DOM en Python es sencillo. Se aplican las
siguientes reglas de mapeo:

* Se accede a las interfaces a través de objetos de instancia. Las
  aplicaciones no deben instanciar las clases en sí mismas; deben usar
  las funciones de creación disponibles en el objeto "Document". Las
  interfaces derivadas admiten todas las operaciones (y atributos) de
  las interfaces base, además de cualquier operación nueva.

* Las operaciones se utilizan como métodos. Dado que el DOM usa solo
  parámetros "in", los argumentos se pasan en el orden normal (de
  izquierda a derecha). No hay argumentos opcionales. Las operaciones
  "void" retornan "None".

* Los atributos IDL se asignan a atributos de instancia. Por
  compatibilidad con el mapeo del lenguaje OMG IDL para Python,
  también se puede acceder a un atributo "foo" a través de los métodos
  de acceso "_get_foo()" y "_set_foo()". Los atributos "readonly" no
  deben modificarse; esto no se aplica en tiempo de ejecución.

* Los tipos "short int", "unsigned int", "unsigned long long" y
  "boolean" se asignan todos a objetos enteros de Python.

* The type "DOMString" maps to Python strings. "xml.dom.minidom"
  supports either bytes or strings, but will normally produce strings.
  Values of type "DOMString" may also be "None" where allowed to have
  the IDL "null" value by the DOM specification from the W3C.

* Las declaraciones "const" se asignan a variables en su ámbito
  respectivo (por ejemplo,
  "xml.dom.minidom.Node.PROCESSING_INSTRUCTION_NODE"); no deben
  modificarse.

* "DOMException" is currently not supported in "xml.dom.minidom".
  Instead, "xml.dom.minidom" uses standard Python exceptions such as
  "TypeError" and "AttributeError".

* Los objetos de la clase "NodeList" se implementan usando el tipo
  lista incorporado de Python. Estos objetos proporcionan la interfaz
  definida en la especificación DOM, pero en versiones anteriores de
  Python no son compatibles con la API oficial. Sin embargo, son mucho
  más "pythónicas" que la interfaz definida en las recomendaciones del
  W3C.

The following interfaces have no implementation in "xml.dom.minidom":

* "DOMTimeStamp"

* "EntityReference"

La mayoría de ellas reflejan información en el documento XML que
generalmente no es de utilidad para la mayoría de los usuarios de DOM.

-[ Notas al pie ]-

[1] El nombre de codificación incluido en la salida XML debe cumplir
    con los estándares apropiados. Por ejemplo, "UTF-8" es válido,
    pero "UTF8" no es válido en la declaración de un documento XML,
    aunque Python lo acepta como nombre de codificación. Para más
    detalles, consulta https://www.w3.org/TR/2006/REC-xml11-20060816
    /#NT-EncodingDecl y https://www.iana.org/assignments/character-
    sets/character-sets.xhtml.
