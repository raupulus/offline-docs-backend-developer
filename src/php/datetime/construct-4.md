---
title: DateTimeImmutable::__construct
description: Devuelve un nuevo objeto DateTimeImmutable
source_url: https://www.php.net/manual/es/datetimeimmutable.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 10580
---

DateTimeImmutable::\_\_construct

date_create_immutable

Devuelve un nuevo objeto DateTimeImmutable

## Descripción

Estilo orientado a objetos

```php
public DateTimeImmutable::__construct([string $datetime], [DateTimeZone $timezone])
```php

Estilo procedimental

```php
date_create_immutable([string $datetime], [DateTimeZone $timezone]): DateTimeImmutable
```

Devuelve un nuevo objeto DateTimeImmutable.

## Parámetros

`datetime`  
Una cadena de fecha/hora. Los formatos válidos son explicados en la documentación sobre los [formatos de Fecha y Hora](#datetime.formats).

Introduzca `"now"` aquí para obtener el instante actual cuando se emplee el parámetro `timezone`.

`timezone`  
Un objeto `DateTimeZone` que representa la zona horaria de `datetime`.

Si se omite `timezone` o es `null`, se usará la zona horaria actual.

> [!NOTE]
> El parámetro `timezone` y la zona horaria actuales se ignoran cuando el parámetro `time` es una marca temporal de UNIX (p.ej. `@946684800`) o especifica una zona horaria (p.ej. `2010-01-28T15:00:00+02:00`, o `2010-07-05T06:00:00Z`).

## Valores devueltos

Devuelve una nueva instancia de DateTimeImmutable.

## Errores/Excepciones

Si se pasa una cadena de fecha/hora incorrecta, lanza DateMalformedStringException. Hasta PHP 8.3, lanzaba Exception.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza DateMalformedStringException si se pasa una cadena incorrecta, en vez de Exception. |
| 7.1.0 | Desde ahora los microsegundos se rellenan con el valor actual. No con '00000'. |

## Ejemplos

Ejemplo de `DateTimeImmutable::__construct`

Estilo orientado a objetos

```php
<?php
try {
    $date = new DateTimeImmutable('2000-01-01');
} catch (Exception $e) {
    echo $e->getMessage();
    exit(1);
}

echo $date->format('Y-m-d');

   
```

El ejemplo anterior mostrará:

    2000-01-01

       

Estilo procedimental

```php
<?php
$date = date_create('2000-01-01');
if (!$date) {
    $e = date_get_last_errors();
    foreach ($e['errors'] as $error) {
        echo "$error\n";
    }
    exit(1);
}

echo date_format($date, 'Y-m-d');

   
```

El ejemplo anterior mostrará:

    2000-01-01

Complejidades de `DateTimeImmutable::__construct`

```php
<?php
date_default_timezone_set('America/Jamaica');

// Especificando una fecha/hora en la zona horaria por omisión
$date = new DateTimeImmutable('2000-01-01');
echo $date->format('Y-m-d H:i:sP') . "\n";

// Especificando una fecha/hora en una zona horaria específica.
$date = new DateTimeImmutable('2000-01-01', new DateTimeZone('Pacific/Nauru'));
echo $date->format('Y-m-d H:i:sP') . "\n";

// Fecha/hora actual en la zona horaria por omisión de PHP.
$date = new DateTimeImmutable();
echo $date->format('Y-m-d H:i:sP') . "\n";

// Fecha/hora actual en la zona horaria especificada.
$date = new DateTimeImmutable('now', new DateTimeZone('Pacific/Nauru'));
echo $date->format('Y-m-d H:i:sP') . "\n";

// Usando una marca temporal de UNIX (UNIX timestamp). Observe que el resultado está en la zona horaria UTC.
$date = new DateTimeImmutable('@946684800');
echo $date->format('Y-m-d H:i:sP') . "\n";

// Completado de los valores inexistentes.
$date = new DateTimeImmutable('2000-02-30');
echo $date->format('Y-m-d H:i:sP') . "\n";

   
```

Resultado del ejemplo anterior es similar a:

    2000-01-01 00:00:00-05:00
    2000-01-01 00:00:00+12:00
    2010-04-24 10:24:16-04:00
    2010-04-25 02:24:16+12:00
    2000-01-01 00:00:00+00:00
    2000-03-01 00:00:00-05:00

       

> [!NOTE]
> Las fechas desbordadas se pueden detectar comprobando las advertencias mediante `DateTimeImmutable::getLastErrors`.

Cambiando la zona horaria asociada

```php
<?php
$timeZone = new \DateTimeZone('Asia/Tokyo');

$time = new \DateTimeImmutable();
$time = $time->setTimezone($timeZone);

echo $time->format('Y/m/d H:i:s e'), "\n";

   
```

Resultado del ejemplo anterior es similar a:

    2022/08/12 23:49:23 Asia/Tokyo

Usando una fecha/hora relativas

```php
<?php
$time = new \DateTimeImmutable("-1 year");

echo $time->format('Y/m/d H:i:s'), "\n";

   
```

Resultado del ejemplo anterior es similar a:

    2021/08/12 15:43:51
