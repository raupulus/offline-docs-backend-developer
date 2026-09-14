---
title: Ds\Vector::map
description: Devuelve el resultado de la aplicación de una retrollamada a cada valor
source_url: https://www.php.net/manual/es/ds-vector.map.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/map.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16350
---

Ds\Vector::map

Devuelve el resultado de la aplicación de una retrollamada a cada valor

## Descripción

```php
public Ds\Vector::map(callable $callback): Ds\Vector
```php

Devuelve el resultado de la aplicación de una `callback` a cada valor del vector.

## Parámetros

`callback`  
```php
callback(mixed $value): mixed
```

Una `retrollamada` a aplicar a cada valor de la deque.

La retrollamada debe tomar un argumento y devolver el nuevo valor.

## Valores devueltos

El resultado de la aplicación de `callback` a cada valor del vector.

> [!NOTE]
> Los valores de la instancia actual no se verán afectados.

## Ejemplos

Ejemplo de `Ds\Vector::map`

```php
<?php
$vector = new \Ds\Vector([1, 2, 3]);

print_r($vector->map(function($value) { return $value * 2; }));
print_r($vector);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => 2
        [1] => 4
        [2] => 6
    )
    Ds\Vector Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
    )
