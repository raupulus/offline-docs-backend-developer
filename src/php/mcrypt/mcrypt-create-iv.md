---
title: mcrypt_create_iv
description: Crea un vector de inicialización (IV) a partir de una fuente aleatoria
source_url: https://www.php.net/manual/es/function.mcrypt-create-iv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-create-iv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45700
---

mcrypt_create_iv

Crea un vector de inicialización (IV) a partir de una fuente aleatoria

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0.
>
> Las alternativas a esta función incluyen:
>
> <div data-wrapper="1" role="alternatives">
>
> random_bytes
>
> </div>

## Descripción

```php
mcrypt_create_iv(int $size, [int $source]): string
```php

`mcrypt_create_iv` crea un IV (vector de inicialización) a partir de una fuente aleatoria.

El vector de inicialización es el único medio de proporcionar una inicialización de reemplazo a los métodos de inicialización. Este vector no necesita ser particularmente secreto, aunque es mejor que lo sea. Puede enviarse con los documentos cifrados sin perder seguridad.

## Parámetros

`size`  
El tamaño del vector.

`source`  
La fuente de un IV. La fuente puede ser `MCRYPT_RAND` (el generador de números aleatorios del sistema), `MCRYPT_DEV_RANDOM` (lee los datos desde `/dev/random`) y `MCRYPT_DEV_URANDOM` (lee los datos desde `/dev/urandom`). Antes de la versión 5.3.0, `MCRYPT_RAND` era la única constante soportada por Windows.

Tenga en cuenta que el valor por defecto de este parámetro era `MCRYPT_DEV_RANDOM` antes de PHP 5.6.0.

> [!NOTE]
> Tenga en cuenta que la constante `MCRYPT_DEV_RANDOM` puede bloquearse mientras espera que haya más entropía disponible.

## Valores devueltos

Devuelve el vector de inicialización, o bien `false` en caso de error.

## Ejemplos

Ejemplo con `mcrypt_create_iv`

```
<?php
     $size = mcrypt_get_iv_size(MCRYPT_CAST_256, MCRYPT_MODE_CFB);
     $iv = mcrypt_create_iv($size, MCRYPT_DEV_RANDOM);
     ?>

  
```php

## Véase también

http://www.ciphersbyritter.com/GLOSSARY.HTM#IV

http://www.quadibloc.com/crypto/co0409.htm

Capítulo 9.3 de Applied Cryptography by Schneier (ISBN 0-471-11709-9)

random_bytes
