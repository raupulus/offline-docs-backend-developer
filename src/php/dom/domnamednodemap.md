---
title: La clase DOMNamedNodeMap
source_url: https://www.php.net/manual/es/class.domnamednodemap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnamednodemap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 2352068d5
order: 13850
---

## Sinopsis de la clase

DOMNamedNodeMap

implements

IteratorAggregate

Countable

Propiedades

public

readonly

int

length

Métodos

## Propiedades

`length`  
El número de nodos en el mapa. El rango de índices de los nodos hijos válidos es de `0` a `length - 1`, inclusivo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Los métodos no implementados DOMNamedNodeMap::setNamedItem, DOMNamedNodeMap::removeNamedItem, DOMNamedNodeMap::setNamedItemNS y DOMNamedNodeMap::removeNamedItem han sido eliminados. |
| 8.0.0 | La clase `DOMNamedNodeMap` ahora implementa IteratorAggregate. Anteriormente, solo Traversable era implementado. |

## Notas

> [!NOTE]
> Los nodos en el mapa pueden ser accedidos mediante la sintaxis de array.
