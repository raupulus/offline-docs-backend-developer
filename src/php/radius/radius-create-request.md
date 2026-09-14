---
title: radius_create_request
description: Crea una solicitud de cuenta o de identificación
source_url: https://www.php.net/manual/es/function.radius-create-request.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-create-request.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67590
---

radius_create_request

Crea una solicitud de cuenta o de identificación

## Descripción

```php
radius_create_request(resource $radius_handle, int $type): bool
```php

Una solicitud Radius consiste en código que especifica una solicitud concreta, así como cero o varios atributos que proporcionan información adicional. Para comenzar a construir una nueva solicitud, llámese a la función `radius_create_request`.

> [!NOTE]
> Advertencia: Debe llamarse a esta función antes de pasar cualquier argumento.

## Parámetros

`radius_handle`  

`type`  
El tipo es `RADIUS_ACCESS_REQUEST` o `RADIUS_ACCOUNTING_REQUEST`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `radius_create_request`

```
<?php
if (!radius_create_request($res, RADIUS_ACCESS_REQUEST)) {
    echo 'Error Radius :' . radius_strerror($res). "\n<br />";
    exit;
}
?>

   
```php

## Véase también

radius_send_request
