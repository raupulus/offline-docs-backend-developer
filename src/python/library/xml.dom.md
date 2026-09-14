---
title: '"xml.dom" --- The Document Object Model API'
source_url: https://docs.python.org/es/3
source_path: library/xml.dom.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4590
---

# "xml.dom" --- The Document Object Model API

**Código Fuente:** Lib/xml/dom/__init__.py

======================================================================

El Modelo de Objetos del Documento, o "DOM" por sus siglas en inglés,
es un lenguaje API del Consorcio *World Wide Web* (W3C) para acceder y
modificar documentos XML. Una implementación del DOM presenta los
documento XML como un árbol, o permite al código cliente construir
dichas estructuras desde cero para luego darles acceso a la estructura
a través de un conjunto de objetos que implementaron interfaces
conocidas.

El DOM es extremadamente útil para aplicaciones de acceso directo. SAX
sólo te permite la vista de una parte del documento a la vez. Si estás
mirando un elemento SAX, no tienes acceso a otro. Si estás viendo un
nodo de texto, no tienes acceso al elemento contenedor. Cuando
desarrollas una aplicación SAX, necesitas registrar la posición de tu
programa en el documento en algún lado de tu código. SAX no lo hace
por ti. Además, desafortunadamente no podrás mirar hacia adelante
(*look ahead*) en el documento XML.

Algunas aplicaciones son imposibles en un modelo orientado a eventos
sin acceso a un árbol. Por supuesto que puedes construir algún tipo de
árbol por tu cuenta en eventos SAX, pero el DOM te evita escribir ese
código. El DOM es una representación de árbol estándar para datos XML.

El Modelo de Objetos del Documento es definido por el *W3C* en fases,
o "niveles" en su terminología. El mapeado de Python de la API está
basado en la recomendación del DOM nivel 2.

Las aplicaciones DOM típicamente empiezan al diseccionar (*parse*) el
XML en un DOM. Cómo esto funciona no está incluido en el DOM nivel 1,
y el nivel 2 provee mejoras limitadas. Existe una clase objeto llamada
"DOMImplementation" que da acceso a métodos de creación de "Document",
pero de ninguna forma da acceso a los constructores (*builders*) de
*reader*/*parser*/*Document* de una forma independiente a la
implementación. No hay una forma clara para acceder a estos método sin
un objeto "Document" existente. En Python, cada implementación del DOM
proporcionará una función "getDOMImplementation()". El DOM de nivel 3
añade una especificación para Cargar(*Load*)/Guardar(*Store*), que
define una interfaz al lector (*reader*), pero no está disponible aún
en la librería estándar de Python.

Una vez que tengas un objeto del documento del DOM, puedes acceder a
las partes de tu documento XML a través de sus propiedades y métodos.
Estas propiedades están definidas en la especificación del DOM; está
porción del manual describe la interpretación de la especificación en
Python.

La especificación estipulada por el *W3C* define la *DOM API* para
Java, ECMAScript, y OMG IDL. El mapeo de Python definido aquí está
basado en gran parte en la versión IDL de la especificación, pero no
se requiere el cumplimiento estricto (aunque las implementaciones son
libres de soportar el mapeo estricto de IDL). Véase la sección
Conformidad para una discusión detallada del mapeo de los requisitos.

Ver también:

  Document Object Model (DOM) Level 2 Specification
     La recomendación del *W3C* con la cual se basa el *DOM API* de
     Python.

  Document Object Model (DOM) Level 1 Specification
     La recomendación del W3C para el DOM soportada por
     "xml.dom.minidom".

  Python Language Mapping Specification
     Este documento especifica el mapeo de OMG IDL a Python.

## Contenido del módulo

The "xml.dom" contains the following functions:

xml.dom.registerDOMImplementation(name, factory)

   Registra la función *factory* con el nombre *name*. La función
   fábrica (*factory*) debe retornar un objeto que implemente la
   interfaz "DOMImplementation". La función fábrica puede retornar el
   mismo objeto cada vez que se llame, o uno nuevo por cada llamada,
   según sea apropiado para la implementación específica (e.g. si la
   implementación soporta algunas personalizaciones).

