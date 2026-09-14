---
title: set_time_limit
description: Establece el tiempo máximo de ejecución de un script
source_url: https://www.php.net/manual/es/function.set-time-limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/set-time-limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_revision: dec1f8445
order: 39220
---

set_time_limit

Establece el tiempo máximo de ejecución de un script

## Descripción

```php
set_time_limit(int $seconds): bool
```php

Establece el tiempo de expiración de un script, en segundos. Si se alcanza este límite, el script se interrumpe y se genera un error fatal. El valor por omisión es 30 segundos o, si está definido, el valor de la directiva `max_execution_time` en el `php.ini`.

Cuando se invoca, `set_time_limit` reinicia el contador. En otras palabras, si el límite por omisión es de 30 segundos, y después de 25 segundos de ejecución del script se realiza la llamada `set_time_limit(20)`, entonces el script ejecutará un total de 45 segundos antes de finalizar.

## Parámetros

`seconds`  
El tiempo máximo de ejecución, en segundos. Si es `0`, no se establece límite alguno.

## Valores devueltos

Devuelve `true` en caso de éxito, o `false` si ocurre un error.

## Notas

> [!NOTE]
> La función `set_time_limit` y la directiva de configuración [max_execution_time](#ini.max-execution-time) solo afectan al tiempo de ejecución del script en sí. Todo tiempo pasado fuera del script, como llamadas al sistema utilizando `system`, operaciones en flujos, consultas a bases de datos, etc., no se tienen en cuenta al calcular la duración máxima de ejecución del script. Esto no es válido en Windows donde el tiempo medido es el tiempo real.

## Véase también

[max_execution_time](#ini.max-execution-time), [max_input_time](#ini.max-input-time)
