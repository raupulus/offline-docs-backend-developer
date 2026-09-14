---
title: gnupg_deletekey
description: Elimina una clave del llavero
source_url: https://www.php.net/manual/es/function.gnupg-deletekey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-deletekey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: true
translation_revision: a148eb08b
order: 29030
---

gnupg_deletekey

Elimina una clave del llavero

## Descripción

```php
gnupg_deletekey(resource $identifier, string $key, bool $allow_secret): bool
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`key`  
La clave a eliminar.

`allow_secret`  
Especifica si se deben eliminar las claves secretas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo procedimental `gnupg_deletekey`

```
<?php
$res = gnupg_init();
gnupg_deletekey($res, "8660281B6051D071D94B5B230549F9DC851566DC");
?>

    
```php

Ejemplo orientado a objetos `gnupg_deletekey`

```
<?php
$gpg = new gnupg();
$gpg->deletekey("8660281B6051D071D94B5B230549F9DC851566DC");
?>

    
```php
