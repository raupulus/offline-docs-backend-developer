---
title: IntlCalendar::fromDateTime
description: Crea un IntlCalendar a partir de un objeto DateTime o string
source_url: https://www.php.net/manual/es/intlcalendar.fromdatetime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/fromdatetime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: bce2cb849
order: 40270
---

IntlCalendar::fromDateTime

Crea un IntlCalendar a partir de un objeto DateTime o string

## Descripción

Estilo orientado a objetos

```php
public static IntlCalendar::fromDateTime(DateTime $datetime, [string $locale]): IntlCalendar
```php

Estilo procedimental

```php
intlcal_from_date_time(DateTime $datetime, [string $locale]): IntlCalendar
```

Crea un objeto `IntlCalendar` ya sea a partir de un objeto `DateTime` o a partir de un string del cual se puede construir un objeto `DateTime`.

El nuevo calendario representará no solo el mismo instante que el `DateTime` dado (sujeto a pérdida de precisión para fechas muy lejanas en el pasado o futuro), sino también la misma zona horaria (sujeto a la salvedad de que se usarán diferentes bases de datos de zonas horarias, y por lo tanto los resultados pueden diferir).

## Parámetros

`datetime`  
Un objeto `DateTime` o un `string` que puede pasarse a `DateTime::__construct`.

## Valores devueltos

El objeto `IntlCalendar` creado o `null` en caso de error. Si se pasa un `string`, cualquier excepción que ocurra dentro del constructor de `DateTime` se propaga.

## Ejemplos

`IntlCalendar::fromDateTime`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');

//igual que IntlCalendar::fromDateTime(new DateTime(...))
$cal1 = IntlCalendar::fromDateTime('2013-02-28 00:01:02 Europe/Berlin', 'de_DE');

//Nota: la zona horaria es Europe/Berlin, no la predeterminada Europe/Lisbon
echo IntlDateFormatter::formatObject($cal1, 'yyyy MMMM d HH:mm:ss VVVV', 'de_DE'), "\n";

    
```

El ejemplo anterior mostrará:

    2013 Februar 28 00:01:02 Deutschland Zeit