xml.dom.getDOMImplementation(name=None, features=())

   Retorna una implementación del DOM apropiada. El *name* es o bien
   conocido, el nombre del módulo de una implementación DOM, o "None".
   Si no es "None" importa el módulo correspondiente y retorna un
   objeto "DomImplementation" si la importación tiene éxito. Si no se
   le pasa un nombre, y el entorno de variable "PYTHON_DOM" ha sido
   puesto, dicha variable es usada para encontrar la información de la
   implementación.

   Si no se le pasa un nombre, examina las implementaciones
   disponibles para encontrar uno con el conjunto de características
   requeridas. Si no se encuentra ninguna implementación, lanza una
   excepción "ImportError". La lista de características debe ser una
   secuencia de pares "(feature,version)" que son pasados al método
   "hasFeature()" en objetos disponibles de "DOMImplementation".

Algunas constantes convenientes son proporcionadas:

xml.dom.EMPTY_NAMESPACE

   El valor usado para indicar que ningún espacio de nombres es
   asociado con un nodo en el DOM. Se encuentra típicamente con el
   "namespaceURI" de un nodo, o usado como el parámetro
   *namespaceURI* para un método específico del *namespace*.

xml.dom.XML_NAMESPACE

   El espacio de nombres de la URI asociada con el prefijo "xml", como
   se define por Namespaces in XML (sección 4).

xml.dom.XMLNS_NAMESPACE

   El espacio de nombres del URI para declaraciones del espacio de
   nombres, como se define en Document Object Model (DOM) Level 2 Core
   Specification (sección 1.1.8).

xml.dom.XHTML_NAMESPACE

   El URI del espacio de nombres del XHTML como se define en XHTML
   1.0: The Extensible HyperText Markup Language (sección 3.1.1).

In addition, "xml.dom" contains a base "Node" class and the DOM
exception classes.  The "Node" class provided by this module does not
implement any of the methods or attributes defined by the DOM
specification; concrete DOM implementations must provide those.  The
"Node" class provided as part of this module does provide the
constants used for the "nodeType" attribute on concrete "Node"
objects; they are located within the class rather than at the module
level to conform with the DOM specifications.

## Objetos en el DOM

La documentación definitiva para el DOM es la especificación del DOM
del W3C.

Note que los atributos del DOM también pueden ser manipulados como
nodos en vez de simples cadenas de caracteres (*strings*). Sin
embargo, es bastante raro que tengas que hacer esto, por lo que su uso
aún no está documentado.

+----------------------------------+-------------------------------------+-----------------------------------+
| Interfaz                         | Sección                             | Propósito                         |
|==================================|=====================================|===================================|
| "DOMImplementation"              | Objetos DOMImplementation           | Interfaz para las                 |
## |                                  |                                     | implementaciones subyacentes.     |

| "Node"                           | Objetos nodo                        | Interfaz base para la mayoría de  |
## |                                  |                                     | objetos en un documento.          |

| "NodeList"                       | Objetos NodeList                    | Interfaz para una secuencia de    |
## |                                  |                                     | nodos.                            |

| "DocumentType"                   | Objetos DocumentType                | Información acerca de la          |
|                                  |                                     | declaraciones necesarias para     |
## |                                  |                                     | procesar un documento.            |

| "Document"                       | Objetos documento                   | Objeto que representa un          |
## |                                  |                                     | documento entero.                 |

| "Element"                        | Objetos elemento                    | Nodos elemento en la jerarquía    |
## |                                  |                                     | del documento.                    |

| "Attr"                           | Objetos atributo                    | Nodos de los valores de los       |
## |                                  |                                     | atributos en los elementos nodo.  |

| "Comment"                        | Objetos comentario                  | Representación de los comentarios |
## |                                  |                                     | en el documento fuente.           |

| "Text"                           | Objetos Texto y CDATASection        | Nodos con contenido textual del   |
## |                                  |                                     | documento.                        |

| "ProcessingInstruction"          | Objetos ProcessingInstruction       | Representación de instrucción del |
## |                                  |                                     | procesamiento.                    |

Una sección adicional describe las excepciones definidas para trabajar
con el *DOM* en Python.

### Objetos *DOMImplementation*

La interfaz "DOMImplementation" proporciona una forma para que las
aplicaciones determinen la disponibilidad de características
particulares en el *DOM* que están usando. El *DOM* nivel 2 añadió la
habilidad de crear nuevos objetos "Document" y "DocumentType" usando
"DOMImplementation" también.

DOMImplementation.hasFeature(feature, version)

   Retorna "True" si la característica identificada por el par de
   cadenas de caracteres *feature* y *version* está implementada.

