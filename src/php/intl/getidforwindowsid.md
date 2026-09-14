---
title: IntlTimeZone::getIDForWindowsID
description: Traduce una zona horaria de Windows a una zona horaria del sistema
source_url: https://www.php.net/manual/es/intltimezone.getidforwindowsid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intltimezone/getidforwindowsid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41710
---

IntlTimeZone::getIDForWindowsID

intltz_get_id_for_windows_id

Traduce una zona horaria de Windows a una zona horaria del sistema

## Descripción

Estilo orientado a objetos (método):

```php
public static IntlTimeZone::getIDForWindowsID(string $timezoneId, [string $region]): string
```php

Estilo procedimental:

```php
intltz_get_id_for_windows_id(string $timezoneId, [string $region]): string
```

Traduce una zona horaria de Windows (por ejemplo "Pacific Standard Time") a una zona horaria del sistema (por ejemplo "America/Los_Angeles").

> [!NOTE]
> Esta función requiere ICU versión ≥ 52.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`timezoneId`  

`region`  

## Valores devueltos

Devuelve la zona horaria del sistema o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 8.0.0   | `region` ahora puede ser nullable. |

## Véase también

IntlTimeZone::getWindowsID
