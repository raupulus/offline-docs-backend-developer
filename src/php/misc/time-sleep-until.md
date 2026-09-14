---
title: time_sleep_until
description: Detiene el script durante una duración especificada
source_url: https://www.php.net/manual/es/function.time-sleep-until.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/time-sleep-until.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: false
translation_revision: 7f569e1f1
order: 47270
---

time_sleep_until

Detiene el script durante una duración especificada

## Descripción

```php
time_sleep_until(float $timestamp): bool
```php

Detiene el script hasta el instante indicado por el argumento `timestamp`.

## Parámetros

`timestamp`  
El timestamp correspondiente al instante en que el script debe despertarse.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el instante indicado por `timestamp` está en el pasado, `time_sleep_until` generará una alerta de nivel `E_WARNING`.

## Ejemplos

Ejemplo con `time_sleep_until`

```
<?php

// Retorna false y genera una alerta
var_dump(time_sleep_until(time()-1));

// Funcionará solo en computadoras rápidas, detendrá el script 0.2 segundos
var_dump(time_sleep_until(microtime(true)+0.2));

?>

    
```php

## Notas

> [!NOTE]
> Todas las señales serán entregadas una vez reanudado el script.

## Véase también

`sleep`, `usleep`, `time_nanosleep`, `set_time_limit`
