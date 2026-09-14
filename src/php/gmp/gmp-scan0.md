---
title: gmp_scan0
description: Escanear para 0
source_url: https://www.php.net/manual/es/function.gmp-scan0.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-scan0.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28770
---

gmp_scan0

Escanear para 0

## Descripción

```php
gmp_scan0(GMP $num1, int $start): int
```php

Escanea `num1`, empezando con el bit de `start`, hacia los bits mas significantes, hasta que el primero bit borrado es encontrado.

## Parámetros

`num1`  
El número a escanear.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`start`  
El inicio del bit.

## Valores devueltos

Devuelve el índice del bit encontrado, como un `int`. El índice inicia desde 0.

## Ejemplos

Ejemplo de `gmp_scan0`

```
<?php
// "0" el bit se encuentra en la posición 3. El índice inicia en 0
$s1 = gmp_init("10111", 2);
echo gmp_scan0($s1, 0) . "\n";

// "0" el bit se encuentra en la posición 7. El índice inicia en 5
$s2 = gmp_init("101110000", 2);
echo gmp_scan0($s2, 5) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    3
    7
