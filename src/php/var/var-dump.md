---
title: var_dump
description: Muestra información sobre una variable
source_url: https://www.php.net/manual/es/function.var-dump.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/var-dump.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 8cdc6621f
order: 100790
---

var_dump

Muestra información sobre una variable

## Descripción

```php
var_dump(mixed $value, mixed ...$values): void
```php

`var_dump` muestra información estructurada sobre una variable, incluyendo su tipo y valor. Los arrays y objetos son explorados recursivamente, con indentaciones, para resaltar su estructura.

Todas las propiedades públicas, privadas y protegidas de los objetos serán mostradas en la salida a menos que el objeto implemente un método [\_\_debugInfo()](#language.oop5.magic.debuginfo).

> [!TIP]
> Al igual que con cualquier cosa que envíe sus resultados directamente al navegador, las [funciones de control de salida](#book.outcontrol) se pueden usar para capturar la salida de esta función y guardarla en un `string` (por ejemplo).

## Parámetros

`value`  
La expresión a mostrar.

`values`  
Expresión adicional a mostrar.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `var_dump`

```
<?php
$a = array(1, 2, array("a", "b", "c"));
var_dump($a);
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      array(3) {
        [0]=>
        string(1) "a"
        [1]=>
        string(1) "b"
        [2]=>
        string(1) "c"
      }
    }

        

```
<?php

$b = 3.1;
$c = true;
var_dump($b, $c);

?>

    
```php

El ejemplo anterior mostrará:

    float(3.1)
    bool(true)

## Véase también

`print_r`, `debug_zval_dump`, `var_export`, [\_\_debugInfo()](#language.oop5.magic.debuginfo)
