---
title: uopz_unset_mock
description: Suprime la simulación previamente fijada
source_url: https://www.php.net/manual/es/function.uopz-unset-mock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-unset-mock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99440
---

uopz_unset_mock

Suprime la simulación previamente fijada

## Descripción

```php
uopz_unset_mock(string $class): void
```php

Suprime la simulación previamente fijada para `class`.

## Parámetros

`class`  
El nombre de la clase simulada.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Una `RuntimeException` es lanzada si ninguna simulación ha sido previamente fijada para `class`.

## Ejemplos

Ejemplo de `uopz_unset_mock`

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
uopz_unset_mock(A::class);
A::who();
?>

   
```php

El ejemplo anterior mostrará:

    A

## Véase también

uopz_set_mock

uopz_get_mock
