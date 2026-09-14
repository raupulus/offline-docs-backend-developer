---
title: sys_getloadavg
description: Obtiene la carga promedio del sistema
source_url: https://www.php.net/manual/es/function.sys-getloadavg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/sys-getloadavg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: false
translation_revision: 4411b371d
order: 47250
---

sys_getloadavg

Obtiene la carga promedio del sistema

## Descripción

```php
sys_getloadavg(): array
```php

Devuelve tres muestras que representan la carga promedio del sistema (el número de procesos en el sistema que está en el proceso de rotación en espera) durante los últimos 1, 5 y 15 minutos, respectivamente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` con tres muestras (últimos 1, 5 y 15 minutos). Devuelve `false` en caso de error.

## Ejemplos

Ejemplo con `sys_getloadavg`

```
<?php
$load = sys_getloadavg();
if ($load[0] > 0.80) {
    header('HTTP/1.1 503 Too busy, try again later');
    die('Server too busy. Please try again later.');
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.
