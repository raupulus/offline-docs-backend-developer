---
title: stomp_connect_error
description: Devuelve una cadena descripción de el último error al conectar
source_url: https://www.php.net/manual/es/function.stomp-connect-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/functions/stomp-connect-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87490
---

stomp_connect_error

Devuelve una cadena descripción de el último error al conectar

## Descripción

```php
stomp_connect_error(): string
```php

Devuelve una cadena descripción de el último error al conectar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una cadena que describe el error, o `null` si no hay errores.

## Ejemplos

Ejemplo de `stomp_connect_error`

```
<?php
$link = stomp_connect('http://localhost:61613');

if(!$link) {
    die('Connection failed: ' . stomp_connect_error());
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Connection failed: Invalid Broker URI scheme
