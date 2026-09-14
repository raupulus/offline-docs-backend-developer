---
title: gnupg_addencryptkey
description: Añade una clave para cifrado
source_url: https://www.php.net/manual/es/function.gnupg-addencryptkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-addencryptkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 28960
---

gnupg_addencryptkey

Añade una clave para cifrado

## Descripción

```php
gnupg_addencryptkey(resource $identifier, string $fingerprint): bool
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`fingerprint`  
La huella de la clave.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `gnupg_addencryptkey` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_addencryptkey($res,"8660281B6051D071D94B5B230549F9DC851566DC");
?>

    
```php

Ejemplo con `gnupg_addencryptkey` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->addencryptkey("8660281B6051D071D94B5B230549F9DC851566DC");
?>

    
```php
