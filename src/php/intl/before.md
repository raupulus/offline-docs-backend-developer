---
title: IntlCalendar::before
description: Verifica si el objeto tiempo está en el pasado en relación con el objeto
  proporcionado
source_url: https://www.php.net/manual/es/intlcalendar.before.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/before.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40210
---

IntlCalendar::before

Verifica si el objeto tiempo está en el pasado en relación con el objeto proporcionado

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::before(IntlCalendar $other): bool
```php

Estilo procedimental

```php
intlcal_before(IntlCalendar $calendar, IntlCalendar $other): bool
```

Verifica si el objeto tiempo está en el pasado en relación con el objeto proporcionado.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`other`  
El calendario para el cual el tiempo será verificado en relación con el tiempo del objeto principal.

## Valores devueltos

Devuelve `true` si el objeto tiempo actual está en el pasado en relación con el tiempo del argumento `calendar`. Devuelve `false` en caso contrario.

En caso de fallo, también se devuelve `false`. Para detectar condiciones de error, utilice `intl_get_error_code`, o configure Intl para lanzar [excepciones](#ini.intl.use-exceptions).
