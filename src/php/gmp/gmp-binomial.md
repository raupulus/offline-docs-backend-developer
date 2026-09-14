---
title: gmp_binomial
description: Calcula el coeficiente binomial
source_url: https://www.php.net/manual/es/function.gmp-binomial.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-binomial.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: 039ab719e
order: 28380
---

gmp_binomial

Calcula el coeficiente binomial

## Descripción

```php
gmp_binomial(GMP $n, int $k): GMP
```php

Calcula el coeficiente binomial C(n, k).

## Parámetros

`n`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`k`  

## Valores devueltos

Retorna el coeficiente binomial C(n, k).

## Errores/Excepciones

Lanza una `ValueError` si `k` es negativo. Anterior a PHP 8.0.0, se emitía `E_WARNING` en su lugar.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.0.0   | Esta función ya no retorna `false` en caso de fallo. |
