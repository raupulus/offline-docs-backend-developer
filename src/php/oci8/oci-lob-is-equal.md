---
title: oci_lob_is_equal
description: Comparar dos LOB/FILE de Oracle
source_url: https://www.php.net/manual/es/function.oci-lob-is-equal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-lob-is-equal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57450
---

oci_lob_is_equal

Comparar dos LOB/FILE de Oracle

## Descripción

```php
oci_lob_is_equal(OCILob $lob1, OCILob $lob2): bool
```php

Compara dos LOB/FILE de Oracle.

## Parámetros

`lob1`  
Un identificador LOB.

`lob2`  
Un identificador LOB.

## Valores devueltos

Devuelve `true` si estos objetos son iguales, `false` en caso contrario.

## Notas

> [!NOTE]
> La clase OCICollection se denominaba OCI-Collection antes de PHP 8 y OCI8 3.0.0.
