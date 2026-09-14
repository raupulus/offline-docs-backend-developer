---
title: money_format
description: Formatea un número como valor monetario
source_url: https://www.php.net/manual/es/function.money-format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/money-format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 06313c3bb
order: 88910
---

money_format

Formatea un número como valor monetario

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
money_format(string $format, float $number): string
```php

`money_format` devuelve una versión formateada del número `number`. Esta función actúa como interfaz con la función `strfmon` de la biblioteca C, con la diferencia de que esta implementación solo convierte un número a la vez.

## Parámetros

`format`  
El parámetro de formato consta de la siguiente secuencia:

- un carácter `%`

- una configuración opcional

- un tamaño de campo opcional

- una precisión izquierda opcional

- una precisión derecha opcional

- un carácter de conversión obligatorio

Flags

Se puede utilizar una o más de las siguientes configuraciones:

`=`\<f\>  
El carácter `=` seguido de un byte único \<f\> que se utilizará como carácter de relleno. El carácter de relleno predeterminado es espacio.

`^`  
Desactiva el agrupamiento de caracteres (tal como se define en la configuración local).

`+` o `(`  
Especifica el estilo de formato para números positivos y negativos. Si se utiliza `+`, se usarán los equivalentes en la configuración local de `+` y `-`. Si se utiliza `(`, las sumas negativas se colocarán entre paréntesis. Si no se proporciona ninguna especificación, el valor predeterminado es `+`.

`!`  
Suprime el símbolo monetario en la cadena final.

`-`  
Si se proporciona, esta configuración hace que los campos se justifiquen a la izquierda (rellenados a la derecha), en contraste con la configuración predeterminada que está justificada a la derecha y rellenada a la izquierda.

Tamaño del campo

\<w\>  
Un número decimal que especifica el tamaño mínimo del campo. El campo se rellenará a la izquierda, a menos que se utilice la configuración `-`. Por defecto, este valor es 0.

Precisión izquierda

`#`\<n\>  
El número máximo de dígitos (\<n\>) esperados a la izquierda del separador decimal (por ejemplo, la coma). Esta opción se utiliza generalmente para mantener el alineamiento de columnas de números, utilizando un carácter para rellenar el número si este tiene menos de \<n\> dígitos. Si el número real de dígitos es mayor que \<n\>, esta especificación se ignora.

Si el agrupamiento no ha sido desactivado mediante la configuración `^`, los separadores de agrupamiento se insertarán antes del carácter de relleno (si corresponde). Los separadores no se aplicarán a los caracteres de relleno, incluso si este carácter es un número.

Para garantizar el alineamiento, todos los caracteres que aparecen antes y después del número formateado, como los símbolos monetarios o los signos negativo y positivo, se colocarán en el mismo lugar mediante espacios adicionales, de modo que todos los tamaños de los números sean iguales.

Precisión derecha

`.`\<p\>  
Un punto seguido de un número de decimales (\<p\>). Si el valor de \<p\> es 0 (cero), el separador decimal y los decimales se eliminarán. Si no se especifica ninguna precisión derecha, el valor predeterminado se leerá en la configuración local. El número formateado se redondeará para satisfacer las restricciones de visualización.

Caracteres de conversión

`i`  
El número se formatea según el formato monetario internacional de la configuración local (por ejemplo, para Francia: 1 234,56 F).

`n`  
El número se formatea según el formato monetario nacional (por ejemplo, para la configuración `de_DE`: `EU1.234,56`).

`%`  
Devuelve el carácter `%`.

`number`  
El número a formatear.

## Valores devueltos

Devuelve la cadena formateada. Los caracteres antes y después de la cadena formateada se devolverán sin cambios. Un valor no numérico para `number` devuelve `null` y emite una advertencia `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ha sido eliminada. |
| 7.4.0 | Esta función está obsoleta. Utilizar NumberFormatter::formatCurrency en su lugar. |

## Ejemplos

Ejemplo con `money_format`

A continuación se muestran varios ejemplos de uso de la función `money_format` con diferentes cadenas de formato y configuraciones locales.

```
<?php

$number = 1234.56;

// Mostremos este número en formato internacional para en_US
setlocale(LC_MONETARY, 'en_US');
echo money_format('%i', $number) . "\n";
// USD 1,234.56

// Y en formato nacional italiano con 2 decimales
setlocale(LC_MONETARY, 'it_IT');
echo money_format('%.2n', $number) . "\n";
// L. 1.234,56

// Uso de un número negativo
$number = -1234.5672;

// Formato nacional de EE.UU., con paréntesis para números negativos
// y 10 dígitos de precisión a la izquierda
setlocale(LC_MONETARY, 'en_US');
echo money_format('%(#10n', $number) . "\n";
// ($        1,234.57)

// Formato similar al anterior, añadiendo 2 decimales
// para la precisión derecha, y utilizando el carácter de relleno '*'
echo money_format('%=*(#10.2n', $number) . "\n";
// ($********1,234.57)

// Utilicemos ahora la justificación a la izquierda, con un campo de 14 caracteres
// de largo, sin agrupamiento de dígitos, y utilizando el formato internacional
// para de_DE
setlocale(LC_MONETARY, 'de_DE');
echo money_format('%=*^-14#8.2i', 1234.56) . "\n";
// DEM 1234,56****

// Añadamos aún más al ejemplo anterior
setlocale(LC_MONETARY, 'en_GB');
$fmt = 'El valor final es %i (tras un 10 %% de descuento)';
echo money_format($fmt, 1234.56) . "\n";
// El valor final es GBP 1,234.56 (tras un 10 % de descuento)

?>

    
```php

## Notas

> [!NOTE]
> La función `money_format` solo está definida si el sistema tiene capacidades `strfmon`. Por ejemplo, Windows no las tiene, por lo tanto, `money_format` no está definida en Windows.

> [!NOTE]
> La categoría `LC_MONETARY` de la configuración local afecta el comportamiento de esta función. Utilice `setlocale` para configurar correctamente PHP antes de usar esta función.

## Véase también

`setlocale`, `sscanf`, `sprintf`, `printf`, `number_format`
