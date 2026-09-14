---
title: Yaf_View_Simple::assignRef
description: El propósito de assignRef
source_url: https://www.php.net/manual/es/yaf-view-simple.assignref.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_view_simple/assignref.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 7cecc752c
order: 107240
---

Yaf_View_Simple::assignRef

El propósito de assignRef

## Descripción

```php
public Yaf_View_Simple::assignRef(string $name, mixed $value): bool
```php

A diferencia de Yaf_View_Simple::assign, este método asigna un valor de referencia al motor.

## Parámetros

`name`  
Un nombre como cadena que será usado para acceder al valor de la plantilla.

`value`  
Valor mixto

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_View_Simple::assignRef`

```
<?php
class IndexController extends Yaf_Controller_Abstract {
    public function indexAction() {
        $value = "bar";
        $this->getView()->assign("foo", $value);

        /* por favor, observe que existía un error antes de Yaf 2.1.4,
         * que hacía que lo siguiente imprimiera "bar";
         */
        $dummy = $this->getView()->render("index/index.phtml");
        echo $value;

        //prevenir la autointerpretación
        Yaf_Dispatcher::getInstance()->autoRender(FALSE);
    }
}
?>

   
```php

Ejemplo de template

```
<html>
 <head>
  <title><?php echo $foo;  $foo = "cambiado"; ?></title>
 </head>
<body>
</body>
</html>

   
```php

Resultado del ejemplo anterior es similar a:

    /* el acceso al controlador index resultará en: */
    cambiado

## Véase también

Yaf_View_Simple::assign

Yaf_View_Simple::\_\_set
