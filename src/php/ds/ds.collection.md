---
title: La interfaz Collection
source_url: https://www.php.net/manual/es/class.ds-collection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.collection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 16520
---

## Introducción

`Ds\Collection` es la interfaz base que cubre las funcionalidades comunes a todas las estructuras de datos de esta biblioteca. Garantiza que todas las estructuras son recorribles, contables y pueden ser convertidas en json utilizando `json_encode`.

## Sinopsis de la interfaz

Ds\Collection

extends

Countable

IteratorAggregate

JsonSerializable

Métodos

Métodos heredados

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL ds 1.4.0 | `Collection` implementa JsonSerializable en lugar de Serializable. (Este cambio fue añadido al polyfill en la versión 1.4.1.) |
