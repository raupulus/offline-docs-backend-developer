---
title: apache_response_headers
description: Recupera todos los encabezados de respuesta HTTP
source_url: https://www.php.net/manual/es/function.apache-response-headers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-response-headers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: 8a0888aeb
order: 4800
---

apache_response_headers

Recupera todos los encabezados de respuesta HTTP

## Descripción

```php
apache_response_headers(): array
```php

Recupera todos los encabezados de respuesta HTTP. Funciona con los servidores web Apache, LiteSpeed, FastCGI, CLI y FPM.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de todos los encabezados de respuesta de Apache en caso de éxito.

## Ejemplos

Ejemplo con `apache_response_headers`

```
<?php
print_r(apache_response_headers());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [Accept-Ranges] => bytes
        [X-Powered-By] => PHP/4.3.8
    )

## Véase también

`apache_request_headers`, `headers_sent`, `headers_list`
