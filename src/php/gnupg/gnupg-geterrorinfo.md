---
title: gnupg_geterrorinfo
description: Devuelve la información de error
source_url: https://www.php.net/manual/es/function.gnupg-geterrorinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-geterrorinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: true
translation_revision: a148eb08b
order: 29090
---

gnupg_geterrorinfo

Devuelve la información de error

## Descripción

```php
gnupg_geterrorinfo(resource $identifier): array
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

## Valores devueltos

Devuelve un array con la información de error.

## Ejemplos

Ejemplo procedimental `gnupg_geterrorinfo`

```
<?php
$res = gnupg_init();
// esto es llamado sin error
print_r(gnupg_geterrorinfo($res));
?>

    
```php

El ejemplo anterior mostrará:

    array(4) {
      ["generic_message"]=>
      bool(false)
      ["gpgme_code"]=>
      int(0)
      ["gpgme_source"]=>
      string(18) "Unspecified source"
      ["gpgme_message"]=>
      string(7) "Success"
    }

Ejemplo orientado a objetos `gnupg_geterrorinfo`

```
<?php
$gpg = new gnupg();
// llamada con error
$gpg->decrypt('abc');
// la información de error debe ser mostrada
print_r($gpg->geterrorinfo());
?>

    
```php

El ejemplo anterior mostrará:

    array(4) {
      ["generic_message"]=>
      string(14) "decrypt failed"
      ["gpgme_code"]=>
      int(117440570)
      ["gpgme_source"]=>
      string(5) "GPGME"
      ["gpgme_message"]=>
      string(7) "No data"
    }
