---
title: gnupg_setarmor
description: Cambia la salida blindada
source_url: https://www.php.net/manual/es/function.gnupg-setarmor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-setarmor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29160
---

gnupg_setarmor

Cambia la salida blindada

## Descripción

```php
gnupg_setarmor(resource $identifier, int $armor): bool
```php

Cambia la salida blindada.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`armor`  
Pase un valor entero diferente de cero a esta función para activar la salida blindada (valor por omisión). Pase 0 para desactivar la salida blindada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `gnupg_setarmor` (Estilo procedimental)

```
<?php
$res = gnupg_init();
gnupg_setarmor($res,1); // Activa la salida blindada;
gnupg_setarmor($res,0); // Desactiva la salida blindada;
?>

    
```php

Ejemplo con `gnupg_setarmor` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$gpg->setarmor(1); // Activa la salida blindada;
$gpg->setarmor(0); // Desactiva la salida blindada;
?>

    
```php
