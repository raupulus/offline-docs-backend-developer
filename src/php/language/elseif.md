---
title: elseif/else if
source_url: https://www.php.net/manual/es/control-structures.elseif.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/elseif.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 22583751f
order: 2140
---

## elseif/else if

`elseif`, como su nombre indica, es una combinación de `if` y de `else`. Como la expresión `else`, permite ejecutar una instrucción después de un `if` en el caso de que el "primer" `if` sea evaluado como `false`. Sin embargo, a diferencia de la expresión `else`, solo ejecutará la instrucción si la expresión condicional `elseif` es evaluada como `true`. El siguiente ejemplo mostrará `a es más grande que b`, `a es igual a b` o `a es más pequeño que b` :

```php
<?php
if ($a > $b) {
    echo "a es más grande que b";
} elseif ($a == $b) {
    echo "a es igual a b";
} else {
    echo "a es más pequeño que b";
}
?>

   
```

Es posible tener varios `elseif` que se sigan unos a otros, después de un `if` inicial. El primer `elseif` que sea evaluado como `true` será ejecutado. En PHP, es posible escribir `else if` en dos palabras y su comportamiento será idéntico al de `elseif` (en una sola palabra). La semántica de las dos expresiones es ligeramente diferente (al igual que en C), pero al final, el resultado será exactamente el mismo.

La expresión `elseif` es ejecutada solo si el `if` anterior y cualquier otro `elseif` anterior son evaluados como `false`, y que su `elseif` es evaluado como `true`.

> [!NOTE]
> Téngase en cuenta que `elseif` y `else if` son tratados de la misma manera solo cuando se utilizan llaves, como en el ejemplo anterior. Cuando se utiliza ":" para definir sus condiciones `if`/`elseif`, el uso de `elseif` en una sola palabra se vuelve necesario. PHP fallará con un error de análisis si se utiliza `else if`.

```php
<?php

/* Mala práctica: */
if ($a > $b):
    echo $a." es más grande que ".$b;
else if ($a == $b): // no compilará
    echo "La línea anterior provoca un error de interpretación";
endif;

   
```

```php
<?php

/* Buena práctica: */
if ($a > $b):
    echo $a." es más grande que ".$b;
elseif ($a == $b): // Las dos palabras están unidas
    echo $a." igual ".$b;
else:
    echo $a." es más grande o igual a ".$b;
endif;

?>

   
```
