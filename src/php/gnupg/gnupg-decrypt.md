---
title: gnupg_decrypt
description: Descifra un texto dado
source_url: https://www.php.net/manual/es/function.gnupg-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29010
---

gnupg_decrypt

Descifra un texto dado

## Descripción

```php
gnupg_decrypt(resource $identifier, string $text): string
```php

Descifra un texto dado con las claves que se han establecido con [gnupg_adddecryptkey](#function.gnupg-adddecryptkey) previamente.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`text`  
El texto a descifrar.

## Valores devueltos

En caso de éxito, esta función devuelve el texto descifrado. En caso de error, esta función devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_decrypt` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_adddecryptkey($res,"8660281B6051D071D94B5B230549F9DC851566DC","test");
$plain = gnupg_decrypt($res,$encrypted_text);
echo $plain;
?>

    
```php

Ejemplo con `gnupg_decrypt` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->adddecryptkey("8660281B6051D071D94B5B230549F9DC851566DC","test");
$plain = $gpg->decrypt($encrypted_text);
echo $plain;
?>

    
```php
