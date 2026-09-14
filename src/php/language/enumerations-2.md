---
title: Las enumeraciones
source_url: https://www.php.net/manual/es/language.types.enumerations.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/enumerations.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: f4609f913
order: 4420
---

## Las enumeraciones

## Las enumeraciones básicas

Las enumeraciones constituyen una capa restrictiva sobre las clases y las constantes de clase. Permiten definir un conjunto cerrado de valores posibles para un tipo.

```php
<?php
enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

function do_stuff(Suit $s)
{
    // ...
}

do_stuff(Suit::Spades);
?>

   
```

Para una descripción completa, ver el capítulo sobre [las enumeraciones](#language.enumerations).

## Conversión

Si una `enum` es convertida en `object`, no es modificada. Si una `enum` es convertida en `array`, un array con una sola clave `name` (para las Pure enums) o un array con las claves `name` y `value` (para las Backed enums) es creado. Todos los otros tipos de conversión resultarán en un error.
