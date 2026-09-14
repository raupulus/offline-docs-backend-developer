---
title: IntlCalendar::setRepeatedWallTimeOption
description: Define el comportamiento para la gestión de las horas murales repetidas
  durante las transiciones de cambio de huso horario negativo
source_url: https://www.php.net/manual/es/intlcalendar.setrepeatedwalltimeoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/setrepeatedwalltimeoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 2ca090342
order: 40620
---

IntlCalendar::setRepeatedWallTimeOption

Define el comportamiento para la gestión de las horas murales repetidas durante las transiciones de cambio de huso horario negativo

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::setRepeatedWallTimeOption(int $option): true
```php

Estilo procedimental

```php
intlcal_set_repeated_wall_time_option(IntlCalendar $calendar, int $option): true
```

Define la estrategia actual para la gestión de las horas murales repetidas cada vez que el reloj se retrasa durante las transiciones de fin del horario de verano. El valor por omisión es `IntlCalendar::WALLTIME_LAST` (tomar el instante post-DST). El otro valor posible es `IntlCalendar::WALLTIME_FIRST` (tomar el instante que ocurre durante el horario de verano).

Esta función requiere ICU 4.9 o superior.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`option`  
Una de las constantes `IntlCalendar::WALLTIME_FIRST` o `IntlCalendar::WALLTIME_LAST`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ver un ejemplo en `IntlCalendar::getRepeatedWallTimeOption`.

## Véase también

intlCalendar::getRepeatedWallTimeOption, intlCalendar::setSkippedWallTimeOption, intlCalendar::getSkippedWallTimeOption
