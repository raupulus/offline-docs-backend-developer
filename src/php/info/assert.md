---
title: assert
description: Verifica una aserción
source_url: https://www.php.net/manual/es/function.assert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/assert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 2916fa416
order: 38730
---

assert

Verifica una aserción

## Descripción

```php
assert(mixed $assertion, [Throwable $description]): bool
```php

`assert` permite definir expectativas: aserciones que tienen efecto en los entornos de desarrollo y prueba, pero que están optimizadas para no tener costo en producción.

Las aserciones pueden ser utilizadas para ayudar en la depuración. Un caso de uso para las aserciones es servir como verificaciones de coherencia para precondiciones que deberían siempre ser `true`, y si no lo son, esto indica errores de programación. Otro caso de uso es garantizar la presencia de ciertas funcionalidades tales como funciones de extensión o ciertos límites y funcionalidades del sistema.

Como las aserciones pueden ser configuradas para ser eliminadas, no deben *ser* utilizadas para operaciones normales en tiempo de ejecución, tales como verificaciones de parámetros de entrada. En general, el código debe comportarse como se espera incluso si la verificación de aserciones está desactivada.

`assert` verificará que la expectativa dada en `assertion` sea satisfecha. Si no lo es y por lo tanto el resultado es `false`, tomará la acción apropiada según la configuración de `assert`.

El comportamiento de `assert` está dictado por los siguientes parámetros INI:

<table>
<caption>Assert Opciones de configuración</caption>
<thead>
<tr>
<th>Nombre</th>
<th>Por defecto</th>
<th>Descripción</th>
<th>Historial de cambios</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#ini.zend.assertions">zend.assertions</a></td>
<td><code>1</code></td>
<td><code>1</code> : genera y ejecuta el código (modo desarrollo), <code>0</code> : genera el código pero lo evita en tiempo de ejecución, <code>-1</code> : no genera el código (modo producción)</td>
<td></td>
</tr>
<tr>
<td><a href="#ini.assert.active">assert.active</a></td>
<td><code>true</code></td>
<td>Si <code>false</code>, <code>assert</code> no verifica la expectativa y siempre devuelve <code>true</code>, sin condición.</td>
<td>Deprecado a partir de PHP 8.3.0.</td>
</tr>
<tr>
<td><a href="#ini.assert.callback">assert.callback</a></td>
<td><code>null</code></td>
<td><p>Una función definida por el usuario a llamar cuando una aserción falla. Su firma debería ser:</p>
<p>```php
assert_callback(string $file, int $line, null $assertion, [string $description]): void
```</p></td>
<td><p>Anterior a PHP 8.0.0, la firma de la función de devolución de llamada debería ser:</p>
<p>```php
assert_callback(string $file, int $line, string $assertion, [string $description]): void
```</p>
<p>Deprecado a partir de PHP 8.3.0.</p></td>
</tr>
<tr>
<td><a href="#ini.assert.exception">assert.exception</a></td>
<td><code>true</code></td>
<td>Si <code>true</code>, lanzará una <code>AssertionError</code> si la expectativa no es cumplida.</td>
<td>Deprecado a partir de PHP 8.3.0.</td>
</tr>
<tr>
<td><a href="#ini.assert.bail">assert.bail</a></td>
<td><code>false</code></td>
<td>Si <code>true</code>, interrumpirá la ejecución del script PHP si la expectativa no es cumplida.</td>
<td>Deprecado a partir de PHP 8.3.0.</td>
</tr>
<tr>
<td><a href="#ini.assert.warning">assert.warning</a></td>
<td><code>true</code></td>
<td>Si <code>true</code>, emitirá un <code>E_WARNING</code> si la expectativa no es cumplida. Este parámetro INI es ineficaz si <a href="#ini.assert.exception">assert.exception</a> está activado.</td>
<td>Deprecado a partir de PHP 8.3.0.</td>
</tr>
</tbody>
</table>

## Parámetros

`assertion`  
Esta es cualquier expresión que devuelve un valor, que será ejecutada y cuyo resultado será utilizado para indicar si la aserción tuvo éxito o falló.

> [!WARNING]
> Anterior a PHP 8.0.0, si `assertion` era una `string`, era interpretada como código PHP y ejecutada vía `eval`. Esta cadena era pasada a la función de devolución de llamada como tercer argumento. Este comportamiento estaba *DEPRECADO* en PHP 7.2.0, y es *ELIMINADO* a partir de PHP 8.0.0

`description`  
Si `description` es una instancia de `Throwable`, será lanzada únicamente si `assertion` es ejecutada y falla.

