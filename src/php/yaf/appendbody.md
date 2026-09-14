---
title: Yaf_Response_Abstract::appendBody
description: Añadir contenido al cuerpo de respuesta
source_url: https://www.php.net/manual/es/yaf-response-abstract.appendbody.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_response_abstract/appendbody.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 0d4f735ed
order: 106580
---

Yaf_Response_Abstract::appendBody

Añadir contenido al cuerpo de respuesta

## Descripción

```php
public Yaf_Response_Abstract::appendBody(string $content, [string $key]): bool
```php

Añade contenido a un bloque de contenido existente.

## Parámetros

`body`  
La cadena con el contenido.

`key`  
La clave del contenido, se puede establecer un contenido con una clave, y si no se especifica, se usará Yaf_Response_Abstract::DEFAULT_BODY.

> [!NOTE]
> Este parámetro se introdujo a partir de la versión 2.2.0

## Valores devueltos

Un valor de tipo booleano.

## Ejemplos

Ejemplo de `Yaf_Response_Abstract::appendBody`

```
<?php
$respuesta = new Yaf_Response_Http();

$respuesta->setBody("Hola")->appendBody(" Mundo");

echo $respuesta;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Hola Mundo

## Véase también

Yaf_Config_Ini

Yaf_Response_Abstract::getBody

Yaf_Response_Abstract::setBody

Yaf_Response_Abstract::prependBody

Yaf_Response_Abstract::clearBody
