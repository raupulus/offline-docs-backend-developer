---
title: Ds\Deque::insert
description: Inserta valores en un índice dado
source_url: https://www.php.net/manual/es/ds-deque.insert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/insert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 14570
---

Ds\Deque::insert

Inserta valores en un índice dado

## Descripción

```php
public Ds\Deque::insert(int $index, mixed ...$values): void
```php

Inserta valores en el deque en un índice dado.

## Parámetros

`index`  
Inserta en el índice dado. `0 <= index <= count`

> [!NOTE]
> Se puede insertar en el índice igual al número de valores.

`values`  
El o los valores a insertar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

`OutOfRangeException` si el índice no es válido.

## Ejemplos

Ejemplo de `Ds\Deque::insert`

```
<?php
$deque = new \Ds\Deque();

$deque->insert(0, "e");             // [e]
$deque->insert(1, "f");             // [e, f]
$deque->insert(2, "g");             // [e, f, g]
$deque->insert(0, "a", "b");        // [a, b, e, f, g]
$deque->insert(2, ...["c", "d"]);   // [a, b, c, d, e, f, g]

var_dump($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Deque)#1 (7) {
      [0]=>
      string(1) "a"
      [1]=>
      string(1) "b"
      [2]=>
      string(1) "c"
      [3]=>
      string(1) "d"
      [4]=>
      string(1) "e"
      [5]=>
      string(1) "f"
      [6]=>
      string(1) "g"
    }
