---
title: '"xml.etree.ElementTree" --- The ElementTree XML API'
source_url: https://docs.python.org/es/3
source_path: library/xml.etree.elementtree.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4600
---

# "xml.etree.ElementTree" --- The ElementTree XML API

**Código fuente:** Lib/xml/etree/ElementTree.py

======================================================================

The "xml.etree.ElementTree" module implements a simple and efficient
API for parsing and creating XML data.

Distinto en la versión 3.3: Este módulo utilizará una implementación
rápida siempre que esté disponible.

Obsoleto desde la versión 3.3: The "xml.etree.cElementTree" module is
deprecated.

Nota:

  If you need to parse untrusted or unauthenticated data, see XML
  security.

## Tutorial

This is a short tutorial for using "xml.etree.ElementTree" ("ET" in
short).  The goal is to demonstrate some of the building blocks and
basic concepts of the module.

### Árbol y elementos XML

XML es un formato de datos inherentemente jerárquico, y la forma más
natural de representarlo es con un árbol. "ET" tiene dos clases para
este propósito - "ElementTree" representa todo el documento XML como
un árbol, y "Element" representa un solo nodo en este árbol. Las
interacciones con todo el documento (leer y escribir en/desde
archivos) se realizan normalmente en el nivel de "ElementTree". Las
interacciones con un solo elemento XML y sus sub-elementos se realizan
en el nivel "Element".

### Procesando XML

We'll be using the fictive "country_data.xml" XML document as the
sample data for this section:

   <?xml version="1.0"?>
   <data>
       <country name="Liechtenstein">
           <rank>1</rank>
           <year>2008</year>
           <gdppc>141100</gdppc>
           <neighbor name="Austria" direction="E"/>
           <neighbor name="Switzerland" direction="W"/>
       </country>
       <country name="Singapore">
           <rank>4</rank>
           <year>2011</year>
           <gdppc>59900</gdppc>
           <neighbor name="Malaysia" direction="N"/>
       </country>
       <country name="Panama">
           <rank>68</rank>
           <year>2011</year>
           <gdppc>13600</gdppc>
           <neighbor name="Costa Rica" direction="W"/>
           <neighbor name="Colombia" direction="E"/>
       </country>
   </data>

Podemos importar estos datos leyendo desde un archivo:

   import xml.etree.ElementTree as ET
   tree = ET.parse('country_data.xml')
   root = tree.getroot()

O directamente desde una cadena de caracteres:

   root = ET.fromstring(country_data_as_string)

"fromstring()" analiza el XML de una cadena de caracteres directamente
en un "Element", que es el elemento raíz del árbol analizado. Otras
funciones de análisis pueden crear un "ElementTree". Compruebe la
documentación para estar seguro.

Como un "Element", "root" tiene una etiqueta y un diccionario de
atributos:

   >>> root.tag
   'data'
   >>> root.attrib
   {}

También tiene nodos hijos sobre los cuales podemos iterar:

   >>> for child in root:
   ...     print(child.tag, child.attrib)
   ...
   country {'name': 'Liechtenstein'}
   country {'name': 'Singapore'}
   country {'name': 'Panama'}

Los hijos están anidados, y podemos acceder a nodos hijos específicos
por el índice:

   >>> root[0][1].text
   '2008'

Nota:

  No todos los elementos de la entrada XML acabarán siendo elementos
  del árbol analizado. Actualmente, este módulo omite cualquier
  comentario XML, instrucciones de procesamiento y declaraciones de
  tipo documento en la entrada. Sin embargo, los árboles construidos
  utilizando la API de este módulo, en lugar de analizar el texto XML,
  pueden contener comentarios e instrucciones de procesamiento, que se
  incluirán al generar la salida XML. Se puede acceder a una
  declaración de tipo documento pasando una instancia "TreeBuilder"
  personalizada al constructor "XMLParser".

### API de consulta para un procesamiento no bloqueante

La mayoría de las funciones de análisis proporcionadas por este módulo
requieren que se lea todo el documento a la vez antes de retornar
cualquier resultado. Es posible utilizar un "XMLParser" y alimentar
los datos en él de forma incremental, pero se trata de una *push* API
que llama a métodos en un objetivo invocable, que es demasiado bajo
nivel e inconveniente para la mayoría de las necesidades. A veces, lo
que el usuario realmente quiere es ser capaz de analizar XML de forma
incremental, sin bloquear las operaciones, mientras disfruta de la
comodidad de los objetos "Element" totalmente construidos.

La herramienta más potente para hacer esto es "XMLPullParser". No
requiere una lectura de bloqueo para obtener los datos XML, y en su
lugar se alimenta de datos de forma incremental con llamadas a
"XMLPullParser.feed()". Para obtener los elementos XML analizados,
llama a "XMLPullParser.read_events()". He aquí un ejemplo:

   >>> parser = ET.XMLPullParser(['start', 'end'])
   >>> parser.feed('<mytag>sometext')
   >>> list(parser.read_events())
   [('start', <Element 'mytag' at 0x7fa66db2be58>)]
   >>> parser.feed(' more text</mytag>')
   >>> for event, elem in parser.read_events():
   ...     print(event)
   ...     print(elem.tag, 'text=', elem.text)
   ...
   end
   mytag text= sometext more text

El caso de uso obvio es el de las aplicaciones que operan de forma no
bloqueante, donde los datos XML se reciben de un socket o se leen de
forma incremental desde algún dispositivo de almacenamiento. En estos
casos, las lecturas bloqueantes son inaceptables.

Debido a su flexibilidad, "XMLPullParser" puede ser un inconveniente
para los casos de uso más simples. Si no te importa que tu aplicación
se bloquee en la lectura de datos XML pero te gustaría tener
capacidades de análisis incremental, echa un vistazo a "iterparse()".
Puede ser útil cuando estás leyendo un documento XML grande y no
quieres mantenerlo completamente en memoria.

Where *immediate* feedback through events is wanted, calling method
"XMLPullParser.flush()" can help reduce delay; please make sure to
study the related security notes.

### Encontrando elementos interesantes

"Element" tiene algunos métodos útiles que ayudan a iterar
recursivamente sobre todo el sub-árbol por debajo de él (sus hijos,
los hijos de sus hijos, y así sucesivamente). Por ejemplo,
"Element.iter()":

   >>> for neighbor in root.iter('neighbor'):
   ...     print(neighbor.attrib)
   ...
   {'name': 'Austria', 'direction': 'E'}
   {'name': 'Switzerland', 'direction': 'W'}
   {'name': 'Malaysia', 'direction': 'N'}
   {'name': 'Costa Rica', 'direction': 'W'}
   {'name': 'Colombia', 'direction': 'E'}

"Element.findall()" encuentra sólo los elementos con una etiqueta que
son hijos directos del elemento actual. "Element.find()" encuentra el
*primer* hijo con una etiqueta determinada, y "Element.text" accede al
contenido de texto del elemento. "Element.get()" accede a los
atributos del elemento:

   >>> for country in root.findall('country'):
   ...     rank = country.find('rank').text
   ...     name = country.get('name')
   ...     print(name, rank)
   ...
   Liechtenstein 1
   Singapore 4
   Panama 68

