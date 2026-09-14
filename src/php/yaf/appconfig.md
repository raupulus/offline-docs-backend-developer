---
title: Configuración de la Aplicación
source_url: https://www.php.net/manual/es/yaf.appconfig.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/appconfig.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: f4ff30a7a
order: 104460
---

## Configuración de la Aplicación

Se debería proporcionar una array de configuración o una ruta a un fichero de configuración ini (véase `Yaf_Config_Ini`) a Yaf_Application::\_\_construct.

Yaf fusionará las configuraciones de la aplicación y del usuario automáticamente. Las configuraciones de la aplicación tienen el prefijo "yaf." o "application.". Si existen ambos prefijos, "yaf." y "application.", "application." tendrá preferencia.

Un ejemplo de array de PHP

```php
<?php

$configs = array(
    "application" => array(
        "directory" => dirname(__FILE__),
        "dispatcher" => array(
            "catchException" => 0,
        ),
        "view" => array(
            "ext" => "phtml",
        ),
    ),
);

$app = new Yaf_Application($configs);

?>

   
```

Un ejemplo de un fichero ini

```php
[yaf]
yaf.directory = APPLICATION_PATH "/application"
yaf.dispatcher.catchException = 0

[product : yaf]
; user configuration list here

   
```

| Nombre | Por defecto | Historial de cambios |
|----|----|----|
| application.directory |  |  |
| application.ext | "php" |  |
| application.view.ext | "phtml" |  |
| application.modules | "index" |  |
| application.library | application.directory . "/library" |  |
| application.library.directory | application.directory . "/library" |  |
| application.library.namespace | "" |  |
| application.bootstrap | application.directory . "/Bootstrap" . application.ext |  |
| application.baseUri | "" |  |
| application.dispatcher.defaultRoute |  |  |
| application.dispatcher.throwException | 1 |  |
| application.dispatcher.catchException | 0 |  |
| application.dispatcher.defaultModule | "index" |  |
| application.dispatcher.defaultController | "index" |  |
| application.dispatcher.defaultAction | "index" |  |
| application.system |  |  |

Configuración de la Aplicación Yaf

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`application.directory` `string`  
El directorio de la aplicación, que es la caperta que contiene las carpetas "controllers", "views", "models", "plugins".

> [!NOTE]
> Esta entrada de configuración es la única que no tiene un valor predeterminado Se debería definir siempre manualmente.

`application.ext` `string`  
La extensión de fichero del script de PHP, usado en la autocarga de clases (`Yaf_Loader`).

`application.view.ext` `string`  
La extensión de fichero de los script de plantilla de vistas.

`application.modules` `string`  
Una lista separada por comas de los módulos registrados, usada en el proceso de enrutamiento, especialmente mientras existan más de tres segmentos en PATH_INFO,

Yaf necesita una forma de averiguar si el primer segmento es un nombre de módulo o no.

`application.library` `string`  
El directorio de bibliotecas local, véase `Yaf_Loader` y [yaf.library](#ini.yaf.library).

> [!NOTE]
> Después de Yaf 2.1.6, esta entrada de configuración puede ser un array. La ruta de la biblioteca intentará emplear los ítems establecidos en [application.library.directory](#configuration.yaf.library.directory)

`application.library.directory` `string`  
Alias de [application.library](#configuration.yaf.library). Introducido en Yaf 2.1.6

`application.library.namespace` `string`  
Un prefijo separado por comas de nombres de espacios de bibliotecas locales.

Introducido en Yaf 2.1.6

`application.bootstrap` `string`  
Una ruta absoluta del script de la clase Bootstrap.

`application.baseUri` `string`  
Usado para eliminar un prefijo fijo de un uri de petición en el proceso de enrutamiento. Como ejemplo, una petición con la uri de petición "/prefix/controller/action". Si se establece application.baseUri a "/prefix", solamente se tomará "/controller/action" como PATH_INFO en el proceso de enrutamiento.

En general, no hay necesidad de establecer este valor.

`application.dispatcher.throwException` `bool`  
Si es On, Yaf lanzará una excepción mientras ocurra algún error. Véase también Yaf_Dispatcher::throwException.

`application.dispatcher.catchException` `bool`  
Si es On, Yaf remitirá al controlador/acción de errores mientras exista una excepción no capturada. Véase también Yaf_Dispatcher::catchException.

`application.dispatcher.defaultRoute` `string`  
El enrutamiento por defecto, si no se especifica se usará un enrutamiento estático como predeterminado. Véase Yaf_Router::addRoute.

`application.dispatcher.defaultModule` `string`  
El nombre de módulo predeterminado, véase también Yaf_Dispatcher::setDefaultModule.

`application.dispatcher.defaultController` `string`  
El nombre de controlador predeterminado, véase también Yaf_Dispatcher::setDefaultController.

`application.dispatcher.defaultAction` `string`  
El nombre de acción predeterminado, véase también Yaf_Dispatcher::setDefaultAction.

`application.system` `string`  
Establecer la configuración en tiempo de ejecuc de yaf en application.ini, como: [application.system.lowcase_path](#ini.yaf.lowcase-path)

> [!NOTE]
> Solamente las configuraciones de `INI_ALL` se pueden establecer de esta manera.
