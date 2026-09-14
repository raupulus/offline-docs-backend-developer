---
title: do-while
source_url: https://www.php.net/manual/es/control-structures.do.while.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/do-while.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 53fb200fe
order: 2120
---

## do-while

Las bucles `do-while` se parecen mucho a las bucles `while`, pero la expresión es evaluada al final de cada iteración en lugar de al principio. La principal diferencia con respecto a la bucle `while` es que la primera iteración de la bucle `do-while` siempre se ejecuta (la expresión solo se evalúa al final de la iteración), lo cual no ocurre cuando se utiliza una bucle `while` (la condición se verifica al inicio de cada iteración, y si resulta `false` desde el principio, la bucle se detendrá de inmediato).

Solo existe una sintaxis posible para las bucles `do-while`:

```php
<?php
$i = 0;
do {
    echo $i;
} while ($i > 0);
?>

   
```

La bucle anterior solo se ejecutará una vez, ya que cuando la expresión es evaluada, resulta `false` (ya que la variable `$i` no es mayor que 0) y la ejecución de la bucle se detiene.

Los usuarios familiarizados con C están acostumbrados a un uso diferente de las bucles `do-while`, que permite detener la ejecución de la bucle en medio de las instrucciones, encapsulando en un `do-while`(0) la función [`break`](#control-structures.break). El siguiente código muestra un uso posible:

```php
<?php
do {
    if ($i < 5) {
        echo "i no es suficientemente grande";
        break;
    }
    $i *= $factor;
    if ($i < $minimum_limit) {
        break;
    }
    echo "i es bueno";

    /* ...procesamiento de i... */

} while (0);
?>

   
```

Es posible utilizar el operador [`goto`](#control-structures.goto) en lugar de este truco.
