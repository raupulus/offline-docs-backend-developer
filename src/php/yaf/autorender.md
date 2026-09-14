---
title: Yaf_Dispatcher::autoRender
description: Activa/desactiva la autointerpretación
source_url: https://www.php.net/manual/es/yaf-dispatcher.autorender.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_dispatcher/autorender.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 49d4fb555
order: 105600
---

Yaf_Dispatcher::autoRender

Activa/desactiva la autointerpretación

## Descripción

```php
public Yaf_Dispatcher::autoRender([bool $flag]): Yaf_Dispatcher
```php

Ya que `Yaf_Dispatcher` realizará la interpretación automáticamente después de despachar una petición entrante, se puede prevenir la interpretación llamando a este método con el parámetro `flag` establecido a `true`.

> [!NOTE]
> Se puede devolver simplemente `false` en una acción para evitar la autointerpretación de dicha acción.

## Parámetros

`flag`  
bool

> [!NOTE]
> Desde 2.2.0, si no se proporciona este parámetro, será devuelto el estado actual

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Dispatcher::autoRender`

```
<?php
class IndexController extends Yaf_Controller_Abstract {
     /* El método init será llamado tan pronto como se inicialice un controlador */
     public function init() {
         if ($this->getRequest()->isXmlHttpRequest()) {
             //do not call render for ajax request
             //we will outpu a json string
             Yaf_Dispatcher::getInstance()->autoRender(FALSE);
         }
     }

}
?>

   
```php

Resultado del ejemplo anterior es similar a:
