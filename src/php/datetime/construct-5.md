---
title: DateTimeZone::__construct
description: Crea un nuevo objeto DateTimeZone
source_url: https://www.php.net/manual/es/datetimezone.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimezone/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10840
---

DateTimeZone::\_\_construct

timezone_open

Crea un nuevo objeto DateTimeZone

## Descripción

Estilo orientado a objetos

```php
public DateTimeZone::__construct(string $timezone)
```php

Estilo procedimental

```php
timezone_open(string $timezone): DateTimeZone
```

Crea un nuevo objeto DateTimeZone.

Un objeto DateTimeZone proporciona acceso a tres tipos diferentes de reglas de zona horaria: un desplazamiento UTC (tipo `1`), una abreviatura de zona horaria (tipo `2`), y un [identificador de zona horaria](#timezones) tal como se publica en la base de datos de zonas horarias IANA (tipo `3`).

El objeto DateTimeZone puede ser adjuntado a los objetos `DateTime` y `DateTimeImmutable` con el fin de poder representar la zona horaria encapsulada por estos objetos en una zona horaria local.

## Parámetros

`timezone`  
Una de las [zonas horarias](#timezones) soportadas, un valor de desplazamiento (+0200), o una abreviatura de zona (BST).

## Valores devueltos

Devuelve un objeto `DateTimeZone` en caso de éxito. Estilo procedimental retorna `false` en caso de error..

## Errores/Excepciones

Este método lanza una DateInvalidTimeZoneException si la zona horaria proporcionada no es reconocida como una zona horaria válida. Anteriormente a PHP 8.3, esto era una Exception.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Los valores inválidos ahora lanzan una DateInvalidTimeZoneException en lugar de una Exception genérica. |

## Ejemplos

Creación y adjuntado de DateTimeZone a un DateTimeImmutable

```php
<?php
$d = new DateTimeImmutable("2022-06-02 15:44:48 UTC");

$timezones = [ 'Europe/London', 'GMT+04:45', '-06:00', 'CEST' ];

foreach ($timezones as $tz) {
    $tzo = new DateTimeZone($tz);

    $local = $d->setTimezone($tzo);
    echo $local->format(DateTimeInterface::RFC2822 . ' — e') . "\n";
}

    
```

El ejemplo anterior mostrará:

    Thu, 02 Jun 2022 16:44:48 +0100 — Europe/London
    Thu, 02 Jun 2022 20:29:48 +0445 — +04:45
    Thu, 02 Jun 2022 09:44:48 -0600 — -06:00
    Thu, 02 Jun 2022 17:44:48 +0200 — CEST

Intercepción de errores con `DateTimeZone`

```php
<?php
// Manejo de errores por intercepción de excepciones
$timezones = array('Europe/London', 'Mars/Phobos', 'Jupiter/Europa');

foreach ($timezones as $tz) {
    try {
        $mars = new DateTimeZone($tz);
        echo $mars->getName() . "\n";
    } catch(Exception $e) {
        echo $e->getMessage() . "\n";
    }
}

    
```

El ejemplo anterior mostrará:

    Europe/London
    DateTimeZone::__construct() [datetimezone.--construct]: Unknown or bad timezone (Mars/Phobos)
    DateTimeZone::__construct() [datetimezone.--construct]: Unknown or bad timezone (Jupiter/Europa)
