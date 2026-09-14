---
title: posix_times
description: Obtener los tiempos de procesos
source_url: https://www.php.net/manual/es/function.posix-times.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-times.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65480
---

posix_times

Obtener los tiempos de procesos

## Descripción

```php
posix_times(): array
```php

Obtiene información sobre el uso actual de CPU.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un hash de cadenas con información sobre el uso de CPU del proceso actual. Los índices del hash son:

- ticks - el número de pulsos de reloj que han transcurrido desde el reinicio.

- utime - tiempo de usuario usado por el proceso actual.

- stime - tiempo de sistema usado por el proceso actual.

- cutime - tiempo de usuario usado por el proceso actual y sus hijos.

- cstime - tiempo de sistema usado por el proceso actual y sus hijos.

La función devuelve `false` en caso de fallo.

## Ejemplos

Ejemplo de uso de `posix_times`

```
<?php

$tiempos = posix_times();

print_r($tiempos );
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [ticks] => 25814410
        [utime] => 1
        [stime] => 1
        [cutime] => 0
        [cstime] => 0
    )

## Notas

> [!WARNING]
> Esta función no es fiable de usar, puede devolver valores negativos para tiempos altos.
