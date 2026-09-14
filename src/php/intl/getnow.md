---
title: IntlCalendar::getNow
description: Obtiene el número que representa la fecha actual
source_url: https://www.php.net/manual/es/intlcalendar.getnow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getnow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40430
---

IntlCalendar::getNow

Obtiene el número que representa la fecha actual

## Descripción

Estilo orientado a objetos

```php
public static IntlCalendar::getNow(): float
```php

Estilo procedimental

```php
intlcal_get_now(): float
```

El número de milisegundos transcurridos desde la fecha de referencia. Este número se deriva del tiempo del sistema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un número de coma flotante que representa un número de milisegundos desde la época, sin contar los segundos intercalares.

## Ejemplos

Ejemplo con `IntlCalendar::getNow`

```php
<?php
$formatter = IntlDateFormatter::create('es_ES',
        IntlDateFormatter::FULL,
        IntlDateFormatter::FULL,
        'Europe/Madrid');

$val = IntlCalendar::getNow();

var_dump($val);
echo $formatter->format(IntlCalendar::getNow() / 1000.), "\n";

    
```

El ejemplo anterior mostrará:

    float(1371425814666)
    lunes, 17 de junio de 2013 01:36:54 Hora de verano de Europa central
