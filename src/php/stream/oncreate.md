---
title: php_user_filter::onCreate
description: Llamado cuando se crea el filtro
source_url: https://www.php.net/manual/es/php-user-filter.oncreate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/php_user_filter/oncreate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 4f6742c6e
order: 88280
---

php_user_filter::onCreate

Llamado cuando se crea el filtro

## Descripción

```php
public php_user_filter::onCreate(): bool
```php

Este método se llama durante la instanciación del objeto de la clase del filtro. Si el filtro asigna o inicializa cualquier otro recurso (como un buffer), éste es el lugar para hacerlo.

Cuando primero se instancia el filtro, y se llama a `elfiltro->onCreate()`, estarán disponibles varias propiedades como se muestra en la tabla de abajo.

| Propiedad | Contenido |
|----|----|
| `FilterClass->filtername` | Una cadena que contiene el nombre del filtro con el que fue instanciado. Los filtros pueden ser registrados bajo múltiples nombres o bajo comodines. Use esta propiedad para determinar qué nombre fue usado. |
| `FilterClass->params` | El contenido del parámetro `params` pasado a `stream_filter_append` o a `stream_filter_prepend`. |
| `FilterClass->stream` | El recurso de flujo que va a ser filtrado. Quizás disponible sólo durante las llamadas a filter cuando el parámetro `closing` es `false`. |

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La implementación de este método debería devolver `false` en caso de error, o `true` en caso de éxito.
