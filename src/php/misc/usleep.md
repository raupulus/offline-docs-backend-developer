---
title: usleep
description: Detiene la ejecución durante algunas microsegundos
source_url: https://www.php.net/manual/es/function.usleep.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/usleep.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: false
translation_revision: 3441bb1c9
order: 47300
---

usleep

Detiene la ejecución durante algunas microsegundos

## Descripción

```php
usleep(int $microseconds): void
```php

Detiene la ejecución de un programa durante un período de tiempo.

## Parámetros

`microseconds`  
Duración de la detención, en microsegundos. Una microsegundo es un millonésimo de segundo.

> [!NOTE]
> Los valores mayores que `1000000` (es decir, dormir por más de un segundo) pueden no ser soportados por el sistema operativo. Utilizar `sleep` en su lugar.

> [!NOTE]
> El tiempo de detención puede ser ligeramente alargado (es decir, puede ser más largo que `microseconds`) por cualquier actividad del sistema o por el tiempo empleado en procesar la llamada o por la granularidad de los temporizadores del sistema.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `usleep`

```
<?php

// Hora actual
echo (new DateTime('now'))->format('H:i:s.v'), "\n";

// Detiene por 2 milisegundos
usleep(2000);

// ¡Vuelta!
echo (new DateTime('now'))->format('H:i:s.v'), "\n";

// Espera 30 milisegundos
usleep(30000);

// ¡Vuelta otra vez!
echo (new DateTime('now'))->format('H:i:s.v'), "\n";

?>

    
```php

El ejemplo anterior mostrará:

    11:13:28.005
    11:13:28.007
    11:13:28.037

## Véase también

`sleep`, `time_nanosleep`, `time_sleep_until`, `set_time_limit`
