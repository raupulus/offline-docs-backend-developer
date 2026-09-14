---
title: mysqli::debug
description: Realiza acciones de depuración
source_url: https://www.php.net/manual/es/mysqli.debug.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/debug.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 637983e27
order: 54990
---

mysqli::debug

mysqli_debug

Realiza acciones de depuración

## Descripción

Estilo orientado a objetos

```php
public mysqli::debug(string $options): true
```php

Estilo procedimental

```php
mysqli_debug(string $options): true
```

Realiza acciones de depuración utilizando la biblioteca de depuración Fred Fish.

## Parámetros

`options`  
Un string que representa la operación de depuración a realizar.

El string de control de depuración es una secuencia de campos separados por dos puntos, como sigue: `<field_1>:<field_2>:<field_N>` Cada campo se compone de un carácter flag obligatorio seguido de un `,` opcional y una lista de modificadores separados por comas: `flag[,modifier,modifier,...,modifier]`

| `options` carácter | Descripción                        |
|--------------------|------------------------------------|
| O                  | `MYSQLND_DEBUG_FLUSH`              |
| A/a                | `MYSQLND_DEBUG_APPEND`             |
| F                  | `MYSQLND_DEBUG_DUMP_FILE`          |
| i                  | `MYSQLND_DEBUG_DUMP_PID`           |
| L                  | `MYSQLND_DEBUG_DUMP_LINE`          |
| m                  | `MYSQLND_DEBUG_TRACE_MEMORY_CALLS` |
| n                  | `MYSQLND_DEBUG_DUMP_LEVEL`         |
| o                  | salida a fichero                   |
| T                  | `MYSQLND_DEBUG_DUMP_TIME`          |
| t                  | `MYSQLND_DEBUG_DUMP_TRACE`         |
| x                  | `MYSQLND_DEBUG_PROFILE_CALLS`      |

Caracteres flag reconocidos

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora siempre `true`. Anteriormente, devolvía `false` en caso de error. |

## Ejemplos

Generación de un fichero de "traza"

```php
<?php

/* Genera un fichero de "traza" en '/tmp/client.trace' en la máquina (cliente) local: */
mysqli_debug("d:t:o,/tmp/client.trace");

?>

    
```

## Notas

> [!NOTE]
> Para utilizar la función `mysqli_debug`, se debe compilar la biblioteca cliente MySQL con soporte de depuración.

## Véase también

`mysqli_dump_debug_info`, `mysqli_report`
