---
title: DateTime::sub
description: Sustrae una cantidad de días, meses, años, horas, minutos y segundos
  de un objeto DateTime
source_url: https://www.php.net/manual/es/datetime.sub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/sub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: c8ba91f7e
order: 10550
---

DateTime::sub

date_sub

Sustrae una cantidad de días, meses, años, horas, minutos y segundos de un objeto DateTime

## Descripción

Estilo orientado a objetos

```php
public DateTime::sub(DateInterval $interval): DateTime
```php

Estilo procedimental

```php
date_sub(DateTime $object, DateInterval $interval): DateTime
```

Modifica el objeto DateTime especificado, sustrayendo el objeto `DateInterval` especificado.

Igual que DateTimeImmutable::sub pero funciona con `DateTime`.

La versión procedural toma el objeto `DateTime` como su primer argumento.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`interval`  
Un objeto `DateInterval`

## Valores devueltos

Retorna el objeto modificado `DateTime` para encadenar métodos.

## Errores/Excepciones

Solo en la API Orientada a Objetos: Si se intenta realizar una operación no soportada, como usar un objeto `DateInterval` que represente especificaciones de tiempo relativas como `próximo día de la semana`, se lanzará una DateInvalidOperationException.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza una DateInvalidOperationException con DateTime::sub, en lugar de una advertencia cuando se intenta realizar una operación no soportada. La función `date_sub` no ha cambiado. |

## Véase también

DateTimeImmutable::sub
