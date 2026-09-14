---
title: Ds\Sequence::apply
description: Actualiza todos los valores aplicando una retrollamada a cada valor
source_url: https://www.php.net/manual/es/ds-sequence.apply.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/apply.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: f94abc244
order: 15500
---

Ds\Sequence::apply

Actualiza todos los valores aplicando una retrollamada a cada valor

## Descripción

```php
abstract public Ds\Sequence::apply(callable $callback): void
```php

Actualiza todos los valores aplicando una `callback` a cada valor en la secuencia.

## Parámetros

`callback`  
```php
callback(mixed $value): mixed
```

Un `callable` a aplicar a cada valor del mapa.

La retrollamada debe devolver el valor por el cual debe ser reemplazado.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Sequence::apply`

```php
<?php
$sequence = new \Ds\Vector([1, 2, 3]);
$sequence->apply(function($value) { return $value * 2; });

print_r($sequence);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => 2
        [1] => 4
        [2] => 6
    )
