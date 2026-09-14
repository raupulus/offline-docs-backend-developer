---
title: DateTime::setISODate
description: Establece la fecha ISO
source_url: https://www.php.net/manual/es/datetime.setisodate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/setisodate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 02ff7fef5
order: 10500
---

DateTime::setISODate

date_isodate_set

Establece la fecha ISO

## Descripción

Estilo orientado a objetos

```php
public DateTime::setISODate(int $year, int $week, [int $dayOfWeek]): DateTime
```php

Estilo procedimental

```php
date_isodate_set(DateTime $object, int $year, int $week, [int $dayOfWeek]): DateTime
```

Establece una fecha según el estándar ISO 8601, empleando índices de semanas y días en vez de fechas específicas.

Igual que DateTimeImmutable::setISODate pero funciona con `DateTime`.

La versión procedural toma el objeto `DateTime` como su primer argumento.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`year`  
Año de la fecha.

`week`  
Semana de la fecha.

`dayOfWeek`  
Desplazamiento desde el primer día de la semana.

## Valores devueltos

Retorna el objeto modificado `DateTime` para encadenar métodos.

## Véase también

DateTimeImmutable::setISODate
