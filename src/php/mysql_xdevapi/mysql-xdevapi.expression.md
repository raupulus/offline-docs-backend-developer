---
title: expression
description: Vincula una expresión a una variable de consulta preparada
source_url: https://www.php.net/manual/es/function.mysql-xdevapi-expression.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/functions/mysql-xdevapi.expression.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ab13bf664
order: 52560
---

expression

Vincula una expresión a una variable de consulta preparada

## Descripción

```php
mysql_xdevapi\expression(string $expression): object
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`expression`  

## Valores devueltos

## Ejemplos

Ejemplo de `mysql_xdevapi\Expression`

```
<?php
$expression = mysql_xdevapi\Expression("[age,job]");

$res  = $coll->find("age > 30")->fields($expression)->limit(3)->execute();
$data = $res->fetchAll();

print_r($data);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    <?php
