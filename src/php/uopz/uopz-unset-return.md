---
title: uopz_unset_return
description: Suprime un valor de retorno previamente fijado para una función
source_url: https://www.php.net/manual/es/function.uopz-unset-return.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-unset-return.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99450
---

uopz_unset_return

Suprime un valor de retorno previamente fijado para una función

## Descripción

```php
uopz_unset_return(string $function): bool
```php

```php
uopz_unset_return(string $class, string $function): bool
```

Suprime el valor de retorno de la `function` previamente fijado por uopz_set_return.

## Parámetros

`class`  
El nombre de la clase que contiene la función

`function`  
El nombre de la función

## Valores devueltos

`true` en caso de éxito.

## Ejemplos

Ejemplo de `uopz_unset_return`

```php
<?php
uopz_set_return("strlen", 42);
$len = strlen("Banana");
uopz_unset_return("strlen");
echo $len + strlen("Banana");
?>

   
```

El ejemplo anterior mostrará:

    48
