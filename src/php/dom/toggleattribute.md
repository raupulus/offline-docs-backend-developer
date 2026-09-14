---
title: DOMElement::toggleAttribute
description: Conmuta el atributo
source_url: https://www.php.net/manual/es/domelement.toggleattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/toggleattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 14170b04f
order: 13690
---

DOMElement::toggleAttribute

Conmuta el atributo

## Descripción

```php
public DOMElement::toggleAttribute(string $qualifiedName, [bool $force]): bool
```php

Conmuta el atributo.

## Parámetros

`qualifiedName`  
El nombre cualificado del atributo.

`force`  
si `null`, la función conmuta el atributo., si `true`, la función añade el atributo., si `false`, la función elimina el atributo.

## Valores devueltos

Devuelve `true` si el atributo está presente después de la llamada, en caso contrario `false`.

## Ejemplos

Ejemplo de DOMElement::toggleAttribute

```
<?php

$dom = new DOMDocument();
$dom->loadXML("<container selected=\"\"/>");

var_dump($dom->documentElement->toggleAttribute('selected'));
echo $dom->saveXML() . PHP_EOL;

var_dump($dom->documentElement->toggleAttribute('selected'));
echo $dom->saveXML();
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)

    <container/>

    bool(true)

    <container selected=""/>
