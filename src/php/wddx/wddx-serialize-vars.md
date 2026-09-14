---
title: wddx_serialize_vars
description: Registra múltiples valores en un paquete WDDX
source_url: https://www.php.net/manual/es/function.wddx-serialize-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/functions/wddx-serialize-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: e41806c30
order: 101250
---

wddx_serialize_vars

Registra múltiples valores en un paquete WDDX

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.4.0.

## Descripción

```php
wddx_serialize_vars(mixed $var_name, mixed ...$var_names): string
```php

Crea un paquete WDDX con una estructura que contiene la representación serializada de las variables pasadas.

## Parámetros

Esta función acepta un número variable de argumentos.

`var_name`  
Puede ser una `string` que nombre una variable o un array que contenga nombres de variables o de otros arrays, etc..

`var_names`  

## Valores devueltos

Devuelve el paquete WDDX, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `wddx_serialize_vars`

```
<?php
$a = 1;
$b = 5.5;
$c = array("blue", "orange", "violet");
$d = "colors";

$clvars = array("c", "d");
echo wddx_serialize_vars("a", "b", $clvars);
?>

    
```php

El ejemplo anterior mostrará:

    <wddxPacket version='1.0'><header/><data><struct><var name='a'><number>1</number></var>
    <var name='b'><number>5.5</number></var><var name='c'><array length='3'>
    <string>blue</string><string>orange</string><string>violet</string></array></var>
    <var name='d'><string>colors</string></var></struct></data></wddxPacket>
