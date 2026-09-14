---
title: DOMParentNode::replaceChildren
description: Reemplaza los hijos en un nodo
source_url: https://www.php.net/manual/es/domparentnode.replacechildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domparentnode/replacechildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1349f957
order: 14200
---

DOMParentNode::replaceChildren

Reemplaza los hijos en un nodo

## Descripción

```php
public DOMParentNode::replaceChildren(DOMNode ...$nodes): void
```php

Reemplaza los hijos en un nodo.

## Parámetros

`nodes`  
Los nodos que reemplazan a los hijos. Las cadenas de caracteres se convierten automáticamente en nodos de texto.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

`DOM_HIERARCHY_REQUEST_ERR`  
Se levanta si este nodo es de un tipo que no permite hijos del tipo de uno de los `nodes` transmitidos, o si el nodo a insertar es uno de los ancestros de este nodo o este nodo mismo.

`DOM_WRONG_DOCUMENT_ERR`  
Se levanta si uno de los `nodes` transmitidos ha sido creado a partir de un documento diferente del que creó este nodo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Llamar a este método en un nodo sin documento propietario funciona ahora. Anteriormente, esto desencadenaba una `DOMException` con el código `DOM_HIERARCHY_REQUEST_ERR`. |

## Ejemplos

Ejemplo de DOMParentNode::replaceChildren

```
<?php

$dom = new DOMDocument();
$dom->loadHTML('<!DOCTYPE HTML><html><p>hi</p> test <p>hi2</p></html>');

$dom->documentElement->replaceChildren('foo', $dom->createElement('p'), 'bar');
echo $dom->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    <!DOCTYPE HTML>
    <html>foo<p/>bar</html>
