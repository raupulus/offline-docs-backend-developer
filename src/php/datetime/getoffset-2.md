---
title: DateTimeZone::getOffset
description: Retorna el desplazamiento GMT de una zona horaria
source_url: https://www.php.net/manual/es/datetimezone.getoffset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimezone/getoffset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10870
---

DateTimeZone::getOffset

timezone_offset_get

Retorna el desplazamiento GMT de una zona horaria

## Descripción

Estilo orientado a objetos

```php
public DateTimeZone::getOffset(DateTimeInterface $datetime): int
```php

Estilo procedimental

```php
timezone_offset_get(DateTimeZone $object, DateTimeInterface $datetime): int
```

Esta función retorna el desplazamiento GMT para la fecha/hora especificada en el parámetro `datetime`. El desplazamiento GMT se calcula a partir de las informaciones de zona horaria contenidas en el objeto DateTimeZone utilizado.

## Parámetros

`object`  
Solo en estilo procedimental: un objeto `DateTimeZone` retornado por `timezone_open`

`datetime`  
DateTime que contiene la fecha/hora desde la cual se debe calcular el desplazamiento.

## Valores devueltos

Retorna el desplazamiento horario, expresado en segundos, en caso de éxito.

## Ejemplos

Ejemplo con `DateTimeZone::getOffset`

```php
<?php
// Crea dos objetos zona horaria, uno para Taipei (Taiwán) y uno para
// Tokio (Japón)
$dateTimeZoneTaipei = new DateTimeZone("Asia/Taipei");
$dateTimeZoneJapan = new DateTimeZone("Asia/Tokyo");

// Crea dos objetos DateTime que contienen el mismo timestamp Unix,
// pero están situados en dos zonas horarias diferentes.
$dateTimeTaipei = new DateTime("now", $dateTimeZoneTaipei);
$dateTimeJapan = new DateTime("now", $dateTimeZoneJapan);

// Calcula el desplazamiento horario GMT para el objeto $dateTimeTaipei
// pero utilizando la zona horaria de Tokio
// ($dateTimeZoneJapan).
$timeOffset = $dateTimeZoneJapan->getOffset($dateTimeTaipei);

// Debería mostrar int(32400) (para las fechas posteriores al Sat Sep 8 01:00:00 1951 JST).
var_dump($timeOffset);

    
```

El ejemplo anterior mostrará:

    int(32400)
