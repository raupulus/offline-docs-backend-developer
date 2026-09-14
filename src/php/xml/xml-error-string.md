---
title: xml_error_string
description: Lee el mensaje de error del analizador XML
source_url: https://www.php.net/manual/es/function.xml-error-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-error-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: ad323a863
order: 102670
---

xml_error_string

Lee el mensaje de error del analizador XML

## Descripción

```php
xml_error_string(int $error_code): string
```php

Lee el mensaje de error del analizador XML asociado con el código `error_code` dado.

## Parámetros

`error_code`  
Un código de error proveniente de `xml_get_error_code`.

## Valores devueltos

Devuelve un string que representa la descripción del error `error_code`, o `null` o `"Unknown"` si no se encuentra ninguna descripción.

## Véase también

`xml_get_error_code`
