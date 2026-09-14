---
title: Ds\Set::remove
description: Elimina todos los valores dados de la secuencia
source_url: https://www.php.net/manual/es/ds-set.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 15960
---

Ds\Set::remove

Elimina todos los valores dados de la secuencia

## Descripción

```php
public Ds\Set::remove(mixed ...$values): void
```php

Elimina todos los `values` dados de la secuencia, ignorando aquellos que no están en la secuencia.

## Parámetros

`values`  
Los valores a eliminar.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Set::remove`

```
<?php
$set = new \Ds\Set([1, 2, 3, 4, 5]);

$set->remove(1);            // Elimina 1
$set->remove(1, 2);         // No encuentra 1, pero elimina 2
$set->remove(...[3, 4]);    // Elimina 3 y 4

var_dump($set);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#1 (1) {
      [0]=>
      int(5)
    }
