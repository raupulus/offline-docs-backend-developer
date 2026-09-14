---
title: cubrid_error_code
description: Obtener el código de error de la llamada a una función más reciente
source_url: https://www.php.net/manual/es/function.cubrid-error-code.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9000
---

cubrid_error_code

Obtener el código de error de la llamada a una función más reciente

## Descripción

```php
cubrid_error_code(): int
```php

La función `cubrid_error_code` se usa para obtener el código de error del error que ocurrión durante la ejecución de la API. Normalmente obtiene el código de error cuando la API devuelve false como valor de retorno.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Código de error del error que ocurrió, o `0` (cero) si no ocurre ningún error.

## Ejemplos

Ejemplo de `cubrid_error_code`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$req = cubrid_prepare($conn , "SELECT * FROM code WHERE s_name=?");

$req = @cubrid_execute($req);
if (!$req) {
    printf("Dispositivo del error: %d\nCódigo de error: %d\nMensaje de error: %s\n",
        cubrid_error_code_facility(), cubrid_error_code(), cubrid_error_msg());

    cubrid_disconnect($conn);
    exit;
}
?>

   
```php

El ejemplo anterior mostrará:

    Dispositivo del error: 4
    Código de error: -30015
    Mensaje de error: Some parameter not binded

## Véase también

cubrid_error_code_facility

cubrid_error_msg
