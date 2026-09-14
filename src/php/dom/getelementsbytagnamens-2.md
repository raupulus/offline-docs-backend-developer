---
title: DOMElement::getElementsByTagNameNS
description: Recupera los elementos por su espacio de nombres y su localName
source_url: https://www.php.net/manual/es/domelement.getelementsbytagnamens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/getelementsbytagnamens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 842bbe35c
order: 13500
---

DOMElement::getElementsByTagNameNS

Recupera los elementos por su espacio de nombres y su localName

## Descripción

```php
public DOMElement::getElementsByTagNameNS(string $namespace, string $localName): DOMNodeList
```php

Esta función recupera todos los elementos descendientes con un nombre local `localName` y un espacio de nombres `namespace` dados.

## Parámetros

`namespace`  
La URI del espacio de nombres de los elementos a buscar. El valor especial `"*"` representa todos los espacios de nombres. Pasar `null` representa el espacio de nombres vacío.

`localName`  
El nombre local de los elementos a buscar. El valor especial `"*"` representa todos los nombres locales.

## Valores devueltos

Esta función devuelve un nuevo objeto de la clase `DOMNodeList` que contiene todos los elementos correspondientes en el orden en que se encuentran durante el recorrido del árbol de este elemento.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.3   | `namespace` es ahora nullable. |

## Véase también

DOMElement::getElementsByTagNameNS
