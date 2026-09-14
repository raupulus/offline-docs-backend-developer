---
title: Yaf_View_Simple::assign
description: Asignar valores
source_url: https://www.php.net/manual/es/yaf-view-simple.assign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_view_simple/assign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4a211b7c8
order: 107230
---

Yaf_View_Simple::assign

Asignar valores

## Descripción

```php
public Yaf_View_Simple::assign(string $name, [mixed $value]): bool
```php

Asigna una variable al motor de vistas.

## Parámetros

`name`  
Una cadena o un array.

Si es una cadena se requiere el argumento \$value siguiente.

`value`  
Valor mixto

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_View_Simple::assign`

```
<?php
class IndexController extends Yaf_Controller_Abstract {
    public function indexAction() {
        $this->getView()->assign("foo", "bar");
        $this->_view->assign( array( "key" => "value", "name" => "value"));
    }
}
?>

   
```php

Ejemplo de template

```
<html>
 <head>
  <title><?php echo $foo; ?></title>
 </head>
<body>
  <?php
    foreach ($this->_tpl_vars as $name => $value) {
         echo $$name; // o echo $this->_tpl_vars[$name];
    }
  ?>
</body>
</html>

   
```php

## Véase también

Yaf_View_Simple::assignRef

Yaf_View_Interface::clear

Yaf_View_Simple::\_\_set
