---
title: DateTime::setDate
description: Establece la fecha
source_url: https://www.php.net/manual/es/datetime.setdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/setdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 02ff7fef5
order: 10490
---

DateTime::setDate

date_date_set

Establece la fecha

## Descripción

Estilo orientado a objetos

```php
public DateTime::setDate(int $year, int $month, int $day): DateTime
```php

Estilo procedimental

```php
date_date_set(DateTime $object, int $year, int $month, int $day): DateTime
```

Reinicia la fecha actual del objeto DateTime a una fecha diferente.

Igual que DateTimeImmutable::setDate pero funciona con `DateTime`, y cambia el objeto existente.

La versión procedural toma el objeto `DateTime` como su primer argumento.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`year`  
Año de la fecha.

`month`  
Mes de la fecha.

`day`  
Día de la fecha.

## Valores devueltos

Retorna el objeto modificado `DateTime` para encadenar métodos.

## Véase también

DateTimeImmutable::setDate
