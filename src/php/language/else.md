---
title: else
source_url: https://www.php.net/manual/es/control-structures.else.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/else.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 690c3ea7c
order: 2130
---

## else

A menudo, se desea ejecutar una sentencia si una condición se cumple y otra sentencia si esta condición no se cumple. Para esto se utiliza `else`. `else` funciona después de un `if` y ejecuta las sentencias correspondientes en caso de que la expresión del `if` sea `false`. En el siguiente ejemplo, este fragmento de código muestra `a es más grande que b` si la variable `$a` es más grande que la variable `$b`, y `a es más pequeño que b` en caso contrario:

```php
<?php
if ($a > $b) {
  echo "a es más grande que b";
} else {
  echo "a es más pequeño que b";
}
?>

   
```

Las sentencias después del `else` solo se ejecutan si la expresión del `if` es `false`, y si existen expresiones `elseif` - solo si también se evalúan como `false` (ver [elseif](#control-structures.elseif)).

> [!NOTE]
> En el caso de sentencias `if`-`else` anidadas, un `else` siempre se asocia con el `if` más cercano.
>
> <div class="informalexample">
>
> ```
> <?php
> $a = false;
> $b = true;
> if ($a)
>     if ($b)
>         echo "b";
> else
>     echo "c";
> ?>
>
>     
> ```
>
> </div>
>
> A pesar de la indentación (que no tiene importancia en PHP), el `else` se asocia con el `if ($b)`, por lo que este ejemplo no produce ninguna salida. Aunque apoyarse en este comportamiento es válido, se recomienda evitarlo utilizando llaves para resolver cualquier posible ambigüedad.
