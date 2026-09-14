---
title: DOMElement::getAttributeNS
description: Devuelve el valor de un atributo
source_url: https://www.php.net/manual/es/domelement.getattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/getattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13480
---

DOMElement::getAttributeNS

Devuelve el valor de un atributo

## Descripción

```php
public DOMElement::getAttributeNS(string $namespace, string $localName): string
```php

Obtiene el valor del atributo en el espacio de nombres `namespace` con el nombre local `localName` para el nodo actual.

## Parámetros

`namespace`  
La URI del espacio de nombres.

`localName`  
El nombre local.

## Valores devueltos

El valor del atributo, o una cadena vacía si no se ecuentra el atributo con los `localName` y `namespace` dados.

## Véase también

DOMElement::hasAttributeNS, DOMElement::setAttributeNS, DOMElement::removeAttributeNS
