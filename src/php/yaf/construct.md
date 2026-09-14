---
title: Yaf_Application::__construct
description: El constructor de la clase Yaf_Application
source_url: https://www.php.net/manual/es/yaf-application.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 330a38c4d
order: 104960
---

Yaf_Application::\_\_construct

El constructor de la clase Yaf_Application

## Descripción

```php
public Yaf_Application::__construct(mixed $config, [string $environ])
```php

Instancia un objeto de la clase `Yaf_Application`.

## Parámetros

`config`  
La ruta de un fichero de configuración ini, o un array de configuración

Si es un fichero ini de configuración, debería existir una sección con el mismo nombre que una definida por [yaf.environ](#ini.yaf.environ), la cual es "product" por omisión.

> [!NOTE]
> Si se está usando un fichero de configuración ini como contenedor de configuración de la aplicación, se debería abrir [yaf.cache_config](#ini.yaf.cache-config) para mejorar el rendimiento.

Y la entrada de configuración (y el valor predeterminado) listada abajo:

A ini config file example

```
[product]
;esta siempre debería ser definida y no tener un valor predeterminado
application.directory=APPLICATION_PATH

;las siguientes configuraciones tienen un valor predeterminados, no se necesitan definirlas
application.library = APPLICATION_PATH . "/library"
application.dispatcher.throwException=1
application.dispatcher.catchException=1

application.baseUri=""

;el nombre de la extensión de script de php
ap.ext=php

;el nombre de la extensión de la plantilla de vista
ap.view.ext=phtml

ap.dispatcher.defaultModule=Index
ap.dispatcher.defaultController=Index
ap.dispatcher.defaultAction=index

;módulos definidos
ap.modules=Index

       
```php

`environ`  
Qué sección se cargará como configuración final

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Application::__construct`

```
<?php
defined('APPLICATION_PATH')                  // APPLICATION_PATH será usada en el archivo de configuración ini
    || define('APPLICATION_PATH', __DIR__);

$application = new Yaf_Application(APPLICATION_PATH.'/conf/application.ini');
$application->bootstrap()->run();
?>

   
```php

Resultado del ejemplo anterior es similar a:

Ejemplo de `Yaf_Application::__construct`

```
<?php
$config = array(
    "application" => array(
        "directory" => realpath(dirname(__FILE__)) . "/application",
    ),
);

/** Yaf_Application */
$application = new Yaf_Application($config);
$application->bootstrap()->run();
?>

   
```php

Resultado del ejemplo anterior es similar a:

## Véase también

Yaf_Config_Ini
