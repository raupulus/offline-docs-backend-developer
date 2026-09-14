---
title: Yaf_Response_Abstract::response
description: Envía una respuesta
source_url: https://www.php.net/manual/es/yaf-response-abstract.response.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_response_abstract/response.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 7418592d8
order: 106660
---

Yaf_Response_Abstract::response

Envía una respuesta

## Descripción

```php
public Yaf_Response_Abstract::response(): void
```php

Envía una respuesta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Response_Abstract::response`

```
<?php
$respuesta = new Yaf_Response_Http();

$respuesta->setBody("Hola")->setBody(" Mundo", "footer");

$respuesta->respuesta();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Hola Mundo

## Véase también

Yaf_Response_Abstract::setBody

Yaf_Response_Abstract::clearBody