DOMImplementation.createDocument(namespaceUri, qualifiedName, doctype)

   Retorna un nuevo objeto "Document" (la raíz del DOM), con un hijo
   objeto "Element" teniendo el *namespaceUri* y *qualifiedName*
   dados. El *doctype* debe ser un "DocumentType" creado por
   "createDocumentType()" o "None". En la *DOM API* de Python, los
   primeros argumentos pueden ser "None" para indicar que ningún hijo
   "Element" va a ser creado.

DOMImplementation.createDocumentType(qualifiedName, publicId, systemId)

   Retorna un nuevo objeto "DocumentType" que encapsula las cadenas de
   caracteres *qualifiedName*, *publicId*, y *systemId* dadas,
   representando la información contenida en un tipo de declaración de
   documento XML.

### Objetos nodo

Todos los componentes de un documento XML son sub-clases de "Node".

Node.nodeType

   Un entero representando el tipo de nodo.  Las Constantes simbólicas
   para los tipos están en el objeto "Nodo": "ELEMENT_NODE",
   "ATTRIBUTE_NODE", "TEXT_NODE", "CDATA_SECTION_NODE", "ENTITY_NODE",
   "PROCESSING_INSTRUCTION_NODE", "COMMENT_NODE", "DOCUMENT_NODE",
   "DOCUMENT_TYPE_NODE", "NOTATION_NODE". Este es un atributo sólo de
   lectura.

Node.parentNode

   El padre del nodo actual, o "None" para el nodo del documento. El
   valor es siempre un objeto "Node" o "None". Para los nodos
   "Element", este será el elemento padre, excepto para el elemento
   raíz, en cuyo caso será el objeto "Document". Para los nodos
   "Attr", este siempre es "None". Este es un atributo de sólo
   lectura.

Node.attributes

   Un "NamedNodeMap" de objetos de atributos. Sólo los elementos
   tienes un valor real para esto; otros nodos proporcionan "None"
   para este atributo. Este es un atributo de sólo lectura.

Node.previousSibling

   El nodo que precede inmediatamente este nodo con el mismo padre.
   Por ejemplo el elemento con una etiqueta final que viene justo
   antes de la etiqueta del comienzo del elemento *self*.  Por
   supuesto, los documentos XML está hechos de más que sólo elementos
   por lo que el hermano anterior puede ser un texto, un comentario, o
   algo más. Si este nodo es el primer hijo del padre, este atributo
   será "None". Este es un atributo de sólo lectura.

Node.nextSibling

   El nodo que sigue inmediatamente este nodo con el mismo padre.
   Véase también "previousSibling". Si este es el último hijo del
   padre, este atributo será "None". Este es un atributo de sólo
   lectura.

Node.childNodes

   Una lista de nodos contenidos dentro de este nodo. Este es un
   atributo de sólo lectura.

Node.firstChild

   El primer hijo del nodo, si hay alguno, o "None". Este es un
   atributo de sólo lectura.

Node.lastChild

   El último hijo del nodo, si hay alguno, o "None". Este es un
   atributo de sólo lectura.

Node.localName

   La parte del "tagName" seguido de los dos puntos si hay uno, si no,
   el "tagName" entero.  El valor es una cadena de caracteres.

Node.prefix

   La parte del "tagName" antes de los dos puntos si hay uno, si no,
   la cadena de caracteres vacía. El valor es una cadena, o "None".

Node.namespaceURI

   El espacio de nombres asociado con el nombre del elemento.  Este
   será una cadena de caracteres o "None".  Este es una atributo de
   sólo lectura.

Node.nodeName

   Este tiene un significado diferente para cada tipo de nodo; véase
   la especificación del DOM para los detalles.  Siempre puedes
   obtener la información que obtendrías aquí desde otra propiedad
   como la propiedad "tagName" para elementos o la propiedad "name"
   para atributos. Para todos los tipos de nodo, el valor de este
   atributo tendrá o una cadena de caracteres o "None". Este es un
   atributo de sólo lectura.

Node.nodeValue

   Este tiene un significado diferente para cada tipo de nodo; véase
   la especificación del DOM para los detalles.  La situación es
   similar a ese con "nodeName".  El valor es una cadena de caracteres
   o "None".

Node.hasAttributes()

   Retorna "True" si el nodo tiene algún atributo.

Node.hasChildNodes()

   Retorna "True" si el nodo tiene algún nodo hijo.

