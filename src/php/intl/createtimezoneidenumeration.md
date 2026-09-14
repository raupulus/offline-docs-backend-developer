---
title: IntlTimeZone::createTimeZoneIDEnumeration
description: Devuelve una enumeración de los identificadores de zona horaria del sistema
  con las condiciones de filtro dadas
source_url: https://www.php.net/manual/es/intltimezone.createtimezoneidenumeration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intltimezone/createtimezoneidenumeration.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41600
---

IntlTimeZone::createTimeZoneIDEnumeration

intltz_create_time_zone_id_enumeration

Devuelve una enumeración de los identificadores de zona horaria del sistema con las condiciones de filtro dadas

## Descripción

Estilo orientado a objetos (método):

```php
public static IntlTimeZone::createTimeZoneIDEnumeration(int $type, [string $region], [int $rawOffset]): IntlIterator
```php

Estilo procedimental:

```php
intltz_create_time_zone_id_enumeration(int $type, [string $region], [int $rawOffset]): IntlIterator
```

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`type`  

`region`  

`rawOffset`  

## Valores devueltos

Devuelve `IntlIterator` o `false` si ocurre un error.
