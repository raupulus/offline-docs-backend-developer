---
title: DOMChildNode::after
description: Añade nodos después del nodo
source_url: https://www.php.net/manual/es/domchildnode.after.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domchildnode/after.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1349f957
order: 12900
---

DOMChildNode::after

Añade nodos después del nodo

## Descripción

```php
public DOMChildNode::after(DOMNode ...$nodes): void
```php

Añade los `nodes` pasados después del nodo.

## Parámetros

`nodes`  
Nodos a añadir después del nodo. Las cadenas de caracteres son automáticamente convertidas en nodos textuales.

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
| 8.3.0 | Llamar a este método en un nodo sin padre es ahora sin efecto para alinear el comportamiento con la especificación del DOM. Anteriormente, esto desencadenaba una `DOMException` con el código `DOM_HIERARCHY_REQUEST_ERR`. |
| 8.3.0 | Llamar a este método en un nodo sin documento propietario funciona ahora. Anteriormente, esto desencadenaba una `DOMException` con el código `DOM_HIERARCHY_REQUEST_ERR`. |

## Véase también

DOMChildNode::before, DOMChildNode::remove, DOMChildNode::replaceWith, DOMNode::appendChild
