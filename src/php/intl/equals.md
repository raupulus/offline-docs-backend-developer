---
title: IntlCalendar::equals
description: Verifica si dos objetos IntlCalendar son iguales
source_url: https://www.php.net/manual/es/intlcalendar.equals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/equals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40250
---

IntlCalendar::equals

Verifica si dos objetos IntlCalendar son iguales

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::equals(IntlCalendar $other): bool
```php

Estilo procedimental

```php
intlcal_equals(IntlCalendar $calendar, IntlCalendar $other): bool
```

Devuelve `true` si este calendario y el proporcionado tienen el mismo tiempo. La configuración, el tipo de calendario, y los estados de los campos no deben ser necesariamente los mismos.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`other`  
El calendario a comparar con el objeto principal.

## Valores devueltos

Devuelve `true` si el tiempo actual es idéntico al del objeto `IntlCalendar` o `false` en caso contrario.

En caso de fallo, también se devuelve `false`. Para detectar condiciones de error, utilice `intl_get_error_code`, o configure Intl para lanzar [excepciones](#ini.intl.use-exceptions).

## Ejemplos

Ejemplo con `IntlCalendar::equals`

```php
<?php
ini_set('date.timezone', 'UTC');

$cal1 = IntlCalendar::createInstance(NULL, 'es_ES');
$cal2 = clone $cal1;

var_dump($cal1->equals($cal2)); //TRUE

//La configuración local no está incluida en la comparación
$cal2 = IntlCalendar::createInstance(NULL, 'pt_PT');
$cal2->setTime($cal1->getTime());
var_dump($cal1->equals($cal2)); //TRUE

//Tampoco lo están los estados de los campos
$cal2->clear(IntlCalendar::FIELD_YEAR);
var_dump($cal1->isSet(IntlCalendar::FIELD_YEAR) ==
        $cal2->isSet(IntlCalendar::FIELD_YEAR)); //FALSE
var_dump($cal1->equals($cal2)); //TRUE

//Ni el tipo de calendario
$cal2 = IntlCalendar::createInstance(NULL, 'es_ES@calendar=islamic');
$cal2->setTime($cal1->getTime());
var_dump($cal1->equals($cal2)); //TRUE

//Solo el tiempo lo es
$cal2 = clone $cal1;
$cal2->setTime($cal1->getTime() + 1.);
var_dump($cal1->equals($cal2)); //FALSE

    
```
