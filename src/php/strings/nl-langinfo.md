---
title: nl_langinfo
description: Recopila información sobre el idioma y la configuración local
source_url: https://www.php.net/manual/es/function.nl-langinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/nl-langinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: bdef72677
order: 88920
---

nl_langinfo

Recopila información sobre el idioma y la configuración local

## Descripción

```php
nl_langinfo(int $item): string
```php

`nl_langinfo` se utiliza para acceder a cada elemento de la configuración local. A diferencia de la función `localeconv` que devuelve todos los elementos, `nl_langinfo` permite seleccionar un elemento específico.

## Parámetros

`item`  
`item` puede ser el valor entero de un elemento, o el nombre de su constante. A continuación se presenta una lista de los nombres de constantes para `item` que pueden ser utilizados y su descripción. Algunas constantes pueden no estar definidas, o no contener ningún valor para ciertas configuraciones locales.

<table>
<caption>Constantes <code>nl_langinfo</code></caption>
<thead>
<tr>
<th>Constante</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: center;"><em>Constantes de la categoría <code>LC_TIME</code></em></td>
</tr>
<tr>
<td><code>ABDAY_(1-7)</code></td>
<td>Nombre corto del día de la semana.</td>
</tr>
<tr>
<td><code>DAY_(1-7)</code></td>
<td>Nombre del día de la semana (DAY_1 = Domingo).</td>
</tr>
<tr>
<td><code>ABMON_(1-12)</code></td>
<td>Nombre abreviado del mes del año.</td>
</tr>
<tr>
<td><code>MON_(1-12)</code></td>
<td>Nombre del mes del año.</td>
</tr>
<tr>
<td><code>AM_STR</code></td>
<td>String para Ante meridian.</td>
</tr>
<tr>
<td><code>PM_STR</code></td>
<td>String para Post meridian.</td>
</tr>
<tr>
<td><code>D_T_FMT</code></td>
<td>String que puede ser utilizado como string de formato para la función <code>strftime</code> para representar la fecha y la hora.</td>
</tr>
<tr>
<td><code>D_FMT</code></td>
<td>String que puede ser utilizado como string de formato para la función <code>strftime</code> para representar la fecha.</td>
</tr>
<tr>
<td><code>T_FMT</code></td>
<td>String que puede ser utilizado como string de formato para la función <code>strftime</code> para representar la hora.</td>
</tr>
<tr>
<td><code>T_FMT_AMPM</code></td>
<td>String que puede ser utilizado como string de formato para la función <code>strftime</code> para representar la hora en formato de 12 horas, con ante/post meridian.</td>
</tr>
<tr>
<td><code>ERA</code></td>
<td>Era de sustitución.</td>
</tr>
<tr>
<td><code>ERA_YEAR</code></td>
<td>Año en el formato de era de sustitución.</td>
</tr>
<tr>
<td><code>ERA_D_T_FMT</code></td>
<td>Fecha y hora en el formato de era de sustitución (string que puede ser utilizado en la función <code>strftime</code>).</td>
</tr>
<tr>
<td><code>ERA_D_FMT</code></td>
<td>Fecha en el formato de era de sustitución (string que puede ser utilizado en la función <code>strftime</code>).</td>
</tr>
<tr>
<td><code>ERA_T_FMT</code></td>
<td>Hora en el formato de era de sustitución (string que puede ser utilizado en la función <code>strftime</code>).</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><em>Constantes de la categoría <code>LC_MONETARY</code></em></td>
</tr>
<tr>
<td><code>INT_CURR_SYMBOL</code></td>
<td>Símbolo monetario internacional.</td>
</tr>
<tr>
<td><code>CURRENCY_SYMBOL</code></td>
<td>Símbolo monetario local.</td>
</tr>
<tr>
<td><code>CRNCYSTR</code></td>
<td>Mismo valor que <code>CURRENCY_SYMBOL</code>.</td>
</tr>
<tr>
<td><code>MON_DECIMAL_POINT</code></td>
<td>Carácter de coma decimal.</td>
</tr>
<tr>
<td><code>MON_THOUSANDS_SEP</code></td>
<td>Separador de centenas (grupos de tres letras).</td>
</tr>
<tr>
<td><code>MON_GROUPING</code></td>
<td>Como el elemento <code>"grouping"</code>.</td>
</tr>
<tr>
<td><code>POSITIVE_SIGN</code></td>
<td>Signo para los valores positivos.</td>
</tr>
<tr>
<td><code>NEGATIVE_SIGN</code></td>
<td>Signo para los valores negativos.</td>
</tr>
<tr>
<td><code>INT_FRAC_DIGITS</code></td>
<td>Dígitos parciales internacionales.</td>
</tr>
<tr>
<td><code>FRAC_DIGITS</code></td>
<td>Dígitos parciales locales.</td>
</tr>
<tr>
<td><code>P_CS_PRECEDES</code></td>
<td>Devuelve 1 si <code>CURRENCY_SYMBOL</code> precede a un valor positivo.</td>
</tr>
<tr>
<td><code>P_SEP_BY_SPACE</code></td>
<td>Devuelve 1 si un espacio separa <code>CURRENCY_SYMBOL</code> de un valor positivo.</td>
</tr>
<tr>
<td><code>N_CS_PRECEDES</code></td>
<td>Devuelve 1 si <code>CURRENCY_SYMBOL</code> precede a un valor negativo.</td>
</tr>
<tr>
<td><code>N_SEP_BY_SPACE</code></td>
<td>Devuelve 1 si un espacio separa <code>CURRENCY_SYMBOL</code> de un valor negativo.</td>
</tr>
<tr>
<td><code>P_SIGN_POSN</code></td>
<td rowspan="2"><ul>
<li><p>Devuelve 0 si paréntesis rodean la cantidad y <code>CURRENCY_SYMBOL</code>.</p></li>
<li><p>Devuelve 1 si la cadena de signos precede a la cantidad y <code>CURRENCY_SYMBOL</code>.</p></li>
<li><p>Devuelve 2 si la cadena de signos sigue a la cantidad y <code>CURRENCY_SYMBOL</code>.</p></li>
<li><p>Devuelve 3 si la cadena de signos precede inmediatamente al <code>CURRENCY_SYMBOL</code>.</p></li>
<li><p>Devuelve 4 si la cadena de signos sigue inmediatamente al <code>CURRENCY_SYMBOL</code>.</p></li>
</ul></td>
</tr>
<tr>
<td><code>N_SIGN_POSN</code></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><em>Constantes de la categoría <code>LC_NUMERIC</code></em></td>
</tr>
<tr>
<td><code>DECIMAL_POINT</code></td>
<td>Carácter de coma decimal.</td>
</tr>
<tr>
<td><code>RADIXCHAR</code></td>
<td>Mismo valor que <code>DECIMAL_POINT</code>.</td>
</tr>
<tr>
<td><code>THOUSANDS_SEP</code></td>
<td>Carácter de separación de centenas (grupo de tres letras).</td>
</tr>
<tr>
<td><code>THOUSEP</code></td>
<td>Mismo valor que <code>THOUSANDS_SEP</code>.</td>
</tr>
<tr>
<td><code>GROUPING</code></td>
<td></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><em>Constantes de la categoría <code>LC_MESSAGES</code></em></td>
</tr>
<tr>
<td><code>YESEXPR</code></td>
<td>String de expresión regular para buscar la entrada <code>"yes"</code>.</td>
</tr>
<tr>
<td><code>NOEXPR</code></td>
<td>String de expresión regular para buscar la entrada <code>"no"</code>.</td>
</tr>
<tr>
<td><code>YESSTR</code></td>
<td>Visualización del string para <code>"yes"</code>.</td>
</tr>
<tr>
<td><code>NOSTR</code></td>
<td>Visualización del string para <code>"no"</code>.</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><em>Constantes de la categoría <code>LC_CTYPE</code></em></td>
</tr>
<tr>
<td><code>CODESET</code></td>
<td>Devuelve un string de caracteres con el nombre del juego de caracteres.</td>
</tr>
</tbody>
</table>

## Valores devueltos

Devuelve el elemento, en forma de `string` o `false` si el argumento `item` no es válido.

## Ejemplos

Ejemplo con `nl_langinfo`

```
<?php

var_dump(nl_langinfo(CODESET));
var_dump(nl_langinfo(YESEXPR));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(14) "ANSI_X3.4-1968"
    string(5) "^[yY]"

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.

## Véase también

`setlocale`, `localeconv`
