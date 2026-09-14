---
title: La interfaz Traversable
source_url: https://www.php.net/manual/es/class.traversable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/traversable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 4d17b7b49
order: 4050
---

## Introducción

Interfaz para detectar si una clase puede recorrerse mediante [`foreach`](#control-structures.foreach).

Una interfaz abstracta base no puede ser implementada sola. En su lugar, debe ser implementada con IteratorAggregate o con Iterator.

## Sinopsis de la interfaz

Traversable

Esta interfaz no tiene métodos, su único propósito es ser la base para todas las clases atravesables.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | La interfaz Traversable ahora puede ser implementada por clases abstractas. Las clases que la extiendan deben implementar Iterator o IteratorAggregate. |

## Notas

> [!NOTE]
> Las clases internas que implementan esta interfaz pueden ser usadas en una construcción [`foreach`](#control-structures.foreach) y no necesitan implementar IteratorAggregate o Iterator.

> [!NOTE]
> Antes de PHP 7.4.0, esta interfaz interna del motor no podía ser implementada en scripts PHP. Se debe usar IteratorAggregate o Iterator deben usarse en su lugar.
