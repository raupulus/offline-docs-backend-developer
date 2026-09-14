---
title: Ds\Set::contains
description: Determina si el conjunto contiene todos los valores
source_url: https://www.php.net/manual/es/ds-set.contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 15810
---

Ds\Set::contains

Determina si el conjunto contiene todos los valores

## Descripción

```php
public Ds\Set::contains(mixed ...$values): bool
```php

Determina si el conjunto contiene todos los valores.

> [!NOTE]
> Los valores de tipo `object` son soportados. Si un objeto implementa `Ds\Hashable`, la igualdad será determinada por la función `equals` del objeto. Si un objeto no implementa `Ds\Hashable`, los objetos deben ser referencias a la misma instancia para ser considerados iguales.

> [!CAUTION]
> Todas las comparaciones son estrictas (tipo y valor).

## Parámetros

`values`  
Los valores a verificar.

## Valores devueltos

`false` si uno de los `valores` proporcionados no está en la secuencia, de lo contrario `true`.

## Ejemplos

Ejemplo de `Ds\Set::contains`

```
<?php
$set = new \Ds\Set([1, 2, 3]);

var_dump($set->contains(1));                // true
var_dump($set->contains(1, 2));             // true
var_dump($set->contains(...[1, 2]));        // true

var_dump($set->contains("1"));              // false
var_dump($set->contains(...[1, 2, 3, 4]));  // false

var_dump($set->contains(...[]));            // true
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    bool(true)
    bool(false)
    bool(false)
    bool(true)
