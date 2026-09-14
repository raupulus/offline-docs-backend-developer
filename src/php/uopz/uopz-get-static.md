---
title: uopz_get_static
description: Devuelve las variables estáticas de una función o método
source_url: https://www.php.net/manual/es/function.uopz-get-static.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-get-static.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 330a38c4d
order: 99320
---

uopz_get_static

Devuelve las variables estáticas de una función o método

## Descripción

```php
uopz_get_static(string $class, string $function): array
```php

```php
uopz_get_static(string $function): array
```

Devuelve las variables estáticas de una función o método.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o método.

## Valores devueltos

Devuelve un `array` asociativo de nombres de variables mapeados a sus valores actuales en caso de éxito, o `null` si la función o método no existe.

Desde PHP 8.3.0, los inicializadores estáticos se calculan ya sea durante la compilación, o si no es posible, solo cuando la función o método se ejecuta por primera vez, en cuyo caso el valor de la variable estática se reporta como `null` antes de la primera invocación.

## Ejemplos

Uso básico de `uopz_get_static`

```php
<?php
function foo() {
    static $bar = 'baz';
}
var_dump(uopz_get_static('foo'));
?>

   
```

El ejemplo anterior mostrará:

    array(1) {
      ["bar"]=>
      string(3) "baz"
    }

## Véase también

ReflectionFunctionAbstract::getStaticVariables

uopz_set_static
