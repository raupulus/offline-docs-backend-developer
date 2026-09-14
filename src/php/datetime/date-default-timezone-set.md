---
title: date_default_timezone_set
description: Establece la zona horaria por defecto para todas las funciones de fecha/hora
source_url: https://www.php.net/manual/es/function.date-default-timezone-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-default-timezone-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11020
---

date_default_timezone_set

Establece la zona horaria por defecto para todas las funciones de fecha/hora

## Descripción

```php
date_default_timezone_set(string $timezoneId): bool
```php

La función `date_default_timezone_set` establece la zona horaria por defecto utilizada por todas las funciones de fecha/hora.

En lugar de utilizar esta función para establecer la zona horaria por defecto en su script, también puede utilizarse la configuración INI [date.timezone](#ini.date.timezone).

## Parámetros

`timezoneId`  
El identificador de zona horaria, como `UTC`, `Africa/Lagos`, `Asia/Hong_Kong`, o `Europe/Lisbon`. La lista de identificadores válidos está disponible en el [???](#timezones).

## Valores devueltos

Esta función devuelve `false` si `timezoneId` no es válido, `true` en caso contrario.

## Ejemplos

Obtención de la zona horaria por defecto

```
<?php
date_default_timezone_set('America/Los_Angeles');

$script_tz = date_default_timezone_get();
$ini_tz = ini_get('date.timezone');

if (strcmp($script_tz, $ini_tz)){
    echo 'La zona horaria del script difiere de la zona horaria definida en el archivo ini.';
} else {
    echo 'La zona horaria del script es equivalente a la definida en el archivo ini.';
}

    
```php

## Véase también

`date_default_timezone_get`, [???](#timezones)
