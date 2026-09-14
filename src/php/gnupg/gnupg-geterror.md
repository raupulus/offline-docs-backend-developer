---
title: gnupg_geterror
description: Devuelve el texto de error, si una función falla
source_url: https://www.php.net/manual/es/function.gnupg-geterror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-geterror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29080
---

gnupg_geterror

Devuelve el texto de error, si una función falla

## Descripción

```php
gnupg_geterror(resource $identifier): string
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

## Valores devueltos

Devuelve el texto de error si se ha producido un error, en caso contrario devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_geterror` (Estilo procedimental)

```
<?php
$res = gnupg_init();
echo gnupg_geterror($res);
?>

    
```php

Ejemplo con `gnupg_geterror` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
echo $gpg->geterror();
?>

    
```php