> [!NOTE]
> A partir de PHP 8.0.0, esto se hace *antes* de llamar a la función de devolución de llamada de aserción eventualmente definida

> [!NOTE]
> A partir de PHP 8.0.0, el objeto `object` será lanzado independientemente de la configuración de [assert.exception](#ini.assert.exception).

> [!NOTE]
> A partir de PHP 8.0.0, el parámetro [assert.bail](#ini.assert.bail) no tiene ningún efecto en este caso.

Si `description` es una `string`, este mensaje será utilizado si se emite una excepción o advertencia. Una descripción opcional, que será incluida en el mensaje de fallo si la `assertion` falla.

Si `description` es omitido. Se crea una descripción por defecto equivalente al código fuente de la llamada a `assert` en tiempo de compilación.

## Valores devueltos

`assert` siempre devolverá `true` si al menos una de las siguientes condiciones es verdadera:

zend.assertions=0

zend.assertions=-1

assert.active=0

assert.exception=1

assert.bail=1

Un objeto de excepción personalizado es pasado a

description

.

Si ninguna de las condiciones es verdadera, `assert` devolverá `true` si `assertion` es verdadero, y `false` de lo contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Todas las configuraciones INI `assert.` han sido depreciadas. |
| 8.0.0 | La función `assert` ya no evaluará argumentos de tipo string, en su lugar, serán tratados como cualquier otro argumento. `assert($a == $b)` debería ser utilizado en lugar de `assert('$a == $b')`. La directiva `assert.quiet_eval` `php.ini` y la constante `ASSERT_QUIET_EVAL` también han sido eliminadas, ya que no tendrían ningún efecto. |
| 8.0.0 | Si `description` es una instancia de `Throwable`, el objeto es lanzado si la aserción falla, independientemente del valor de [assert.exception](#ini.assert.exception). |
| 8.0.0 | Si `description` es una instancia de `Throwable`, ninguna función de devolución de llamada de usuario es llamada incluso si está definida. |
| 8.0.0 | Declarar una función que se llame `assert()` dentro de un espacio de nombres ya no es permitido, y genera una `E_COMPILE_ERROR`. |
| 7.3.0 | Declarar una función que se llame `assert()` dentro de un espacio de nombres se ha depreciado. Tales declaraciones generan ahora una `E_DEPRECATED`. |
| 7.2.0 | El uso de una `string` como `assertion` se ha depreciado. Esto emite ahora una advertencia `E_DEPRECATED` cuando [assert.active](#ini.assert.active) y [zend.assertions](#ini.zend.assertions) están ambos definidos a `1`. |

## Ejemplos

Ejemplo de `assert`

```
<?php
assert(1 > 2);
echo '¡Hola!';
?>

    
```php

Si las aserciones están activadas ([`zend.assertions=1`](#ini.zend.assertions)) el ejemplo anterior mostraría:

    Fatal error: Uncaught AssertionError: assert(1 > 2) in example.php:2
    Stack trace:
    #0 example.php(2): assert(false, 'assert(1 > 2)')
    #1 {main}
      thrown in example.php on line 2

        

Si las aserciones están desactivadas (`zend.assertions=0` o `zend.assertions=-1`) el ejemplo anterior mostraría:

    ¡Hola!

Uso de un mensaje personalizado

```
<?php
assert(1 > 2, "Se esperaba que uno fuera mayor que dos");
echo '¡Hola!';
?>

    
```php

Si las aserciones están activadas, el ejemplo anterior mostraría: el ejemplo anterior mostraría:

    Fatal error: Uncaught AssertionError: Se esperaba que uno fuera mayor que dos in example.php:2
    Stack trace:
    #0 example.php(2): assert(false, 'Se esperaba que uno...')
    #1 {main}
      thrown in example.php on line 2

        

Si las aserciones están desactivadas, el ejemplo anterior mostraría: el ejemplo anterior mostraría:

    ¡Hola!

Uso de una clase de excepción personalizada

```
      
      <?php
      class ArithmeticAssertionError extends AssertionError {}

      assert(1 > 2, new ArithmeticAssertionError("Se esperaba que uno fuera mayor que dos"));
      echo '¡Hola!';
      
     
```php

Si las aserciones están activadas, el ejemplo anterior mostraría: el ejemplo anterior mostraría:

    Fatal error: Uncaught ArithmeticAssertionError: Se esperaba que uno fuera mayor que dos in example.php:4
    Stack trace:
    #0 {main}
      thrown in example.php on line 4

        

Si las aserciones están desactivadas, el ejemplo anterior mostraría:

    ¡Hola!

## Véase también

`assert_options`