Node.isSameNode(other)

   Retorna "True" si *other* hace referencia al mismo nodo como este
   nodo. Esto es especialmente útil para las implementaciones DOM que
   usan una arquitectura *proxy* de cualquier tipo (porque más de un
   objeto puede hacer referencia al mismo nodo).

   Nota:

     Esto se basa en una *DOM API* de nivel 3 propuesta que está en la
     etapa de "borrador de trabajo" (*"working draft"*), pero esta
     interfaz en particular no parece controversial.  Los cambios del
     *W3C* necesariamente no afectaran este método en la interfaz del
     *DOM* del Python (aunque cualquier nueva *API* del *W3C* para
     esto también sería soportado).

Node.appendChild(newChild)

   Añade un nuevo nodo hijo a este nodo al final de la lista de hijos,
   retornando *newChild*. Si el nodo ya estaba en el árbol, este se
   remueve primero.

Node.insertBefore(newChild, refChild)

   Inserta un nuevo nodo hijo antes de un hijo existente.  Debe ser el
   caso que *refChild* sea un hijo de este nodo; si no, "ValueError"
   es lanzado. *newChild* es retornado. Si *refChild* es "None", se
   inserta a *newChild* al final de la lista de hijos.

Node.removeChild(oldChild)

   Elimina un nodo hijo.  *oldChild* debe ser un hijo de este nodo; si
   no, "ValueError" es lanzado.  *oldChild* es retornado si tiene
   éxito.  Si *oldChild* no será usado más adelante, se debe llamar a
   su método "unlink()".

Node.replaceChild(newChild, oldChild)

   Reemplaza un nodo existente con un nuevo nodo. Debe ser el caso que
   *oldChild* sea un hijo de este nodo; si no, "ValueError" es
   lanzado.

Node.normalize()

   Une nodos de texto adyacentes para que todos los tramos de texto
   sean guardados como únicas instancias de "Text". Esto simplifica el
   procesamiento de texto de un árbol del *DOM* para muchas
   aplicaciones.

Node.cloneNode(deep)

   Clona este nodo.  Poner *deep* significa clonar todos los nodos
   hijo también.  Esto retorna el clon.

### Objetos *NodeList*

Un "NodeList" representa una secuencia de nodos.  Estos objetos se
usan de dos formas en la recomendación principal del *DOM*:  un objeto
"Element" proporciona uno como su lista de nodos hijo, y los métodos
"getElementsByTagName()" y "getElementsByTagNameNS()" de "Node"
retornan objetos con esta interfaz para representar resultados de
consulta.

La recomendación del *DOM* nivel 2 define un método y un atributo para
estos objetos:

NodeList.item(i)

   Retorna el i-ésimo *item* de la secuencia, si hay uno, o "None". El
   índice *i* no puede ser menor que cero o mayor o igual que el
   tamaño de la secuencia.

NodeList.length

   El número de nodos en la secuencia.

Además, la interfaz *DOM* de Python requiere que un algún soporte
adicional sea proporcionado para que los objetos "NodeList" puedan ser
usados como secuencias de Python.  Todas las implementaciones de
"NodeList" deben incluir soporte para "__len__()" y "__getitem__()";
esto permite la iteración de "NodeList" en sentencias con "for" y un
soporte apropiado para la función incorporada "len()".

Si una implementación DOM soporta la modificación del documento, la
implementación de "NodeList" debe también soportar los métodos
"__setitem__()" y "__delitem__()".

### Objetos *DocumentType*

La información acerca de las notaciones y entidades declaradas por un
documento (incluido el subconjunto externo si el analizador lo usa y
puede proporcionar información) está disponible desde un objeto
"DocumentType".  El "DocumentType" para un documento está disponible
desde el atributo "doctype" del objeto "Document"; si no hay ninguna
declaración "DOCTYPE" para el documento, el atributo "doctype" del
documento se pondrá como "None" en vez de una instancia de esta
interfaz.

"DocumentType" es una especialización de "Node", y añade los
siguientes atributos:

DocumentType.publicId

   El identificador público para el subconjunto externo de la
   definición del tipo de documento. Esto será una cadena de
   caracteres o "None".

DocumentType.systemId

   El identificador del sistema para el subconjunto externo de la
   definición del tipo de documento. Esto será una *URI* como una
   cadena de caracteres, o "None".

