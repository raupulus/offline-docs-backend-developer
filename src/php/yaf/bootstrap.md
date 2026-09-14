---
title: Yaf_Application::bootstrap
description: Llamar al arranque
source_url: https://www.php.net/manual/es/yaf-application.bootstrap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/bootstrap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4a211b7c8
order: 104940
---

Yaf_Application::bootstrap

Llamar al arranque

## Descripción

```php
public Yaf_Application::bootstrap([Yaf_Bootstrap_Abstract $bootstrap]): void
```php

Ejecuta un Arranque, todos los métodos definidos en el Arranque y prefijados con "\_init" serán llamados según su orden de declaración. Si no se proporciona el parámetro bootstrap, Yaf buscará un Arranque en application.directory.

## Parámetros

`bootstrap`  
Una instancia de la clase `Yaf_Bootstrap_Abstract`

## Valores devueltos

Una instancia de la clase `Yaf_Application`

## Ejemplos

Un ejemplo de Bootstrap

```
<?php
/**
 * Este fichero debería estar en la ruta APPLICATION_PATH . "/application/" (la cual estaría definida en la configuración pasada a Yaf_Application),
 * y llamarse Bootstrap.php, para que la instancia de Yaf_Application lo pueda encontrar
 */
class Bootstrap extends Yaf_Bootstrap_Abstract {
    function _initConfig(Yaf_Dispatcher $dispatcher) {
        echo "Primera llamada\n";
    }

    function _initPlugin($dispatcher) {
        echo "Segunda llamada\n";
    }
}
?>

   
```php

Ejemplo de `Yaf_Application::bootstrap`

```
<?php

defined('APPLICATION_PATH') // APPLICATION_PATH será usada en el fichero ini de configuración
    || define('APPLICATION_PATH', __DIR__);

$application = new Yaf_Application(APPLICATION_PATH.'/conf/application.ini');
$application->bootstrap();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Primera llamada
    Segunda llamada

## Véase también

Yaf_Bootstrap_Abstract
