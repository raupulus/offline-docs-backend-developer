---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/dom.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: a8b6f4dd3
order: 12090
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

| Constantes | Valor | Descripción |
|----|----|----|
| `XML_ELEMENT_NODE` (`int`) | 1 | El nodo es un `DOMElement` / `Dom\Element` |
| `XML_ATTRIBUTE_NODE` (`int`) | 2 | El nodo es un `DOMAttr` / `Dom\Attr` |
| `XML_TEXT_NODE` (`int`) | 3 | El nodo es un `DOMText` / `Dom\Text` |
| `XML_CDATA_SECTION_NODE` (`int`) | 4 | El nodo es un `DOMCharacterData` / `Dom\CharacterData` |
| `XML_ENTITY_REF_NODE` (`int`) | 5 | El nodo es un `DOMEntityReference` / `Dom\EntityReference` |
| `XML_ENTITY_NODE` (`int`) | 6 | El nodo es un `DOMEntity` / `Dom\Entity` |
| `XML_PI_NODE` (`int`) | 7 | El nodo es un `DOMProcessingInstruction` / `Dom\ProcessingInstruction` |
| `XML_COMMENT_NODE` (`int`) | 8 | El nodo es un `DOMComment` / `Dom\Comment` |
| `XML_DOCUMENT_NODE` (`int`) | 9 | El nodo es un `DOMDocument` / `Dom\Document` |
| `XML_DOCUMENT_TYPE_NODE` (`int`) | 10 | El nodo es un `DOMDocumentType` / `Dom\DocumentType` |
| `XML_DOCUMENT_FRAG_NODE` (`int`) | 11 | El nodo es un `DOMDocumentFragment` / `Dom\DocumentFragment` |
| `XML_NOTATION_NODE` (`int`) | 12 | El nodo es un `DOMNotation` / `Dom\Notation` |
| `XML_HTML_DOCUMENT_NODE` (`int`) | 13 |  |
| `XML_DTD_NODE` (`int`) | 14 |  |
| `XML_ELEMENT_DECL_NODE` (`int`) | 15 |  |
| `XML_ATTRIBUTE_DECL_NODE` (`int`) | 16 |  |
| `XML_ENTITY_DECL_NODE` (`int`) | 17 |  |
| `XML_NAMESPACE_DECL_NODE` (`int`) | 18 |  |
| `XML_ATTRIBUTE_CDATA` (`int`) | 1 |  |
| `XML_ATTRIBUTE_ID` (`int`) | 2 |  |
| `XML_ATTRIBUTE_IDREF` (`int`) | 3 |  |
| `XML_ATTRIBUTE_IDREFS` (`int`) | 4 |  |
| `XML_ATTRIBUTE_ENTITY` (`int`) | 5 |  |
| `XML_ATTRIBUTE_NMTOKEN` (`int`) | 7 |  |
| `XML_ATTRIBUTE_NMTOKENS` (`int`) | 8 |  |
| `XML_ATTRIBUTE_ENUMERATION` (`int`) | 9 |  |
| `XML_ATTRIBUTE_NOTATION` (`int`) | 10 |  |
| `XML_LOCAL_NAMESPACE` (`int`) |  | Un nodo de declaración de espacio de nombres. |

Constantes XML

<table>
<caption>Constantes HTML</caption>
<thead>
<tr>
<th>Constantes</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Dom\HTML_NO_DEFAULT_NS</code> (<code>int</code>)</td>
<td><p>Esto desactiva la definición del espacio de nombres de los elementos durante el análisis al utilizar <code>Dom\HTMLDocument</code>. Esto existe para la compatibilidad ascendente con <code>DOMDocument</code>.</p>

&#10;</div>
<p>Algunos métodos DOM dependen de la definición del espacio de nombres HTML. Al utilizar esta opción del analizador, el comportamiento de estos métodos puede ser influenciado.</p>
</div></td>
</tr>
</tbody>
</table>

| Constantes | Valor | Descripción |
|----|----|----|
| `DOM_PHP_ERR` (`int`) | 0 | Código de error que no forma parte de la especificación DOM. Destinado a errores PHP. Deprecado a partir de PHP 8.4.0 ya que ya no se utiliza. Antes de PHP 8.4.0, se utilizaba de manera inconsistente para indicar situaciones de falta de memoria. |
| `DOM_INDEX_SIZE_ERR` / `Dom\INDEX_SIZE_ERR` (`int`) | 1 | Si el índice o el tamaño es negativo, o superior al valor permitido. |
| `DOMSTRING_SIZE_ERR` / `Dom\STRING_SIZE_ERR` (`int`) | 2 | Si el rango de texto especificado no cabe en una `string`. |
| `DOM_HIERARCHY_REQUEST_ERR` / `Dom\HIERARCHY_REQUEST_ERR` (`int`) | 3 | Si un nodo es insertado en un lugar donde no tiene cabida |
| `DOM_WRONG_DOCUMENT_ERR` / `Dom\WRONG_DOCUMENT_ERR` (`int`) | 4 | Si un nodo es utilizado en un documento diferente al que lo creó. |
| `DOM_INVALID_CHARACTER_ERR` / `Dom\INVALID_CHARACTER_ERR` (`int`) | 5 | Si se especifica un carácter inválido o ilegal, como en un nombre. |
| `DOM_NO_DATA_ALLOWED_ERR` / `Dom\NO_DATA_ALLOWED_ERR` (`int`) | 6 | Si se especifican datos para un nodo que no soporta datos. |
| `DOM_NO_MODIFICATION_ALLOWED_ERR` / `Dom\NO_MODIFICATION_ALLOWED_ERR` (`int`) | 7 | Si se intenta modificar un objeto cuando las modificaciones no están permitidas. |
| `DOM_NOT_FOUND_ERR` / `Dom\NOT_FOUND_ERR` (`int`) | 8 | Si se intenta referenciar un nodo en un contexto donde no existe. |
| `DOM_NOT_SUPPORTED_ERR` / `Dom\NOT_SUPPORTED_ERR` (`int`) | 9 | Si la implementación no soporta el tipo de objeto o la operación solicitada. |
| `DOM_INUSE_ATTRIBUTE_ERR` / `Dom\INUSE_ATTRIBUTE_ERR` (`int`) | 10 | Si se intenta añadir un atributo que ya está siendo utilizado en otro lugar. |
| `DOM_INVALID_STATE_ERR` / `Dom\INVALID_STATE_ERR` (`int`) | 11 | Si se intenta utilizar un objeto que no es, o ya no es, utilizable. |
| `DOM_SYNTAX_ERR` / `Dom\SYNTAX_ERR` (`int`) | 12 | Si se especifica una cadena de caracteres inválida o ilegal. |
| `DOM_INVALID_MODIFICATION_ERR` / `Dom\INVALID_MODIFICATION_ERR` (`int`) | 13 | Si se intenta modificar el tipo del objeto subyacente. |
| `DOM_NAMESPACE_ERR` / `Dom\NAMESPACE_ERR` (`int`) | 14 | Si se intenta crear o modificar un objeto de manera incorrecta con respecto a los espacios de nombres. |
| `DOM_INVALID_ACCESS_ERR` / `Dom\INVALID_ACCESS_ERR` (`int`) | 15 | Si un parámetro o una operación no es soportada por el objeto subyacente. |
| `DOM_VALIDATION_ERR` / `Dom\VALIDATION_ERR` (`int`) | 16 | Si una llamada a un método como insertBefore o removeChild haría que el nodo fuera inválido con respecto a la "valididad parcial", se lanzaría esta excepción y la operación no se realizaría. |

Constantes `DOMException` / `Dom\Exception`
