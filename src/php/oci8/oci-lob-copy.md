---
title: oci_lob_copy
description: Copia un LOB Oracle
source_url: https://www.php.net/manual/es/function.oci-lob-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-lob-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57440
---

oci_lob_copy

Copia un LOB Oracle

## Descripción

```php
oci_lob_copy(OCILob $to, OCILob $from, [int $length]): bool
```php

Copia un LOB o una parte de un LOB a otro LOB. Los datos antiguos del LOB de destino serán sobrescritos por los nuevos.

Si se debe copiar una parte específica de un LOB a una posición particular de otro LOB, utilice la función `OCILob::seek` para mover el puntero interno de LOB.

## Parámetros

`to`  
El LOB de destino.

`from`  
El LOB copiado.

`length`  
Indica el tamaño de los datos a copiar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión                | Descripción                 |
|------------------------|-----------------------------|
| 8.0.0, PECL OCI8 3.0.0 | `length` es ahora nullable. |

## Notas

> [!NOTE]
> La clase OCILob se llamaba OCI-Lob antes de PHP 8 y OCI8 3.0.0.
