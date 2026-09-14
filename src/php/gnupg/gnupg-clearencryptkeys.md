---
title: gnupg_clearencryptkeys
description: Elimina todas las claves que fueron establecidas para cifrado con anterioridad
source_url: https://www.php.net/manual/es/function.gnupg-clearencryptkeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-clearencryptkeys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 28990
---

gnupg_clearencryptkeys

Elimina todas las claves que fueron establecidas para cifrado con anterioridad

## Descripción

```php
gnupg_clearencryptkeys(resource $identifier): bool
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `gnupg_clearencryptkeys` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_clearencryptkeys($res);
?>

    
```php

Ejemplo con `gnupg_clearencryptkeys` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->clearencryptkeys();
?>

    
```php
