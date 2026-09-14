---
title: IntlCalendar::after
description: Verifica si el objeto tiempo actual está en el futuro respecto al objeto
  tiempo pasado
source_url: https://www.php.net/manual/es/intlcalendar.after.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/after.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40200
---

IntlCalendar::after

Verifica si el objeto tiempo actual está en el futuro respecto al objeto tiempo pasado

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::after(IntlCalendar $other): bool
```php

Estilo procedimental

```php
intlcal_after(IntlCalendar $calendar, IntlCalendar $other): bool
```

Verifica si el objeto tiempo actual está en el futuro respecto al objeto tiempo pasado.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`other`  
El calendario para el cual el tiempo será verificado respecto al tiempo del objeto primario.

## Valores devueltos

Retorna `true` si el objeto tiempo actual está en el futuro respecto al tiempo del argumento `calendar`. Retorna `false` en caso contrario.

En caso de fallo, también se devuelve `false`. Para detectar condiciones de error, utilice `intl_get_error_code`, o configure Intl para lanzar [excepciones](#ini.intl.use-exceptions).

## Ejemplos

Ejemplo con `IntlCalendar::after`

```php
<?php
$cal1 = IntlCalendar::createInstance();
$cal2 = clone $cal1;

var_dump($cal1->after($cal2), //false
        $cal2->after($cal1)); //false

$cal1->roll(IntlCalendar::FIELD_MILLISECOND, true);

var_dump($cal1->after($cal2), //true
        $cal2->after($cal1)); //false

    
```
