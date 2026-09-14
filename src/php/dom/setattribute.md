---
title: DOMElement::setAttribute
description: Añade un nuevo atributo o modifica uno existente
source_url: https://www.php.net/manual/es/domelement.setattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/setattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 7d5c74c9a
order: 13620
---

DOMElement::setAttribute

Añade un nuevo atributo o modifica uno existente

## Descripción

```php
public DOMElement::setAttribute(string $qualifiedName, string $value): DOMAttr
```php

Establece un atributo con nombre `qualifiedName` al valor dado. Si el atributo no existe, se creará.

## Parámetros

`qualifiedName`  
El nombre del atributo.

`value`  
El valor del atributo.

## Valores devueltos

El `DOMAttr` creado o modificado o `false` si ocurrió un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de sólo lectura.

## Ejemplos

Establecer un atributo

```
<?php
$doc = new DOMDocument("1.0");
$node = $doc->createElement("para");
$newnode = $doc->appendChild($node);
$newnode->setAttribute("align", "left");
?>

    
```php

## Véase también

DOMElement::hasAttribute, DOMElement::getAttribute, DOMElement::removeAttribute
