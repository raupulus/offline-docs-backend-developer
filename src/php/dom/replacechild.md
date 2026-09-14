---
title: DOMNode::replaceChild
description: Reemplaza un hijo
source_url: https://www.php.net/manual/es/domnode.replacechild.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/replacechild.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 7d5c74c9a
order: 14090
---

DOMNode::replaceChild

Reemplaza un hijo

## Descripción

```php
public DOMNode::replaceChild(DOMNode $node, DOMNode $child): DOMNode
```php

Esta función reemplaza el hijo `child` por el nuevo nodo especificado. Si `node` ya es un hijo, no será añadido una segunda vez. Si el reemplazo tiene éxito, el nodo antiguo será devuelto.

## Parámetros

`node`  
El nuevo nodo. Debe ser miembro del documento destino, es decir, creado por una de las métodos de DOMDocument-\>createXXX() o importado en el documento por [???](#domdocument.importnode).

`child`  
El nodo antiguo.

## Valores devueltos

El nodo antiguo o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de solo lectura o si el padre anterior del nodo a insertar es de solo lectura.

`DOM_HIERARCHY_REQUEST_ERR`  
Lanzado si el nodo es de un tipo que no permite hijos del tipo del nodo `node`, o si el nodo a insertar es uno de los ancestros de este nodo o este nodo mismo.

`DOM_WRONG_DOCUMENT_ERR`  
Emitido si `node` ha sido creado desde un documento diferente al que creó este nodo.

`DOM_NOT_FOUND_ERR`  
Lanzado si `child` no es un hijo de este nodo.

## Véase también

DOMChildNode::replaceWith, DOMNode::appendChild, DOMNode::removeChild