DocumentType.internalSubset

   Una cadena de caracteres proporcionando el subconjunto interno
   completo del documento. Esto no incluye los paréntesis que cierran
   el subconjunto.  Si el documento no tiene ningún subconjunto
   interno, debe ser "None".

DocumentType.name

   El nombre del elemento raíz como se indica en la declaración
   "DOCTYPE", si está presente.

DocumentType.entities

   Este es un "NamedNodeMap" proporcionando las definiciones de las
   entidades externas. Para nombres de entidades definidas más de una
   vez, sólo la primera definición es proporcionada (el resto es
   ignorado como se requiere por la recomendación de *XML*).  Puede
   ser "None" si el analizador no proporciona la información, o si
   ninguna entidad es definida.

DocumentType.notations

   Este es un "NamedNodeMap" proporcionando las definiciones de las
   notaciones. Para nombres de notaciones definidas más de una vez,
   sólo la primera definición es proporcionada (el resto es ignorado
   como se requiere por la recomendación *XML*).  Puede ser "None" si
   el analizador no proporciona la información, o si no hay notaciones
   definidas.

### Objetos documento

Un "Documento" representa un documento *XML* entero, incluyendo sus
elementos constituyentes, atributos, instrucciones de procesamiento,
comentarios, etc. Recuerda que este hereda propiedades de "Node".

Document.documentElement

   El único elemento raíz del documento.

Document.createElement(tagName)

   Crea y retorna un nuevo elemento nodo.  El elemento no se inserta
   en el documento cuando es creado.  Necesitas insertarlo
   explícitamente con uno de los otros métodos como "insertBefore()" o
   "appendChild()".

Document.createElementNS(namespaceURI, tagName)

   Crea y retorna un nuevo elemento con un espacio de nombres.  El
   *tagName* puede tener un prefijo.  El elemento no se inserta en el
   documento cuando es creado.  Necesitas insertarlo explícitamente
   con uno de los otros métodos como "insertBefore()" o
   "appendChild()".

Document.createTextNode(data)

   Crea y retorna un nodo texto conteniendo los datos pasados como
   parámetros,  Como con los otros métodos de creación, este no
   inserta el nodo en el árbol.

Document.createComment(data)

   Crea y retorna un nodo comentario conteniendo los datos pasados
   como parámetros.  Como con los otros métodos de creación, este no
   inserta el nodo en el árbol.

Document.createProcessingInstruction(target, data)

   Crea y retorna una instrucción de procesamiento conteniendo el
   *target* y *data* pasados como parámetros.  Como con los otros
   métodos de creación, este no inserta en nodo en el árbol.

Document.createAttribute(name)

   Crea y retorna un nodo atributo.  Este método no asocia el nodo
   atributo con ningún elemento particular.  Debes usar
   "setAttributeNode()" en el objeto "Element" apropiado para usar la
   instancia del atributo recién creada.

Document.createAttributeNS(namespaceURI, qualifiedName)

   Crea y retorna un nodo atributo con un espacio de nombres.  El
   *tagName* puede ser un prefijo.  Este método no asocia el nodo
   atributo con ningún elemento en particular.  Debes usar
   "setAttributeNode()" en el objeto "Element" apropiado para usar la
   instancia del atributo recién creada.

Document.getElementsByTagName(tagName)

   Busca todos los descendientes (hijos directos, hijos de los hijos,
   etc.) con un nombre del tipo de elemento particular.

Document.getElementsByTagNameNS(namespaceURI, localName)

   Busca todos los descendientes (hijos directos, hijos de hijos,
   etc.) con un espacio de nombres URI particular (*namespaceURI*) y
   nombre local (*localname*). El nombre local es parte del espacio de
   nombres después del prefijo.

### Objetos elemento

"Element" es una subclase de "Node", por lo que hereda todos los
atributos de esa clase.

Element.tagName

   El nombre del tipo de elemento.  En un documento que usa espacios
   de nombres este puede tener varios dos puntos en el. El valor es
   una cadena de caracteres.

Element.getElementsByTagName(tagName)

   Igual al método equivalente en la clase "Document".

Element.getElementsByTagNameNS(namespaceURI, localName)

   Igual al método equivalente en la clase "Document".

Element.hasAttribute(name)

   Retorna "True" si el elemento tiene un atributo nombrado *name*.

Element.hasAttributeNS(namespaceURI, localName)

   Retorna "True" si el elemento tiene un atributo nombrado por
   *namespaceURI* y *localName*.

