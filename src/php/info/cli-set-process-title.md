---
title: cli_set_process_title
description: Define el título del proceso
source_url: https://www.php.net/manual/es/function.cli-set-process-title.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/cli-set-process-title.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: b08b472de
order: 38750
---

cli_set_process_title

Define el título del proceso

## Descripción

```php
cli_set_process_title(string $title): bool
```php

Define el título del proceso visible con herramientas como `top` y `ps`. Esta función solo está disponible en modo [CLI](#features.commandline).

## Parámetros

`title`  
El nuevo título.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se generará una alerta de nivel `E_WARNING` si el sistema subyacente no es compatible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `cli_set_process_title` ahora emite una alerta `E_WARNING` al definir un título de proceso demasiado largo; antes el título era truncado. |

## Ejemplos

```
<?php
$title = "Mi super script PHP";
$pid = getmypid(); // puede utilizarse para ver el título del proceso en ps

if (!cli_set_process_title($title)) {
    echo "No se puede definir el título del proceso para el PID $pid...\n";
    exit(1);
} else {
    echo "¡El título del proceso '$title' para el PID $pid ha sido definido correctamente!\n";
    sleep(5);
}
?>

   
```php

## Véase también

cli_get_process_title
