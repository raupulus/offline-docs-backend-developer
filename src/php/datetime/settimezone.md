---
title: DateTime::setTimezone
description: Establece la zona horaria para el objeto DateTime
source_url: https://www.php.net/manual/es/datetime.settimezone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/settimezone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 10540
---

DateTime::setTimezone

date_timezone_set

Establece la zona horaria para el objeto DateTime

## Descripción

Estilo orientado a objetos

```php
public DateTime::setTimezone(DateTimeZone $timezone): DateTime
```php

Estilo procedimental

```php
date_timezone_set(DateTime $object, DateTimeZone $timezone): DateTime
```

Establece una nueva zona horaria para un `object` de `DateTime`.

Igual que DateTimeImmutable::setTimezone pero funciona con `DateTime`.

La versión procedural toma el objeto `DateTime` como su primer argumento.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`timezone`  
Un objeto `DateTimeZone` que representa la zona horaria deseada.

## Valores devueltos

Devuelve el objeto `DateTime` para encadenar métodos. El punto en el tiempo subyacente no cambia al llamar a este método.

## Ejemplos

Ejemplo de `DateTime::setTimeZone`

Estilo orientado a objetos

```php
<?php
$date = new DateTime('2000-01-01', new DateTimeZone('Pacific/Nauru'));
echo $date->format('Y-m-d H:i:sP') . "\n";

$date->setTimezone(new DateTimeZone('Pacific/Chatham'));
echo $date->format('Y-m-d H:i:sP') . "\n";

   
```

El ejemplo anterior mostrará:

    2000-01-01 00:00:00+12:00
    2000-01-01 01:45:00+13:45

       

Estilo procedimental

```php
<?php
$date = date_create('2000-01-01', timezone_open('Pacific/Nauru'));
echo date_format($date, 'Y-m-d H:i:sP') . "\n";

date_timezone_set($date, timezone_open('Pacific/Chatham'));
echo date_format($date, 'Y-m-d H:i:sP') . "\n";

   
```

El ejemplo anterior mostrará:

    2000-01-01 00:00:00+12:00
    2000-01-01 01:45:00+13:45

## Véase también

DateTimeImmutable::setTimezone

DateTime::getTimezone

DateTimeZone::\_\_construct
