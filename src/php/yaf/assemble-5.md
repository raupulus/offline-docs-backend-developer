---
title: Yaf_Route_Simple::assemble
description: Ensamblar un URL
source_url: https://www.php.net/manual/es/yaf-route-simple.assemble.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_simple/assemble.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: c9389e4a0
order: 106830
---

Yaf_Route_Simple::assemble

Ensamblar un URL

## Descripción

```php
public Yaf_Route_Simple::assemble(array $info, [array $query]): string
```php

Ensamblar un URL.

## Parámetros

`info`  

`query`  

## Valores devueltos

Devuelve un `string`.

## Errores/Excepciones

Lanza `Yaf_Exception_TypeError` si las claves `':c'` o `':a'` de `info` no están establecidas.

## Ejemplos

Ejemplo de `Yaf_Route_Simple::assemble`

```
<?php

$router = new Yaf_Router();

$route  = new Yaf_Route_Simple('m', 'c', 'a');

$router->addRoute("simple", $route);

var_dump($router->getRoute('simple')->assemble(
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

   
```php

Resultado del ejemplo anterior es similar a:

    string(64) "?m=yafmodule&c=yafcontroller&a=yafaction&tkey1=tval1&tkey2=tval2"
