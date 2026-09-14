---
title: La clase Map
source_url: https://www.php.net/manual/es/class.ds-map.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.map.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_revision: 94b069b11
order: 16550
---

## Introducción

Un Map es una colección secuencial de pares clave-valor, casi identico a un `array` usado en un contexto similar. Las claves pueden ser de cualquier tipo, pero deben ser únicos. Los valores se reemplazan si se agregan al mapa usando la misma clave.

## Fortalezas

Las claves y valores pueden ser de cualquer tipo, incluyendo objetos., Soporta la sintaxis array (corchetes)., Se mantiene el orden de inserción., El rendimiento y la eficiencia de memoria son muy similares al de un `array`., Automáticamente libera la memoria asignada cuando su tamaño cae lo suficientemente bajo.

## Debilidades

No puede ser convertido a un array cuando los objetos son usados como claves.

## Sinopsis de la clase

Ds\Map

Ds\Map

Ds\Collection

ArrayAccess

Constantes

const

int

Ds\Map::MIN_CAPACITY

8

Métodos

## Constantes predefinidas

`Ds\Map::MIN_CAPACITY`  

## Historial de cambios

| Versión       | Descripción                              |
|---------------|------------------------------------------|
| PECL ds 1.3.0 | La clase ahora implementa `ArrayAccess`. |
| PECL ds 1.2.0 | `Ds\Map::MIN_CAPACITY` cambió de 16 a 8. |
