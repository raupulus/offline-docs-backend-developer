---
title: Yaf_Plugin_Abstract::routerShutdown
description: El propósito de routerShutdown
source_url: https://www.php.net/manual/es/yaf-plugin-abstract.routershutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_plugin_abstract/routershutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 106040
---

Yaf_Plugin_Abstract::routerShutdown

El propósito de routerShutdown

## Descripción

```php
public Yaf_Plugin_Abstract::routerShutdown(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response): void
```php

Este enganche será provocado después de que finalice el proceso de enrutamiento. Este enganche se usa normalmente para la verificación de identificación.

## Parámetros

`request`  

`response`  

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Plugin_Abstract::routerShutdown`

```
<?php
class UserInitPlugin extends Yaf_Plugin_Abstract {

    public function routerShutdown(Yaf_Request_Abstract $petición, Yaf_Response_Abstract $respuesta) {
        $controlador = $petición->getControllerName();

        /**
         * El uso de accesos a controladores no es necesario para APIs
         */
        if (in_array(strtolower($controlador), array(
            'api',
        ))) {
            return TRUE;
        }

        if (Yaf_Session::getInstance()->has("login")) {
            return TRUE;
        }

        /* El uso de verificación de acceso falló, se necesita identificarse */
        $respuesta->setRedirect("http://yourdomain.com/login/");
        return FALSE;
    }
}
?>

   
```php

## Véase también

Yaf_Plugin_Abstract::routerStartup

Yaf_Plugin_Abstract::dispatchLoopStartup

Yaf_Plugin_Abstract::preDispatch

Yaf_Plugin_Abstract::postDispatch

Yaf_Plugin_Abstract::dispatchLoopShutdown
