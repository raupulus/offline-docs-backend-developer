---
title: ssdeep_fuzzy_hash
description: Crea un hash difuso desde un string
source_url: https://www.php.net/manual/es/function.ssdeep-fuzzy-hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssdeep/functions/ssdeep-fuzzy-hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssdeep
translation_status: ready
translation_revision: 2885123b1
order: 86380
---

ssdeep_fuzzy_hash

Crea un hash difuso desde un

string

## Descripción

```php
ssdeep_fuzzy_hash(string $to_hash): string
```php

`ssdeep_fuzzy_hash` calcula el hash de `to_hash` utilizando el [ contexto desencadenado por fragmentos de hashing](http://dfrws.org/2006/proceedings/12-Kornblum.pdf), y devuelve el hash correspondiente.

## Parámetros

`to_hash`  
El `string` de entrada

## Valores devueltos

Devuelve un `string` si tiene éxito, `false` en caso contrario.