Es posible especificar de forma más sofisticada qué elementos buscar
utilizando XPath.

### Modificando un archivo XML

"ElementTree" proporciona una forma sencilla de construir documentos
XML y escribirlos en archivos. El método "ElementTree.write()" sirve
para este propósito.

Una vez creado, un objeto "Element" puede ser manipulado cambiando
directamente sus campos (como "Element.text"), añadiendo y modificando
atributos (método "Element.set()"), así como añadiendo nuevos hijos
(por ejemplo con "Element.append()").

Digamos que queremos añadir uno al rango de cada país, y añadir un
atributo "updated" al elemento rango:

   >>> for rank in root.iter('rank'):
   ...     new_rank = int(rank.text) + 1
   ...     rank.text = str(new_rank)
   ...     rank.set('updated', 'yes')
   ...
   >>> tree.write('output.xml')

Nuestro XML tiene ahora este aspecto:

   <?xml version="1.0"?>
   <data>
       <country name="Liechtenstein">
           <rank updated="yes">2</rank>
           <year>2008</year>
           <gdppc>141100</gdppc>
           <neighbor name="Austria" direction="E"/>
           <neighbor name="Switzerland" direction="W"/>
       </country>
       <country name="Singapore">
           <rank updated="yes">5</rank>
           <year>2011</year>
           <gdppc>59900</gdppc>
           <neighbor name="Malaysia" direction="N"/>
       </country>
       <country name="Panama">
           <rank updated="yes">69</rank>
           <year>2011</year>
           <gdppc>13600</gdppc>
           <neighbor name="Costa Rica" direction="W"/>
           <neighbor name="Colombia" direction="E"/>
       </country>
   </data>

Podemos eliminar elementos utilizando "Element.remove()". Digamos que
queremos eliminar todos los países con un rango superior a 50:

   >>> for country in root.findall('country'):
   ...     # using root.findall() to avoid removal during traversal
   ...     rank = int(country.find('rank').text)
   ...     if rank > 50:
   ...         root.remove(country)
   ...
   >>> tree.write('output.xml')

Tenga en cuenta que la modificación concurrente mientras se itera
puede conducir a problemas, al igual que cuando se itera y modifica
listas o diccionarios de Python. Por lo tanto, el ejemplo recoge
primero todos los elementos coincidentes con "root.findall()", y sólo
entonces itera sobre la lista de coincidencias.

Nuestro XML tiene ahora este aspecto:

   <?xml version="1.0"?>
   <data>
       <country name="Liechtenstein">
           <rank updated="yes">2</rank>
           <year>2008</year>
           <gdppc>141100</gdppc>
           <neighbor name="Austria" direction="E"/>
           <neighbor name="Switzerland" direction="W"/>
       </country>
       <country name="Singapore">
           <rank updated="yes">5</rank>
           <year>2011</year>
           <gdppc>59900</gdppc>
           <neighbor name="Malaysia" direction="N"/>
       </country>
   </data>

### Construyendo documentos XML

La función "SubElement()" también proporciona una forma cómoda de
crear nuevos sub-elementos para un elemento dado:

   >>> a = ET.Element('a')
   >>> b = ET.SubElement(a, 'b')
   >>> c = ET.SubElement(a, 'c')
   >>> d = ET.SubElement(c, 'd')
   >>> ET.dump(a)
   <a><b /><c><d /></c></a>

### Procesando XML con espacio de nombres

Si la entrada XML tiene espacio de nombres, las etiquetas y los
atributos con prefijos de la forma "prefix:sometag" se expanden a
"{uri}sometag" donde el *prefix* se sustituye por el *URI* completo.
Además, si hay un espacio de nombre por defecto, ese URI completo se
antepone a todas las etiquetas sin prefijo.

A continuación se muestra un ejemplo de XML que incorpora dos espacios
de nombres, uno con el prefijo "fictional" y el otro que sirve como
espacio de nombres por defecto:

   <?xml version="1.0"?>
   <actors xmlns:fictional="http://characters.example.com"
           xmlns="http://people.example.com">
       <actor>
           <name>John Cleese</name>
           <fictional:character>Lancelot</fictional:character>
           <fictional:character>Archie Leach</fictional:character>
       </actor>
       <actor>
           <name>Eric Idle</name>
           <fictional:character>Sir Robin</fictional:character>
           <fictional:character>Gunther</fictional:character>
           <fictional:character>Commander Clement</fictional:character>
       </actor>
   </actors>

Una forma de buscar y explorar este ejemplo XML es añadir manualmente
el URI a cada etiqueta o atributo en el XPath de un "find()" o
"findall()":

   root = fromstring(xml_text)
   for actor in root.findall('{http://people.example.com}actor'):
       name = actor.find('{http://people.example.com}name')
       print(name.text)
       for char in actor.findall('{http://characters.example.com}character'):
           print(' |-->', char.text)

Una mejor manera de buscar en el ejemplo de XML con espacio para
nombres es crear un diccionario con sus propios prefijos y utilizarlos
en las funciones de búsqueda:

   ns = {'real_person': 'http://people.example.com',
         'role': 'http://characters.example.com'}

   for actor in root.findall('real_person:actor', ns):
       name = actor.find('real_person:name', ns)
       print(name.text)
       for char in actor.findall('role:character', ns):
           print(' |-->', char.text)

Estos dos enfoques dan como resultado:

   John Cleese
    |--> Lancelot
    |--> Archie Leach
   Eric Idle
    |--> Sir Robin
    |--> Gunther
    |--> Commander Clement

## Soporte de XPath

Este módulo proporciona un soporte limitado para las expresiones XPath
para localizar elementos en un árbol. El objetivo es soportar un
pequeño subconjunto de la sintaxis abreviada; un motor XPath completo
está fuera del alcance del módulo.

### Ejemplo

A continuación se muestra un ejemplo que demuestra algunas de las
capacidades de XPath del módulo. Utilizaremos el documento XML
"countrydata" de la sección Parsing XML:

   import xml.etree.ElementTree as ET

   root = ET.fromstring(countrydata)

   # Top-level elements
   root.findall(".")

   # All 'neighbor' grand-children of 'country' children of the top-level
   # elements
   root.findall("./country/neighbor")

   # Nodes with name='Singapore' that have a 'year' child
   root.findall(".//year/..[@name='Singapore']")

   # 'year' nodes that are children of nodes with name='Singapore'
   root.findall(".//*[@name='Singapore']/year")

   # All 'neighbor' nodes that are the second child of their parent
   root.findall(".//neighbor[2]")

Para XML con espacios de nombre, use la notación calificada habitual
"{namespace}tag":

   # All dublin-core "title" tags in the document
   root.findall(".//{http://purl.org/dc/elements/1.1/}title")

### Sintaxis XPath soportada

+-------------------------+--------------------------------------------------------+
| Sintaxis                | Significado                                            |
|=========================|========================================================|
| "tag"                   | Selecciona todos los elementos hijos con la etiqueta   |
|                         | dada. Por ejemplo, "spam" selecciona todos los         |
|                         | elementos hijos llamados "spam", y "spam/egg"          |
|                         | selecciona todos los nietos llamados "egg" en todos    |
|                         | los hijos llamados "spam". "{namespace}*" selecciona   |
|                         | todas las etiquetas en el espacio de nombres dado,     |
|                         | "{*}spam" selecciona las etiquetas llamadas "spam" en  |
|                         | cualquier (o ningún) espacio de nombres, y "{}*" sólo  |
|                         | selecciona las etiquetas que no están en un espacio de |
|                         | nombres.  Distinto en la versión 3.8: Se ha añadido la |
## |                         | posibilidad de utilizar comodines asterisco.           |

