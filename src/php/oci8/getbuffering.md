---
title: OCILob::getBuffering
description: Devuelve el estado de bufferización LOB de Oracle
source_url: https://www.php.net/manual/es/ocilob.getbuffering.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/getBuffering.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57870
---

OCILob::getBuffering

Devuelve el estado de bufferización LOB de Oracle

## Descripción

```php
public OCILob::getBuffering(): bool
```php

Devuelve el estado de bufferización LOB de Oracle.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `false` si la bufferización de los LOB está desactivada, y `true` si está activada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.setbuffering)
