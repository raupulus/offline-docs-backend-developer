---
title: La clase Yaf_Bootstrap_Abstract
source_url: https://www.php.net/manual/es/class.yaf-bootstrap-abstract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-bootstrap-abstract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4d17b7b49
order: 104540
---

## Introducción

El arranque (bootstrap) es un mecanismo usado para realizar una configuración inicial antes de ejecutar una Aplicación.

Los usuarios puede definir su propia clase Bootstrap heredando la clase `Yaf_Bootstrap_Abstract`

Cualquier método declarado en la clase Arranque al que se le anteponga "\_init" será llamado uno a uno por el método Yaf_Application::bootstrap según su orden de definición.

## Ejemplos

Ejemplo de arranque

```php
<?php
   /* la clase de arranque debería estar definida bajo ./application/Bootstrap.php */
   class Bootstrap extends Yaf_Bootstrap_Abstract {
        public function _initConfig(Yaf_Dispatcher $dispatcher) {
            var_dump(__METHOD__);
        }
        public function _initPlugin(Yaf_Dispatcher $dispatcher) {
            var_dump(__METHOD__);
        }
   }

   $config = array(
       "application" => array(
           "directory" => dirname(__FILE__) . "/application/",
       ),
   );

   $app = new Yaf_Application($config);
   $app->bootstrap();
?>

    
```

Resultado del ejemplo anterior es similar a:

    string(22) "Bootstrap::_initConfig"
    string(22) "Bootstrap::_initPlugin"

## Sinopsis de la clase

Yaf_Bootstrap_Abstract

abstract

Yaf_Bootstrap_Abstract

Propiedades

Métodos
