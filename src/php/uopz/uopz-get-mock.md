---
title: uopz_get_mock
description: Devuelve la simulación actual de una clase
source_url: https://www.php.net/manual/es/function.uopz-get-mock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-get-mock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99290
---

uopz_get_mock

Devuelve la simulación actual de una clase

## Descripción

```php
uopz_get_mock(string $class): mixed
```php

Devuelve la simulación actual de `class`.

## Parámetros

`class`  
El nombre de la clase simulada.

## Valores devueltos

O bien una cadena que contiene el nombre de la simulación, o bien un objeto, o bien `null` si ninguna simulación ha sido definida.

## Ejemplos

Ejemplo de `uopz_get_mock`

```
<?php
class A {
    public static function who() {
        echo "A";
    }
}

class mockA {
    public static function who() {
        echo "mockA";
    }
}

uopz_set_mock(A::class, mockA::class);
echo uopz_get_mock(A::class);
?>

   
```php

El ejemplo anterior mostrará:

    mockA

## Véase también

uopz_set_mock

uopz_unset_mock
