---
title: cubrid_error_code_facility
description: Obtener el código de error del dispositivo
source_url: https://www.php.net/manual/es/function.cubrid-error-code-facility.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-error-code-facility.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8990
---

cubrid_error_code_facility

Obtener el código de error del dispositivo

## Descripción

```php
cubrid_error_code_facility(): int
```php

La función `cubrid_error_code_facility` se usa para obtener el código de dispositivo (nivel en el que ocurrió el error) desde el código de error del error que ocurrió durante la ejecución de la API. Normalmente, se puede obtener el código de error cuando la API devuelve false como valor de retorno.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Código de dispositivo del código de error que ocuriió: `CUBRID_FACILITY_DBMS`, `CUBRID_FACILITY_CAS`, `CUBRID_FACILITY_CCI`, `CUBRID_FACILITY_CLIENT`.

## Ejemplos

Ejemplo de `cubrid_error_code_facility`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$req = @cubrid_execute($conn, "SELECT * FROM unknown");
if (!$req) {
    printf("Dispositivo del error: %d\nCódigo de error: %d\nMensaje de error: %s\n",
        cubrid_error_code_facility(), cubrid_error_code(), cubrid_error_msg());

    cubrid_disconnect($conn);
    exit;
}
?>

   
```php

El ejemplo anterior mostrará:

    Dispositivo del error: 1
    Código de error: -493
    Mensaje de error: Syntax: In line 1, column 15 before END OF STATEMENT
    Syntax error: unexpected 'unknown'

## Véase también

cubrid_error_code

cubrid_error_msg
