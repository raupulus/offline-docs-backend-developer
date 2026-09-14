---
title: DateTimeZone::getName
description: Devuelve el nombre de la zona horaria
source_url: https://www.php.net/manual/es/datetimezone.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimezone/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 02ff7fef5
order: 10860
---

DateTimeZone::getName

timezone_name_get

Devuelve el nombre de la zona horaria

## Descripción

Estilo orientado a objetos

```php
public DateTimeZone::getName(): string
```php

Estilo procedimental

```php
timezone_name_get(DateTimeZone $object): string
```

Devuelve el nombre de la zona horaria.

## Parámetros

`object`  
El objeto `DateTimeZone` utilizado para recuperar el nombre de la zona horaria.

## Valores devueltos

Según el tipo de zona, el desplazamiento UTC (tipo 1), la abreviatura de zona horaria (tipo 2) y los identificadores de zona horaria tales como se publican en la base de datos de zonas horarias IANA (tipo 3), la cadena de descripción para crear un nuevo objeto `DateTimeZone` con el mismo desplazamiento y/o las mismas reglas. Por ejemplo `02:00`, `CEST` o uno de los nombres de zonas horarias en la [lista de zonas horarias](#timezones).
