---
title: IntlGregorianCalendar::__construct
description: Crear la clase del calendario gregoriano
source_url: https://www.php.net/manual/es/intlgregoriancalendar.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlgregoriancalendar/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: d3ee29b81
order: 41340
---

IntlGregorianCalendar::\_\_construct

Crear la clase del calendario gregoriano

## Descripción

```php
public IntlGregorianCalendar::__construct([IntlTimeZone $tz], [string $locale])
```php

```php
public IntlGregorianCalendar::__construct(int $timeZoneOrYear, int $localeOrMonth, int $dayOfMonth)
```

```php
public IntlGregorianCalendar::__construct(int $timeZoneOrYear, int $localeOrMonth, int $dayOfMonth, int $hour, int $minute, [int $second])
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`tz`  

`locale`  

`timeZoneOrYear`  

`localeOrMonth`  

`dayOfMonth`  

`hour`  

`minute`  

`second`  

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Esto ha sido deprecado en favor de los métodos IntlGregorianCalendar::createFromDate y IntlGregorianCalendar::createFromDateTime. |
