---
title: La clase Yaf_Plugin_Abstract
source_url: https://www.php.net/manual/es/class.yaf-plugin-abstract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-plugin-abstract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4d17b7b49
order: 104710
---

## Introducción

Los complementos tienen en cuenta una extensibilidad y personalización sencillas del framework.

Los complementos son clases. La definición real de una clase variará según el componente -- se puede necesitar implementar esta interfaz, pero de hecho el complemento es en sí mismo una clase.

Un complemento podría cargarse dentro de Yaf utilizando el método Yaf_Dispatcher::registerPlugin, después de registrarlo. Todos los métodos que implementa el complemento según esta interfaz, serán llamados a su debido tiempo.

## Ejemplos

Plugin example

```php
<?php
   /* la clase de arranque debería estar definida bajo ./application/Bootstrap.php */
   class Bootstrap extends Yaf_Bootstrap_Abstract {
        public function _initPlugin(Yaf_Dispatcher $dispatcher) {
            /* register a plugin */
            $dispatcher->registerPlugin(new TestPlugin());
        }
   }

   /* la clase complemento debería estar ubicada bajo ./application/plugins/ */
   class TestPlugin extends Yaf_Plugin_Abstract {
        public function routerStartup(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response) {
            /* before router
               en este hook, el usuario puede hacer alguna reescritura de la url */
            var_dump("routerStartup");
        }
        public function routerShutdown(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response) {
            /* router complete
               en este hook, el usuario puede hacer un control de acceso */
            var_dump("routerShutdown");
        }
        public function dispatchLoopStartup(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response) {
            var_dump("dispatchLoopStartup");
        }
        public function preDispatch(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response) {
            var_dump("preDispatch");
        }
        public function postDispatch(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response) {
            var_dump("postDispatch");
        }
        public function dispatchLoopShutdown(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response) {
            /* final hook
               en este hook el usuario puede hacer el registro o implementar el diseño */
            var_dump("dispatchLoopShutdown");
        }
   }

   Class IndexController extends Yaf_Controller_Abstract {
        public function indexAction() {
            return FALSE; //prevent rendering
        }
   }

   $config = array(
       "application" => array(
           "directory" => dirname(__FILE__) . "/application/",
       ),
   );

   $app = new Yaf_Application($config);
   $app->bootstrap()->run();
?>

   
```

Resultado del ejemplo anterior es similar a:

    string(13) "routerStartup"
    string(14) "routerShutdown"
    string(19) "dispatchLoopStartup"
    string(11) "preDispatch"
    string(12) "postDispatch"
    string(20) "dispatchLoopShutdown"

## Sinopsis de la clase

Yaf_Plugin_Abstract

Yaf_Plugin_Abstract

Métodos
