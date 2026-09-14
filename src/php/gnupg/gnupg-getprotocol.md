---
title: gnupg_getprotocol
description: Devuelve el protocolo activo actual para todas las operaciones
source_url: https://www.php.net/manual/es/function.gnupg-getprotocol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-getprotocol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29100
---

gnupg_getprotocol

Devuelve el protocolo activo actual para todas las operaciones

## Descripción

```php
gnupg_getprotocol(resource $identifier): int
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

## Valores devueltos

Devuelve el protocolo activo actual, que puede ser uno de estos: `GNUPG_PROTOCOL_OpenPGP` o `GNUPG_PROTOCOL_CMS`.

## Ejemplos

Ejemplo con `gnupg_getprotocol` (Estilo procedimental)

```
<?php
$res = gnupg_init();
echo gnupg_getprotocol($res);
?>

    
```php

Ejemplo con `gnupg_getprotocol` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
echo $gpg->getprotocol();
?>

    
```php
