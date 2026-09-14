---
title: ssdeep_fuzzy_hash_filename
description: Crea un hash difuso de un fichero
source_url: https://www.php.net/manual/es/function.ssdeep-fuzzy-hash-filename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssdeep/functions/ssdeep-fuzzy-hash-filename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssdeep
translation_status: ready
translation_revision: 2885123b1
order: 86370
---

ssdeep_fuzzy_hash_filename

Crea un hash difuso de un fichero

## Descripción

```php
ssdeep_fuzzy_hash_filename(string $file_name): string
```php

`ssdeep_fuzzy_hash_filename` calcula el hash del fichero especificado por `file_name` utilizando el [contexto desencadenado por trozos de hashing](http://dfrws.org/2006/proceedings/12-Kornblum.pdf), y devuelve el hash correspondiente.

## Parámetros

`file_name`  
El nombre del fichero a calcular el hash.

## Valores devueltos

Devuelve un `string` si tiene éxito, o `false` en caso contrario.
