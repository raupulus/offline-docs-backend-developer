---
title: Yaf_Dispatcher::throwException
description: Activa/desactiva el lanzamiento de excepciones
source_url: https://www.php.net/manual/es/yaf-dispatcher.throwexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_dispatcher/throwexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 49d4fb555
order: 105830
---

Yaf_Dispatcher::throwException

Activa/desactiva el lanzamiento de excepciones

## Descripción

```php
public Yaf_Dispatcher::throwException([bool $flag]): Yaf_Dispatcher
```php

Activa/desactiva el lanzamiento de excepciones mientras ocurran errores inesperados. Cuando está activado, Yaf lanzará excepciones en lugar de provocar errores capturables.

También se puede usar [ application.dispatcher.throwException](#configuration.yaf.dispatcher.throwexception) para el mismo propósito.

## Parámetros

`flag`  
Booleano

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Dispatcher::throwexception`

```
<?php

$config = array(
    'application' => array(
        'directory' => dirname(__FILE__),
    ),
);
$app = new Yaf_Application($config);

$app->getDispatcher()->throwException(true);

try {
    $app->run();
} catch (Yaf_Exception $e) {
    var_dump($e->getMessage());
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(59) "Could not find controller script /tmp/controllers/Index.php"

Ejemplo de `Yaf_Dispatcher::throwexception`

```
<?php

$config = array(
    'application' => array(
        'directory' => dirname(__FILE__),
    ),
);
$app = new Yaf_Application($config);

$app->getDispatcher()->throwException(false);

$app->run();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    PHP Catchable fatal error:  Yaf_Application::run(): Could not find controller script /tmp/controllers/Index.php in /tmp/1.php on line 12

## Véase también

Yaf_Dispatcher::catchException

Yaf_Exception
