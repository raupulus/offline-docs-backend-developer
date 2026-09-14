---
title: La interfaz Reflector
source_url: https://www.php.net/manual/es/class.reflector.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflector.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 72040
---

## Introducción

`Reflector` es una interfaz implementada por todas las clases exportables Reflection.

## Sinopsis de la interfaz

Reflector

extends

Stringable

Métodos heredados

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Reflector::export ha sido eliminado. |
| 8.0.0 | `Reflector` ahora extiende Stringable. Hereda Stringable::\_\_toString, reemplazando Reflector::\_\_toString. |

## Véase también

Reflector::export
