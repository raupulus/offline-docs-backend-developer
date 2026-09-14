---
title: Yaf_Controller_Abstract::forward
description: Avanza a la siguiente acción
source_url: https://www.php.net/manual/es/yaf-controller-abstract.forward.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_controller_abstract/forward.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: c9389e4a0
order: 105460
---

Yaf_Controller_Abstract::forward

Avanza a la siguiente acción

## Descripción

```php
public Yaf_Controller_Abstract::forward(string $action, [array $paramters]): bool
```php

```php
public Yaf_Controller_Abstract::forward(string $controller, string $action, [array $paramters]): bool
```

```php
public Yaf_Controller_Abstract::forward(string $module, string $controller, string $action, [array $paramters]): bool
```php

Avanza el proceso de ejecución actual a otra acción.

> [!NOTE]
> Este método no cambia a la acción destino de inmediato, toma lugar después de la finalización del flujo actual.

## Parámetros

`module`  
El nombre del módulo destino. Si es NULL, se asume el nombre del módulo predeterminado

`controller`  
El nombre del controlador destino

`action`  
El nombre de la acción destino

`paramters`  
Argumentos de llamada

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `Yaf_Controller_Abstract::forward`

```
<?php
class IndexController extends Yaf_Controller_Abstract
{
    public function indexAction(){
         $logined = $_SESSION["login"];
         if (!$logined) {
             $this->forward("login", array("from" => "Index")); // forward to login action
             return FALSE;  // this is important, this finish current working flow
                            // and tell the Yaf do not doing auto-render
         }

         // otros procesos
    }

    public function loginAction() {
         echo "login, redirected from ", $this->getInvokeArg("from") , " action";
    }
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

       login, redirected from Index action

## Véase también

Yaf_Request_Abstrace::getParam
