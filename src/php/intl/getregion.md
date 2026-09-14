---
title: IntlTimeZone::getRegion
description: Devuelve el código de región asociado al identificador de zona horaria
  del sistema dado
source_url: https://www.php.net/manual/es/intltimezone.getregion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intltimezone/getregion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41740
---

IntlTimeZone::getRegion

intltz_get_region

Devuelve el código de región asociado al identificador de zona horaria del sistema dado

## Descripción

Estilo orientado a objetos (método):

```php
public static IntlTimeZone::getRegion(string $timezoneId): string
```php

Estilo procedimental:

```php
intltz_get_region(string $timezoneId): string
```

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`timezoneId`  
El identificador de zona horaria del sistema.

## Valores devueltos

Devuelve la región o o `false` si ocurre un error.