Element.getAttribute(name)

   Retorna el valor del atributo nombrado por *name* como una cadena
   de caracteres. Si no existe dicho atributo, una cadena vacía es
   retornada, como si el atributo no tuviera valor.

Element.getAttributeNode(attrname)

   Retorna el nodo "Attr" para el atributo nombrado por *attrname*.

Element.getAttributeNS(namespaceURI, localName)

   Retorna el valor del atributo nombrado por *namespaceURI* y
   *localName* como una cadena de caracteres. Si no existe dicho
   atributo, una cadena vacía es retornada, como si el atributo no
   tuviera valor.

Element.getAttributeNodeNS(namespaceURI, localName)

   Retorna un valor de atributo como nodo, dado un *namespaceURI* y
   *localName*.

Element.removeAttribute(name)

   Remueve un atributo por nombre (*name*).  Si no hay un atributo
   correspondiente, un "NotFoundErr" es lanzado.

Element.removeAttributeNode(oldAttr)

   Remueve y retorna *oldAttr* de la lista de atributos, si está
   presenta. Si *oldAttr* no está presente, "NotFoundErr" es lanzado.

Element.removeAttributeNS(namespaceURI, localName)

   Remueve un atributo por nombre (*name*).  Note que esto usa un
   *localName*, no un *qname*.  Ninguna excepción es lanzada si no
   existe el atributo correspondiente.

Element.setAttribute(name, value)

   Pone un valor de atributo como una cadena de caracteres.

Element.setAttributeNode(newAttr)

   Añade un nuevo atributo nodo al elemento, reemplazando un atributo
   existente si es necesario si el atributo "name" coincide. Si un
   reemplazo ocurre, el viejo atributo será retornado. Si *newAttr* ya
   está en uso, "InuseAttributeErr" será lanzado.

Element.setAttributeNodeNS(newAttr)

   Añade un nuevo nodo atributo al elemento, reemplazando un atributo
   existente si es necesario, si el "namesapceURI" y "localName"
   coinciden. Si un reemplazo ocurre, el viejo atributo será
   retornado.  Si *newAttr* está en uso, "InuseAttributeErr" será
   lanzado.

Element.setAttributeNS(namespaceURI, qname, value)

   Pone un valor de atributo a partir de una cadena de caracteres,
   dados un *namespaceURI* y *qname*. Note que un *qname* es el nombre
   completo del atributo. Esto es diferente al de arriba.

### Objetos atributo

"Attr" hereda de "Node", por lo que hereda todos sus atributos.

Attr.name

   El nombre del atributo. En un documento que usa espacio de nombres,
   puede incluir dos puntos.

Attr.localName

   La parte del nombre seguido después de los dos puntos si hay uno,
   si no el nombre entero. Este es un atributo de sólo lectura.

Attr.prefix

   La parte del nombre que precede los dos puntos si hay uno, si no la
   cadena de caracteres vacía.

Attr.value

   El valor textual del atributo.  Este es un sinónimo para el
   atributo "nodeValue".

### Objetos *NamedNodeMap*

"NamedNodeMap" *no* hereda de "Node".

NamedNodeMap.length

   La longitud de la lista de atributos.

NamedNodeMap.item(index)

   Retorna un atributo con un índice particular.  El orden en los que
   obtienes los atributos es arbitrario pero será consistente en la
   vida de un *DOM*. Cada *item* es un nodo atributo.  Obtén su valor
   con el atributo "value".

There are also experimental methods that give this class more mapping
behavior. You can use them or you can use the standardized
"getAttribute*()" family of methods on the "Element" objects.

### Objetos comentario

"Comment" representa un comentario en el documento *XML*.  Es una
subclase de "Node", pero no puede tener hijos nodo.

Comment.data

   El contenido del comentario como una cadena de caracteres.  El
   atributo contiene todos los caracteres entre el "<!-""-" que
   empieza y el "-""->" que termina, pero no los incluye.

### Objetos Texto y *CDATASection*

La interfaz "Text" representa el texto en el documento *XML*.  Si el
analizador y la implementación del *DOM* soporta la extensión *XML*
del *DOM*, las porciones de texto rodeadas secciones marcadas como
*CDATA* se guardan en objetos "CDATASection". Estas dos interfaces son
idénticas, pero proveen valores diferentes para el atributo
"nodeType".

Estas interfaces extienden la interfaz "Node".  No pueden tener nodos
hijo.

