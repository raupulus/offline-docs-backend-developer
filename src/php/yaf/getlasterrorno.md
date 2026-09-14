---
title: Yaf_Application::getLastErrorNo
description: Pbetner el código del último error ocurrido
source_url: https://www.php.net/manual/es/yaf-application.getlasterrorno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/getlasterrorno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: a023d0b24
order: 105040
---

Yaf_Application::getLastErrorNo

Pbetner el código del último error ocurrido

## Descripción

```php
public Yaf_Application::getLastErrorNo(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Application::getLastErrorNo`

```
<?php
function error_handler($errno, $errstr, $errfile, $errline) {
   var_dump(Yaf_Application::app()->getLastErrorNo());
   var_dump(Yaf_Application::app()->getLastErrorNo() == YAF_ERR_NOTFOUND_CONTROLLER);
}

$config = array(
  "application" => array(
   "directory" => "/tmp/notexists",
     "dispatcher" => array(
       "throwException" => 0, //provocar un error en lugar de lanzar una excepción cuando ocurra un error
      ),
  ),
);

$app = new Yaf_Application($config);
$app->getDispatcher()->setErrorHandler("error_handler", E_RECOVERABLE_ERROR);
$app->run();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(516)
    bool(true)
