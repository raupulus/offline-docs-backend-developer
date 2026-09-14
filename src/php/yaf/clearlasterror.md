---
title: Yaf_Application::clearLastError
description: Limpiar la información del último error
source_url: https://www.php.net/manual/es/yaf-application.clearlasterror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/clearlasterror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: a023d0b24
order: 104950
---

Yaf_Application::clearLastError

Limpiar la información del último error

## Descripción

```php
public Yaf_Application::clearLastError(): Yaf_Application
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Application::clearLastError`

```
<?php
function error_handler($errno, $errstr, $errfile, $errline) {
   Yaf_Application::app()->clearLastError();
   var_dump(Yaf_Application::app()->getLastErrorNo());
}

$config = array(
 "application" => array(
   "directory" => "/tmp/noexiste",
     "dispatcher" => array(
       "throwException" => 0, //provocar un error en vez de lanzar una excepción cuando ocurra un error
      ),
  ),
);

$app = new Yaf_Application($config);
$app->getDispatcher()->setErrorHandler("error_handler", E_RECOVERABLE_ERROR);
$app->run();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(0)
