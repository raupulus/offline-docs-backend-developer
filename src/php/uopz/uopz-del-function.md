---
title: uopz_del_function
description: Elimina una función o método previamente añadido
source_url: https://www.php.net/manual/es/function.uopz-del-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-del-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 3447c129e
order: 99220
---

uopz_del_function

Elimina una función o método previamente añadido

## Descripción

```php
uopz_del_function(string $function): bool
```php

```php
uopz_del_function(string $class, string $function, [int $all]): bool
```

Elimina una función o método previamente añadido.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o método.

`all`  
Si todas las clases que heredan de `class` serán también afectadas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

`uopz_del_function` lanza una `RuntimeException` si la función o método a eliminar no ha sido añadido por `uopz_add_function`.

## Ejemplos

Uso básico de `uopz_del_function`

```php
<?php
uopz_add_function('foo', function () {echo 'bar';});
var_dump(function_exists('foo'));
uopz_del_function('foo');
var_dump(function_exists('foo'));
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

uopz_add_function

uopz_unset_return
