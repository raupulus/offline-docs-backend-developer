---
title: uopz_add_function
description: Añade una función o método inexistente
source_url: https://www.php.net/manual/es/function.uopz-add-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-add-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 3447c129e
order: 99170
---

uopz_add_function

Añade una función o método inexistente

## Descripción

```php
uopz_add_function(string $function, Closure $handler, [int $flags]): bool
```php

```php
uopz_add_function(string $class, string $function, Closure $handler, [int $flags], [int $all]): bool
```

Añade una función o método inexistente.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o método.

`handler`  
La `Closure` que define la nueva función o método.

`flags`  
Los flags a definir para la nueva función o método.

`all`  
Si todas las clases que heredan de `class` serán también afectadas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

`uopz_add_function` lanza una `RuntimeException` si la función o método a añadir ya existe.

## Ejemplos

Uso básico de `uopz_add_function`

```php
<?php
uopz_add_function('foo', function () {echo 'bar';});
foo();
?>

   
```

El ejemplo anterior mostrará:

    bar

## Véase también

uopz_del_function

uopz_set_return
