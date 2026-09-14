---
title: Ds\Deque::find
description: Intenta encontrar el índice de un valor.
source_url: https://www.php.net/manual/es/ds-deque.find.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/find.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14540
---

Ds\Deque::find

Intenta encontrar el índice de un valor.

## Descripción

```php
public Ds\Deque::find(mixed $value): mixed
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

Ejemplo de `Ds\Deque::find`

```
<?php
$deque = new \Ds\Deque(["a", 1, true]);

var_dump($deque->find("a")); // 0
var_dump($deque->find("b")); // false
var_dump($deque->find("1")); // false
var_dump($deque->find(1));   // 1
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(0)
    bool(false)
    bool(false)
    int(1)
