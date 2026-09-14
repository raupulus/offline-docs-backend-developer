---
title: stripcslashes
description: Decodifica un string codificado con addcslashes
source_url: https://www.php.net/manual/es/function.stripcslashes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/stripcslashes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 6330e4d73
order: 89300
---

stripcslashes

Decodifica un string codificado con

addcslashes

## Descripción

```php
stripcslashes(string $string): string
```php

Devuelve el string `str` después de eliminar todas las barras invertidas. `stripcslashes` respeta las secuencias especiales de C, tales como `\n`, `\r`..., los números octales y hexadecimales.

## Parámetros

`string`  
El string a procesar.

## Valores devueltos

Devuelve el string modificado.

## Ejemplos

Ejemplo con `stripcslashes`

```
     
<?php

var_dump(stripcslashes('I\'d have a coffee.\nNot a problem.') === "I'd have a coffee.
Not a problem."); // true
?>

    
```php

## Véase también

`addcslashes`
