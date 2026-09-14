---
title: DOMNamedNodeMap::item
description: Recupera un nodo especificado por su índice
source_url: https://www.php.net/manual/es/domnamednodemap.item.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnamednodemap/item.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13840
---

DOMNamedNodeMap::item

Recupera un nodo especificado por su índice

## Descripción

```php
public DOMNamedNodeMap::item(int $index): DOMNode
```php

Recupera un nodo especificado por `index` dentro del objeto `DOMNamedNodeMap`.

## Parámetros

`index`  
Índice dentro de este mapa.

## Valores devueltos

El nodo en la posición marcada por `index` en el mapa, o `null` si no es un índice válido (mayor o igual que el número de nodos de este mapa).
