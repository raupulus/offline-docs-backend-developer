---
title: openssl_error_string
description: Retorna el mensaje de error OpenSSL
source_url: https://www.php.net/manual/es/function.openssl-error-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-error-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: cbac1ecf7
order: 59160
---

openssl_error_string

Retorna el mensaje de error OpenSSL

## Descripción

```php
openssl_error_string(): string
```php

`openssl_error_string` retorna el último error de la biblioteca OpenSSL. Los mensajes de error son puestos en cola, y la función `openssl_error_string` debe ser llamada varias veces para mostrar todos los errores. El último error será el más reciente en esta cola.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna un mensaje de error, en forma de `string`, o `false` si no hay más mensajes que mostrar.

## Ejemplos

Ejemplo con `openssl_error_string`

```
<?php
// Supongamos que se ha llamado a una función que ha generado un error
while ($msg = openssl_error_string())
    echo $msg . "<br />\n";
?>

    
```php
