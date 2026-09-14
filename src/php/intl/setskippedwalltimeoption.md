---
title: IntlCalendar::setSkippedWallTimeOption
description: Define el comportamiento para la gestión de las horas murales saltadas
  durante las transiciones de desplazamiento horario positivo
source_url: https://www.php.net/manual/es/intlcalendar.setskippedwalltimeoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/setskippedwalltimeoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 2ca090342
order: 40630
---

IntlCalendar::setSkippedWallTimeOption

Define el comportamiento para la gestión de las horas murales saltadas durante las transiciones de desplazamiento horario positivo

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::setSkippedWallTimeOption(int $option): true
```php

Estilo procedimental

```php
intlcal_set_skipped_wall_time_option(IntlCalendar $calendar, int $option): true
```

Define la estrategia actual para la gestión de las horas murales saltadas cada vez que el reloj se adelanta durante las transiciones de inicio del horario de verano. El valor por omisión es `IntlCalendar::WALLTIME_LAST` (tomar el instante post-DST). Los otros valores posibles son `IntlCalendar::WALLTIME_FIRST` (tomar el instante que ocurre durante el horario de verano) y `IntlCalendar::WALLTIME_NEXT_VALID` (tomar el instante cuando comienza el horario de verano).

Esto afecta únicamente al instante representado por el calendario (tal como se informa por `IntlCalendar::getTime`), los valores de los campos no serán sobrescritos en consecuencia.

El calendario debe ser [tolerante](#intlcalendar.setlenient) para que esta opción tenga efecto, de lo contrario intentar definir un tiempo inexistente provocará una error.

Esta función requiere ICU 4.9 o superior.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`option`  
Una de las constantes `IntlCalendar::WALLTIME_FIRST`, `IntlCalendar::WALLTIME_LAST` o `IntlCalendar::WALLTIME_NEXT_VALID`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ver un ejemplo en `IntlCalendar::getSkippedWallTimeOption`.

## Véase también

intlCalendar::getSkippedWallTimeOption, intlCalendar::setRepeatedWallTimeOption, intlCalendar::getRepeatedWallTimeOption
