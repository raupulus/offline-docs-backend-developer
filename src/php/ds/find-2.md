---
title: Ds\Sequence::find
description: Intenta encontrar el índice de un valor.
source_url: https://www.php.net/manual/es/ds-sequence.find.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/find.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15540
---

Ds\Sequence::find

Intenta encontrar el índice de un valor.

## Descripción

```php
abstract public Ds\Sequence::find(mixed $value): mixed
```php

Devuelve el índice del `valor`, o `false` si no se encuentra.

## Parámetros

`value`  
El valor a encontrar.

## Valores devueltos

El índice del valor, o `false` si no se encuentra.

> [!NOTE]
> Los valores serán comparados por valor y por tipo.

## Ejemplos

Ejemplo de `Ds\Sequence::find`

```
<?php
$sequence = new \Ds\Vector(["a", 1, true]);

var_dump($sequence->find("a")); // 0
var_dump($sequence->find("b")); // false
var_dump($sequence->find("1")); // false
var_dump($sequence->find(1));   // 1
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(0)
    bool(false)
    bool(false)
    int(1)
