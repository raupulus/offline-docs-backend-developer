---
title: radius_auth_open
description: Crea un identificador de Radius para la autenticación
source_url: https://www.php.net/manual/es/function.radius-auth-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-auth-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_revision: 9ac4d06c0
order: 67560
---

radius_auth_open

Crea un identificador de Radius para la autenticación

## Descripción

```php
radius_auth_open(): resource
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un manejador en caso de éxito, `false` en caso de error. Esta función sólo falla si hay insuficiente memoria disponible.

## Ejemplos

Ejemplo de `radius_auth_open`

```
<?php
$radh = radius_auth_open()
    or die ("No se pudo crear el manejador");
echo "Manejador creado con éxito";
?>

   
```php
