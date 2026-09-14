---
title: ob_list_handlers
description: Lista los gestores de salida utilizados
source_url: https://www.php.net/manual/es/function.ob-list-handlers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-list-handlers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 87a266cdd
order: 59850
---

ob_list_handlers

Lista los gestores de salida utilizados

## Descripción

```php
ob_list_handlers(): array
```php

Lista los gestores de salida utilizados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con el gestor de salida en uso (si existe).

Si [output_buffering](#ini.output-buffering) está activado y no se ha definido ningún [output_handler](#ini.output-handler), o si no se ha pasado ninguna función de retorno o `null` a `ob_start`, se devuelve `"default output handler"`. Activar [output_buffering](#ini.output-buffering) y definir un [output_handler](#ini.output-handler) equivale a pasar una [función interna (integrada)](#functions.internal) a `ob_start`.

Si se ha pasado un `callable` a `ob_start`, se devuelve el [nombre completamente cualificado](#language.namespaces.basics) del `callable`. Si el `callable` es un objeto que implementa [\_\_invoke()](#language.oop5.magic.invoke), se devuelve el [nombre completamente cualificado](#language.namespaces.basics) del método [\_\_invoke()](#language.oop5.magic.invoke) del objeto. Si el `callable` es una `Closure`, se devuelve `"Closure::__invoke"`.

## Ejemplos

Ejemplo con `ob_list_handlers`

```
<?php
// uso de output_buffering=On, sin output_handler definido
var_dump(ob_list_handlers());
ob_end_flush();

// ningún retorno o null
ob_start();
var_dump(ob_list_handlers());

// Función anónima
ob_start(function($string) { return $string; });
var_dump(ob_list_handlers());
ob_end_flush();

// función flecha
ob_start(fn($string) => $string);
var_dump(ob_list_handlers());
ob_end_flush();

// callable de primera clase
$firstClassCallable = userDefinedFunction(...);

ob_start([$firstClassCallable, '__invoke']);
var_dump(ob_list_handlers());
ob_end_flush();

// función interna (integrada)
ob_start('print_r');
var_dump(ob_list_handlers());
ob_end_flush();

// función definida por el usuario
function userDefinedFunction($string, $flags) { return $string; };

ob_start('userDefinedFunction');
var_dump(ob_list_handlers());
ob_end_flush();

class MyClass {
    public static function staticHandle($string) {
        return $string;
    }

    public static function handle($string) {
        return $string;
    }

    public function __invoke($string) {
        return $string;
    }
}

// clase y método estático
ob_start(['MyClass','staticHandle']);
var_dump(ob_list_handlers());
ob_end_flush();

// objeto y método no estático
ob_start([new MyClass,'handle']);
var_dump(ob_list_handlers());
ob_end_flush();

// objeto invocable
ob_start(new MyClass);
var_dump(ob_list_handlers());
ob_end_flush();
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      string(22) "default output handler"
    }
    array(1) {
      [0]=>
      string(22) "default output handler"
    }
    array(1) {
      [0]=>
      string(7) "print_r"
    }
    array(1) {
      [0]=>
      string(19) "userDefinedFunction"
    }
    array(1) {
      [0]=>
      string(17) "Closure::__invoke"
    }
    array(1) {
      [0]=>
      string(17) "Closure::__invoke"
    }
    array(1) {
      [0]=>
      string(17) "Closure::__invoke"
    }
    array(1) {
      [0]=>
      string(21) "MyClass::staticHandle"
    }
    array(1) {
      [0]=>
      string(15) "MyClass::handle"
    }
    array(1) {
      [0]=>
      string(17) "MyClass::__invoke"
    }

## Véase también

`ob_end_clean`, `ob_end_flush`, `ob_get_flush`, `ob_start`
