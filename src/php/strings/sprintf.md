---
title: sprintf
description: Devuelve una string formateada
source_url: https://www.php.net/manual/es/function.sprintf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/sprintf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 89080
---

sprintf

Devuelve una string formateada

## Descripción

```php
sprintf(string $format, mixed ...$values): string
```php

Devuelve una string formateada, con el formato `format`, utilizando los argumentos `args`.

## Parámetros

`format`  
La cadena de formato está compuesta por cero o más directivas: caracteres ordinarios (excepto `%`) que se copian directamente al resultado y *especificaciones de conversión*, cada una con su propio parámetro.

Una especificación de conversión que sigue este prototipo: `%[argnum$][flags][width][.precision]specifier`.

Argnum

Un `int` seguido de un signo dólar `$`, para especificar qué número de argumento tratar en la conversión.

Banderas

| Bandera | Descripción |
|----|----|
| `-` | Justifica el texto a la izquierda dado el ancho del campo; la justificación a la derecha es el comportamiento predeterminado. |
| `+` | Prefija los números positivos con un signo más `+`; por defecto solo los números negativos son prefijados con un signo negativo. |
| ``(espacio) | Rellena el resultado con espacios. Esto es por defecto. |
| `0` | Rellena solo los números a la izquierda con ceros. Con el especificador `s` esto también puede rellenar a la derecha con ceros. |
| `'`(char) | Rellena el resultado con el carácter (char). |

Ancho

Sea un entero indicando el número de caracteres (mínimo) que esta conversión debe producir, o `*`. Si `*` es utilizado, entonces el ancho es proporcionado como un valor entero adicional precediendo al que se formatea por el especificador.

Precisión

Un punto `.` seguido opcionalmente sea de un entero, o de `*`, cuya significación depende del especificador:

- Para los especificadores `e`, `E`, `f` y `F` : esto es el número de dígitos a mostrar después de la coma (por defecto, esto es 6).

- Para los especificadores `g`, `G`, `h` y `H` : esto es el número máximo de dígitos significativos a mostrar.

- Para el especificador `s`: actúa como un punto de corte, definiendo un límite máximo de caracteres de la cadena.

> [!NOTE]
> Si el punto es especificado sin un valor explícito para la precisión, 0 es asumido. Si `*` es utilizado, la precisión es proporcionada como un valor entero adicional precediendo al que se formatea por el especificador.

<table>
<caption>Especificadores</caption>
<thead>
<tr>
<th>Especificador</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>%</code></td>
<td>Un carácter de porcentaje literal. No se necesita ningún argumento.</td>
</tr>
<tr>
<td><code>b</code></td>
<td>El argumento es tratado como un entero y presentado como un número binario.</td>
</tr>
<tr>
<td><code>c</code></td>
<td>El argumento es tratado como un entero y presentado como el carácter de código ASCII correspondiente.</td>
</tr>
<tr>
<td><code>d</code></td>
<td>El argumento es tratado como un entero y presentado como un número entero decimal (firmado).</td>
</tr>
<tr>
<td><code>e</code></td>
<td>El argumento es tratado como una notación científica (ej. 1.2e+2).</td>
</tr>
<tr>
<td><code>E</code></td>
<td>Como el especificador <code>e</code> pero utiliza una letra mayúscula (por ejemplo 1.2E+2).</td>
</tr>
<tr>
<td><code>f</code></td>
<td>El argumento es tratado como un número de coma flotante (tipo <code>float</code>) y presentado como un número de coma flotante (teniendo en cuenta la configuración local).</td>
</tr>
<tr>
<td><code>F</code></td>
<td>El argumento es tratado como un número de coma flotante (tipo <code>float</code>) y presentado como un número de coma flotante (sin tener en cuenta la configuración local).</td>
</tr>
<tr>
<td><code>g</code></td>
<td><p>Formato general.</p>
<p>Sea P igual a la precisión si diferente de 0, 6 si la precisión es omitida o 1 si la precisión es cero. Entonces, si la conversión con el estilo E tuviera como exponente X:</p>
<p>Si P &gt; X ≥ −4, la conversión es con estilo f y precisión P − (X + 1). De lo contrario, la conversión es con el estilo e y precisión P - 1.</p></td>
</tr>
<tr>
<td><code>G</code></td>
<td>Como el especificador <code>g</code> pero utiliza <code>E</code> y <code>f</code>.</td>
</tr>
<tr>
<td><code>h</code></td>
<td>Como el especificador <code>g</code> pero utiliza <code>F</code>. Disponible a partir de PHP 8.0.0.</td>
</tr>
<tr>
<td><code>H</code></td>
<td>Como el especificador <code>g</code> pero utiliza <code>E</code> y <code>F</code>. Disponible a partir de PHP 8.0.0.</td>
</tr>
<tr>
<td><code>o</code></td>
<td>El argumento es tratado como un entero y presentado como un número octal.</td>
</tr>
<tr>
<td><code>s</code></td>
<td>El argumento es tratado y presentado como una cadena de caracteres.</td>
</tr>
<tr>
<td><code>u</code></td>
<td>El argumento es tratado como un entero y presentado como un número decimal no firmado.</td>
</tr>
<tr>
<td><code>x</code></td>
<td>El argumento es tratado como un entero y presentado como un número hexadecimal (las letras en minúsculas).</td>
</tr>
<tr>
<td><code>X</code></td>
<td>El argumento es tratado como un entero y presentado como un número hexadecimal (las letras en mayúsculas).</td>
</tr>
</tbody>
</table>

> [!WARNING]
> El especificador de tipo `c` ignora el alineamiento y el tamaño.

