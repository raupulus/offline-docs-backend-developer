---
title: gnupg_decryptverify
description: Descifra y verifica un texto dado
source_url: https://www.php.net/manual/es/function.gnupg-decryptverify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-decryptverify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29020
---

gnupg_decryptverify

Descifra y verifica un texto dado

## Descripción

```php
gnupg_decryptverify(resource $identifier, string $text, string $plaintext): array
```php

Descifra y verifica un texto dado y devuelve las informaciones sobre la firma.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`text`  
El texto a descifrar.

`plaintext`  
El argumento `plaintext` se rellena con el texto descifrado.

## Valores devueltos

En caso de éxito, esta función devuelve las informaciones sobre la firma y rellena el argumento `plaintext` con el texto descifrado. En caso de fallo, esta función devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_decryptverify` (Estilo procedimental)

```
<?php
$plaintext = "";
$res = gnupg_init();
gnupg_adddecryptkey($res,"8660281B6051D071D94B5B230549F9DC851566DC","test");
$info = gnupg_decryptverify($res,$text,$plaintext);
print_r($info);
?>

    
```php

Ejemplo con `gnupg_decryptverify` (Estilo orientado a objetos)

```
<?php
$plaintext = "";
$gpg = new gnupg();
$gpg->adddecryptkey("8660281B6051D071D94B5B230549F9DC851566DC","test");
$info = $gpg->decryptverify($text,$plaintext);
print_r($info);
?>

    
```php
