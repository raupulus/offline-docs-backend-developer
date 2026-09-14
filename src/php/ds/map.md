---
title: Ds\Deque::map
description: Devuelve el resultado de la aplicación de una retrollamada a cada valor
source_url: https://www.php.net/manual/es/ds-deque.map.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/map.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14620
---

Ds\Deque::map

Devuelve el resultado de la aplicación de una retrollamada a cada valor

## Descripción

```php
public Ds\Deque::map(callable $callback): Ds\Deque
```php

Devuelve el resultado de la aplicación de `callback` a cada valor de la deque.

## Parámetros

`callback`  
```php
callback(mixed $value): mixed
```

Una `callable` a aplicar a cada valor de la deque.

La retrollamada debe tomar un argumento y devolver el nuevo valor.

## Valores devueltos

El resultado de la aplicación de `callback` a cada valor de la deque.

> [!NOTE]
> Los valores de la instancia actual no serán afectados.

## Ejemplos

Ejemplo de `Ds\Deque::map`

```php
<?php
$deque = new \Ds\Deque([1, 2, 3]);

print_r($deque->map(function($value) { return $value * 2; }));
print_r($deque);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => 2
        [1] => 4
        [2] => 6
    )
    Ds\Deque Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
    )