> [!WARNING]
> Intentar utilizar una combinación de una cadena y especificadores con juegos de caracteres que necesitan más de un octeto por carácter dará un resultado inesperado.

Las variables serán forzadas a un tipo apropiado para el especificador:

| Tipo     | Especificadores                        |
|----------|----------------------------------------|
| `string` | `s`                                    |
| `int`    | `d`, `u`, `c`, `o`, `x`, `X`, `b`      |
| `float`  | `e`, `E`, `f`, `F`, `g`, `G`, `h`, `H` |

Manejo de tipos

`values`  

## Valores devueltos

Devuelve una `string` creada siguiendo el formato `format`.

## Errores/Excepciones

A partir de PHP 8.0.0, se lanza una `ValueError` si el número de argumentos es nulo. Anterior a PHP 8.0.0, se emitía un `E_WARNING` en su lugar.

A partir de PHP 8.0.0, se lanza una `ValueError` si `[width]` es inferior a cero o superior a `PHP_INT_MAX`. Anterior a PHP 8.0.0, se emitía un `E_WARNING` en su lugar.

A partir de PHP 8.0.0, se lanza una `ValueError` si `[precision]` es inferior a cero o superior a `PHP_INT_MAX`. Anterior a PHP 8.0.0, se emitía un `E_WARNING` en su lugar.

A partir de PHP 8.0.0, se lanza una `ArgumentCountError` cuando se proporcionan menos argumentos de los requeridos. Anterior a PHP 8.0.0, se devolvía `false` y se emitía un `E_WARNING` en su lugar.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ya no devuelve `false` en caso de fallo. |
| 8.0.0 | Lanza una `ValueError` si el número de argumentos es cero; anteriormente, esta función emitía un `E_WARNING`. |
| 8.0.0 | Lanza una `ValueError` si `[width]` es inferior a cero o superior a `PHP_INT_MAX`; anteriormente, esta función emitía un `E_WARNING`. |
| 8.0.0 | Lanza una `ValueError` si `[precision]` es inferior a cero o superior a `PHP_INT_MAX`; anteriormente, esta función emitía un `E_WARNING`. |
| 8.0.0 | Lanza una `ArgumentCountError` cuando se proporcionan menos argumentos de los requeridos; anteriormente, esta función emitía un `E_WARNING`. |

## Ejemplos

Intercambio de argumentos

La string de formato soporta la numeración y el intercambio de argumentos.

```
<?php
$num = 5;
$location = 'bananero';

$format = 'Hay %d monos en el %s';
echo sprintf($format, $num, $location);
?>

   
```php

El ejemplo anterior mostrará:

    Hay 5 monos en el bananero

Pero imagine que la string de formato sea creada en un script separado, como una biblioteca: esto ocurre cuando se debe internacionalizar una aplicación. Según el idioma, puede que sea necesario escribir:

Orden incorrecto de los argumentos

La string de formato soporta la numeración y el intercambio de argumentos.

```
<?php
$num = 5;
$location = 'árbol';
$format = 'El %s tiene %d monos';

echo sprintf($format, $num, $location);
?>

   
```php

Ahora tenemos un problema. El orden de los argumentos ha sido cambiado, y ya no corresponde al orden de los argumentos en el script PHP. Se desea dejar el código PHP intacto, pero simplemente indicar en la string de formato el orden en el que los argumentos deben ser utilizados. La string de formato puede ser reescrita así:

Uso del marcador de orden

```
<?php
$num = 5;
$location = 'árbol';

$format = 'El %2$s tiene %1$d monos';
echo sprintf($format, $num, $location);
?>

  
```php

Una de las ventajas es que los parámetros ficticios pueden ser repetidos sin añadir más argumentos en el código.

Repetición del marcador

```
<?php
$format = 'El %2$s tiene %1$d monos.
           Es un hermoso %2$s con %1$d monos.';
echo sprintf($format, $num, $location);
?>

   
```php

Al utilizar el mecanismo de intercambio de argumentos, el *especificador de posición* `n$` debe ocurrir inmediatamente después del signo de porcentaje(`%`), antes de cualquier otro especificador, como en el siguiente ejemplo.

Especificación del carácter de relleno

```
<?php
echo sprintf("%'.9d\n", 123);
echo sprintf("%'.09d\n", 123);
?>

   
```php

El ejemplo anterior mostrará:

    ......123
    000000123

Especificador de posición con otros especificadores

```
<?php
$format = 'El %2$s contiene %1$04d monos';
echo sprintf($format, $num, $location);
?>

   
```php

El ejemplo anterior mostrará:

    El árbol contiene 0005 monos

`sprintf`: entero sin espacios

```
<?php
$year = 2005;
$month = 5;
$day = 6;

$isodate = sprintf("%04d-%02d-%02d", $year, $month, $day);
echo $isodate;
?>

   
```php

`sprintf`: formateo de divisas

```
<?php
$money1 = 68.75;
$money2 = 54.35;
$money = $money1 + $money2;
echo $money, PHP_EOL;

$formatted = sprintf("%01.2f", $money);
echo $formatted, PHP_EOL;
?>

   
```php

El ejemplo anterior mostrará:

    123.1
    123.10

`sprintf`: notación científica

```
<?php
$number = 362525200;

echo sprintf("%.3e", $number), PHP_EOL;
?>

   
```php

El ejemplo anterior mostrará:

    3.625e+8

## Véase también

`printf`, `fprintf`, `vprintf`, `vsprintf`, `vfprintf`, `sscanf`, `fscanf`, `number_format`, `date`
