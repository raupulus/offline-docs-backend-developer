---
title: gnupg_setsignmode
description: Establece el modo para firmar
source_url: https://www.php.net/manual/es/function.gnupg-setsignmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-setsignmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29180
---

gnupg_setsignmode

Establece el modo para firmar

## Descripción

```php
gnupg_setsignmode(resource $identifier, int $signmode): bool
```php

Establece el modo para firmar.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`sigmode`  
El modo de firma.

`signmode` acepta una constante que indica qué tipo de firma debe ser producida. Los valores posibles son: `GNUPG_SIG_MODE_NORMAL`, `GNUPG_SIG_MODE_DETACH` y `GNUPG_SIG_MODE_CLEAR`. Por omisión, se utiliza `GNUPG_SIG_MODE_CLEAR`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `gnupg_setsignmode` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_setsignmode($res, GNUPG_SIG_MODE_DETACH); // produce una firma desvinculada
?>

    
```php

Ejemplo con `gnupg_setsignmode` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->setsignmode(gnupg::SIG_MODE_DETACH); // produce una firma desvinculada
?>

    
```php
