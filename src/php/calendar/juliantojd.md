---
title: juliantojd
description: Convierte una fecha del Calendario Juliano a una Fecha Juliana
source_url: https://www.php.net/manual/es/function.juliantojd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/juliantojd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 6690
---

juliantojd

Convierte una fecha del Calendario Juliano a una Fecha Juliana

## Descripción

```php
juliantojd(int $month, int $day, int $year): int
```php

El rango válido para el Calendario Juliano es desde 4713 A.C. a 9999 D.C.

Aunque esta función puede manejar fechas que se remontan hasta 4713 A.C., tal uso puede no ser significativo. El calendario fue creado en el 46 A.C., pero los detalles no se estabilizaron hasta al menos el 8 D.C., y quizás hasta el siglo IV tardío. También, el comienzo de un año variaba de una cultura a otra - no todas aceptaron enero como el primer mes.

> [!CAUTION]
> Recuerde, el sistema de calendario actual que se usa mundialmente es el Calendario Gregoriano. `gregoriantojd` se puede usar para convertir tales fechas a sus Fechas Julianas.

## Parámetros

`month`  
El mes como un número de 1 (para enero) a 12 (para diecienbre)

`day`  
El día como un número de 1 a 31

`year`  
El año como un número entre -4713 y 9999

## Valores devueltos

La Fecha Juliana para la fecha del Calendario Juliano dado como un entero.

## Véase también

`jdtojulian`, `cal_to_jd`
