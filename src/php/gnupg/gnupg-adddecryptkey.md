---
title: gnupg_adddecryptkey
description: Añade una clave para descifrado
source_url: https://www.php.net/manual/es/function.gnupg-adddecryptkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-adddecryptkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 28950
---

gnupg_adddecryptkey

Añade una clave para descifrado

## Descripción

```php
gnupg_adddecryptkey(resource $identifier, string $fingerprint, string $passphrase): bool
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`fingerprint`  
La huella de la clave.

`passphrase`  
La frase de contraseña (similar a la contraseña, pero más larga).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `gnupg_adddecryptkey` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_adddecryptkey($res,"8660281B6051D071D94B5B230549F9DC851566DC","test");
?>

    
```php

Ejemplo con `gnupg_adddecryptkey` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->adddecryptkey("8660281B6051D071D94B5B230549F9DC851566DC","test");
?>

    
```php
