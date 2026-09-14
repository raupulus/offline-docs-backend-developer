---
title: La clase SimdJsonValueError
source_url: https://www.php.net/manual/es/class.simdjsonvalueerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simdjson/simdjsonvalueerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simdjson
translation_status: ready
translation_reviewed: false
translation_revision: 78cc29837
order: 74360
---

## Introducción

Una excepción `SimdJsonValueError` es lanzada cuando el tipo de un argumento de una función de simdjson es correcto pero el valor de éste es incorrecto. Por ejemplo, cuando la decodificación JSON `$depth` no es positiva o cuando `$depth` es demasiado grande.

## Sinopsis de la clase

SimdJsonValueError

SimdJsonValueError

extends

ValueError

Propiedades heredadas

Métodos heredados

## Historial de cambios

| Versión | Descripción |
|----|----|
| PHP 8.0.0 | `SimdJsonValueError` extiende ahora `ValueError` en lugar de `Error`. |
