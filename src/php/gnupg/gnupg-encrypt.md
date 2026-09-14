---
title: gnupg_encrypt
description: Cifra un texto dado
source_url: https://www.php.net/manual/es/function.gnupg-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29040
---

gnupg_encrypt

Cifra un texto dado

## Descripción

```php
gnupg_encrypt(resource $identifier, string $plaintext): string
```php

Cifra el argumento `plaintext` con las claves que han sido establecidas con [gnupg_addencryptkey](#function.gnupg-addencryptkey) previamente y devuelve el texto cifrado.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`plaintext`  
El texto a cifrar.

## Valores devueltos

En caso de éxito, esta función devuelve el texto cifrado. En caso de error, esta función devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_encrypt` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_addencryptkey($res,"8660281B6051D071D94B5B230549F9DC851566DC");
$enc = gnupg_encrypt($res, "sólo una prueba");
echo $enc;
?>

    
```php

Ejemplo con `gnupg_encrypt` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->addencryptkey("8660281B6051D071D94B5B230549F9DC851566DC");
$enc = $gpg->encrypt("sólo una prueba");
echo $enc;
?>

    
```php
