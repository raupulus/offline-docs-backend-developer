---
title: IntlCalendar::getLocale
description: Devuelve la configuración local asociada al objeto
source_url: https://www.php.net/manual/es/intlcalendar.getlocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getlocale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40390
---

IntlCalendar::getLocale

Devuelve la configuración local asociada al objeto

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getLocale(int $type): string
```php

Estilo procedimental

```php
intlcal_get_locale(IntlCalendar $calendar, int $type): string
```

Devuelve la configuración local utilizada por este objeto calendario.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`type`  
Indica si la configuración local actual (la configuración local a partir de la cual provienen los datos del calendario, con `Locale::ACTUAL_LOCALE`) o la configuración local válida, es decir, la configuración local más específica soportada por ICU en relación con la configuración local solicitada – ver `Locale::VALID_LOCALE`. De la más general a la más específica, las configuraciones locales se ordenan de esta forma – configuración local actual, configuración local válida, configuración local solicitada.

## Valores devueltos

Un string que representa la configuración local o `false` si ocurre un error.

## Ejemplos

`IntlCalendar::getLocale`

```php
<?php
$cal = IntlCalendar::createInstance(IntlTimeZone::getGMT(), 'en_US_CALIFORNIA');
var_dump(
    $cal->getLocale(Locale::ACTUAL_LOCALE),
    $cal->getLocale(Locale::VALID_LOCALE)
);

    
```

El ejemplo anterior mostrará:

    string(2) "en"
    string(5) "en_US"
