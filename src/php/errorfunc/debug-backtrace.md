---
title: debug_backtrace
description: Genera el contexto de depuración
source_url: https://www.php.net/manual/es/function.debug-backtrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/debug-backtrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: true
translation_revision: a8dfc2c06
order: 17590
---

debug_backtrace

Genera el contexto de depuración

## Descripción

```php
debug_backtrace([int $options], [int $limit]): array
```php

`debug_backtrace` genera un contexto de depuración PHP.

## Parámetros

`options`  
Este argumento es una máscara de las siguientes opciones:

|  |  |
|----|----|
| DEBUG_BACKTRACE_PROVIDE_OBJECT | Si se debe o no poblar el índice "object". |
| DEBUG_BACKTRACE_IGNORE_ARGS | Si se debe o no omitir el índice "args" y por lo tanto todos los argumentos de la función/método para ahorrar memoria. |

Opciones para la función `debug_backtrace`

> [!NOTE]
> Existen cuatro combinaciones posibles:
>
> <table>
> <caption>Opciones de <code>debug_backtrace</code></caption>
> <tbody>
> <tr>
> <td><code>debug_backtrace()</code></td>
> <td rowspan="2">Rellena los dos índices</td>
> </tr>
> <tr>
> <td><code>debug_backtrace(DEBUG_BACKTRACE_PROVIDE_OBJECT)</code></td>
> </tr>
> <tr>
> <td><code>debug_backtrace(~DEBUG_BACKTRACE_PROVIDE_OBJECT)</code></td>
> <td rowspan="2">Omite el índice <code>"object"</code> y rellena el índice <code>"args"</code>.</td>
> </tr>
> <tr>
> <td><code>debug_backtrace(0)</code></td>
> </tr>
> <tr>
> <td><code>debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS)</code></td>
> <td rowspan="2">Omite <em>ambos</em> el índice <code>"object"</code> <em>y</em> el índice <code>"args"</code>.</td>
> </tr>
> <tr>
> <td><code>debug_backtrace(~DEBUG_BACKTRACE_PROVIDE_OBJECT | DEBUG_BACKTRACE_IGNORE_ARGS)</code></td>
> </tr>
> <tr>
> <td><code>debug_backtrace(DEBUG_BACKTRACE_PROVIDE_OBJECT|DEBUG_BACKTRACE_IGNORE_ARGS)</code></td>
> <td>Rellena el índice <code>"object"</code> <em>y</em> omite el índice <code>"args"</code>.</td>
> </tr>
> </tbody>
> </table>

`limit`  
Este argumento puede ser utilizado para limitar el número de marcos en la pila devuelta. Por omisión (`limit`=`0`), la función devuelve todos los marcos de la pila.

## Valores devueltos

Devuelve un array de arrays asociativos. Los elementos de retorno posibles son los siguientes:

| Nombre | Tipo | Descripción |
|----|----|----|
| function | `string` | El nombre de la función actual. Ver también [\_\_FUNCTION\_\_](#language.constants.magic). |
| line | `int` | El número de línea actual. Ver también [\_\_LINE\_\_](#language.constants.magic). |
| file | `string` | El nombre del fichero actual. Ver también [\_\_FILE\_\_](#language.constants.magic). |
| class | `string` | El nombre de la [clase](#language.oop5) actual. Ver también [\_\_CLASS\_\_](#language.constants.magic). |
| object | `object` | El [objeto](#language.oop5) actual si `DEBUG_BACKTRACE_PROVIDE_OBJECT` es proporcionado. |
| type | `string` | El tipo de clase actual. Si un método es llamado, "-\>" es devuelto. Si un método estático es llamado, "::" es devuelto. Si una función es llamada, nada será devuelto. |
| args | `array` | Si dentro de una función, esto lista los argumentos. Si en un fichero incluido, esto lista los ficheros incluidos. A menos que `DEBUG_BACKTRACE_IGNORE_ARGS` sea proporcionado. |

Elementos posibles de retorno de la función `debug_backtrace`

## Ejemplos

Ejemplo con `debug_backtrace`

```
<?php
// filename: /tmp/a.php

function a_test($str)
{
  echo "\nHi: $str";
  var_dump(debug_backtrace());
}

a_test('friend');
?>

<?php
// filename: /tmp/b.php
include_once '/tmp/a.php';
?>

    
```php

Resultado de la ejecución de `/tmp/b.php`:

    Hi: friend
    array(2) {
      [0]=>
        array(4) {
          ["file"] => string(10) "/tmp/a.php"
          ["line"] => int(10)
          ["function"] => string(6) "a_test"
          ["args"]=>
            array(1) {
              [0] => &string(6) "friend"
            }
        }
      [1]=>
        array(4) {
          ["file"] => string(10) "/tmp/b.php"
          ["line"] => int(2)
          ["args"] =>
            array(1) {
              [0] => string(10) "/tmp/a.php"
            }
          ["function"] => string(12) "include_once"
        }
    }

## Véase también

`trigger_error`, `debug_print_backtrace`
