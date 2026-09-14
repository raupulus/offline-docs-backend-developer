---
title: frenchtojd
description: Convierte una fecha del Calendario Republicano Francés a una fecha Juliana
source_url: https://www.php.net/manual/es/function.frenchtojd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/frenchtojd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_revision: db43575bd
order: 6590
---

frenchtojd

Convierte una fecha del Calendario Republicano Francés a una fecha Juliana

## Descripción

```php
frenchtojd(int $month, int $day, int $year): int
```php

Convierte una fecha del Calendario Republicano Francés a una fecha Juliana.

Estas rutinas sólamente convierten fechas de los años 1 al 14 (fechas gregorianas desde el 22 de septiembre de 1792 hasta el 22 de septiembre de 1806). Esto cubre con creces el periodo cuando el calendario estaba en uso.

## Parámetros

`month`  
El mes como un número desde 1 (para Vendémiaire) hasta 13 (para el periodo de 5-6 días al final de cada año)

`day`  
El día como un número de 1 a 30

`year`  
El año como un número entre 1 y 14

## Valores devueltos

La fecha Juliana para la fecha de la Revolución Francesa dada como un entero.

## Véase también

`jdtofrench`, `cal_to_jd`
