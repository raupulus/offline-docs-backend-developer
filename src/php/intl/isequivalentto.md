---
title: IntlCalendar::isEquivalentTo
description: Indica si otro calendario es equivalente, pero para otro momento
source_url: https://www.php.net/manual/es/intlcalendar.isequivalentto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/isequivalentto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40510
---

IntlCalendar::isEquivalentTo

Indica si otro calendario es equivalente, pero para otro momento

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::isEquivalentTo(IntlCalendar $other): bool
```php

Estilo procedimental

```php
intlcal_is_equivalent_to(IntlCalendar $calendar, IntlCalendar $other): bool
```

Devuelve si este objeto y el proporcionado son equivalentes para todos los usos, excepto por el momento que han definido. Las zonas horarias no necesitan coincidir, siempre que no resulte ningún cambio de comportamiento. Esto incluye la [zona horaria](#intlcalendar.gettimezone), si el [modo laxista](#intlcalendar.islenient) está definido, los parámetros de tiempo de pared [repetido](#intlcalendar.getrepeatedwalltimeoption) y [saltado](#intlcalendar.getskippedwalltimeoption), los [días de la semana donde comienza y termina el fin de semana](#intlcalendar.getdayofweektype) y las [horas donde ocurren tales transiciones](#intlcalendar.getweekendtransition). Esto puede incluir también otros parámetros específicos del calendario, como el instante de transición gregoriano/juliano.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`other`  
El otro calendario con respecto al cual se debe realizar la comparación.

## Valores devueltos

Suponiendo que no hay errores de argumento, devuelve `true` si los calendarios son equivalentes, excepto quizás por su momento definido.

## Ejemplos

`IntlCalendar::isEquivalentTo`

```php
<?php
$cal1 = IntlCalendar::createInstance('Europe/Lisbon', 'pt_PT');
$cal2 = IntlCalendar::createInstance('Europe/Lisbon', 'es_ES');
$cal2->clear();

var_dump($cal1->isEquivalentTo($cal2)); // true

$cal3 = IntlCalendar::createInstance('Europe/Lisbon', 'en_US');
var_dump($cal1->isEquivalentTo($cal3)); // false
var_dump($cal1->getFirstDayOfWeek(),    // 2 (Monday)
$cal3->getFirstDayOfWeek());            // 1 (Sunday)

    
```

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    int(2)
    int(1)

## Véase también

IntlCalendar::equals
