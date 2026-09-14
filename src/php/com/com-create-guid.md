---
title: com_create_guid
description: Genera un identificador único global (GUID)
source_url: https://www.php.net/manual/es/function.com-create-guid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/com-create-guid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: cbac1ecf7
order: 7680
---

com_create_guid

Genera un identificador único global (GUID)

## Descripción

```php
com_create_guid(): string
```php

Genera un identificador único global (GUID).

Un GUID se genera de la misma manera que DCE UUID, excepto por el hecho de que la convención de Microsoft incluye el GUID en un paréntesis.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el GUID, en forma de `string`, o `false` si ocurre un error.

## Véase también

`uuid_create` en la extensión PECL uuid
