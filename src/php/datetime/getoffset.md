---
title: DateTimeInterface::getOffset
description: Devuelve el desplazamiento horario
source_url: https://www.php.net/manual/es/datetime.getoffset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/getoffset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10770
---

DateTimeInterface::getOffset

DateTimeImmutable::getOffset

DateTime::getOffset

date_offset_get

Devuelve el desplazamiento horario

## Descripción

Estilo orientado a objetos

```php
public DateTimeInterface::getOffset(): int
```php

```php
public DateTimeImmutable::getOffset(): int
```

```php
public DateTime::getOffset(): int
```php

Estilo procedimental

```php
date_offset_get(DateTimeInterface $object): int
```

Devuelve el desplazamiento horario.

## Parámetros

`object`  
Solo en estilo procedimental: un objeto `DateTime` retornado por `date_create`

## Valores devueltos

Devuelve el desplazamiento horario en segundos, desde UTC en caso de éxito.

## Ejemplos

Ejemplo con `DateTime::getOffset`

Estilo orientado a objetos

```php
<?php
$winter = new DateTimeImmutable('2010-12-21', new DateTimeZone('America/New_York'));
$summer = new DateTimeImmutable('2008-06-21', new DateTimeZone('America/New_York'));

echo $winter->getOffset() . "\n";
echo $summer->getOffset() . "\n";

   
```

El ejemplo anterior mostrará:

    -18000
    -14400

       

Estilo procedimental

```php
<?php
$winter = date_create('2010-12-21', timezone_open('America/New_York'));
$summer = date_create('2008-06-21', timezone_open('America/New_York'));

echo date_offset_get($winter) . "\n";
echo date_offset_get($summer) . "\n";

   
```

El ejemplo anterior mostrará:

    -18000
    -14400

       

Nota: -18000 = -5 horas, -14400 = -4 horas.
