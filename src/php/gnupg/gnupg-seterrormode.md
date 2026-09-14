---
title: gnupg_seterrormode
description: Establece el modo para error_reporting
source_url: https://www.php.net/manual/es/function.gnupg-seterrormode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-seterrormode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29170
---

gnupg_seterrormode

Establece el modo para error_reporting

## Descripción

```php
gnupg_seterrormode(resource $identifier, int $errormode): void
```php

Establece el modo para [error_reporting](#ini.error-reporting).

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`errormode`  
El modo de error.

`errormode` acepta una constante que indica qué tipo de error_reporting debe ser utilizado. Los valores posibles son `GNUPG_ERROR_WARNING`, `GNUPG_ERROR_EXCEPTION` y `GNUPG_ERROR_SILENT`. Por omisión `GNUPG_ERROR_SILENT`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `gnupg_seterrormode` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_seterrormode($res, GNUPG_ERROR_WARNING); // emite un PHP-Warning en caso de error
?>

    
```php

Ejemplo con `gnupg_seterrormode` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->seterrormode(gnupg::ERROR_EXCEPTION); // lanza una excepción en caso de error
?>

    
```php
