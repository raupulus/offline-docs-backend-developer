---
title: radius_get_attr
description: Extrae un atributo
source_url: https://www.php.net/manual/es/function.radius-get-attr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-get-attr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67650
---

radius_get_attr

Extrae un atributo

## Descripción

```php
radius_get_attr(resource $radius_handle): mixed
```php

Al igual que las solicitudes Radius, cada respuesta debe contener cero o varios atributos. Tras recibir una respuesta con éxito mediante la función `radius_send_request`, estos atributos pueden ser extraídos uno a uno utilizando la función `radius_get_attr`. En cada llamada a `radius_get_attr`, se recupera el siguiente atributo desde la respuesta actual.

## Parámetros

`radius_handle`  
El recurso RADIUS.

## Valores devueltos

Devuelve un array asociativo que contiene el tipo de atributo junto con los datos o un número de error \<= 0.

## Ejemplos

Ejemplo con `radius_get_attr`

```
<?php
while ($resa = radius_get_attr($res)) {

    if (!is_array($resa)) {
        printf("Error al recuperar el atributo: %s\n",  radius_strerror($res));
        exit;
    }

    $attr = $resa['attr'];
    $data = $resa['data'];
    printf("Atributo recuperado :%d %d bytes %s\n", $attr, strlen($data), bin2hex($data));
}
?>

   
```php

## Véase también

radius_put_attr

radius_get_vendor_attr

radius_put_vendor_attr

radius_send_request
