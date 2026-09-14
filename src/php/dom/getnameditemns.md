---
title: DOMNamedNodeMap::getNamedItemNS
description: Recupera un nodo especificado por el nombre local y la URI del espacio
  de nombres
source_url: https://www.php.net/manual/es/domnamednodemap.getnameditemns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnamednodemap/getnameditemns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13830
---

DOMNamedNodeMap::getNamedItemNS

Recupera un nodo especificado por el nombre local y la URI del espacio de nombres

## Descripción

```php
public DOMNamedNodeMap::getNamedItemNS(string $namespace, string $localName): DOMNode
```php

Recupera un nodo especificado por `localName` y `namespace`.

## Parámetros

`namespace`  
La URI del espacio de nombres del nodo a recuperar.

`localName`  
El nombre local del nodo a recuperar.

## Valores devueltos

Un nodo (de cualquier tipo) con el nombre local y la URI del espacio de nombres especificados, o `null` si no se encuentra ningún nodo.

## Véase también

DOMNamedNodeMap::getNamedItem
