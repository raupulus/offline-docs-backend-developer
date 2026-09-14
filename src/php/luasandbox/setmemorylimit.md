---
title: LuaSandbox::setMemoryLimit
description: Define el límite de memoria para el entorno Lua
source_url: https://www.php.net/manual/es/luasandbox.setmemorylimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/setmemorylimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44040
---

LuaSandbox::setMemoryLimit

Define el límite de memoria para el entorno Lua

## Descripción

```php
public LuaSandbox::setMemoryLimit(int $limit): void
```php

Define el límite de memoria para el entorno Lua.

Si se supera este límite, se lanza una excepción `LuaSandboxMemoryError`.

## Parámetros

`limit`  
El límite de memoria en bytes.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Llamando a una función Lua

```
<?php

// crear un nuevo LuaSandbox
$sandbox = new LuaSandbox();

// define un límite de memoria
$sandbox->setMemoryLimit( 50 * 1024 * 1024 );

// ejecuta el código Lua
$sandbox->loadString( 'local x = "x"; while true do x = x .. x; end' )->call();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    PHP Fatal error:  Uncaught LuaSandboxMemoryError: not enough memory

## Véase también

LuaSandbox::getMemoryUsage

LuaSandbox::getPeakMemoryUsage

LuaSandbox::setCPULimit
