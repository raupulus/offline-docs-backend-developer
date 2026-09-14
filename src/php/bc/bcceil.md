---
title: bcceil
description: Redondea al alza un número de precisión arbitraria
source_url: https://www.php.net/manual/es/function.bcceil.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcceil.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6230
---

bcceil

Redondea al alza un número de precisión arbitraria

## Descripción

```php
bcceil(string $num): string
```php

Devuelve el valor entero superior redondeando `num` si es necesario.

## Parámetros

`num`  
El valor a redondear.

## Valores devueltos

Devuelve un string numérico representando `num` redondeado al alza al entero más cercano.

## Errores/Excepciones

Esta función lanza una ValueError si `num` no es un string numérico BCMath bien formado.

## Ejemplos

Ejemplo de `bcceil`

```
<?php
var_dump(bcceil('4.3'));
var_dump(bcceil('9.999'));
var_dump(bcceil('-3.14'));
?>

   
```php

El ejemplo anterior mostrará:

```
string(1) "5"
string(2) "10"
string(2) "-3"

   
```php

## Véase también

bcfloor

bcround

BcMath\Number::ceil
