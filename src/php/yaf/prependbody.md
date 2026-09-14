---
title: Yaf_Response_Abstract::prependBody
description: El propósito de prependBody
source_url: https://www.php.net/manual/es/yaf-response-abstract.prependbody.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_response_abstract/prependbody.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 30f488ae2
order: 106650
---

Yaf_Response_Abstract::prependBody

El propósito de prependBody

## Descripción

```php
public Yaf_Response_Abstract::prependBody(string $content, [string $key]): bool
```php

Antepone un contenido a un bloque de contenido existente

## Parámetros

`body`  
La cadena con el contenido.

`key`  
La clave del contenido, se puede establecer una clave, y si no se especifica, se usará Yaf_Response_Abstract::DEFAULT_BODY.

> [!NOTE]
> Este parámetro se introdujo a partir de la versión 2.2.0.

## Valores devueltos

Un valor de tipo booleano.

## Ejemplos

Ejemplo de `Yaf_Response_Abstract::prependBody`

```
<?php
$respuesta = new Yaf_Response_Http();

$respuesta->setBody("Mundo")->prependBody("Hola ");

echo $respuesta;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Hola Mundo

## Véase también

Yaf_Response_Abstract::getBody

Yaf_Response_Abstract::setBody

Yaf_Response_Abstract::appendBody

Yaf_Response_Abstract::clearBody
