---
title: oci_free_descriptor
description: Libera un descriptor
source_url: https://www.php.net/manual/es/function.oci-free-descriptor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-free-descriptor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: c6fb604f3
order: 57410
---

oci_free_descriptor

Libera un descriptor

## Descripción

```php
oci_free_descriptor(OCILob $lob): bool
```php

Libera un descriptor asignado por la función `oci_new_descriptor`.

## Parámetros

`lob`  
Descriptor asignado por `oci_new_descriptor`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> Esta función es habitualmente utilizada como método [OCILOB::free](#ocilob.free).

## Véase también

[OCILOB::free](#ocilob.free)
