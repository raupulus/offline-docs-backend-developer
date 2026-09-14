---
title: mcrypt_generic_init
description: Inicializa todos los buffers necesarios
source_url: https://www.php.net/manual/es/function.mcrypt-generic-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-generic-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45840
---

mcrypt_generic_init

Inicializa todos los buffers necesarios

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_generic_init(resource $td, string $key, string $iv): int
```php

Se debe llamar a `mcrypt_generic_init` antes de cada llamada a `mcrypt_generic` o `mdecrypt_generic`.

## Parámetros

`td`  
El recurso de cifrado.

`key`  
El tamaño máximo de la clave debe ser el devuelto por `mcrypt_enc_get_key_size` y todos los valores inferiores también serán válidos.

`iv`  
El vector de inicialización (VI) debe tener el tamaño de un bloque, pero se debe leer su tamaño llamando a `mcrypt_enc_get_iv_size`. VI es ignorado en modo ECB. VI DEBE existir en modos `"CFB"`, `"CBC"`, `"STREAM"`, `"nOFB"` y `"OFB"`. Debe ser aleatorio y único (pero no secreto). El mismo VI debe ser utilizado para el cifrado y el descifrado. Si no se desea utilizar, se puede rellenar con ceros, pero no se recomienda.

## Valores devueltos

Devuelve un valor negativo en caso de error: -3 si el tamaño de la clave es incorrecto, -4 cuando hay un problema de asignación de memoria y cualquier otro valor en caso de error desconocido. Si ocurre un error, se muestra una alerta. `false` es devuelto si se pasan parámetros incorrectos a la función.

## Véase también

mcrypt_module_open
