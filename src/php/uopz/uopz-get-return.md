---
title: uopz_get_return
description: Devuelve un valor de retorno previamente definido para una función
source_url: https://www.php.net/manual/es/function.uopz-get-return.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-get-return.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99310
---

uopz_get_return

Devuelve un valor de retorno previamente definido para una función

## Descripción

```php
uopz_get_return(string $function): mixed
```php

```php
uopz_get_return(string $class, string $function): mixed
```

Devuelve el valor de retorno de la `function` previamente definido por uopz_set_return.

## Parámetros

`class`  
El nombre de la clase que contiene la función

`function`  
El nombre de la función

## Valores devueltos

El valor de retorno o la closure previamente definida.

## Ejemplos

Ejemplo de `uopz_get_return`

```php
<?php
uopz_set_return("strlen", 42);
echo uopz_get_return("strlen");
?>

   
```

El ejemplo anterior mostrará:

    42
