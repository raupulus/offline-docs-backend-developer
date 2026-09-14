---
title: DateTimeInterface::getTimezone
description: Devuelve la zona horaria relativa al DateTime proporcionado
source_url: https://www.php.net/manual/es/datetime.gettimezone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/gettimezone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10790
---

DateTimeInterface::getTimezone

DateTimeImmutable::getTimezone

DateTime::getTimezone

date_timezone_get

Devuelve la zona horaria relativa al DateTime proporcionado

## Descripción

Estilo orientado a objetos

```php
public DateTimeInterface::getTimezone(): DateTimeZone
```php

```php
public DateTimeImmutable::getTimezone(): DateTimeZone
```

```php
public DateTime::getTimezone(): DateTimeZone
```php

Estilo procedimental

```php
date_timezone_get(DateTimeInterface $object): DateTimeZone
```

Devuelve la zona horaria relativa al DateTime proporcionado.

## Parámetros

`object`  
Solo en estilo procedimental: un objeto `DateTime` retornado por `date_create`

## Valores devueltos

Devuelve un objeto `DateTimeZone` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `DateTime::getTimezone`

Estilo orientado a objetos

```php
<?php
$date = new DateTimeImmutable("now", new DateTimeZone('Europe/London'));
$tz = $date->getTimezone();
echo $tz->getName();

   
```

El ejemplo anterior mostrará:

    Europe/London

       

Estilo procedimental

```php
<?php
$date = date_create("now", timezone_open('Europe/London'));
$tz = date_timezone_get($date);
echo timezone_name_get($tz);

   
```

El ejemplo anterior mostrará:

    Europe/London

## Véase también

DateTime::setTimezone
