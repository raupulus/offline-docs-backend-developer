---
title: oci_client_version
description: Devuelve la versión de la biblioteca cliente Oracle
source_url: https://www.php.net/manual/es/function.oci-client-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-client-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: ed6de1ae2
order: 57210
---

oci_client_version

Devuelve la versión de la biblioteca cliente Oracle

## Descripción

```php
oci_client_version(): string
```php

Devuelve un `string` que contiene el número de versión de la biblioteca cliente Oracle C, a la cual PHP está ligada.

## Parámetros

Ninguno.

## Valores devueltos

Devuelve el número de versión, en forma de un `string`.

## Ejemplos

Ejemplo con `oci_client_version`

```
<?php
    echo "Client Version: " . oci_client_version(); // Versión del cliente: 19.9.0.0.0
?>

    
```php

## Notas

> [!NOTE]
> Las bibliotecas Oracle anteriores a la 10*g*R2 no poseían funcionalidad interna para recuperar el número de versión de la biblioteca. La cadena "Unknow" será devuelta en este caso.

## Véase también

`oci_server_version`
