---
title: La clase DOMNodeList
source_url: https://www.php.net/manual/es/class.domnodelist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnodelist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 83ef90503
order: 14160
---

## Introducción

Representa una lista dinámica de nodos.

## Sinopsis de la clase

DOMNodeList

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
El número de nodos en la lista. El intervalo válido de los índices de los nodos hijos es 0 a `length - 1`, inclusivo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `DOMNodeList` implementa ahora IteratorAggregate. Anteriormente, Traversable era implementado en su lugar. |
| 7.2.0 | La interfaz `Countable` es implementada y devuelve el valor de la propiedad [length](#domnodelist.props.length). |

## Notas

> [!NOTE]
> Los nodos en el mapa pueden ser accedidos a través de la sintaxis de array.

## Véase también

[Las especificaciones W3C de NodeList](http://www.w3.org/TR/2003/WD-DOM-Level-3-Core-20030226/DOM3-Core.html#core-ID-536297177)
