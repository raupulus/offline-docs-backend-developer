---
title: Yaf_View_Simple::clear
description: Limpiar valores asignados
source_url: https://www.php.net/manual/es/yaf-view-simple.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_view_simple/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 73fae4ee5
order: 107250
---

Yaf_View_Simple::clear

Limpiar valores asignados

## Descripción

```php
public Yaf_View_Simple::clear([string $name]): bool
```php

Limpia una variable asignada

## Parámetros

`name`  
El nombre de la variable asignada

Si está vacía, limpiará todas las variables asignadas

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_View_Simple::clear`

```
<?php
class IndexController extends Yaf_Controller_Abstract {
    public function indexAction() {
        $this->getView()->clear("foo")->clear("bar"); // clear "foo" and "bar"
        $this->_view->clear(); //clear all assigned variables
    }
}
?>

   
```php

## Véase también

Yaf_View_Simple::assignRef

Yaf_View_Interface::assign

Yaf_View_Simple::\_\_set