| "*"                     | Selecciona todos los elementos hijos, incluidos los    |
|                         | comentarios y las instrucciones de procesamiento. Por  |
|                         | ejemplo, "*/egg" selecciona todos los hijos llamados   |
## |                         | "egg".                                                 |

| "."                     | Selecciona el nodo actual. Esto es útil sobre todo al  |
|                         | principio de la ruta, para indicar que es una ruta     |
## |                         | relativa.                                              |

| "//"                    | Selecciona todos los sub-elementos, en todos los       |
|                         | niveles por debajo del elemento actual. Por ejemplo,   |
|                         | ".//egg" selecciona todos los elementos "egg" en todo  |
## |                         | el árbol.                                              |

| ".."                    | Selecciona el elemento padre. Retorna "None" si la     |
|                         | ruta intenta llegar a los ancestros del elemento       |
## |                         | inicial (el elemento "find" fue invocado).             |

| "[@attrib]"             | Selecciona todos los elementos que tengan el atributo  |
## |                         | dado.                                                  |

| "[@attrib='value']"     | Selecciona todos los elementos para los que el         |
|                         | atributo dado tiene el valor dado. El valor no puede   |
## |                         | contener comillas.                                     |

| "[@attrib!='value']"    | Selecciona todos los elementos para los que el         |
|                         | atributo dado no tiene el valor dado. El valor no      |
## |                         | puede contener comillas.  Added in version 3.10.       |

| "[tag]"                 | Selecciona todos los elementos que tienen un hijo      |
## |                         | llamado "tag". Sólo se admiten los hijos inmediatos.   |

| "[.='text']"            | Selecciona todos los elementos cuyo contenido de texto |
|                         | completo, incluyendo los descendientes, es igual al    |
## |                         | "texto" dado.  Added in version 3.7.                   |

| "[.!='text']"           | Selecciona todos los elementos cuyo contenido de texto |
|                         | completo, incluidos los descendientes, no es igual al  |
## |                         | "text" proporcionado.  Added in version 3.10.          |

| "[tag='text']"          | Selecciona todos los elementos que tienen un hijo      |
|                         | llamado "tag" cuyo contenido de texto completo,        |
## |                         | incluyendo los descendientes, es igual al "text" dado. |

| "[tag!='text']"         | Selecciona todos los elementos que tienen un hijo      |
|                         | llamado "tag" cuyo contenido de texto completo,        |
|                         | incluidos los descendientes, no es igual al "text"     |
## |                         | dado.  Added in version 3.10.                          |

| "[position]"            | Selecciona todos los elementos que se encuentran en la |
|                         | posición dada. La posición puede ser un número entero  |
|                         | (1 es la primera posición), la expresión "last()"      |
|                         | (para la última posición), o una posición relativa a   |
## |                         | la última posición (por ejemplo, "last()-1").          |

Los predicados (expresiones entre corchetes) deben ir precedidos de un
nombre de etiqueta, un asterisco u otro predicado. Los predicados
"position" deben ir precedidos de un nombre de etiqueta.

## Referencia

### Funciones

xml.etree.ElementTree.canonicalize(xml_data=None, *, out=None, from_file=None, **options)

   Función de transformación C14N 2.0.

   Canonicalization is a way to normalise XML output in a way that
   allows byte-by-byte comparisons and digital signatures.  It reduces
   the freedom that XML serializers have and instead generates a more
   constrained XML representation.  The main restrictions regard the
   placement of namespace declarations, the ordering of attributes,
   and ignorable whitespace.

   Esta función toma una cadena de datos XML (*xml_data*) o una ruta
   de archivo o un objeto tipo archivo (*from_file*) como entrada, la
   convierte a la forma canónica y la escribe utilizando el objeto
   archivo (o tipo archivo) *out*, si se proporciona, o la devuelve
   como una cadena de texto si no. El archivo de salida recibe texto,
   no bytes. Por tanto, debe abrirse en modo texto con codificación
   "utf-8".

   Usos típicos:

      xml_data = "<root>...</root>"
      print(canonicalize(xml_data))

      with open("c14n_output.xml", mode='w', encoding='utf-8') as out_file:
          canonicalize(xml_data, out=out_file)

      with open("c14n_output.xml", mode='w', encoding='utf-8') as out_file:
          canonicalize(from_file="inputfile.xml", out=out_file)

   Las opciones de configuración *options* son las siguientes:

   * *with_comments*: configurar a "True" para incluir los comentarios
     (por defecto: "False")

   * *strip_text*: configurar a "True" para eliminar los espacios en
     blanco antes y después del contenido del texto
        (por defecto: "False")

   * *rewrite_prefixes*: configurar a "True" para sustituir los
     prefijos de espacios de nombres por "n{number}"
        (por defecto: "False")

   * *qname_aware_tags*: un conjunto de nombres de etiquetas
     conscientes de qname en el que los prefijos
        deben ser reemplazados en el contenido del texto (por defecto:
        vacío)

   * *qname_aware_attrs*: un conjunto de nombres de atributos
     conscientes de qname en el que los prefijos
        deben ser reemplazados en el contenido del texto (por defecto:
        vacío)

   * *exclude_attrs*: un conjunto de nombres de atributos que no deben
     serializarse

   * *exclude_tags*: un conjunto de nombres de etiquetas que no deben
     serializarse

   En la lista de opciones anterior, "un conjunto" se refiere a
   cualquier colección o iterable de cadenas, no se espera ningún
   orden.

   Added in version 3.8.

xml.etree.ElementTree.Comment(text=None)

   Fábrica de elementos de comentario. Esta función de fábrica crea un
   elemento especial que será serializado como un comentario XML por
   el serializador estándar. La cadena de comentario puede ser una
   cadena de bytes o una cadena Unicode. *text* es una cadena que
   contiene la cadena de comentario. Devuelve una instancia de
   elemento que representa un comentario.

   Tenga en cuenta que "XMLParser" omite los comentarios en la entrada
   en lugar de crear objetos de comentario para ellos. Un
   "ElementTree" sólo contendrá nodos de comentario si se han
   insertado en el árbol utilizando uno de los métodos "Element".

xml.etree.ElementTree.dump(elem)

   Escribe un árbol de elementos o una estructura de elementos en
   sys.stdout. Esta función debe utilizarse únicamente para debugging.

   El formato de salida exacto depende de la implementación. En esta
   versión, se escribe como un archivo XML ordinario.

   *elem* es un árbol de elementos o un elemento individual.

   Distinto en la versión 3.8: La función "dump()" ahora preserva el
   orden de atributos especificado por el usuario.

xml.etree.ElementTree.fromstring(text, parser=None)

   Analiza una sección XML a partir de una constante de cadena. Igual
   que "XML()". *text* es una cadena que contiene datos XML. *parser*
   es una instancia de parser opcional. Si no se da, se utiliza el
   analizador estándar "XMLParser". Devuelve una instancia de
   "Element".

