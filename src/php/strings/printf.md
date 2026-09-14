---
title: printf
description: Muestra una string formateada
source_url: https://www.php.net/manual/es/function.printf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/printf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 49999607f
order: 88980
---

printf

Muestra una string formateada

## Descripción

```php
printf(string $format, mixed ...$values): int
```php

Produce una salida de acuerdo con `format`.

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

Devuelve la longitud de la string mostrada.

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

`printf`: varios ejemplos

```
<?php
$n =  43951789;
$u = -43951789;
$c = 65; // ASCII 65 es 'A'

// note el doble %%, esto muestra un carácter '%' literal
printf("%%b = '%b'\n", $n); // representación binaria
printf("%%c = '%c'\n", $c); // muestra el carácter ascii, como la función chr()
printf("%%d = '%d'\n", $n); // representación estándar de un integer
printf("%%e = '%e'\n", $n); // notación científica
printf("%%u = '%u'\n", $n); // representación de integer sin signo de un integer positivo
printf("%%u = '%u'\n", $u); // representación de integer sin signo de un integer negativo
printf("%%f = '%f'\n", $n); // representación en coma flotante
printf("%%o = '%o'\n", $n); // representación octal
printf("%%s = '%s'\n", $n); // representación string
printf("%%x = '%x'\n", $n); // representación hexadecimal (minúscula)
printf("%%X = '%X'\n", $n); // representación hexadecimal (mayúscula)

printf("%%+d = '%+d'\n", $n); // indicación del signo para un integer positivo
printf("%%+d = '%+d'\n", $u); // indicación del signo para un integer negativo
?>

    
```php

El ejemplo anterior mostrará:

    %b = '10100111101010011010101101'
    %c = 'A'
    %d = '43951789'
    %e = '4.39518e+7'
    %u = '43951789'
    %u = '4251015507'
    %f = '43951789.000000'
    %o = '247523255'
    %s = '43951789'
    %x = '29ea6ad'
    %X = '29EA6AD'
    %+d = '+43951789'
    %+d = '-43951789'

`printf`: especificadores de strings

```
<?php
$s = 'monkey';
$t = 'many monkeys';

printf("[%s]\n",        $s); // muestra de una string estándar
printf("[%10s]\n",      $s); // alineación a la derecha con espacios
printf("[%-10s]\n",     $s); // alineación a la izquierda con espacios
printf("[%010s]\n",     $s); // el espaciado nulo funciona también en strings
printf("[%'#10s]\n",    $s); // uso del carácter personalizado de separación '#'
printf("[%'#*s]\n", 10, $s); // Proporcionar el ancho de alineación como argumento adicional
printf("[%10.9s]\n",    $t); // alineación a la derecha pero con corte a 8 caracteres
printf("[%-10.9s]\n",   $t); // alineación a la izquierda pero con corte a 8 caracteres
?>

    
```php

El ejemplo anterior mostrará:

    [monkey]
    [    monkey]
    [monkey    ]
    [0000monkey]
    [####monkey]
    [####monkey]
    [ many monk]
    [many monk ]

## Véase también

`print`, `sprintf`, `fprintf`, `vprintf`, `vsprintf`, `vfprintf`, `sscanf`, `fscanf`, `number_format`, `date`, `flush`
