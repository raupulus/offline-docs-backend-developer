---
title: Sintaxis alternativa
source_url: https://www.php.net/manual/es/control-structures.alternative-syntax.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/alternative-syntax.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 22583751f
order: 2080
---

## Sintaxis alternativa

PHP ofrece otra manera de agrupar instrucciones dentro de un bloque, para las funciones de control `if`, `while`, `for`, `foreach` y `switch`. En cada caso, el principio es reemplazar la llave de apertura por dos puntos (:) y la llave de cierre por, respectivamente, `endif;`, `endwhile;`, `endfor;`, `endforeach;`, o `endswitch;`.

```php
<?php if ($a == 5): ?>
A igual 5
<?php endif; ?>

   
```

En el ejemplo anterior, el bloque HTML "A igual 5" se incluye dentro de un `if` utilizando esta nueva sintaxis. Este código HTML solo se mostrará si la variable `$a` es igual a 5.

Esta otra sintaxis también funciona con `else` y `elseif`. El siguiente ejemplo muestra una estructura con un `if`, un `elseif` y un `else` utilizando esta otra sintaxis:

```php
<?php
if ($a == 5):
    echo "a igual 5";
    echo "...";
elseif ($a == 6):
    echo "a igual 6";
    echo "!!!";
else:
    echo "a no vale ni 5 ni 6";
endif;
?>

   
```

> [!NOTE]
> No se puede utilizar diferentes sintaxis en el mismo bloque de control.

> [!WARNING]
> Cualquier visualización (incluyendo espacios) entre una estructura `switch` y el primer `case` producirá un error de sintaxis. Por ejemplo, esto no es válido:
>
> <div class="informalexample">
>
> ```
> <?php switch ($foo): ?>
>     <?php case 1: ?>
>     // ...
> <?php endswitch; ?>
>
>    
> ```
>
> </div>
>
> Mientras que esto es válido, ya que la última nueva línea después de la estructura `switch` se considera parte de la etiqueta de cierre `?>` y, por lo tanto, no se muestra nada entre `switch` y `case`:
>
> <div class="informalexample">
>
> ```
> <?php switch ($foo): ?>
> <?php case 1: ?>
>     ...
> <?php endswitch; ?>
>
>    
> ```
>
> </div>

Ver también [while](#control-structures.while), [for](#control-structures.for), y [if](#control-structures.if) para otros ejemplos.
