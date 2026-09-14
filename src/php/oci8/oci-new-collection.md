---
title: oci_new_collection
description: Inicializa una nueva colección Oracle
source_url: https://www.php.net/manual/es/function.oci-new-collection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-new-collection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57460
---

oci_new_collection

Inicializa una nueva colección Oracle

## Descripción

```php
oci_new_collection(resource $connection, string $type_name, [string $schema]): OCICollection
```php

Inicializa una nueva colección Oracle.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect` o la función `oci_pconnect`.

`type_name`  
Debe ser un tipo nombrado válido (en mayúsculas).

`schema`  
Debe apuntar al esquema de la base de datos, donde el tipo fue creado. El nombre del usuario actual es utilizado cuando `null` es proporcionado.

## Valores devueltos

Devuelve un nuevo objeto `OCICollection`, o `false` si ocurre un error.

## Historial de cambios

| Versión                | Descripción                 |
|------------------------|-----------------------------|
| 8.0.0, PECL OCI8 3.0.0 | `schema` ahora es nullable. |

## Notas

> [!NOTE]
> La clase `OCICollection` se llamaba `OCI-Collection` antes de PHP 8 y OCI8 3.0.0.
