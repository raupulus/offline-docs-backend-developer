---
title: spl_autoload_functions
description: Devuelve todas las funciones __autoload() registradas
source_url: https://www.php.net/manual/es/function.spl-autoload-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-autoload-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 0181b7f92
order: 82270
---

spl_autoload_functions

Devuelve todas las funciones \_\_autoload() registradas

## Descripción

```php
spl_autoload_functions(): array
```php

Obtiene todas las funciones \_\_autoload() registradas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todas las funciones \_\_autoload registradas. Si no hay funciones registradas, o si la pila de autoload no está activa, entonces el valor de retorno será un array vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El valor de retorno ha sido actualizado para siempre ser un `array`; anteriormente, esta función devolvía `false` si la pila de autoload no estaba activa. |
