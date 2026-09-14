---
title: ssh2_fingerprint
description: Recupera la huella de un servidor remoto
source_url: https://www.php.net/manual/es/function.ssh2-fingerprint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-fingerprint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86510
---

ssh2_fingerprint

Recupera la huella de un servidor remoto

## Descripción

```php
ssh2_fingerprint(resource $session, [int $flags]): string
```php

Recupera la huella de un servidor remoto.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

`flags`  
`flags` puede ser `SSH2_FINGERPRINT_MD5` o `SSH2_FINGERPRINT_SHA1` asociado lógicamente con `SSH2_FINGERPRINT_HEX` o `SSH2_FINGERPRINT_RAW`.

## Valores devueltos

Devuelve la huella, en forma de `string`.

## Ejemplos

Comparación de una huella con un valor conocido

```
<?php
$known_host = '6F89C2F0A719B30CC38ABDF90755F2E4';

$connection = ssh2_connect('shell.example.com', 22);

$fingerprint = ssh2_fingerprint($connection,
               SSH2_FINGERPRINT_MD5 | SSH2_FINGERPRINT_HEX);

if ($fingerprint != $known_host) {
  die("HOSTKEY MISMATCH!\n" .
      "Posible ataque Man-In-The-Middle ?");
}
?>

   
```php
