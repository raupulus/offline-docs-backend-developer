---
title: Comparación de tipos en PHP
source_url: https://www.php.net/manual/es/types.comparisons.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/comparisons.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 88890f831
order: 30
---

## Comparación de tipos en PHP

La tabla siguiente resume los diferentes comportamientos de PHP con los [tipos](#language.types) y [operadores de comparación](#language.operators.comparison), estricta o amplia. Esta tabla también está relacionada con el [transtipado](#language.types.type-juggling). Fue inspirada por diferentes comentarios de usuarios, y por el trabajo realizado en [BlueShoes](http://www.blueshoes.org/en/developer/php_cheat_sheet/).

Antes de utilizar estas tablas, es importante comprender los tipos y su significado. Por ejemplo, `"42"` es un `string`, mientras que `42` es un `int`. `false` es `bool` mientras que `"false"` es un `string`.

> [!NOTE]
> Los formularios HTML no conocen los enteros, números de coma flotante y otros booleanos. Para saber si una estructura es un entero, utilice `is_numeric`.

> [!NOTE]
> La línea `if ($x)` genera un error de nivel `E_NOTICE` cuando `$x` está indefinido. Alternativamente, utilice las funciones `empty` o `isset`, o inicialice todas sus variables.

> [!NOTE]
> Las operaciones numéricas pueden dar como resultado un valor representado por la constante `NAN`. Todas las comparaciones de este valor con cualquier otro valor, incluyendo el mismo valor, excepto `true` tendrán como resultado `false` (i.e. `NAN != NAN` y `NAN !== NAN`). Ejemplos de operaciones que producen el valor `NAN`: `sqrt(-1)`, `asin(2)`, y `acosh(0)`.

| Expresión            | `gettype` | `empty` | `is_null` | `isset` | `bool` : `if($x)` |
|----------------------|-----------|---------|-----------|---------|-------------------|
| `$x = "";`           | `string`  | `true`  | `false`   | `true`  | `false`           |
| `$x = null;`         | `NULL`    | `true`  | `true`    | `false` | `false`           |
| `var $x;`            | `NULL`    | `true`  | `true`    | `false` | `false`           |
| `$x` está indefinido | `NULL`    | `true`  | `true`    | `false` | `false`           |
| `$x = [];`           | `array`   | `true`  | `false`   | `true`  | `false`           |
| `$x = ['a', 'b'];`   | `array`   | `false` | `false`   | `true`  | `true`            |
| `$x = false;`        | `bool`    | `true`  | `false`   | `true`  | `false`           |
| `$x = true;`         | `bool`    | `false` | `false`   | `true`  | `true`            |
| `$x = 1;`            | `int`     | `false` | `false`   | `true`  | `true`            |
| `$x = 42;`           | `int`     | `false` | `false`   | `true`  | `true`            |
| `$x = 0;`            | `int`     | `true`  | `false`   | `true`  | `false`           |
| `$x = -1;`           | `int`     | `false` | `false`   | `true`  | `true`            |
| `$x = "1";`          | `string`  | `false` | `false`   | `true`  | `true`            |
| `$x = "0";`          | `string`  | `true`  | `false`   | `true`  | `false`           |
| `$x = "-1";`         | `string`  | `false` | `false`   | `true`  | `true`            |
| `$x = "php";`        | `string`  | `false` | `false`   | `true`  | `true`            |
| `$x = "true";`       | `string`  | `false` | `false`   | `true`  | `true`            |
| `$x = "false";`      | `string`  | `false` | `false`   | `true`  | `true`            |

Comparaciones de `$x` con funciones PHP

|  | `true` | `false` | `1` | `0` | `-1` | `"1"` | `"0"` | `"-1"` | `null` | `[]` | `"php"` | `""` |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `true` | `true` | `false` | `true` | `false` | `true` | `true` | `false` | `true` | `false` | `false` | `true` | `false` |
| `false` | `false` | `true` | `false` | `true` | `false` | `false` | `true` | `false` | `true` | `true` | `false` | `true` |
| `1` | `true` | `false` | `true` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` |
| `0` | `false` | `true` | `false` | `true` | `false` | `false` | `true` | `false` | `true` | `false` | `false`\* | `false`\* |
| `-1` | `true` | `false` | `false` | `false` | `true` | `false` | `false` | `true` | `false` | `false` | `false` | `false` |
| `"1"` | `true` | `false` | `true` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` |
| `"0"` | `false` | `true` | `false` | `true` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` |
| `"-1"` | `true` | `false` | `false` | `false` | `true` | `false` | `false` | `true` | `false` | `false` | `false` | `false` |
| `null` | `false` | `true` | `false` | `true` | `false` | `false` | `false` | `false` | `true` | `true` | `false` | `true` |
| `[]` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` | `true` | `true` | `false` | `false` |
| `"php"` | `true` | `false` | `false` | `false`\* | `false` | `false` | `false` | `false` | `false` | `false` | `true` | `false` |
| `""` | `false` | `true` | `false` | `false`\* | `false` | `false` | `false` | `false` | `true` | `false` | `false` | `true` |

Comparación amplia con `==` {#types.comparisions-loose}

\* `true` anterior a PHP 8.0.0.

|  | `true` | `false` | `1` | `0` | `-1` | `"1"` | `"0"` | `"-1"` | `null` | `[]` | `"php"` | `""` |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
| `true` | `true` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` |
| `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` |
| `1` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` |
| `0` | `false` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` |
| `-1` | `false` | `false` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` | `false` |
| `"1"` | `false` | `false` | `false` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `false` |
| `"0"` | `false` | `false` | `false` | `false` | `false` | `false` | `true` | `false` | `false` | `false` | `false` | `false` |
| `"-1"` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `true` | `false` | `false` | `false` | `false` |
| `null` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `true` | `false` | `false` | `false` |
| `[]` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `true` | `false` | `false` |
| `"php"` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `true` | `false` |
| `""` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `true` |

Comparación estricta con `===` {#type.comparisons-strict}
