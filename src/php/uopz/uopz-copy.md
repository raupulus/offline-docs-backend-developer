---
title: uopz_copy
description: Copia una función
source_url: https://www.php.net/manual/es/function.uopz-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99210
---

uopz_copy

Copia una función

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_copy(string $function): Closure
```php

```php
uopz_copy(string $class, string $function): Closure
```

Copia una función a partir de su nombre.

## Parámetros

`class`  
El nombre de la clase que contiene la función a copiar

`function`  
El nombre de la función

## Valores devueltos

Una closure para la función especificada.

## Ejemplos

Ejemplo con `uopz_copy`

```php
<?php
$strtotime = uopz_copy('strtotime');

uopz_function("strtotime", function($arg1, $arg2) use($strtotime) {
    /* se puede llamar a la función strtotime original desde aquí */
    var_dump($arg1);
});

var_dump(strtotime('dummy'));
?>

   
```

El ejemplo anterior mostrará:

    string(5) "dummy"
