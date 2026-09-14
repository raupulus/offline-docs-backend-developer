---
title: IntlTimeZone::getWindowsID
description: Traduce una zona horaria del sistema a una zona horaria de Windows
source_url: https://www.php.net/manual/es/intltimezone.getwindowsid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intltimezone/getwindowsid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41770
---

IntlTimeZone::getWindowsID

intltz_get_windows_id

Traduce una zona horaria del sistema a una zona horaria de Windows

## Descripción

Estilo orientado a objetos (método):

```php
public static IntlTimeZone::getWindowsID(string $timezoneId): string
```php

Estilo procedimental:

```php
intltz_get_windows_id(string $timezoneId): string
```

Traduce una zona horaria del sistema (por ejemplo "America/Los_Angeles") a una zona horaria de Windows (por ejemplo "Pacific Standard Time").

> [!NOTE]
> Esta función requiere ICU versión ≥ 52.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`timezoneId`  
El identificador de la zona horaria.

## Valores devueltos

Devuelve la zona horaria de Windows o `false` si ocurre un error.

## Véase también

IntlTimeZone::getIDForWindowsID
