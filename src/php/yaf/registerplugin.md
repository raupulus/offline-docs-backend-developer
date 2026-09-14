---
title: Yaf_Dispatcher::registerPlugin
description: Registra un complemento
source_url: https://www.php.net/manual/es/yaf-dispatcher.registerplugin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_dispatcher/registerplugin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 49d4fb555
order: 105750
---

Yaf_Dispatcher::registerPlugin

Registra un complemento

## Descripción

```php
public Yaf_Dispatcher::registerPlugin(Yaf_Plugin_Abstract $plugin): Yaf_Dispatcher
```php

Registra un complemento (véase `Yaf_Plugin_Abstract`). Generalmente se registran complementos en el Arranque (véase la clase `Yaf_Bootstrap_Abstract`).

## Parámetros

`plugin`  

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Dispatcher::registerPlugin`

```
<?php
class Bootstrap extends Yaf_Bootstrap_Abstract{
  public function _initPlugin(Yaf_Dispatcher $despachador) {
    /**
    * Yaf asume que los scripts de complementos están en [application.directory] .  "/plugins"
    * para este caso, será:
    * [application.directory] . "/plugins/" . "User" . [application.ext]
    */
    $usuario = new UserPlugin();
    $despachador->registerPlugin($usuario);
 }

   
```php

## Véase también

Yaf_Plugin_Abstract

Yaf_Bootstrap_Abstract
