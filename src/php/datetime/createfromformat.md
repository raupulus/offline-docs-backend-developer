---
title: DateTime::createFromFormat
description: Analiza una cadena con un instante según un formato especificado
source_url: https://www.php.net/manual/es/datetime.createfromformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/createfromformat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 4d13f5e4b
order: 10420
---

DateTime::createFromFormat

date_create_from_format

Analiza una cadena con un instante según un formato especificado

## Descripción

Estilo orientado a objetos

```php
public static DateTime::createFromFormat(string $format, string $datetime, [DateTimeZone $timezone]): DateTime
```php

Estilo procedimental

```php
date_create_from_format(string $format, string $datetime, [DateTimeZone $timezone]): DateTime
```

Devuelve un nuevo objeto DateTime que representa la fecha y la hora especificadas por la cadena `time`, la cual fue formateada en el formato indicado en `format`.

Igual que DateTimeImmutable::createFromFormat y `date_create_immutable_from_format`, respectivamente, pero crea un objeto `DateTime`.

Este método, incluyendo parámetros, ejemplos y consideraciones están documentados en la página [DateTimeImmutable::createFromFormat](#datetimeimmutable.createfromformat).

## Parámetros

Vease [DateTimeImmutable::createFromFormat](#datetimeimmutable.createfromformat).

## Valores devueltos

Devuelve una nueva instancia de DateTime o `false` si ocurre un error.

## Errores/Excepciones

Este método lanza ValueError cuando `datetime` contiene bytes nulos (NULL-bytes).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.21, 8.1.8, 8.2.0 | Ahora lanza ValueError cuando se pasan bytes nulos (NULL-bytes) a `datetime`, cuando antes eran ignorados silenciosamente. |

## Ejemplos

Para una lista extensa de ejemplos, vea [DateTimeImmutable::createFromFormat](#datetimeimmutable.createfromformat).

## Véase también

DateTimeImmutable::createFromFormat
