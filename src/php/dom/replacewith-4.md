---
title: DOMChildNode::replaceWith
description: Reemplaza el nodo por nuevos nodos
source_url: https://www.php.net/manual/es/domchildnode.replacewith.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domchildnode/replacewith.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1349f957
order: 12930
---

DOMChildNode::replaceWith

Reemplaza el nodo por nuevos nodos

## Descripción

```php
public DOMChildNode::replaceWith(DOMNode ...$nodes): void
```php

Reemplaza el nodo por los nuevos `nodes`.

## Parámetros

`nodes`  
Los nodos de reemplazo.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

`DOM_HIERARCHY_REQUEST_ERR`  
Se levanta si el padre es de un tipo que no permite hijos del tipo de uno de los `nodes` transmitidos, o si el nodo a insertar es uno de los ancestros de este nodo o este nodo mismo.

`DOM_WRONG_DOCUMENT_ERR`  
Se levanta si uno de los `nodes` transmitidos ha sido creado a partir de un documento diferente del que creó este nodo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Llamar a este método en un nodo sin padre es ahora una operación sin efecto para alinear el comportamiento con la especificación del DOM. Anteriormente, esto desencadenaba una `DOMException` con el código `DOM_HIERARCHY_REQUEST_ERR`. |

## Véase también

DOMChildNode::after, DOMChildNode::before, DOMChildNode::remove, DOMNode::replaceChild
