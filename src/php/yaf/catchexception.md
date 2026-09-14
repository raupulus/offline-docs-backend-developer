---
title: Yaf_Dispatcher::catchException
description: Activar/desactivar la captura de excepciones
source_url: https://www.php.net/manual/es/yaf-dispatcher.catchexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_dispatcher/catchexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 49d4fb555
order: 105610
---

Yaf_Dispatcher::catchException

Activar/desactivar la captura de excepciones

## Descripción

```php
public Yaf_Dispatcher::catchException([bool $flag]): Yaf_Dispatcher
```php

Mientras que application.dispatcher.throwException esté activado (también se puede llamar al método Yaf_Dispatcher::throwException(TRUE) para habilitarlo), Yaf lanzará una excepción en lugar de emitir un error cuando ocurren errores.

Entonces, si se habilita Yaf_Dispatcher::catchException (también se puede habilitar estableciendo [application.dispatcher.catchException](#configuration.yaf.dispatcher.catchexception)), todas las excepciones no capturadas lo serán por ErrorController::error si se ha definido una.

## Parámetros

`flag`  
bool

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Dispatcher::catchException`

```
/* si se define una clase ErrorController como la siguiente */
<?php
class ErrorController extends Yaf_Controller_Abstract {
     /**
      * también se puede llamar a Yaf_Request_Abstract::getException para obtener
      * la excepción no capturada.
      */
     public function errorAction($excepción) {
        /* error occurs */
        switch ($excepción->getCode()) {
            case YAF_ERR_NOTFOUND_MODULE:
            case YAF_ERR_NOTFOUND_CONTROLLER:
            case YAF_ERR_NOTFOUND_ACTION:
            case YAF_ERR_NOTFOUND_VIEW:
                echo 404, ":", $excepción->getMessage();
                break;
            default :
                $message = $excepción->getMessage();
                echo 0, ":", $excepción->getMessage();
                break;
        }
     }
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /* ahora, si ocurre algún error, se asume el acceso a un controlador no existente (o uno mismo puede lanzar una excepción): */
    404:Could not find controller script **/application/controllers/Controlador-no-existente.php

## Véase también

Yaf_Dispatcher::throwException

Yaf_Dispatcher::setErrorHandler
