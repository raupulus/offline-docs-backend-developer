---
title: exp
description: Calcula la exponencial de e
source_url: https://www.php.net/manual/es/function.exp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/exp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44640
---

exp

Calcula la exponencial de

e

## Descripción

```php
exp(float $num): float
```php

Devuelve `e`, elevado a la potencia `num`.

> [!NOTE]
> '`e`' es el logaritmo natural, o aproximadamente 2.718282.

## Parámetros

`num`  
El argumento a tratar

## Valores devueltos

'e', elevado a la potencia `num`.

## Ejemplos

Ejemplo con `exp`

```
<?php
echo exp(12), PHP_EOL;
echo exp(5.7);
?>

    
```php

El ejemplo anterior mostrará:

    162754.791419
    298.86740096706

## Véase también

`log`, `pow`
