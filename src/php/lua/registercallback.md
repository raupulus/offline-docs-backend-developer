---
title: Lua::registerCallback
description: Registra una función PHP en Lua
source_url: https://www.php.net/manual/es/lua.registercallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/lua/lua/registercallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: lua
translation_status: ready
translation_revision: 64ae8f745
order: 43820
---

Lua::registerCallback

Registra una función PHP en Lua

## Descripción

```php
public Lua::registerCallback(string $name, callable $function): mixed
```php

Registra una función PHP en Lua con el nombre de función que se indique en "\$name"

## Parámetros

`name`  

`function`  
Una función de llamada de retorno válida PHP

## Valores devueltos

Devuelve `$this`, `null` en caso que los argumentos sean erróneos o `false` para cualquier otro tipo de error.

## Ejemplos

Ejemplo de `Lua::registerCallback`

```
<?php
$lua = new Lua();
$lua->registerCallback("echo", "var_dump");
$lua->eval(<<<CODE
    echo({1, 2, 3});
CODE
);
?>

   
```php

El ejemplo anterior mostrará:

    array(3) {
      [1]=>
      float(1)
      [2]=>
      float(2)
      [3]=>
      float(3)
    }
