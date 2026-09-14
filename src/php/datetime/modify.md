---
title: DateTime::modify
description: Altera la marca temporal
source_url: https://www.php.net/manual/es/datetime.modify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/modify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 10470
---

DateTime::modify

date_modify

Altera la marca temporal

## Descripción

Estilo orientado a objetos

```php
public DateTime::modify(string $modifier): DateTime
```php

Estilo procedimental

```php
date_modify(DateTime $object, string $modifier): DateTime
```

Altera la marca temporal de un objeto DateTime aumentando o disminuyendo en un formato aceptado por `DateTimeImmutable::__construct`.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`modifier`  
Una cadena de fecha/hora. Los formatos válidos son explicados en la documentación sobre los [formatos de Fecha y Hora](#datetime.formats).

## Valores devueltos

Devuelve `DateTime` en caso de éxito. Estilo procedimental retorna `false` en caso de error.

## Errores/Excepciones

Solo en la API Orientada a Objetos: Si se pasa una cadena de Fecha/Hora inválida, se lanza DateMalformedStringException.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora tiene un tipo de retorno tentativo de `DateTime`. Anteriormente era `DateTimefalse`. |
| 8.3.0 | DateTime::modify ahora lanza DateMalformedStringException si se pasa una cadena inválida. Anteriormente, devolvía `false`, y se emitía una advertencia. `date_modify` no ha cambiado. |

## Ejemplos

Ejemplo de `DateTime::modify`

Estilo orientado a objetos

```php
<?php
$date = new DateTime('2006-12-12');
$date->modify('+1 day');
echo $date->format('Y-m-d');

   
```

El ejemplo anterior mostrará:

    2006-12-13

       

Estilo procedimental

```php
<?php
$date = date_create('2006-12-12');
date_modify($date, '+1 day');
echo date_format($date, 'Y-m-d');

   
```

El ejemplo anterior mostrará:

    2006-12-13

Cuidado al añadir o sustraer meses

```php
<?php
$date = new DateTime('2000-12-31');

$date->modify('+1 month');
echo $date->format('Y-m-d') . "\n";

$date->modify('+1 month');
echo $date->format('Y-m-d') . "\n";

   
```

El ejemplo anterior mostrará:

    2001-01-31
    2001-03-03

Todos los formatos de Fecha y Hora son admitidos

```php
<?php
$date = new DateTime('2020-12-31');

$date->modify('July 1st, 2023');
echo $date->format('Y-m-d H:i') . "\n";

$date->modify('Monday next week');
echo $date->format('Y-m-d H:i') . "\n";

$date->modify('17:30');
echo $date->format('Y-m-d H:i') . "\n";

   
```

El ejemplo anterior mostrará:

    2023-07-01 00:00
    2023-07-03 00:00
    2023-07-03 17:30

## Véase también

strtotime

DateTimeImmutable::modify

DateTime::add

DateTime::sub

DateTime::setDate

DateTime::setISODate

DateTime::setTime

DateTime::setTimestamp
