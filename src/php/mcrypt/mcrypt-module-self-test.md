---
title: mcrypt_module_self_test
description: Prueba un modo
source_url: https://www.php.net/manual/es/function.mcrypt-module-self-test.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-module-self-test.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 46000
---

mcrypt_module_self_test

Prueba un modo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_module_self_test(string $algorithm, [string $lib_dir]): bool
```php

Realiza una prueba sobre el algoritmo especificado.

## Parámetros

`algorithm`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

`lib_dir`  
El argumento opcional `lib_dir` contiene la ruta de acceso hasta el módulo del algoritmo en el sistema.

## Valores devueltos

Devuelve `true` si la prueba funciona, y `false` en caso contrario.

## Ejemplos

Ejemplo con `mcrypt_module_self_test`

```
<?php
var_dump(mcrypt_module_self_test(MCRYPT_RIJNDAEL_128)) . "\n";
var_dump(mcrypt_module_self_test(MCRYPT_BOGUS_CYPHER));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
