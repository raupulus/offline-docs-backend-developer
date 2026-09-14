---
title: while
source_url: https://www.php.net/manual/es/control-structures.while.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/while.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 7104ee97c
order: 2260
---

## while

La estructura de control `while` es la forma más simple de implementar un bucle en PHP. Esta estructura se comporta de la misma manera que en C. El ejemplo más simple de un bucle `while` es el siguiente :

    while (expression)
        comandos

El significado de un bucle `while` es muy simple. PHP ejecuta la instrucción mientras que la expresión del bucle `while` es evaluada como `true`. El valor de la expresión es verificado al inicio de cada bucle, y, si el valor cambia durante la ejecución de la instrucción, la ejecución no se detendrá hasta el final de la iteración (cada vez que PHP ejecuta la instrucción, se llama una iteración). Si la expresión del `while` es `false` antes de la primera iteración, la instrucción nunca será ejecutada.

Al igual que con el `if`, se pueden agrupar varias instrucciones en el mismo bucle `while` agrupándolas dentro de llaves o utilizando la siguiente sintaxis :

    while (expression):
        comandos
        ...
    endwhile;

Los siguientes ejemplos son idénticos y muestran todos los números de 1 hasta 10 :

```php
<?php
/* ejemplo 1 */

$i = 1;
while ($i <= 10) {
    echo $i++;  /* El valor mostrado es $i antes del incremento
                   (post-incremento)  */
}

/* ejemplo 2 */

$i = 1;
while ($i <= 10):
    echo $i;
    $i++;
endwhile;
?>

   
```
