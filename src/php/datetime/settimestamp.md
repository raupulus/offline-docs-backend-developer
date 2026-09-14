---
title: DateTime::setTimestamp
description: Establece la fecha y la hora basándose en una marca temporal de Unix
source_url: https://www.php.net/manual/es/datetime.settimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/settimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 726154e3c
order: 10530
---

DateTime::setTimestamp

date_timestamp_set

Establece la fecha y la hora basándose en una marca temporal de Unix

## Descripción

Estilo orientado a objetos

```php
public DateTime::setTimestamp(int $timestamp): DateTime
```php

Estilo procedimental

```php
date_timestamp_set(DateTime $object, int $timestamp): DateTime
```

Establece la fecha y la hora basándose en una marca temporal de Unix (Unix timestamp).

Igual que DateTimeImmutable::setTimestamp pero funciona con `DateTime`.

La versión procedural toma el objeto `DateTime` como su primer argumento.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`timestamp`  
La marca temporal de Unix que representa la fecha. Establecer marcas de tiempo fuera del rango de `int` es posible usando DateTimeImmutable::modify con el formato `@`.

## Valores devueltos

Retorna el objeto modificado `DateTime` para encadenar métodos.

## Véase también

DateTimeImmutable::setTimestamp

DateTime::setMicrosecond