Text.data

   El contenido del nodo texto como una cadena de caracteres.

Nota:

  El uso de un nodo "CDATASection" no indica que el nodo represente
  una sección completa marcada como *CDATA*, sólo que el contenido del
  nodo fue parte de una sección *CDATA*.  Una sola sección *CDATA*
  puede ser representada por más de un nodo en el árbol del documento.
  No hay manera de determinar si dos nodos adyacentes "CDATASection"
  son representados diferentes a secciones marcadas como *CDATA*.

### Objetos *ProcessingInstruction*

Representa una instrucción de procesamiento en el documento *XML*;
hereda de la interfaz "Node" y no puede tener hijos.

ProcessingInstruction.target

   El contenido de la instrucción de procesamiento hasta el carácter
   en blanco. Este es un atributo de sólo lectura.

ProcessingInstruction.data

   El contenido de la instrucción de procesamiento después del primer
   carácter en blanco.

### Excepciones

La recomendación del *DOM* nivel 2 define una sola excepción,
"DOMException", y un número de constantes que permite que las
aplicaciones determinen qué tipo de error ocurrió. las instancias de
"DOMException" llevan un atributo "code" que proporciona el valor
apropiado para la excepción específica.

La interfaz *DOM* de Python provee las constantes, pero también
expande el conjunto de excepciones para que exista una excepción
específica para cada uno de los códigos de excepción definidos por el
*DOM*. Las implementaciones deben lanzar la excepción específica
apropiada, cada uno de los cuales lleva el valor apropiado para el
atributo "code".

exception xml.dom.DOMException

   Clase base de excepción usada para todas las excepciones del *DOM*
   específicas. Esta clase de excepción no puede ser instanciada
   directamente.

exception xml.dom.DomstringSizeErr

   Lanzado cuando un rango de texto específico no cabe en una cadena
   de caracteres.  No se sabe si se usa in las implementación *DOM* de
   Python, pero puede ser recibido de otras implementaciones *DOM* que
   no hayan sido escritas en Python.

exception xml.dom.HierarchyRequestErr

   Lanzado cuando se intenta insertar un nodo donde el tipo de nodo no
   es permitido.

exception xml.dom.IndexSizeErr

   Lanzado cuando un parámetro del índice o tamaño de un método es
   negativo o excede los valores permitidos.

exception xml.dom.InuseAttributeErr

   Lanzado cuando se intenta insertar un nodo "Attr" que está presente
   en algún lado en el documento.

exception xml.dom.InvalidAccessErr

   Lanzado si un parámetro o una operación no es soportada por el
   objeto subyacente.

exception xml.dom.InvalidCharacterErr

   Esta excepción es lanzada cuando un parámetro de cadena de
   caracteres contiene un carácter que no está permitido en el
   contexto que está siendo usado por la recomendación *XML 1.0*. Por
   ejemplo, intentar crear un nodo "Element" con un espacio en el
   nombre del tipo de elemento causará que se lance este error.

exception xml.dom.InvalidModificationErr

   Lanzado cuando se intenta modificar el tipo de un nodo.

exception xml.dom.InvalidStateErr

   Lanzado cuando se intenta usar un objeto que no está definido o ya
   no es usable.

exception xml.dom.NamespaceErr

   Si se intenta cambiar cualquier objeto de forma que no sea
   permitida con respecto a la recomendación Namespaces in XML, esta
   excepción es lanzada.

exception xml.dom.NotFoundErr

   Excepción cuando un nodo no existe en el contexto referenciado.
   Por ejemplo, "NamedNodeMap.removeNamedItem()" será lanzado si el
   nodo pasado no existe en el mapa.

exception xml.dom.NotSupportedErr

   Lanzado cuando la implementación no soporta el tipo requerido del
   objeto u operación.

exception xml.dom.NoDataAllowedErr

   Es lanzado si se especifican datos para un nodo que no soporta
   datos.

exception xml.dom.NoModificationAllowedErr

   Lanzado cuando se intenta modificar un objeto donde las
   modificaciones no son permitidas (tal como los nodos de sólo-
   lectura).

exception xml.dom.SyntaxErr

   Lanzado cuando se especifica una cadena de caracteres inválida o
   ilegal.

exception xml.dom.WrongDocumentErr

   Lanzado cuando un nodo es insertado en un documento diferente al
   que este actualmente pertenece, y la implementación no soporta
   migrar el nodo de un documento a otro.

