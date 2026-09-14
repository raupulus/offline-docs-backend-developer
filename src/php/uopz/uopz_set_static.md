---
title: uopz_set_static
description: Fija las variables estáticas en el ámbito de una función o de un método
source_url: https://www.php.net/manual/es/function.uopz-set-static.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz_set_static.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: ef509edbd
order: 99460
---

uopz_set_static

Fija las variables estáticas en el ámbito de una función o de un método

## Descripción

```php
uopz_set_static(string $function, array $static): void
```php

```php
uopz_set_static(string $class, string $function, array $static): void
```

Fija las variables estáticas en el ámbito de una función o de un método.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o del método.

`static`  
El `array` asociativo de nombres de variables mapeados a sus valores.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de uso de `uopz_set_static`

```php
<?php
function foo() {
    static $bar = 'baz';
    var_dump($bar);
}
uopz_set_static('foo', ['bar' => 'qux']);
foo();
?>

   
```

El ejemplo anterior mostrará:

    string(3) "qux"

## Véase también

uopz_get_static
