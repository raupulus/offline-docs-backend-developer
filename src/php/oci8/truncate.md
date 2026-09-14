---
title: OCILob::truncate
description: Trunca un LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.truncate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/truncate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57980
---

OCILob::truncate

Trunca un LOB Oracle

## Descripción

```php
public OCILob::truncate([int $length]): bool
```php

Trunca un LOB Oracle.

## Parámetros

`length`  
Si `length` es proporcionado, este método truncará el LOB a `length` bytes. De lo contrario, vaciará completamente el LOB.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.erase)
