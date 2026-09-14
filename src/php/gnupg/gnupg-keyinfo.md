---
title: gnupg_keyinfo
description: Retorna un array con las informaciones acerca de todas las claves que
  coinciden con el patrón dado
source_url: https://www.php.net/manual/es/function.gnupg-keyinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-keyinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29140
---

gnupg_keyinfo

Retorna un array con las informaciones acerca de todas las claves que coinciden con el patrón dado

## Descripción

```php
gnupg_keyinfo(resource $identifier, string $pattern): array
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`pattern`  
La máscara a utilizar sobre las claves.

## Valores devueltos

Retorna un array con las informaciones acerca de todas las claves que coinciden con el patrón dado o retorna `false` si ha ocurrido un error.

## Ejemplos

Ejemplo con `gnupg_keyinfo` (Estilo procedimental)

```
<?php
$res = gnupg_init();
$info = gnupg_keyinfo($res, 'test');
print_r($info);
?>

    
```php

Ejemplo con `gnupg_keyinfo` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$info = $gpg->keyinfo("test");
print_r($info);
?>

    
```php
