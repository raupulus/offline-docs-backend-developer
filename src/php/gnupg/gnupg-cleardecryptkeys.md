---
title: gnupg_cleardecryptkeys
description: Elimina todas las claves que fueron fijadas para el descifrado anteriormente
source_url: https://www.php.net/manual/es/function.gnupg-cleardecryptkeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-cleardecryptkeys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 28980
---

gnupg_cleardecryptkeys

Elimina todas las claves que fueron fijadas para el descifrado anteriormente

## Descripción

```php
gnupg_cleardecryptkeys(resource $identifier): bool
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `gnupg_cleardecryptkeys` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_cleardecryptkeys($res);
?>

    
```php

Ejemplo con `gnupg_cleardecryptkeys` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->cleardecryptkeys();
?>

    
```php
