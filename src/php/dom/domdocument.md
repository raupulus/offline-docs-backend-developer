---
title: La clase DOMDocument
source_url: https://www.php.net/manual/es/class.domdocument.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: d75a54118
order: 13320
---

## Introducción

Representa un documento HTML o XML completo; será la raíz del árbol del documento.

## Sinopsis de la clase

DOMDocument

extends

DOMNode

implements

DOMParentNode

Constantes heredadas

Propiedades

public

readonly

DOMDocumentType

null

doctype

public

readonly

DOMImplementation

implementation

public

readonly

DOMElement

null

documentElement

public

readonly

string

null

actualEncoding

public

string

null

encoding

public

readonly

string

null

xmlEncoding

public

bool

standalone

public

bool

xmlStandalone

public

string

null

version

public

string

null

xmlVersion

public

bool

strictErrorChecking

public

string

null

documentURI

public

readonly

mixed

config

public

bool

formatOutput

public

bool

validateOnParse

public

bool

resolveExternals

public

bool

preserveWhiteSpace

public

bool

recover

public

bool

substituteEntities

public

readonly

DOMElement

null

firstElementChild

public

readonly

DOMElement

null

lastElementChild

public

readonly

int

childElementCount

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`actualEncoding`  
*Obsoleto a partir de PHP 8.4.0*. La codificación actual del documento, en lectura única, equivalente a `encoding`.

`childElementCount`  
El número de elementos hijos.

`config`  
*Obsoleto a partir de PHP 8.4.0*. Configuración utilizada cuando `DOMDocument::normalizeDocument` es llamado.

`doctype`  
La Declaración de Tipo de Documento asociada con este documento.

`documentElement`  
El objeto `DOMElement` que es el primer elemento del documento. Si no se encuentra, esto se evalúa a `null`.

`documentURI`  
La localización del documento, o `null` si indefinido.

`encoding`  
La codificación del documento, tal como se especifica en la declaración XML. Este atributo no está presente en la especificación DOM Nivel 3 final, pero representa la única manera de manipular la codificación del documento XML en esta implementación.

`firstElementChild`  
Primer elemento hijo o `null`.

`formatOutput`  
Formatea elegantemente el resultado con una indentación y espacios adicionales. Este parámetro no tiene ningún efecto si el documento ha sido cargado con la activación de `preserveWhiteSpace`.

`implementation`  
El objeto `DOMImplementation` que gestiona este documento.

`lastElementChild`  
Último elemento hijo o `null`.

`preserveWhiteSpace`  
No eliminar los espacios redundantes. Por omisión, `true`. Definir este parámetro a `false` tiene el mismo efecto de definir a `LIBXML_NOBLANKS` el parámetro `option` del método DOMDocument::load.

`recover`  
*Propietario*. Activa el modo "recovery", es decir, intenta analizar un documento mal formado. Este atributo no forma parte de la especificación DOM y es específico de libxml.

`resolveExternals`  
Defínase a `true` para cargar entidades externas desde la declaración doctype. Es útil para incluir entidades en sus documentos XML.

`standalone`  
*Obsoleto*. Si el documento es "standalone" o no, tal como se especifica en la declaración XML, correspondiente a `xmlStandalone`.

`strictErrorChecking`  
Lanza una `DOMException` en caso de error. Por omisión, `true`.

`substituteEntities`  
*Propietario*. Si se deben o no sustituir las entidades. Este atributo no forma parte de la especificación DOM y es específico de libxml. Por omisión, `false`

> [!CAUTION]
> Activar la sustitución de entidades puede facilitar los ataques XML External Entity (XXE).

`validateOnParse`  
Carga y valida la DTD. Por omisión, `false`.

> [!CAUTION]
> Activar la validación del DTD puede facilitar los ataques XML External Entity (XXE).

`version`  
*Obsoleto*. Versión del XML, corresponde a `xmlVersion`.

`xmlEncoding`  
Un atributo especificando la codificación del documento. Es `null` cuando la codificación no está especificada, o cuando es desconocida, como es el caso cuando el documento ha sido creado en memoria.

`xmlStandalone`  
Un atributo especificando si el documento es "standalone". Es `false` cuando no está especificado. Un documento standalone es un documento donde no hay declaraciones de marcado externas. Un ejemplo de tal declaración de marcado es cuando la DTD declara un atributo con un valor por omisión.

`xmlVersion`  
Un atributo especificando el número de versión del documento. Si no hay declaración y si el documento soporta la funcionalidad "XML", el valor será "1.0".

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `actualEncoding` y `config` son ahora formalmente deprecados. |
| 8.0.0 | `DOMDocument` implementa ahora DOMParentNode. |
| 8.0.0 | El método no implementado DOMDocument::renameNode ha sido retirado. |

## Notas

> [!NOTE]
> La extensión DOM utiliza el codificado UTF-8. Utilice `mb_convert_encoding`, UConverter::transcode, o `iconv` para manipular otros codificados.

> [!NOTE]
> Al utilizar `json_encode` sobre un objeto `DOMDocument` el resultado será el de codificar un objeto vacío.

## Véase también

[Especificación W3C de Document](http://www.w3.org/TR/2003/WD-DOM-Level-3-Core-20030226/DOM3-Core.html#core-i-Document)
