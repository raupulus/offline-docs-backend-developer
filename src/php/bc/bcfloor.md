---
title: bcfloor
description: Redondea hacia abajo un número de precisión arbitraria
source_url: https://www.php.net/manual/es/function.bcfloor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcfloor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6270
---

bcfloor

Redondea hacia abajo un número de precisión arbitraria

## Descripción

```php
bcfloor(string $num): string
```php

Devuelve el valor entero inferior siguiente redondeando `num` si es necesario.

## 

## Valores devueltos

Devuelve una cadena numérica representando `num` redondeado hacia abajo al entero más cercano.

## Ejemplos

Ejemplo de `bcfloor`

```
<?php
var_dump(bcfloor('4.3'));
var_dump(bcfloor('9.999'));
var_dump(bcfloor('-3.14'));
?>

   
```php

El ejemplo anterior mostrará:

```
string(1) "4"
string(1) "9"
string(2) "-4"

   
```php

## Véase también

bcceil

bcround

BcMath\Number::floor
