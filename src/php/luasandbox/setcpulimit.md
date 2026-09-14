---
title: LuaSandbox::setCPULimit
description: Define la limitación de tiempo CPU para el entorno Lua
source_url: https://www.php.net/manual/es/luasandbox.setcpulimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/setcpulimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44030
---

LuaSandbox::setCPULimit

Define la limitación de tiempo CPU para el entorno Lua

## Descripción

```php
public LuaSandbox::setCPULimit(float $limit): void
```php

Define la limitación de tiempo CPU para el entorno Lua.

Si el tiempo total de usuario y sistema utilizado por el entorno después de la llamada a este método excede este límite, se lanza una excepción `LuaSandboxTimeoutError`.

El tiempo utilizado en las funciones de retrollamada PHP se incluye en el límite.

Definir el tiempo límite a una función de retrollamada Lua en ejecución provoca que el temporizador se reinicie, o se inicie si no estaba ya en ejecución.

> [!NOTE]
> En Windows, la limitación de tiempo CPU será ignorada. En los sistemas operativos que no soportan `CLOCK_THREAD_CPUTIME_ID`, como FreeBSD y Mac OS X, el tiempo transcurrido en el muro, en lugar del tiempo CPU, será limitado.

## Parámetros

`limit`  
El límite como `float` en segundos, o `false` para ningún límite.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Llamada a una función Lua

```
<?php

// crear un nuevo LuaSandbox
$sandbox = new LuaSandbox();

// definir un límite de tiempo
$sandbox->setCPULimit( 2 );

// lanza el código Lua
$sandbox->loadString( 'while true do end' )->call();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    PHP Fatal error:  Uncaught LuaSandboxTimeoutError: The maximum execution time for this script was exceeded

## Véase también

LuaSandbox::getCPUUsage

LuaSandbox::setMemoryLimit
