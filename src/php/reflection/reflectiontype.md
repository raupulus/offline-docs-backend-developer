---
title: La clase ReflectionType
source_url: https://www.php.net/manual/es/class.reflectiontype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiontype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 71900
---

## Introducción

La clase `ReflectionType` proporciona información sobre el tipo de retorno de una función. La extensión Reflection declara los siguientes subtipos: `ReflectionNamedType` (disponible a partir de PHP 7.1.0), `ReflectionUnionType` (disponible a partir de PHP 8.0.0), `ReflectionIntersectionType` (disponible a partir de PHP 8.1.0)

## Sinopsis de la clase

abstract

ReflectionType

implements

Stringable

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `ReflectionType` se ha convertido en abstracta y `ReflectionType::isBuiltin` ha sido movida a `ReflectionNamedType::isBuiltin`. |
