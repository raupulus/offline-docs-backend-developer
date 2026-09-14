---
title: OCILob::eof
description: Prueba el final del LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.eof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/eof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57820
---

OCILob::eof

Prueba el final del LOB Oracle

## Descripción

```php
public OCILob::eof(): bool
```php

Verifica si el puntero interno de un LOB está al final.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el puntero interno de LOB ha alcanzado el final del LOB, y `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Notas

> [!NOTE]
> Esta función devolverá un error de Oracle si [???](#ocilob.setbuffering) está activo en el LOB.

## Véase también

[???](#ocilob.size)
