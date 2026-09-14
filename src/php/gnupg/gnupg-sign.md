---
title: gnupg_sign
description: Firma un texto dado
source_url: https://www.php.net/manual/es/function.gnupg-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29190
---

gnupg_sign

Firma un texto dado

## Descripción

```php
gnupg_sign(resource $identifier, string $plaintext): string
```php

Firma el argumento `plaintext` con las claves que fueron establecidas con [gnupg_addsignkey](#function.gnupg-addsignkey) previamente y devuelve el texto firmado o la firma, dependiendo de lo que fue establecido con [gnupg_setsignmode](#function.gnupg-setsignmode).

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`plaintext`  
El texto a firmar.

## Valores devueltos

En caso de éxito, esta función devuelve el texto firmado o la firma. En caso de fallo, esta función devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_sign` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_addsignkey($res,"8660281B6051D071D94B5B230549F9DC851566DC","test");
$signed = gnupg_sign($res, "sólo una prueba");
echo $signed;
?>

    
```php

Ejemplo con `gnupg_sign` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->addsignkey("8660281B6051D071D94B5B230549F9DC851566DC","test");
$signed = $gpg->sign("just a test");
echo $signed;
?>

    
```php
