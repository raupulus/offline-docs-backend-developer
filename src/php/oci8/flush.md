---
title: OCILob::flush
description: Escribe los LOB Oracle en el disco
source_url: https://www.php.net/manual/es/ocilob.flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57850
---

OCILob::flush

Escribe los LOB Oracle en el disco

## Descripción

```php
public OCILob::flush([int $flag]): bool
```php

`OCILob::flush` escribe los datos en el servidor.

## Parámetros

`flag`  
Por omisión, los recursos no son liberados, pero utilizando la opción `flag` con el valor `OCI_LOB_BUFFER_FREE`, puede hacerse explícitamente. Asegúrese de saber bien lo que hace: la próxima lectura o escritura en el mismo LOB requerirá entonces una petición al servidor, y la reasignación de recursos. Se recomienda utilizar la opción `OCI_LOB_BUFFER_FREE` únicamente si ya no se necesita el LOB.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Retorna `false` si la bufferización no ha sido activada, o si ha ocurrido un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.getbuffering), [???](#ocilob.setbuffering)
