---
title: DateTimeImmutable::modify
description: Crea un nuevo objeto con la marca de tiempo modificada
source_url: https://www.php.net/manual/es/datetimeimmutable.modify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/modify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 10640
---

DateTimeImmutable::modify

Crea un nuevo objeto con la marca de tiempo modificada

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::modify() does not modify the object itself")] public DateTimeImmutable::modify(string $modifier): DateTimeImmutable
```php

Crea un nuevo objeto `DateTimeImmutable` con la marca de tiempo modificada. El objeto original no se modifica.

## Parámetros

`modifier`  
Una cadena de fecha/hora. Los formatos válidos son explicados en la documentación sobre los [formatos de Fecha y Hora](#datetime.formats).

## Valores devueltos

Devuelve `DateTimeImmutable` en caso de éxito. Estilo procedimental retorna `false` en caso de error.

## Errores/Excepciones

Si se pasa una cadena de Fecha/Hora no válida, se lanza DateMalformedStringException. Antes de PHP 8.3, esto emitía una advertencia.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora tiene un tipo de retorno tentativo de `DateTimeImmutable`. Anteriormente era `DateTimeImmutablefalse`. |
| 8.3.0 | DateTimeImmutable::modify ahora lanzará DateMalformedStringException si es pasada una cadena no válida. Anteriormente, devolvía `false`, y se emitía una advertencia. |

## Ejemplos

Ejemplo de `DateTimeImmutable::modify`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable('2006-12-12');
$newDate = $date->modify('+1 day');
echo $newDate->format('Y-m-d');

   
```php

El ejemplo anterior mostrará:

    2006-12-13

Tenga cuidado al añadir o restar meses

```
<?php
$date = new DateTimeImmutable('2000-12-31');

$newDate1 = $date->modify('+1 month');
echo $newDate1->format('Y-m-d') . "\n";

$newDate2 = $newDate1->modify('+1 month');
echo $newDate2->format('Y-m-d') . "\n";

   
```php

El ejemplo anterior mostrará:

    2001-01-31
    2001-03-03

## Véase también

DateTimeImmutable::add

DateTimeImmutable::sub

DateTimeImmutable::setDate

DateTimeImmutable::setISODate

DateTimeImmutable::setTime

DateTimeImmutable::setTimestamp
