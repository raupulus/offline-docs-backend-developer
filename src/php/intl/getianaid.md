---
title: IntlTimeZone::getIanaID
description: Traduce un identificador de zona horaria a su equivalente IANA
source_url: https://www.php.net/manual/es/intltimezone.getianaid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intltimezone/getianaid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 3f1722ae5
order: 41690
---

IntlTimeZone::getIanaID

intltz_get_iana_id

Traduce un identificador de zona horaria a su equivalente IANA

## Descripción

Estilo orientado a objetos (método):

```php
public static IntlTimeZone::getIanaID(string $timezoneId): string
```php

Estilo procedimental:

```php
intltz_get_iana_id(string $timezoneId): string
```

Traduce un identificador de zona horaria a su equivalente IANA. Por ejemplo, `"GMT"` devuelve `"Etc/GMT"`, y `"US/Eastern"` devuelve `"America/New_York"`.

> [!NOTE]
> Esta función requiere ICU versión \>= 74.

## Parámetros

`timezoneId`  
El identificador de la zona horaria a traducir.

## Valores devueltos

Devuelve el identificador de zona horaria IANA como `string`, o `false` en caso de fallo.

## Véase también

intltz_get_id_for_windows_id

intltz_get_windows_id

intltz_create_time_zone
