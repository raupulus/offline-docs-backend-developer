---
title: gmp_scan1
description: Escanear para 1
source_url: https://www.php.net/manual/es/function.gmp-scan1.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-scan1.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28780
---

gmp_scan1

Escanear para 1

## Descripción

```php
gmp_scan1(GMP $num1, int $start): int
```php

Escanea `num1`, empezando con el bit de `start`, hacia los bits mas significantes, hasta que el primero bit establecido es encontrado.

## Parámetros

`num1`  
El número a escanear.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`start`  
El inicio del bit.

## Valores devueltos

Devuelve el índice del bit encontrado, como un `int`. Si el bit establecido no es encontrado, -1 se devuelto.

## Ejemplos

Ejemplo de `gmp_scan1`

```
<?php
// "1" el bit se encuentra en la posición 3. El índice inica en 0
$s1 = gmp_init("01000", 2);
echo gmp_scan1($s1, 0) . "\n";

// "1" el bit se encuentra en la posición 9. El índice inica en 5
$s2 = gmp_init("01000001111", 2);
echo gmp_scan1($s2, 5) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    3
    9
