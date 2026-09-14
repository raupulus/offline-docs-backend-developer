---
title: OCILob::setBuffering
description: Activa/desactiva la bufferización de los LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.setbuffering.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/setBuffering.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57950
---

OCILob::setBuffering

Activa/desactiva la bufferización de los LOB Oracle

## Descripción

```php
public OCILob::setBuffering(bool $mode): bool
```php

Activa o desactiva la bufferización de los LOB Oracle, en función del parámetro `mode`.

Utilizar esta función aporta mejoras de rendimiento mediante la bufferización de pequeñas lecturas y escrituras de LOB: el buffer limita los intercambios con el servidor. `OCILob::flush` debe ser utilizado para vaciar los buffers una vez finalizado el trabajo con el LOB.

## Parámetros

`mode`  
`true` para activarlo, y `false` para desactivarlo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Llamadas repetidas a `lob->setbuffering` con el mismo valor de parámetro siempre devolverá `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.getbuffering)
