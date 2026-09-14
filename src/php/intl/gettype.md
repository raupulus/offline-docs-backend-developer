---
title: IntlCalendar::getType
description: Obtiene el tipo de calendario
source_url: https://www.php.net/manual/es/intlcalendar.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40480
---

IntlCalendar::getType

Obtiene el tipo de calendario

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getType(): string
```php

Estilo procedimental

```php
intlcal_get_type(IntlCalendar $calendar): string
```

Una cadena de caracteres que describe el tipo de este calendario. Esta cadena será una de las [valores válidos](#intlcalendar.getkeywordvaluesforlocale) de la palabra clave `'calendar'` del calendario.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Una cadena de caracteres `string` que representa el tipo de calendario, por ejemplo, `'gregorian'`, `'islamic'`, etc.

## Ejemplos

Ejemplo con `IntlCalendar::getType`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'en_US');

$cal = IntlCalendar::createInstance(NULL, '@calendar=ethiopic-amete-alem');
var_dump($cal->getType());

$cal = new IntlGregorianCalendar();
var_dump($cal->getType());

    
```

El ejemplo anterior mostrará:

    string(19) "ethiopic-amete-alem"
    string(9) "gregorian"
