---
title: La clase Yaf_Loader
source_url: https://www.php.net/manual/es/class.yaf-loader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-loader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 330a38c4d
order: 104700
---

## Introducción

`Yaf_Loader` introduce una solución completa de autocarga para Yaf.

La primera vez que se recupera una instancia de la clase `Yaf_Application`, `Yaf_Loader` instanciará un singleton, y se registrará a sí mismo con spl_autoload. Se recupera una instancia usando el método Yaf_Loader::getInstance

`Yaf_Loader` intenta cargar una clase sólo una vez, y si falla, dependiendo de [yaf.use_spl_autoload](#ini.yaf.use-spl-autoload), si esta configuración es "On" Yaf_Loader::autoload devolverá `false`, y así dará otra oportunidad a otra función de autocarga; si es "Off" (por omisión), Yaf_Loader::autoload devolverá `true`, y lo que es más importante: emitirá una advertencia muy útil (muy útil para averiguar por qué no se cargó una clase).

> [!NOTE]
> Por favor, mantenga yaf.use_spl_autoload en "Off" a menos que exista una biblioteca que tenga su propio mecanismo de autocarga y sea imposible reescribirlo.

Por defecto, `Yaf_Loader` asume que todas las bibliotecas (las clases definidas en el script) se almacenan en el [directorio de clases global](#ini.yaf.library), el cual está definido en php.ini (yaf.library).

Si quiere que `Yaf_Loader` busque algunas clases (bibliotecas) en el [directorio de clases local](#yaf-loader.props.library) (el cual está definido en application.ini, y por omisión es [application.directory](#configuration.yaf.directory) . "/libraray"), debería registrar el prefijo de clases usando el método Yaf_Loader::registerLocalNameSpace

Veamos algunos ejemplos (asumiendo que APPLICATION_PATH es [application.directory](#configuration.yaf.directory)):

Ejemplo de configuración

```php
// Se asume la siguiente configuración en php.ini:
yaf.library = "/global_dir"

// Se asume la siguiente configuración en application.ini
application.library = APPLICATION_PATH "/library"

     
```

Se asume que el siguiente espacio de nombres local está registrado:

Registrar el espacio de nombres local

```php
<?php
class Bootstrap extends Yaf_Bootstrap_Abstract{
     public function _initLoader($dispatcher) {
          Yaf_Loader::getInstance()->registerLocalNameSpace(array("Foo", "Bar"));
     }
}
?>

     
```

Ahora los ejemplos de autocarga:

Ejemplo de carga de clases

```php
class Foo_Bar_Test =>
  // APPLICATION_PATH/library/Foo/Bar/Test.php

class GLO_Name  =>
  // /global_dir/Glo/Name.php

class BarNon_Test
  // /global_dir/Barnon/Test.php

     
```

Ejemplo de carga de una clase en el espacio de nombres

```php
class \Foo\Bar\Dummy =>
   // APPLICATION_PATH/library/Foo/Bar/Dummy.php

class \FooBar\Bar\Dummy =>
   // /global_dir/FooBar/Bar/Dummy.php

     
```

Se puede observar que todas las carpetas tienen la primera letra en mayúsculas, se pueden ponerlas en minúsculas estableciendo [yaf.lowcase_path](#ini.yaf.lowcase-path) = On en php.ini

`Yaf_Loader` también está diseñada para cargar las clases MVC, y la regla es:

Ejemplo de carga de clase MVC

```php
Controller Classes =>
// APPLICATION_PATH/controllers/

Model Classes =>
// APPLICATION_PATH/models/

Plugin Classes =>
// APPLICATION_PATH/plugins/

     
```

Yaf identifica un sufijo de clases (por omisión, se puede cambiar el sufijo cambiando la opción de configuración [yaf.name_suffix](#ini.yaf.name-suffix)) para decidir si es una clase MVC:

Distinciones de clases MVC

```php
Controller Classes =>
    // ***Controller

Model Classes =>
    // ***Model

Plugin Classes =>
    // ***Plugin

     
```

algunos ejemplos:

Ejemplo de carga MVC

```php
class IndexController
    // APPLICATION_PATH/controllers/Index.php

class DataModel =>
   // APPLICATION_PATH/models/Data.php

class DummyPlugin =>
  // APPLICATION_PATH/plugins/Dummy.php

class A_B_TestModel =>
  // APPLICATION_PATH/models/A/B/Test.php

     
```

> [!NOTE]
> A partir de 2.1.18, Yaf admite que los Controllers se autocarguen para el lado del scrpt cliente, (lo que significa que la autocarga se desencadena por el script del usuario de php, p.ej., acceder a una propiedad de un Controller estático en Bootstrap o Plugins), aunque el autocargador solamente intenta localizar el controlador bajo la carpeta del módulo predeterminado, que es "APPLICATION_PATH/controllers/".

también, el directorio será afectado por [yaf.lowcase_path](#ini.yaf.lowcase-path).

## Sinopsis de la clase

Yaf_Loader

Yaf_Loader

Propiedades

protected

\_local_ns

protected

\_library

protected

\_global_library

static

\_instance

Métodos

## Propiedades

`_local_ns`  

`_library`  
Por omisión, este valor es [application.directory](#configuration.yaf.directory) . "/library", se puede cambiar en application.ini (application.library) o llamando al método Yaf_Loader::setLibraryPath

`_global_library`  

`_instance`
