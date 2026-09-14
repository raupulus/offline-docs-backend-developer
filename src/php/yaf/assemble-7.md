---
title: Yaf_Route_Supervar::assemble
description: Ensamblar un URL
source_url: https://www.php.net/manual/es/yaf-route-supervar.assemble.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_supervar/assemble.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: c9389e4a0
order: 106890
---

Yaf_Route_Supervar::assemble

Ensamblar un URL

## Descripción

```php
public Yaf_Route_Supervar::assemble(array $info, [array $query]): string
```php

Ensamblar un URL.

## Parámetros

`info`  

`query`  

## Valores devueltos

Devuelve un `string`.

## Errores/Excepciones

Lanza `Yaf_Exception_TypeError` si las claves `':c'` y `':a'` de `info` no están establecidas.

## Ejemplos

Ejemplo de `Yaf_Route_Supervar::assemble`

```
<?php

$router = new Yaf_Router();

$route  = new Yaf_Route_Supervar('r');

$router->addRoute("supervar", $route);

var_dump($router->getRoute('supervar')->assemble(
        array(
              ':a' => 'yafaction',
              'tkey' => 'tval',
              ':c' => 'yafcontroller',
              ':m' => 'yafmodule'
        ),
        array(
              'tkey1' => 'tval1',
              'tkey2' => 'tval2'
        )
));

try {
var_dump($router->getRoute('supervar')->assemble(
        array(
              ':a' => 'yafaction',
              'tkey' => 'tval',
              ':m' => 'yafmodule'
        ),
        array(
              'tkey1' => 'tval1',
              'tkey2' => 'tval2',
              1 => array(),
        )
));
} catch (Exception $e) {
    var_dump($e->getMessage());
}

   
```php

Resultado del ejemplo anterior es similar a:

    string(%d) "?r=/yafmodule/yafcontroller/yafaction&tkey1=tval1&tkey2=tval2"
    string(%d) "You need to specify the controller by ':c'"
