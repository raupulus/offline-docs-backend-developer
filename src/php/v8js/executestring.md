---
title: V8Js::executeString
description: Ejecuta un string como código Javascript
source_url: https://www.php.net/manual/es/v8js.executestring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/v8js/v8js/executestring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: v8js
translation_status: ready
translation_revision: c6e69f3a4
order: 100340
---

V8Js::executeString

Ejecuta un string como código Javascript

## Descripción

```php
public V8Js::executeString(string $script, [string $identifier], [int $flags]): mixed
```php

Compila y ejecuta el string pasado con `script` como código Javascript.

## Parámetros

`script`  
El string de código que a ejecutar.

`identifier`  
Identificador para el código ejecutado. Usado para depuración.

`flags`  
Flags de ejecución. Este valor debe ser una de las constantes `V8Js::FLAG_*`, y por omisión es `V8Js::FLAG_NONE`.

- `V8Js::FLAG_NONE` : ningún flag

- `V8Js::FLAG_FORCE_ARRAY` : fuerza a todos los objetos Javascript pasados a PHP a ser arrays asociativos

## Valores devueltos

Devuelve la última variable instanciada en el código Javascript, convertida en una variable PHP del tipo correspondiente.
