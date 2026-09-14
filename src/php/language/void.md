---
title: Void
source_url: https://www.php.net/manual/es/language.types.void.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/void.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 50f76f269
order: 4570
---

## Void

`void` es un tipo de declaración de retorno que indica que la función no devuelve ningún valor, pero la función aún puede terminar. Por lo tanto, no puede formar parte de una [declaración de tipo unión](#language.types.type-system.composite.union). Disponible a partir de PHP 7.1.0.

> [!NOTE]
> Incluso si una función tiene un tipo de retorno `void`, seguirá devolviendo un valor; este valor siempre es `null`.

## Descartar un valor con `(void)`

La sintaxis `(void)` puede usarse para descartar explícitamente el resultado de una expresión. Esto es útil para indicar que ignorar un valor de retorno es intencional, especialmente al llamar a una función o método marcado con el atributo `NoDiscard`.

A diferencia de otros moldes, `(void)` no convierte el valor a otro tipo ni produce un valor. Es una sentencia y no puede usarse como parte de una expresión.

Descartar un valor de retorno

```php
    
<?php
#[\NoDiscard]
function process(): bool {
    return true;
}

(void) process(); // Descartar explícitamente el valor de retorno
?>

   
```
