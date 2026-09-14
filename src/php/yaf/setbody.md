---
title: Yaf_Response_Abstract::setBody
description: Establece el contenido de una respuesta
source_url: https://www.php.net/manual/es/yaf-response-abstract.setbody.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_response_abstract/setbody.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 30f488ae2
order: 106680
---

Yaf_Response_Abstract::setBody

Establece el contenido de una respuesta

## Descripción

```php
public Yaf_Response_Abstract::setBody(string $content, [string $key]): bool
```php

Establece el contenido de una respuesta.

## Parámetros

`body`  
La cadena con el contenido.

`key`  
La clave del contenido, se puede establecer una clave, y so no se especifica, se usará Yaf_Response_Abstract::DEFAULT_BODY.

> [!NOTE]
> Este parámetro se introdujo a partir de la versión 2.2.0.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Response_Abstract::setBody`

```
<?php
$respuesta = new Yaf_Response_Http();

$respuesta->setBody("Hola")->setBody(" Mundo", "footer");

print_r($respuesta);
echo $respuesta;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Yaf_Response_Http Object
    (
        [_header:protected] => Array
            (
            )

        [_body:protected] => Array
            (
                [content] => Hola
                [footer] =>  Mundo
            )

        [_sendheader:protected] => 1
        [_response_code:protected] => 200
    )
    Hola Mundo

## Véase también

Yaf_Response_Abstract::getBody

Yaf_Response_Abstract::appendBody

Yaf_Response_Abstract::prependBody

Yaf_Response_Abstract::clearBody
