---
title: DateTimeInterface::getTimestamp
description: Obtiene el timestamp Unix
source_url: https://www.php.net/manual/es/datetime.gettimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/gettimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 726154e3c
order: 10780
---

DateTimeInterface::getTimestamp

DateTimeImmutable::getTimestamp

DateTime::getTimestamp

date_timestamp_get

Obtiene el timestamp Unix

## Descripción

Estilo orientado a objetos

```php
public DateTimeInterface::getTimestamp(): int
```php

```php
public DateTimeImmutable::getTimestamp(): int
```

```php
public DateTime::getTimestamp(): int
```php

Estilo procedimental

```php
date_timestamp_get(DateTimeInterface $object): int
```

Obtiene el timestamp Unix.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el timestamp Unix que representa la fecha.

## Errores/Excepciones

Si el sello de tiempo no puede ser representado como un `int`, se lanza una DateRangeError. Anterior a PHP 8.3.0, se lanzaba una ValueError. Y anterior a PHP 8.0.0, se devolvía `false` en este caso. Sin embargo, el sello de tiempo puede ser obtenido como un `string` utilizando DateTimeInterface::format con el formato `U`.

## Historial de cambios

| Versión | Descripción                                                 |
|---------|-------------------------------------------------------------|
| 8.3.0   | La excepción de fuera de rango ahora es una DateRangeError. |
| 8.0.0   | Estas funciones ya no devuelven `false` en caso de fallo.   |

## Ejemplos

Ejemplo con `DateTime::getTimestamp`

Estilo orientado a objetos

```php
<?php
$date = new DateTimeImmutable();
echo $date->getTimestamp();

   
```

Resultado del ejemplo anterior es similar a:

    1272509157

       

Estilo procedimental

```php
<?php
$date = date_create();
echo date_timestamp_get($date);

   
```

Resultado del ejemplo anterior es similar a:

    1272509157

Para obtener el sello de tiempo con precisión en milisegundos o microsegundos, es posible utilizar la función `DateTimeInterface::format`.

Obtención del sello de tiempo con precisión en milisegundos y microsegundos

Estilo orientado a objetos

```php
<?php
$date = new DateTimeImmutable();
$milli = (int) $date->format('Uv'); // Timestamp en milisegundos
$micro = (int) $date->format('Uu'); // Timestamp en microsegundos

echo $milli, "\n", $micro, "\n";

   
```

Resultado del ejemplo anterior es similar a:

    1674057635586
    1674057635586918

## Véase también

DateTime::setTimestamp

DateTimeImmutable::setTimestamp

DateTimeInterface::format

DateTimeInterface::getMicrosecond
