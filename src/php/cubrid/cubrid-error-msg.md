---
title: cubrid_error_msg
description: Obtener el último mensaje de error de la llamada a la función más reciente
source_url: https://www.php.net/manual/es/function.cubrid-error-msg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-error-msg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9010
---

cubrid_error_msg

Obtener el último mensaje de error de la llamada a la función más reciente

## Descripción

```php
cubrid_error_msg(): string
```php

La función `cubrid_error_msg` se usa para obtener el mensaje de error que ocurrió durante la utilización de la API CUBRID. Normalmente obtiene el mensaje de error cuando la API devuelve false como valor de retorno.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El mensaje de error que ocurrió.

## Ejemplos

Ejemplo de `cubrid_error_msg`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

if (!@cubrid_schema($conn, 100000)) {
    printf("Dispositivo del error: %d\nCódigo de error: %d\nMensaje de error: %s\n",
        cubrid_error_code_facility(), cubrid_error_code(), cubrid_error_msg());

    cubrid_disconnect($conn);
    exit;
}
?>

   
```php

El ejemplo anterior mostrará:

    Dispositivo del error: 2
    Código de error: -10015
    Mensaje de error: Invalid T_CCI_SCH_TYPE value

## Véase también

cubrid_error_code

cubrid_error_code_facility
