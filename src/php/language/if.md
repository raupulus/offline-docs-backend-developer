---
title: if
source_url: https://www.php.net/manual/es/control-structures.if.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/if.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 7104ee97c
order: 2180
---

## if

La instrucción `if` es una de las más importantes instrucciones de todos los lenguajes, PHP incluido. Permite la ejecución condicional de una parte de código. Las funcionalidades de la instrucción `if` son las mismas en PHP que en C :

    if (expression)
      commandes

Como se ha visto en el párrafo dedicado a las [expressions](#language.expressions), \<expression\> es convertida en su valor booléen. Si la \<expression\> vale `true`, PHP ejecutará la \<instruction\> y si vale `false`, la instrucción será ignorada. Más detalles sobre los valores que valen `false` están disponibles en la sección [Conversión en booléen](#language.types.boolean.casting).

El siguiente ejemplo muestra la frase `a es más grande que b` si `$a` es más grande que `$b` :

```php
<?php
if ($a > $b)
  echo "a es más grande que b";
?>

   
```

A menudo, se desea que varias instrucciones sean ejecutadas después de un desvío condicional. Por supuesto, no es obligatorio repetir la instrucción condicional `if` tantas veces como instrucciones se tengan que ejecutar. En su lugar, se pueden agrupar todas las instrucciones en un bloque. El siguiente ejemplo muestra `a es más grande que b`, si `$a` es más grande que `$b`, y luego asigna el valor de `$a` a la variable `$b` :

```php
<?php
if ($a > $b) {
  echo "a es más grande que b";
  $b = $a;
}
?>

   
```

Se pueden anidar indefinidamente instrucciones `if` dentro de otras instrucciones `if`, lo que permite una gran flexibilidad en la ejecución de una parte de código según un gran número de condiciones.
