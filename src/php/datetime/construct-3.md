---
title: DateTime::__construct
description: Devuelve un nuevo objeto DateTime
source_url: https://www.php.net/manual/es/datetime.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 4de6272a1
order: 10410
---

DateTime::\_\_construct

Devuelve un nuevo objeto DateTime

## Descripción

```php
public DateTime::__construct([string $datetime], [DateTimeZone $timezone])
```php

Igual que DateTimeImmutable::\_\_construct pero funciona con `DateTime`. Considere usar `DateTimeImmutable` y sus características en su lugar.

Devuelve un nuevo objeto DateTime.

## Parámetros

`datetime`  
Una cadena de fecha/hora. Los formatos válidos son explicados en la documentación sobre los [formatos de Fecha y Hora](#datetime.formats).

Introduzca `"now"` aquí para obtener el instante actual cuando se emplee el parámetro `timezone`.

`timezone`  
Un objeto `DateTimeZone` que representa la zona horaria de `datetime`.

Si se omite `timezone` o es `null`, se usará la zona horaria actual.

> [!NOTE]
> El parámetro `timezone` y la zona horaria actuales se ignoran cuando el parámetro `time` es una marca temporal de UNIX (p.ej. `@946684800`) o especifica una zona horaria (p.ej. `2010-01-28T15:00:00+02:00`).

## Valores devueltos

Devuelve una nueva instancia de DateTime.

## Errores/Excepciones

Si se pasa una cadena de fecha/hora incorrecta, lanza DateMalformedStringException. Hasta PHP 8.3, lanzaba Exception.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza DateMalformedStringException si se pasa una cadena incorrecta, en vez de Exception. |

## Véase también

DateTimeImmutable::\_\_construct
