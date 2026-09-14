---
title: La clase Yaf_Controller_Abstract
source_url: https://www.php.net/manual/es/class.yaf-controller-abstract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-controller-abstract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 104580
---

## Introducción

`Yaf_Controller_Abstract` es el corazón del sistema de Yaf. MVC significa Modelo Vista Controlador (Model-View-Controller en inglés) y es un patrón de diseño cuyo objetivo es separa la lógica de aplicación de la lógica de vista.

Cada controlador personalizado heredará de la clase `Yaf_Controller_Abstract`.

Se encontrará con que no se pude definir la función \_\_construct en los controladores personalizados, y por esto `Yaf_Controller_Abstract` proporciona un método mágico: Yaf_Controller_Abstract::init().

Si se ha definido un método init() en el controlador personalizado, será llamado en cuanto el controlador se instancie.

Las acciones pueden tener argumentos, al hacerle una petición, si en los parámetros de la petición existen los mismos nombres de variables (véase Yaf_Request_Abstract::getParam) después del enrutamiento, Yaf los pasará al método de acción (véase Yaf_Action_Abstract::execute).

> [!NOTE]
> Estos argumentos se obtienen directamente sin filtración, se deberían porcesar con cuidado antes de usarlos.

## Sinopsis de la clase

Yaf_Controller_Abstract

abstract

Yaf_Controller_Abstract

Propiedades

public

actions

protected

\_module

protected

\_name

protected

\_request

protected

\_response

protected

\_invoke_args

protected

\_view

Métodos

## Propiedades

`actions`  
También se puede definir un método de acción en un script de PHP por separado usando esta propiedad y la clase `Yaf_Action_Abstract`.

Definir una acción en un fichero aparte

```php
<?php
class IndexController extends Yaf_Controller_Abstract {
    protected $acciones = array(
        /** ahora dummyAction está definida en un fichero aparte */
        "dummy" => "actions/Dummy_action.php",
    );

    /* el método de acción puede tener argumentos */
    public function indexAction($name, $id) {
       /* $name e $id son datos no seguros sin tratar */
       assert($nombre == $this->getRequest()->getParam("nombre"));
       assert($id   == $this->_request->getParam("id"));
    }
}
?>

        
```

Dummy_action.php

```php
<?php
class DummyAction extends Yaf_Action_Abstract {
    /* una clase de acción definirá este método como el punto de entrada */
    public function execute() {
    }
}
?>

        
```

`_module`  
El nombre del módulo

`_name`  
El nombre del controlador

`_request`  
El objeto de petición actual

`_response`  
El objeto respuesta actual

`_invoke_args`  

`_view`  
El objeto de motor de vistas
