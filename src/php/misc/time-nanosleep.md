---
title: time_nanosleep
description: Esperar durante un número de segundos y nanosegundos
source_url: https://www.php.net/manual/es/function.time-nanosleep.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/time-nanosleep.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 47260
---

time_nanosleep

Esperar durante un número de segundos y nanosegundos

## Descripción

```php
time_nanosleep(int $seconds, int $nanoseconds): array
```php

time_nanosleep impone un retraso de ejecución de `seconds` segundos y `nanoseconds` nanosegundos.

## Parámetros

`seconds`  
Debe ser un integer no negativo.

`nanoseconds`  
Debe ser un integer no negativo, inferior a 1000 millones.

> [!NOTE]
> En Windows, el sistema puede esperar más tiempo que el número de nanosegundos dado, según el hardware.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Si el retraso es interrumpido por una señal, se devolverá un array asociativo con los elementos:

- `seconds`: número de segundos restantes en el retraso

- `nanoseconds`: número de nanosegundos restantes en el retraso

## Ejemplos

Ejemplo con `time_nanosleep`

```
<?php
// ¡Atención! Esto no funcionará como se espera si se devuelve un array
if (time_nanosleep(0, 500000000)) {
    echo "Dormir durante media segundo.\n";
}

// Esto es mejor:
if (time_nanosleep(0, 500000000) === true) {
    echo "Dormir durante media segundo.\n";
}

// Y esto es la mejor forma:
$nano = time_nanosleep(2, 100000);

if ($nano === true) {
    echo "Dormir durante 2 segundos y 100 microsegundos.\n";
} elseif ($nano === false) {
    echo "El retraso ha fallado.\n";
} elseif (is_array($nano)) {
    $seconds = $nano['seconds'];
    $nanoseconds = $nano['nanoseconds'];
    echo "Interrumpido por una señal.\n";
    echo "Tiempo restante: $seconds segundos, $nanoseconds nanosegundos.";
}
?>

    
```php

## Véase también

`sleep`, `usleep`, `time_sleep_until`, `set_time_limit`
