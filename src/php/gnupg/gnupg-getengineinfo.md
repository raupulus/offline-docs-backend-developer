---
title: gnupg_getengineinfo
description: Devuelve la información del motor
source_url: https://www.php.net/manual/es/function.gnupg-getengineinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-getengineinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: true
translation_revision: 330a38c4d
order: 29070
---

gnupg_getengineinfo

Devuelve la información del motor

## Descripción

```php
gnupg_getengineinfo(resource $identifier): array
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

## Valores devueltos

Devuelve un array que contiene la información del motor compuesto por `protocol`, `file_name` y `home_dir`.

## Ejemplos

Ejemplo procedimental `gnupg_getengineinfo`

```
<?php
$res = gnupg_init();
print_r(gnupg_getengineinfo($res));
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      ["protocol"]=>
      int(0)
      ["file_name"]=>
      string(12) "/usr/bin/gpg"
      ["home_dir"]=>
      string(0) ""
    }

Ejemplo orientado a objetos `gnupg_getengineinfo`

```
<?php
$gpg = new gnupg(["file_name" => "/usr/bin/gpg2", "home_dir" => "/var/www/.gnupg"]);
print_r($gpg->getengineinfo());
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      ["protocol"]=>
      int(0)
      ["file_name"]=>
      string(13) "/usr/bin/gpg2"
      ["home_dir"]=>
      string(15) "/var/www/.gnupg"
    }
