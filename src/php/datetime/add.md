---
title: DateTime::add
description: Modifica un objeto DateTime, añadiendo una cantidad de días, meses, años,
  horas, minutos y segundos
source_url: https://www.php.net/manual/es/datetime.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 02ff7fef5
order: 10400
---

DateTime::add

date_add

Modifica un objeto DateTime, añadiendo una cantidad de días, meses, años, horas, minutos y segundos

## Descripción

Estilo orientado a objetos

```php
public DateTime::add(DateInterval $interval): DateTime
```php

Estilo procedimental

```php
date_add(DateTime $object, DateInterval $interval): DateTime
```

Añade el objeto `DateInterval` especificado al objeto `DateTime` especificado.

Igual que DateTimeImmutable::add, pero funciona con `DateTime`.

La versión procedimental toma el objeto `DateTime` como su primer argumento.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`interval`  
Un objeto `DateInterval`

## Valores devueltos

Retorna el objeto modificado `DateTime` para encadenar métodos.

## Véase también

DateTimeImmutable::add
