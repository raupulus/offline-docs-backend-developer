---
title: gnupg_import
description: Importa una clave
source_url: https://www.php.net/manual/es/function.gnupg-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29120
---

gnupg_import

Importa una clave

## Descripción

```php
gnupg_import(resource $identifier, string $keydata): array
```php

Importa la clave `keydata` y devuelve un array con la información sobre el proceso de importación.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`keydata`  
La clave a importar.

## Valores devueltos

En caso de éxito, esta función devuelve un array de información sobre el proceso de importación. En caso de fallo, esta función devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_import` (Estilo procedimental)

```
<?php
$res = gnupg_init();
$info = gnupg_import($res,$keydata);
print_r($info);
?>

    
```php

Ejemplo con `gnupg_import` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$info = $gpg->import($keydata);
print_r($info);
?>

    
```php
