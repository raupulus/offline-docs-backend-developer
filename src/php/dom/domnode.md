---
title: La clase DOMNode
source_url: https://www.php.net/manual/es/class.domnode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 3a5f43224
order: 14120
---

## Sinopsis de la clase

DOMNode

Constantes

public

const

int

DOMNode::DOCUMENT_POSITION_DISCONNECTED

0x1

public

const

int

DOMNode::DOCUMENT_POSITION_PRECEDING

0x2

public

const

int

DOMNode::DOCUMENT_POSITION_FOLLOWING

0x4

public

const

int

DOMNode::DOCUMENT_POSITION_CONTAINS

0x8

public

const

int

DOMNode::DOCUMENT_POSITION_CONTAINED_BY

0x10

public

const

int

DOMNode::DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

0x20

Propiedades

public

readonly

string

nodeName

public

string

null

nodeValue

public

readonly

int

nodeType

public

readonly

DOMNode

null

parentNode

public

readonly

DOMElement

null

parentElement

public

readonly

DOMNodeList

childNodes

public

readonly

DOMNode

null

firstChild

public

readonly

DOMNode

null

lastChild

public

readonly

DOMNode

null

previousSibling

public

readonly

DOMNode

null

nextSibling

public

readonly

DOMNamedNodeMap

null

attributes

public

readonly

bool

isConnected

public

readonly

DOMDocument

null

ownerDocument

public

readonly

string

null

namespaceURI

public

string

prefix

public

readonly

string

null

localName

public

readonly

string

null

baseURI

public

string

textContent

Métodos

## Constantes predefinidas

`DOMNode::DOCUMENT_POSITION_DISCONNECTED`  
Definido cuando el otro nódo y el nódo de referencia no están en el mismo árbol.

`DOMNode::DOCUMENT_POSITION_PRECEDING`  
Definido cuando el otro nódo precede al nódo de referencia.

`DOMNode::DOCUMENT_POSITION_FOLLOWING`  
Definido cuando el otro nódo sigue al nódo de referencia.

`DOMNode::DOCUMENT_POSITION_CONTAINS`  
Definido cuando el otro nódo es un ancestro del nódo de referencia.

`DOMNode::DOCUMENT_POSITION_CONTAINED_BY`  
Definido cuando el otro nódo es un descendiente del nódo de referencia.

`DOMNode::DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC`  
Definido cuando el resultado depende de un comportamiento específico de la implementación y puede no ser portable. Esto puede ocurrir con nódulos desconectados o con nódulos de atributos.

## Propiedades

`nodeName`  
Devuelve el nombre más preciso para el tipo de nódo actual.

`nodeValue`  
El valor de este nódo, según su tipo. A diferencia de las especificaciones W3C, el valor del nódo de los nódulos `DOMElement` es igual a [DOMNode::textContent](#domnode.props.textcontent) en lugar de `null`.

`nodeType`  
Recupera el tipo del nódo. Una de las constantes predefinidas `XML_*_NODE`

`parentNode`  
El padre de este nódo. Si este tipo de nódo no existe, esto devolverá `null`.

`parentElement`  
El elemento padre de este elemento. Si no hay tal elemento, esto devuelve `null`.

`childNodes`  
Un `DOMNodeList` que contiene todos los hijos de este nódo. Si no hay hijos, será un `DOMNodeList` vacío.

`firstChild`  
El primer hijo de este nódo. Si no hay nódo de este tipo, devuelve `null`.

`lastChild`  
El último hijo de este nódo. Si no hay nódo de este tipo, devuelve `null`.

`previousSibling`  
El nódo que precede inmediatamente a este nódo. Si no hay nódo, devuelve `null`.

`nextSibling`  
El nódo que sigue inmediatamente a este nódo. Si no hay nódo, devuelve `null`.

`attributes`  
Un `DOMNamedNodeMap` que contiene los atributos de este nódo (si es un `DOMElement`) o `null` en caso contrario.

`isConnected`  
Si el nódo está conectado a un documento o no.

`ownerDocument`  
El objeto `DOMDocument` asociado con este nódo, o `null` si este nódo no tiene un documento asociado (p. ej., si está separado o es un `DOMDocument`).

`namespaceURI`  
El espacio de nombres de la URL para este nódo, o `null` si no está especificado.

`prefix`  
El prefijo del espacio de nombres de este nódo.

`localName`  
Devuelve la parte local del nombre cualificado del nódo.

`baseURI`  
La base de la URL absoluta del nódo, o `null` si la implementación no ha logrado obtener la URL absoluta.

`textContent`  
El contenido textual de este nódo y sus descendientes.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El método DOMNode::compareDocumentPosition ha sido añadido. |
| 8.4.0 | Las constantes `DOMNode::DOCUMENT_POSITION_DISCONNECTED`, `DOMNode::DOCUMENT_POSITION_PRECEDING`, `DOMNode::DOCUMENT_POSITION_FOLLOWING`, `DOMNode::DOCUMENT_POSITION_CONTAINS`, `DOMNode::DOCUMENT_POSITION_CONTAINED_BY`, y `DOMNode::DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC` han sido añadidas. |
| 8.3.0 | Los métodos DOMNode::contains y DOMNode::isEqualNode han sido añadidos. |
| 8.3.0 | Las propiedades DOMNode::\$parentElement, y DOMNode::\$isConnected han sido añadidas. |
| 8.0.0 | Los métodos no implementados DOMNode::compareDocumentPosition, DOMNode::isEqualNode, DOMNode::getFeature, DOMNode::setUserData y DOMNode::getUserData han sido eliminados. |

## Notas

> [!NOTE]
> La extensión DOM utiliza el codificado UTF-8. Utilice `mb_convert_encoding`, UConverter::transcode, o `iconv` para manipular otros codificados.

## Véase también

[La especificación W3C de un nódo](http://www.w3.org/TR/2003/WD-DOM-Level-3-Core-20030226/DOM3-Core.html#core-ID-1950641247)
