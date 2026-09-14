---
title: Yaf_Action_Abstract::execute
description: Punto de entrada de una acción
source_url: https://www.php.net/manual/es/yaf-action-abstract.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_action_abstract/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 104900
---

Yaf_Action_Abstract::execute

Punto de entrada de una acción

## Descripción

```php
abstract public Yaf_Action_Abstract::execute(mixed ...$args): mixed
```php

El usuario debería definir siempre este método para un acción, este es el punto de entrada de la misma. Yaf_Action_Abstract::execute podría tener argumentos.

> [!NOTE]
> El valor recuperado desde la petición no es seguro. Se debería filtrar el trabajo antes de usarlo.

## Parámetros

`args`  

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Action_Abstract::execute`

```
<?php
/**
 * Un ejemplo de controlador
 */
class ProductController extends Yaf_Controller_Abstract {
      protected $actions = array(
          "index" => "actions/Index.php",
      );
}
?>

   
```php

Ejemplo de `Yaf_Action_Abstract::execute`

```
<?php
/**
 * ListAction
 */
class ListAction extends Yaf_Action_Abstract {
     public function execute ($name, $id) {
         assert($name == $this->getRequest()->getParam("name"));
         assert($id   == $this->getRequest()->getParam("id"));
     }
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    /**
     * Ahora asumimos que estamos usando la ruta Yaf_Route_Static
     * para la petición: http://yourdomain/product/list/name/yaf/id/22
     * resultará:
     */
     bool(true)
     bool(true)

## Véase también
