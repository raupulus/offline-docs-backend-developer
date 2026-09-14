---
title: Yaf_View_Simple::__set
description: Establece el valor para el motor
source_url: https://www.php.net/manual/es/yaf-view-simple.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_view_simple/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 107330
---

Yaf_View_Simple::\_\_set

Establece el valor para el motor

## Descripción

```php
public Yaf_View_Simple::__set(string $name, mixed $value): void
```php

Esta es una manera alternativa y más sencilla de usar Yaf_View_Simple::assign.

## Parámetros

`name`  
Un nombre de valor de tipo string.

`value`  
Valor mixto.

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_View_Simple::__set`

```
<?php
class IndexController extends Yaf_Controller_Abstract {
    public function indexAction() {
        $this->getView()->foo = "bar"; // es lo mismo que assign("foo", "bar");
    }
}
?>

   
```php

## Véase también

Yaf_View_Simple::assignRef

Yaf_View_Interface::assign