xml.etree.ElementTree.fromstringlist(sequence, parser=None)

   Analiza un documento XML a partir de una secuencia de fragmentos de
   cadena de caracteres. *sequence* es una lista u otra secuencia que
   contiene fragmentos de datos XML. *parser* es una instancia de
   parser opcional. Si no se da, se utiliza el analizador estándar
   "XMLParser". Retorna una instancia de "Element".

   Added in version 3.2.

xml.etree.ElementTree.indent(tree, space='  ', level=0)

   Añade espacios en blanco al subárbol para indentar el árbol
   visualmente. Esto puede utilizarse para generar una salida XML con
   una impresión bonita. *tree* puede ser un Element o ElementTree.
   *space* es la cadena de espacio en blanco que se insertará para
   cada nivel de indentación, dos caracteres de espacio por defecto.
   Para indentar subárboles parciales dentro de un árbol ya indentado,
   pase el nivel de indentación inicial como *level*.

   Added in version 3.9.

xml.etree.ElementTree.iselement(element)

   Comprueba si un objeto parece ser un objeto elemento válido.
   *element* es una instancia de elemento. Retorna "True" si se trata
   de un objeto elemento.

xml.etree.ElementTree.iterparse(source, events=None, parser=None)

   Parses an XML section into an element tree incrementally, and
   reports what's going on to the user.  *source* is a filename or
   *file object* containing XML data.  *events* is a sequence of
   events to report back.  The supported events are the strings
   ""start"", ""end"", ""comment"", ""pi"", ""start-ns"" and ""end-
   ns"" (the "ns" events are used to get detailed namespace
   information).  If *events* is omitted, only ""end"" events are
   reported. *parser* is an optional parser instance.  If not given,
   the standard "XMLParser" parser is used.  *parser* must be a
   subclass of "XMLParser" and can only use the default "TreeBuilder"
   as a target. Returns an *iterator* providing "(event, elem)" pairs;
   it has a "root" attribute that references the root element of the
   resulting XML tree once *source* is fully read. The iterator has
   the "close()" method that closes the internal file object if
   *source* is a filename.

   Tenga en cuenta que mientras "iterparse()" construye el árbol de
   forma incremental, emite lecturas de bloqueo en la *source* (o en
   el fichero que nombra). Por lo tanto, no es adecuado para
   aplicaciones en las que no se pueden realizar lecturas de bloqueo.
   Para un análisis completamente no bloqueante, véase
   "XMLPullParser".

   Nota:

     "iterparse()" sólo garantiza que ha visto el carácter ">" de una
     etiqueta de inicio cuando emite un evento "start", por lo que los
     atributos están definidos, pero el contenido de los atributos
     text y tail está indefinido en ese momento. Lo mismo ocurre con
     los hijos del elemento; pueden estar presentes o no.Si necesita
     un elemento totalmente poblado, busque los eventos "end" en su
     lugar.

   Obsoleto desde la versión 3.4: El argumento *parser*.

   Distinto en la versión 3.8: Los eventos "comment" y "pi" han sido
   añadidos.

   Distinto en la versión 3.13: Added the "close()" method.

xml.etree.ElementTree.parse(source, parser=None)

   Analiza una sección XML en un árbol de elementos. *source* es un
   nombre de archivo o un objeto de archivo que contiene datos XML.
   *parser* es una instancia de parser opcional. Si no se da, se
   utiliza el analizador estándar "XMLParser". Devuelve una instancia
   de "ElementTree".

xml.etree.ElementTree.ProcessingInstruction(target, text=None)

   Fábrica de elementos PI. Esta función de fábrica crea un elemento
   especial que será serializado como una instrucción de procesamiento
   XML. *target* es una cadena que contiene el objetivo de PI. *text*
   es una cadena que contiene el contenido de PI, si se da. Devuelve
   una instancia de elemento, representando una instrucción de
   procesamiento.

   Note that "XMLParser" skips over processing instructions in the
   input instead of creating PI objects for them. An "ElementTree"
   will only contain processing instruction nodes if they have been
   inserted into to the tree using one of the "Element" methods.

xml.etree.ElementTree.register_namespace(prefix, uri)

   Registra un prefijo de espacio de nombres. El registro es global, y
   cualquier asignación existente para el prefijo dado o el URI del
   espacio de nombres será eliminado. *prefix* es un prefijo de
   espacio de nombres. *uri* es una uri del espacio de nombres. Las
   etiquetas y los atributos de este espacio de nombres se
   serializarán con el prefijo dado, si es posible.

   Added in version 3.2.

xml.etree.ElementTree.SubElement(parent, tag, attrib={}, **extra)

   Fábrica de sub-elementos. Esta función crea una instancia de
   elemento y la añade a un elemento existente.

   El nombre del elemento, los nombres de los atributos y los valores
   de los atributos pueden ser cadenas de bytes o cadenas de
   caracteres Unicode. *parent* es el elemento padre. *tag* es el
   nombre del sub-elemento. *attrib* es un diccionario opcional que
   contiene los atributos del elemento. *extra* contiene atributos
   adicionales, dados como argumentos de palabras clave. Devuelve una
   instancia de elemento.

xml.etree.ElementTree.tostring(element, encoding='us-ascii', method='xml', *, xml_declaration=None, default_namespace=None, short_empty_elements=True)

   Genera una representación de cadena de caracteres de un elemento
   XML, incluyendo todos los sub-elementos. *element* es una instancia
   de "Element". *encoding* [1] es la codificación de salida (por
   defecto es US-ASCII). Utilice "encoding="unicode"" para generar una
   cadena de caracteres Unicode (de lo contrario, se genera una cadena
   de bytes). *method* es ""xml"", ""html"" o ""text"" (por defecto es
   ""xml""). *xml_declaration*, *default_namespace* y
   *short_empty_elements* tienen el mismo significado que en
   "ElementTree.write()". Devuelve una cadena (opcionalmente)
   codificada que contiene los datos XML.

   Distinto en la versión 3.4: Added the *short_empty_elements*
   parameter.

   Distinto en la versión 3.8: Added the *xml_declaration* and
   *default_namespace* parameters.

   Distinto en la versión 3.8: La función "tostring()" ahora preserva
   el orden de atributos especificado por el usuario.

xml.etree.ElementTree.tostringlist(element, encoding='us-ascii', method='xml', *, xml_declaration=None, default_namespace=None, short_empty_elements=True)

   Genera una representación de cadena de caracteres de un elemento
   XML, incluyendo todos los sub-elementos. *element* es una instancia
   de "Element". *encoding* [1] es la codificación de salida (por
   defecto es US-ASCII). Utilice "encoding="unicode"" para generar una
   cadena de caracteres Unicode (de lo contrario, se genera una cadena
   de bytes). *method* es ""xml"", ""html"" o ""text"" (por defecto es
   ""xml""). *xml_declaration*, *default_namespace* y
   *short_empty_elements* tienen el mismo significado que en
   "ElementTree.write()". Devuelve una lista de cadenas
   (opcionalmente) codificadas que contienen los datos XML. No
   garantiza ninguna secuencia específica, excepto que
   "b"".join(tostringlist(element)) == tostring(element)".

   Added in version 3.2.

   Distinto en la versión 3.4: Added the *short_empty_elements*
   parameter.

   Distinto en la versión 3.8: Added the *xml_declaration* and
   *default_namespace* parameters.

   Distinto en la versión 3.8: La función "tostringlist()" ahora
   preserva el orden de atributos especificado por el usuario.

