---
title: DateTime::setTime
description: Establece la hora
source_url: https://www.php.net/manual/es/datetime.settime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/settime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 02ff7fef5
order: 10520
---

DateTime::setTime

date_time_set

Establece la hora

## Descripción

Estilo orientado a objetos

```php
public DateTime::setTime(int $hour, int $minute, [int $second], [int $microsecond]): DateTime
```php

Estilo procedimental

```php
date_time_set(DateTime $object, int $hour, int $minute, [int $second], [int $microsecond]): DateTime
```

Reinicia la hora actual del objeto DateTime a una hora diferente.

Igual que DateTimeImmutable::setTime pero funciona con `DateTime`.

La versión procedural toma el objeto `DateTime` como su primer argumento.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`hour`  
Hora del instante.

`minute`  
Minuto de la hora.

`second`  
Segundo de la hora.

`microsecond`  
Microsegundo de la hora.

## Valores devueltos

Retorna el objeto modificado `DateTime` para encadenar métodos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El comportamiento con horas dobles existentes (durante la transición de DST de retroceso) cambió. Anteriormente, PHP elegiría la segunda ocurrencia (después de la transición de DST), en lugar de la primera ocurrencia (antes de la transición de DST). |
| 7.1.0 | Se ha añadido el parametro `microsecond`. |

## Véase también

DateTimeImmutable::setTime
