---
title: gnupg_addsignkey
description: Añade una clave para firmar
source_url: https://www.php.net/manual/es/function.gnupg-addsignkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-addsignkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 28970
---

gnupg_addsignkey

Añade una clave para firmar

## Descripción

```php
gnupg_addsignkey(resource $identifier, string $fingerprint, [string $passphrase]): bool
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

Ejemplo con `gnupg_addsignkey` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_addsignkey($res,"8660281B6051D071D94B5B230549F9DC851566DC","test");
?>

    
```php

Ejemplo con `gnupg_addsignkey` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->addsignkey("8660281B6051D071D94B5B230549F9DC851566DC","test");
?>

    
```php
