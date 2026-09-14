---
title: sleep
description: Detiene la ejecución durante algunos segundos
source_url: https://www.php.net/manual/es/function.sleep.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/sleep.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 0abd79a0d
order: 47240
---

sleep

Detiene la ejecución durante algunos segundos

## Descripción

```php
sleep(int $seconds): int
```php

Detiene la ejecución del programa durante `seconds` segundos.

> [!NOTE]
> Para retrasar la ejecución de un programa durante una fracción de segundo, utilice la función `usleep` ya que la función `sleep` espera un `int`. Por ejemplo, `sleep(0.25)` retrasará la ejecución del programa durante `0` segundos.

## Parámetros

`seconds`  
El tiempo de detención, en número de segundos (debe ser superior o igual a `0`).

## Valores devueltos

Retorna cero en caso de éxito.

Si la llamada es interrumpida por una señal, la función `sleep` retornará un valor diferente de cero. En Windows, el valor será siempre `192` (el valor de la constante `WAIT_IO_COMPLETION` de la API de Windows). En otras plataformas, el valor retornado será el número de segundos restantes para la función `sleep`.

## Errores/Excepciones

Se lanza una `ValueError` si el número `seconds` especificado es negativo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | La función lanza una `ValueError` si `seconds` es negativo; anteriormente, se generaba un error de nivel `E_WARNING` y la función retornaba `false`. |

## Ejemplos

Ejemplo con `sleep`

```
<?php

// Hora actual
echo date('h:i:s') . "\n";

// Detiene por 10 segundos
sleep(10);

// ¡Regreso!
echo date('h:i:s') . "\n";

?>

    
```php

Este ejemplo mostrará (después de 10 segundos):

    05:31:23
    05:31:33

## Véase también

`usleep`, `time_nanosleep`, `time_sleep_until`, `set_time_limit`