Los códigos de excepción definidos en la recomendación del *DOM* se
mapean a las excepciones descritas arriba de acuerdo a esta tabla:

+----------------------------------------+-----------------------------------+
| Constante                              | Excepción                         |
|========================================|===================================|
## | "DOMSTRING_SIZE_ERR"                   | "DomstringSizeErr"                |

## | "HIERARCHY_REQUEST_ERR"                | "HierarchyRequestErr"             |

## | "INDEX_SIZE_ERR"                       | "IndexSizeErr"                    |

## | "INUSE_ATTRIBUTE_ERR"                  | "InuseAttributeErr"               |

## | "INVALID_ACCESS_ERR"                   | "InvalidAccessErr"                |

## | "INVALID_CHARACTER_ERR"                | "InvalidCharacterErr"             |

## | "INVALID_MODIFICATION_ERR"             | "InvalidModificationErr"          |

## | "INVALID_STATE_ERR"                    | "InvalidStateErr"                 |

## | "NAMESPACE_ERR"                        | "NamespaceErr"                    |

## | "NOT_FOUND_ERR"                        | "NotFoundErr"                     |

## | "NOT_SUPPORTED_ERR"                    | "NotSupportedErr"                 |

## | "NO_DATA_ALLOWED_ERR"                  | "NoDataAllowedErr"                |

## | "NO_MODIFICATION_ALLOWED_ERR"          | "NoModificationAllowedErr"        |

## | "SYNTAX_ERR"                           | "SyntaxErr"                       |

## | "WRONG_DOCUMENT_ERR"                   | "WrongDocumentErr"                |

## Conformidad

Esta sección describe los requisitos de conformidad y las relaciones
entre el *DOM API* de Python, las recomendaciones del *DOM* del *W3C*,
y el mapeo *OMG IDL* para Python.

### Mapeo de tipos

Los tipos IDL usados en la especificación del *DOM* son mapeados a los
tipos de tipos de Python de acuerdo a la siguiente tabla.

+--------------------+---------------------------------------------+
| Tipo IDL           | Tipo en Python                              |
|====================|=============================================|
## | "boolean"          | "bool" o "int"                              |

## | "int"              | "int"                                       |

## | "long int"         | "int"                                       |

## | "unsigned int"     | "int"                                       |

## | "DOMString"        | "str" o "bytes"                             |

## | "null"             | "None"                                      |

### Métodos de acceso (*accessor*)

El mapeo de *OMG IDL* a python define funciones de acceso para las
declaraciones del atributo *IDL* de la que misma forma en que el mapeo
de Java lo hace. Mapear las declaraciones IDL:

   readonly attribute string someValue;
            attribute string anotherValue;

produce tres funciones de acceso:  un método "get" para "someValue"
("_get_someValue()"), y métodos "get" y "set" para "anotherValue"
("_get_anotherValue()" y "_set_anotherValue()"). El mapeado, en
particular, no requiere que los atributos *IDL* sean accesibles como
los atributos normales de Python:  No es obligatorio que
"object.someValue" funcione, y puede lanzar un "AttributeError".

El *DOM API* de Python, sin embargo, *si* requiere que los atributos
de acceso normales funcionen. Esto significa que no es probable que
los típicos sustitutos generados por compiladores de *IDL* en Python
funcionen, y los objetos envoltorio (*wrapper*) pueden ser necesarios
en el cliente si los objetos del *DOM* son accedidos mediante *CORBA*.
Mientras que esto requiere consideraciones adicionales para clientes
*DOM* en *CORBA*, los implementadores con experiencia que usen *DOM*
por encima de *CORBA* desde Python no lo consideran un problema.  Los
atributos que se declaran "readonly" pueden no restringir el acceso de
escritura en todas las implementaciones DOM.

En el *DOM API* de Python, las funciones de acceso no son
obligatorias. Si se proveen, deben tomar la forma definida por el
mapeo *IDL* de Python, pero estos métodos se consideran innecesarios
debido a que los atributos son accesibles directamente desde Python.
Nunca se deben proporcionar métodos de acceso (*accessor*) "Set" para
los atributos "readonly".

Las definiciones de IDL no encarnan los requisitos del *DOM API* del
*W3C* por completo, como las nociones de ciertos objetos, como el
valor de retorno "getElementsByTagName()", siendo "live". El DOM API
de Python no requiere que las implementaciones hagan cumplir tales
requisitos.