xml.etree.ElementTree.XML(text, parser=None)

   Analiza una sección XML a partir de una constante de cadena de
   caracteres. Esta función puede utilizarse para incrustar "literales
   XML" en el código de Python. *text* es una cadena de caracteres que
   contiene datos XML. *parser* es una instancia de parser opcional.
   Si no se da, se utiliza el analizador estándar "XMLParser".
   Devuelve una instancia de "Element".

xml.etree.ElementTree.XMLID(text, parser=None)

   Analiza una sección XML a partir de una constante de cadena de
   caracteres, y también devuelve un diccionario que mapea los id:s de
   elementos a elementos. *text* es una cadena de caracteres que
   contiene datos XML. *parser* es una instancia de parser opcional.
   Si no se da, se utiliza el analizador estándar de "XMLParser".
   Devuelve una tupla que contiene una instancia de "Element" y un
   diccionario.

## Soporte de XInclude

Este módulo proporciona un soporte limitado para las directivas
XInclude, a través del módulo de ayuda "xml.etree.ElementInclude".
Este módulo puede utilizarse para insertar subárboles y cadenas de
texto en árboles de elementos, basándose en la información del árbol.

### Ejemplo

Aquí hay un ejemplo que demuestra el uso del módulo XInclude. Para
incluir un documento XML en el documento actual, utilice el elemento
"{http://www.w3.org/2001/XInclude}include" y establezca el atributo
**parse** como ""xml"", y utilice el atributo **href** para
especificar el documento a incluir.

   <?xml version="1.0"?>
   <document xmlns:xi="http://www.w3.org/2001/XInclude">
     <xi:include href="source.xml" parse="xml" />
   </document>

Por defecto, el atributo **href** se trata como un nombre de archivo.
Puede utilizar cargadores personalizados para anular este
comportamiento. También tenga en cuenta que el ayudante estándar no
soporta la sintaxis XPointer.

To process this file, load it as usual, and pass the root element to
the "xml.etree.ElementTree" module:

   from xml.etree import ElementTree, ElementInclude

   tree = ElementTree.parse("document.xml")
   root = tree.getroot()

   ElementInclude.include(root)

El módulo ElementInclude sustituye el elemento
"{http://www.w3.org/2001/XInclude}include" por el elemento raíz del
documento **source.xml**. El resultado podría ser algo así:

   <document xmlns:xi="http://www.w3.org/2001/XInclude">
     <para>This is a paragraph.</para>
   </document>

Si se omite el atributo **parse**, el valor por defecto es "xml". El
atributo href es obligatorio.

Para incluir un documento de texto, utilice el elemento
"{http://www.w3.org/2001/XInclude}include" y establezca el atributo
**parse** como "text":

   <?xml version="1.0"?>
   <document xmlns:xi="http://www.w3.org/2001/XInclude">
     Copyright (c) <xi:include href="year.txt" parse="text" />.
   </document>

El resultado podría ser algo así:

   <document xmlns:xi="http://www.w3.org/2001/XInclude">
     Copyright (c) 2003.
   </document>

## Referencia

### Funciones

xml.etree.ElementInclude.default_loader(href, parse, encoding=None)

   Default loader. This default loader reads an included resource from
   disk. *href* is a URL.  *parse* is for parse mode either "xml" or
   "text". *encoding* is an optional text encoding.  If not given,
   encoding is "utf-8". Returns the expanded resource. If the parse
   mode is ""xml"", this is an "Element" instance. If the parse mode
   is ""text"", this is a string. If the loader fails, it can return
   "None" or raise an exception.

xml.etree.ElementInclude.include(elem, loader=None, base_url=None, max_depth=6)

   This function expands XInclude directives in-place in tree pointed
   by *elem*. *elem* is either the root "Element" or an "ElementTree"
   instance to find such element. *loader* is an optional resource
   loader.  If omitted, it defaults to "default_loader()". If given,
   it should be a callable that implements the same interface as
   "default_loader()".  *base_url* is base URL of the original file,
   to resolve relative include file references.  *max_depth* is the
   maximum number of recursive inclusions.  Limited to reduce the risk
   of malicious content explosion. Pass "None" to disable the
   limitation.

   Distinto en la versión 3.9: Added the *base_url* and *max_depth*
   parameters.

### Objetos Element

