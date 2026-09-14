---
title: oci_server_version
description: Devuelve la versión del servidor Oracle
source_url: https://www.php.net/manual/es/function.oci-server-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-server-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57580
---

oci_server_version

Devuelve la versión del servidor Oracle

## Descripción

```php
oci_server_version(resource $connection): string
```php

Devuelve una cadena que contiene la versión del servidor Oracle junto con las opciones disponibles.

## Parámetros

`connection`  

## Valores devueltos

Devuelve la información sobre la versión, en forma de `string`, o `false` en caso de error.

## Ejemplos

Ejemplo con `oci_server_version`

```
<?php
$conn = oci_connect("hr", "hrpwd", "localhost/XE");
echo "Versión del servidor : " . oci_server_version($conn);

// Muestra :
// Versión del servidor : Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
// With the Partitioning, OLAP, Data Mining and Real Application Testing option

oci_close($conn);
?>

    
```php

## Véase también

`oci_client_version`
