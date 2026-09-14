---
title: opcache_compile_file
description: Compila y almacena en caché un script PHP sin ejecutarlo
source_url: https://www.php.net/manual/es/function.opcache-compile-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-compile-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: false
translation_revision: 87d6bb1bb
order: 58570
---

opcache_compile_file

Compila y almacena en caché un script PHP sin ejecutarlo

## Descripción

```php
opcache_compile_file(string $filename): bool
```php

Esta función compila un script PHP y lo añade a la caché de opcode sin ejecutarlo. Esto puede ser utilizado para llenar una caché después de un reinicio del servidor precargando los ficheros que van a ser utilizados.

## Parámetros

`filename`  
La ruta de acceso al fichero PHP a compilar y almacenar en caché.

## Valores devueltos

Devuelve `true` si `filename` ha sido compilado con éxito o `false` si ocurre un error.

## Errores/Excepciones

Si `filename` no puede ser cargado o compilado, se genera un error de tipo `E_WARNING`. Puede utilizarse [@](#language.operators.errorcontrol) para suprimirlo.

## Véase también

opcache_invalidate