class xml.etree.ElementTree.Element(tag, attrib={}, **extra)

   Clase Element. Esta clase define la interfaz Element, y provee una
   implementación de referencia de esta interfaz.

   El nombre del elemento, los nombres de los atributos y los valores
   de los atributos pueden ser cadenas de bytes o cadenas Unicode.
   *tag* es el nombre del elemento. *attrib* es un diccionario
   opcional que contiene los atributos del elemento. *extra* contiene
   atributos adicionales, dados como argumentos de palabras clave.

   tag

      Una cadena de caracteres que identifica qué tipo de datos
      representa este elemento (el tipo de elemento, en otras
      palabras).

   text
   tail

      Estos atributos pueden utilizarse para contener datos
      adicionales asociados al elemento. Sus valores suelen ser
      cadenas, pero pueden ser cualquier objeto específico de la
      aplicación. Si el elemento se crea a partir de un archivo XML,
      el atributo *text* contiene el texto entre la etiqueta inicial
      del elemento y su primera etiqueta hija o final, o "None", y el
      atributo *tail* contiene el texto entre la etiqueta final del
      elemento y la siguiente etiqueta, o "None". Para los datos XML

         <a><b>1<c>2<d/>3</c></b>4</a>

      el elemento *a* tiene "None" para los atributos *text* y *tail*,
      el elemento *b* tiene *text* ""1"" y *tail* ""4"", el elemento
      *c* tiene *text* ""2"" y *tail* "None", y el elemento *d* tiene
      *text* "None" y *tail* ""3"".

      Para recoger el texto interior de un elemento, véase
      "itertext()", por ejemplo """.join(element.itertext())".

      Las aplicaciones pueden almacenar objetos arbitrarios en estos
      atributos.

   attrib

      Un diccionario que contiene los atributos del elemento. Ten en
      cuenta que aunque el valor *attrib* es siempre un diccionario
      mutable real de Python, una implementación de ElementTree puede
      elegir utilizar otra representación interna, y crear el
      diccionario sólo si alguien lo pide. Para aprovechar este tipo
      de implementaciones, utiliza los métodos de diccionario que
      aparecen a continuación siempre que sea posible.

   Los siguientes métodos tipo diccionario funcionan con los atributos
   de los elementos.

   clear()

      Restablece un elemento.  Esta función elimina todos los sub-
      elementos, borra todos los atributos y establece los atributos
      de texto y cola como "None".

   get(key, default=None)

      Obtiene el atributo del elemento llamado *key*.

      Retorna el valor del atributo, o *default* si el atributo no fue
      encontrado.

   items()

      Retorna los atributos del elemento como una secuencia de pares
      (nombre, valor). Los atributos se retornan en un orden
      arbitrario.

   keys()

      Retorna los nombres de los atributos de los elementos como una
      lista. Los nombres se retornan en un orden arbitrario.

   set(key, value)

      Establecer el atributo *key* en el elemento a *value*.

   Los siguientes métodos actúan sobre los hijos del elemento (sub-
   elementos).

   append(subelement)

      Añade el elemento *subelement* al final de la lista interna de
      sub-elementos de este elemento. Lanza "TypeError" si
      *subelement* no es un "Element".

   extend(subelements)

      Appends *subelements* from an iterable of elements. Raises
      "TypeError" if a subelement is not an "Element".

      Added in version 3.2.

   find(match, namespaces=None)

      Encuentra el primer sub-elemento que coincide con *match*.
      *match* puede ser un nombre de etiqueta o un path. Retorna una
      instancia de elemento o "None". *namespaces* es un mapeo
      opcional del prefijo del espacio de nombres al nombre completo.
      Pasa "''" como prefijo para mover todos los nombres de etiquetas
      sin prefijo en la expresión al espacio de nombres dado.

   findall(match, namespaces=None)

      Encuentra todos los sub-elementos coincidentes, por nombre de
      etiqueta o path. Retorna una lista que contiene todos los
      elementos coincidentes en el orden del documento. *namespaces*
      es un mapeo opcional del prefijo del espacio de nombres al
      nombre completo. Pasa "''" como prefijo para mover todos los
      nombres de etiquetas sin prefijo en la expresión al espacio de
      nombres dado.

   findtext(match, default=None, namespaces=None)

      Busca el texto del primer sub-elemento que coincida con *match*.
      *match* puede ser un nombre de etiqueta o un path. Retorna el
      contenido del texto del primer elemento que coincida, o
      *default* si no se encuentra ningún elemento. Tenga en cuenta
      que si el elemento coincidente no tiene contenido de texto se
      devuelve una cadena vacía. *namespaces* es un mapeo opcional del
      prefijo del espacio de nombres al nombre completo. Pasa "''"
      como prefijo para mover todos los nombres de etiquetas sin
      prefijo en la expresión al espacio de nombres dado.

   insert(index, subelement)

      Inserta *subelement* en la posición dada en este elemento. Lanza
      "TypeError" si *subelement* no es un "Element".

   iter(tag=None)

      Crea un árbol *iterator* con el elemento actual como raíz. El
      iterador itera sobre este elemento y todos los elementos por
      debajo de él, en el orden del documento (profundidad primero).
      Si *tag* no es "None" o "'*'", sólo los elementos cuya etiqueta
      es igual a *tag* son retornados por el iterador. Si la
      estructura del árbol se modifica durante la iteración, el
      resultado es indefinido.

      Added in version 3.2.

   iterfind(match, namespaces=None)

      Encuentra todos los subelementos que coinciden, por nombre de
      etiqueta o ruta. Retorna un iterable con todos los elementos
      coincidentes en el orden del documento. *namespaces* es un mapeo
      opcional del prefijo del espacio de nombres al nombre completo.

      Added in version 3.2.

   itertext()

      Crea un iterador de texto. El iterador hace un bucle sobre este
      elemento y todos los subelementos, en el orden del documento, y
      retorna todo el texto interior.

      Added in version 3.2.

   makeelement(tag, attrib)

      Crea un nuevo objeto elemento del mismo tipo que este elemento.
      No llame a este método, utilice la función de fábrica
      "SubElement()" en su lugar.

   remove(subelement)

      Elimina el *subelement* del elemento. A diferencia de los
      métodos find*, este método compara los elementos basándose en la
      identidad de la instancia, no en el valor de la etiqueta o el
      contenido.

   Los objetos "Element" también soportan los siguientes métodos de
   tipo secuencia para trabajar con subelementos: "__delitem__()",
   "__getitem__()", "__setitem__()", "__len__()".

   Caution: Elements with no subelements will test as "False".  In a
   future release of Python, all elements will test as "True"
   regardless of whether subelements exist.  Instead, prefer explicit
   "len(elem)" or "elem is not None" tests.:

      element = root.find('foo')

      if not element:  # careful!
          print("element not found, or element has no subelements")

      if element is None:
          print("element not found")

   Distinto en la versión 3.12: Testing the truth value of an Element
   emits "DeprecationWarning".

   Antes de Python 3.8, el orden de serialización de los atributos XML
   de los elementos se hacía predecible artificialmente ordenando los
   atributos por su nombre. Basado en el ordenamiento -ahora
   garantizado- de los diccionarios, este reordenamiento arbitrario
   fue eliminado en Python 3.8 para preservar el orden en que los
   atributos fueron originalmente analizados o creados por el código
   del usuario.

   En general, el código del usuario debería intentar no depender de
   un orden específico de los atributos, dado que el XML Information
   Set excluye explícitamente el orden de los atributos para
   transmitir información. El código debe estar preparado para hacer
   frente a cualquier orden en la entrada. En los casos en los que se
   requiere una salida XML determinista, por ejemplo, para la firma
   criptográfica o los conjuntos de datos de prueba, la serialización
   canónica está disponible con la función "canonicalize()".

   En los casos en los que la salida canónica no es aplicable, pero un
   orden de atributos específico sigue siendo deseable en la salida,
   el código debe tratar de crear los atributos directamente en el
   orden deseado, para evitar desajustes perceptivos para los lectores
   del código. En los casos en que esto es difícil de lograr, una
   receta como la siguiente se puede aplicar antes de la serialización
   para hacer cumplir un orden independientemente de la creación de
   elementos:

      def reorder_attributes(root):
          for el in root.iter():
              attrib = el.attrib
              if len(attrib) > 1:
                  # adjust attribute order, e.g. by sorting
                  attribs = sorted(attrib.items())
                  attrib.clear()
                  attrib.update(attribs)

### Objetos ElementTree

class xml.etree.ElementTree.ElementTree(element=None, file=None)

   Clase envoltorio de un ElementTree. Esta clase representa una
   jerarquía de elementos completa, y añade algún soporte extra para
   la serialización hacia y desde XML estándar.

   *element* es el elemento raíz. El árbol se inicializa con el
   contenido del *file* XML si se da.

   _setroot(element)

      Reemplaza el elemento raíz de este árbol. Esto descarta el
      contenido actual del árbol, y lo reemplaza con el elemento dado.
      Utilícelo con cuidado. *element* es una instancia de elemento.

   find(match, namespaces=None)

      Igual que "Element.find()", empezando por la raíz del árbol.

   findall(match, namespaces=None)

      Igual que "Element.findall()", empezando por la raíz del árbol.

   findtext(match, default=None, namespaces=None)

      Igual que "Element.findtext()", empezando por la raíz del árbol.

   getroot()

      Retorna el elemento raíz de este árbol.

   iter(tag=None)

      Crea y retorna un iterador de árbol para el elemento raíz. El
      iterador recorre todos los elementos de este árbol, en orden de
      sección. *tag* es la etiqueta a buscar (por defecto devuelve
      todos los elementos).

   iterfind(match, namespaces=None)

      Igual que "Element.iterfind()", empezando por la raíz del árbol.

      Added in version 3.2.

   parse(source, parser=None)

      Carga una sección XML externa en este árbol de elementos.
      *source* es un nombre de archivo o un *file object*. *parser* es
      una instancia opcional del analizador. Si no se da, se utiliza
      el analizador estándar "XMLParser". Retorna el elemento raíz de
      la sección.

   write(file, encoding='us-ascii', xml_declaration=None, default_namespace=None, method='xml', *, short_empty_elements=True)

      Escribe el árbol de elementos en un archivo, como XML. *file* es
      un nombre de archivo, o un *file object* abierto para escritura.
      *encoding* [1] es la codificación de salida (por defecto es US-
      ASCII). *xml_declaration* controla si se debe añadir una
      declaración XML al archivo. Utilice "False" para nunca, "True"
      para siempre, "None" para sólo si no es US-ASCII o UTF-8 o
      Unicode (por defecto es "None"). *default_namespace* establece
      el espacio de nombres XML por defecto (para "xmlns"). *method*
      es ""xml"", ""html"" o ""text"" (por defecto es ""xml""). El
      parámetro *short_empty_elements* controla el formato de los
      elementos sin contenido. Si es "True" (por defecto), se emiten
      como una sola etiqueta autocerrada, de lo contrario se emiten
      como un par de etiquetas de inicio/fin.

      La salida es una cadena de caracteres ("str") o binaria
      ("bytes"). Esto es controlado por el argumento *encoding*. Si
      *encoding* es "unicode", la salida es una cadena de caracteres;
      en caso contrario, es binaria. Tenga en cuenta que esto puede
      entrar en conflicto con el tipo de *file* si es un *file object*
      abierto; asegúrese de no intentar escribir una cadena en un
      flujo binario y viceversa.

      Distinto en la versión 3.4: Added the *short_empty_elements*
      parameter.

      Distinto en la versión 3.8: El método "write()" ahora conserva
      el orden de los atributos especificado por el usuario.

Este es el archivo XML que será manipulado:

   <html>
       <head>
           <title>Example page</title>
       </head>
       <body>
           <p>Moved to <a href="http://example.org/">example.org</a>
           or <a href="http://example.com/">example.com</a>.</p>
       </body>
   </html>

Ejemplo de cambio del atributo "target" de cada enlace en el primer
párrafo:

   >>> from xml.etree.ElementTree import ElementTree
   >>> tree = ElementTree()
   >>> tree.parse("index.xhtml")
   <Element 'html' at 0xb77e6fac>
   >>> p = tree.find("body/p")     # Finds first occurrence of tag p in body
   >>> p
   <Element 'p' at 0xb77ec26c>
   >>> links = list(p.iter("a"))   # Returns list of all links
   >>> links
   [<Element 'a' at 0xb77ec2ac>, <Element 'a' at 0xb77ec1cc>]
   >>> for i in links:             # Iterates through all found links
   ...     i.attrib["target"] = "blank"
   ...
   >>> tree.write("output.xhtml")

### Objetos QName

class xml.etree.ElementTree.QName(text_or_uri, tag=None)

   QName wrapper. Se puede utilizar para envolver un valor de atributo
   QName, con el fin de obtener un manejo adecuado del espacio de
   nombres en la salida. *text_or_uri* es una cadena de caracteres que
   contiene el valor QName, en la forma {uri}local, o, si se da el
   argumento tag, la parte URI de un QName. Si se da *tag*, el primer
   argumento se interpreta como un URI, y este argumento se interpreta
   como un nombre local. Las instancias de "QName" son opacas.

### Objetos TreeBuilder

class xml.etree.ElementTree.TreeBuilder(element_factory=None, *, comment_factory=None, pi_factory=None, insert_comments=False, insert_pis=False)

   Constructor genérico de estructuras de elementos. Este constructor
   convierte una secuencia de llamadas a los métodos start, data, end,
   comment y pi en una estructura de elementos bien formada. Puedes
   utilizar esta clase para construir una estructura de elementos
   utilizando un analizador XML personalizado, o un analizador para
   algún otro formato similar a XML.

   *element_factory*, cuando se da, debe ser un callable que acepta
   dos argumentos posicionales: una etiqueta y un diccionario de
   atributos. Se espera que retorne una nueva instancia de elemento.

   Las funciones *comment_factory* y *pi_factory*, cuando se dan,
   deben comportarse como las funciones "Comment()" y
   "ProcessingInstruction()" para crear comentarios e instrucciones de
   procesamiento. Si no se dan, se utilizarán las fábricas por
   defecto. Cuando *insert_comments* y/o *insert_pis* es verdadero,
   los comentarios/pis se insertarán en el árbol si aparecen dentro
   del elemento raíz (pero no fuera de él).

   close()

      Vacía los buffers del constructor y retorna el elemento del
      documento de nivel superior. Retorna una instancia de "Element".

   data(data)

      Añade texto al elemento actual. *data* es una cadena. Debe ser
      una cadena de bytes o una cadena Unicode.

   end(tag)

      Cierra el elemento actual. *tag* es el nombre del elemento.
      Retorna el elemento cerrado.

   start(tag, attrs)

      Abre un nuevo elemento. *tag* es el nombre del elemento. *attrs*
      es un diccionario que contiene los atributos del elemento.
      Retorna el elemento abierto.

   comment(text)

      Crea un comentario con el *texto* dado. Si "insert_comments" es
      verdadero, esto también lo añadirá al árbol.

      Added in version 3.8.

   pi(target, text)

      Creates a process instruction with the given *target* name and
      *text*. If "insert_pis" is true, this will also add it to the
      tree.

      Added in version 3.8.

   Además, un objeto "TreeBuilder" personalizado puede proporcionar
   los siguientes métodos:

   doctype(name, pubid, system)

      Maneja una declaración de doctype. *name* es el nombre del
      doctype. *pubid* es el identificador público. *system* es el
      identificador del sistema. Este método no existe en la clase por
      defecto "TreeBuilder".

      Added in version 3.2.

   start_ns(prefix, uri)

      Se llama cada vez que el analizador encuentra una nueva
      declaración de espacio de nombres, antes de la llamada de
      retorno "start()" para el elemento de apertura que lo define.
      *prefix* es "''" para el espacio de nombres por defecto y el
      nombre del prefijo del espacio de nombres declarado en caso
      contrario. *uri* es el URI del espacio de nombres.

      Added in version 3.8.

   end_ns(prefix)

      Se llama después de la llamada de retorno "end()" de un elemento
      que declaró un mapeo de prefijo de espacio de nombres, con el
      nombre del *prefijo* que salió del ámbito.

      Added in version 3.8.

class xml.etree.ElementTree.C14NWriterTarget(write, *, with_comments=False, strip_text=False, rewrite_prefixes=False, qname_aware_tags=None, qname_aware_attrs=None, exclude_attrs=None, exclude_tags=None)

   Un escritor C14N 2.0. Los argumentos son los mismos que para la
   función "canonicalize()". Esta clase no construye un árbol, sino
   que traduce los eventos de devolución de llamada directamente a una
   forma serializada utilizando la función *write*.

   Added in version 3.8.

### Objetos XMLParser

class xml.etree.ElementTree.XMLParser(*, target=None, encoding=None)

   Esta clase es el bloque de construcción de bajo nivel del módulo.
   Utiliza "xml.parsers.expat" para un análisis eficiente de XML
   basado en eventos. Puede ser alimentada con datos XML de forma
   incremental con el método "feed()", y los eventos de análisis se
   traducen en una API push - invocando callbacks en el objeto
   *target*. Si se omite *target*, se utiliza la clase estándar
   "TreeBuilder". Si se da *encoding* [1], el valor anula la
   codificación especificada en el archivo XML.

   Distinto en la versión 3.8: Parameters are now keyword-only. The
   *html* argument is no longer supported.

   close()

      Finaliza la alimentación de datos al analizador. Retorna el
      resultado de llamar al método "close()" del *target* pasado
      durante la construcción; por defecto, es el elemento del
      documento de nivel superior.

   feed(data)

      Introduce los datos en el analizador sintáctico. *data* son
      datos codificados.

   flush()

      Triggers parsing of any previously fed unparsed data, which can
      be used to ensure more immediate feedback, in particular with
      Expat >=2.6.0. The implementation of "flush()" temporarily
      disables reparse deferral with Expat (if currently enabled) and
      triggers a reparse. Disabling reparse deferral has security
      consequences; please see
      "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()" for
      details.

      Note that "flush()" has been backported to some prior releases
      of CPython as a security fix.  Check for availability of
      "flush()" using "hasattr()" if used in code running across a
      variety of Python versions.

      Added in version 3.13.

   "XMLParser.feed()" llama al método "start(tag, attrs_dict)" de
   *target* para cada etiqueta de apertura, a su método "end(tag)"
   para cada etiqueta de cierre, y los datos son procesados por el
   método "data(data)". Para más métodos de callback soportados, véase
   la clase "TreeBuilder". "XMLParser.close()" llama al método
   "close()" de *target*. "XMLParser" puede utilizarse no sólo para
   construir una estructura de árbol. Este es un ejemplo de contar la
   profundidad máxima de un archivo XML:

      >>> from xml.etree.ElementTree import XMLParser
      >>> class MaxDepth:                     # The target object of the parser
      ...     maxDepth = 0
      ...     depth = 0
      ...     def start(self, tag, attrib):   # Called for each opening tag.
      ...         self.depth += 1
      ...         if self.depth > self.maxDepth:
      ...             self.maxDepth = self.depth
      ...     def end(self, tag):             # Called for each closing tag.
      ...         self.depth -= 1
      ...     def data(self, data):
      ...         pass            # We do not need to do anything with data.
      ...     def close(self):    # Called when all data has been parsed.
      ...         return self.maxDepth
      ...
      >>> target = MaxDepth()
      >>> parser = XMLParser(target=target)
      >>> exampleXml = """
      ... <a>
      ...   <b>
      ...   </b>
      ...   <b>
      ...     <c>
      ...       <d>
      ...       </d>
      ...     </c>
      ...   </b>
      ... </a>"""
      >>> parser.feed(exampleXml)
      >>> parser.close()
      4

### Objetos XMLPullParser

class xml.etree.ElementTree.XMLPullParser(events=None)

   Un analizador sintáctico pull adecuado para aplicaciones no
   bloqueantes. Su API de entrada es similar a la de "XMLParser", pero
   en lugar de enviar llamadas a un objetivo de devolución de llamada,
   "XMLPullParser" recoge una lista interna de eventos de análisis y
   permite al usuario leer de ella. *events* son una secuencia de
   eventos a reportar. Los eventos soportados son las cadenas
   ""start"", ""end"", ""comment"", ""pi"", ""start-ns"" y ""end-ns""
   (los eventos "ns" se utilizan para obtener información detallada
   del espacio de nombres). Si se omite *events*, sólo se informará de
   los eventos ""end"".

   feed(data)

      Introduce los datos de los bytes dados en el analizador.

   flush()

      Triggers parsing of any previously fed unparsed data, which can
      be used to ensure more immediate feedback, in particular with
      Expat >=2.6.0. The implementation of "flush()" temporarily
      disables reparse deferral with Expat (if currently enabled) and
      triggers a reparse. Disabling reparse deferral has security
      consequences; please see
      "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()" for
      details.

      Note that "flush()" has been backported to some prior releases
      of CPython as a security fix.  Check for availability of
      "flush()" using "hasattr()" if used in code running across a
      variety of Python versions.

      Added in version 3.13.

   close()

      Señala al analizador que el flujo de datos ha terminado. A
      diferencia de "XMLParser.close()", este método siempre retorna
      "None". Cualquier evento que no haya sido recuperado cuando el
      analizador se cierra puede ser leído con "read_events()".

   read_events()

      Retorna un iterador sobre los eventos que se han encontrado en
      los datos alimentados al analizador. El iterador retorna pares
      "(event, elem)", donde *event* es una cadena de caracteres que
      representa el tipo de evento (por ejemplo, ""fin"") y *elem* es
      el objeto "Element" encontrado, u otro valor de contexto como el
      siguiente.

      * "start", "end": el Element actual.

      * "comment", "pi": el comentario / la instrucción de
        procesamiento actual

      * "start-ns": una tupla "(prefix, uri)" que nombra el mapeo del
        espacio de nombres declarado.

      * "end-ns": "None" (esto puede cambiar en una versión futura)

      Los eventos proporcionados en una llamada anterior a
      "read_events()" no serán retornados nuevamente. Los eventos se
      consumen de la cola interna sólo cuando se recuperan del
      iterador, por lo que múltiples lectores iterando en paralelo
      sobre iteradores obtenidos de "read_events()" tendrán resultados
      impredecibles.

   Nota:

     "XMLPullParser" sólo garantiza que ha visto el carácter ">" de
     una etiqueta de inicio cuando emite un evento "start", por lo que
     los atributos están definidos, pero el contenido de los atributos
     text y tail está indefinido en ese momento. Lo mismo ocurre con
     los hijos del elemento; pueden estar presentes o no.Si necesita
     un elemento totalmente poblado, busque los eventos "end" en su
     lugar.

   Added in version 3.4.

   Distinto en la versión 3.8: Los eventos "comment" y "pi" han sido
   añadidos.

### Excepciones

class xml.etree.ElementTree.ParseError

   Error de análisis de XML, lanzado por los distintos métodos de
   análisis de este módulo cuando el análisis falla. La representación
   en cadena de caracteres de una instancia de esta excepción
   contendrá un mensaje de error fácil de entender. Además, tendrá los
   siguientes atributos disponibles:

   code

      Un código de error numérico del analizador sintáctico expat.
      Consulte la documentación de "xml.parsers.expat" para ver la
      lista de códigos de error y sus significados.

   position

      Una tupla de números de *line*, *column*, que especifica dónde
      se produjo el error.

-[ Notas al pie de página ]-

[1] La cadena de caracteres de codificación incluida en la salida XML
    debe ajustarse a los estándares adecuados. Por ejemplo, "UTF-8" es
    válido, pero "UTF8" no lo es. Consulte https://www.w3.org/TR/2006
    /REC-xml11-20060816/#NT-EncodingDecl y
    https://www.iana.org/assignments/character-sets/character-
    sets.xhtml.
