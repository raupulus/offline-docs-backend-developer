---
title: Yaf_Response_Abstract::getBody
description: Recupera un contenido existente
source_url: https://www.php.net/manual/es/yaf-response-abstract.getbody.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_response_abstract/getbody.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 106630
---

Yaf_Response_Abstract::getBody

Recupera un contenido existente

## Descripción

```php
public Yaf_Response_Abstract::getBody([string $key]): mixed
```php

Recupera un contenido existente.

## Parámetros

`key`  
La clave del contenido, si no se especifica, se usará Yaf_Response_Abstract::DEFAULT_BODY. Si se pasa `null`, todos el contenido será devuelto como un array.

> [!NOTE]
> Este parámetro se introdujo en la versión 2.2.0

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Response_Abstract::getBody`

```
<?php
$respuesta = new Yaf_Response_Http();

$respuesta->setBody("Hola")->setBody(" Mundo", "footer");

var_dump($respuesta->getBody()); // predeterminado
var_dump($respuesta->getBody(Yaf_Response_Abstract::DEFAULT_BODY)); // lo mismo que arriba
var_dump($respuesta->getBody("footer"));
var_dump($respuesta->getBody(NULL)); // obtener todo
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(4) "Hola"
    string(4) "Hola"
    string(6) " Mundo"
    array(2) {
      ["content"]=>
      string(4) "Hola"
      ["footer"]=>
      string(6) " Mundo"
    }

## Véase también

Yaf_Response_Abstract::setBody

Yaf_Response_Abstract::appendBody

Yaf_Response_Abstract::prependBody

Yaf_Response_Abstract::clearBody
