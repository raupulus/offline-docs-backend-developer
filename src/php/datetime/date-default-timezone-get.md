---
title: date_default_timezone_get
description: Recupera el huso horario por defecto utilizado por todas las funciones
  de fecha/hora de un script
source_url: https://www.php.net/manual/es/function.date-default-timezone-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-default-timezone-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11010
---

date_default_timezone_get

Recupera el huso horario por defecto utilizado por todas las funciones de fecha/hora de un script

## Descripción

```php
date_default_timezone_get(): string
```php

Esta función devuelve el huso horario siguiendo el siguiente orden de preferencia:

- Lectura del huso horario definido utilizando la función `date_default_timezone_set` (si existe)

- Lectura del valor de la opción de configuración [date.timezone](#ini.date.timezone) (si está definida)

Si todo lo anterior falla, date_default_timezone_get devolverá el huso horario por defecto de `UTC`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string`.

## Ejemplos

Recuperación del huso horario por defecto

```
<?php
date_default_timezone_set('Europe/London');

if (date_default_timezone_get()) {
    echo 'date_default_timezone_set: ' . date_default_timezone_get() . "\n";
}

if (ini_get('date.timezone')) {
    echo 'date.timezone : ' . ini_get('date.timezone');
}

    
```php

Resultado del ejemplo anterior es similar a:

    date_default_timezone_set : Europe/London
    date.timezone : Europe/London

Recuperación de la abreviatura de un huso horario

```
<?php
date_default_timezone_set('America/Los_Angeles');
echo date_default_timezone_get() . ' => ' . date('e') . ' => ' . date('T');

    
```php

El ejemplo anterior mostrará:

    America/Los_Angeles => America/Los_Angeles => PST

## Véase también

`date_default_timezone_set`, [???](#timezones)
