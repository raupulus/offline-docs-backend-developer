---
title: gnupg_verify
description: Verifica un texto firmado
source_url: https://www.php.net/manual/es/function.gnupg-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29200
---

gnupg_verify

Verifica un texto firmado

## Descripción

```php
gnupg_verify(resource $identifier, string $signed_text, string $signature, [string $plaintext]): array
```php

Verifica el argumento `signed_text` y devuelve las informaciones acerca de la firma.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`signed_text`  
El texto firmado.

`signature`  
La firma. Para verificar un texto firmado en claro, se establece la firma a `false`.

`plaintext`  
El texto. Si este argumento opcional es pasado, se rellena con el `plaintext`.

## Valores devueltos

En caso de éxito, esta función devuelve informaciones acerca de la firma. En caso de fallo, esta función devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_verify` (Estilo procedimental)

```
<?php
$plaintext = "";
$res = gnupg_init();
// firmado en claro
$info = gnupg_verify($res,$signed_text,false,$plaintext);
print_r($info);
// firma separada
$info = gnupg_verify($res,$signed_text,$signature);
print_r($info);
?>

    
```php

Ejemplo con `gnupg_verify` (Estilo orientado a objetos)

```
<?php
$plaintext = "";
$gpg = new gnupg();
// firmado en claro
$info = $gpg->verify($signed_text,false,$plaintext);
print_r($info);
// firma separada
$info = $gpg->verify($signed_text,$signature);
print_r($info);
?>

    
```php
