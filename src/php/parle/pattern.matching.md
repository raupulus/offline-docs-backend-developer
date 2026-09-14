---
title: Correspondencia de patrón Parle
source_url: https://www.php.net/manual/es/parle.pattern.matching.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/pattern.matching.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 61060
---

## Correspondencia de patrón Parle

Parle soporta la correspondencia de patrón con expresiones regulares similares a flex. Los siguientes conjuntos de caracteres POSIX también son soportados: `[:alnum:]`, `[:alpha:]`, `[:blank:]`, `[:cntrl:]`, `[:digit:]`, `[:graph:]`, `[:lower:]`, `[:print:]`, `[:punct:]`, `[:space:]`, `[:upper:]`, `[:xdigit:]`.

Las clases de caracteres Unicode no están actualmente activadas por omisión, pase --enable-parle-utf32 para hacerlas disponibles. Una codificación particular puede ser mapeada con una regex correctamente construida. Por ejemplo, para corresponder al símbolo EURO codificado en UTF-8, la expresión regular `[\xe2][\x82][\xac]` puede ser utilizada. El patrón para una cadena codificada en UTF-8 podría ser `[ -\x7f]{+}[\x80-\xbf]{+}[\xc2-\xdf]{+}[\xe0-\xef]{+}[\xf0-\xff]+`.

## Representación de caracteres

| Secuencia | Descripción                                                |
|-----------|------------------------------------------------------------|
| \a        | Alerta (campana).                                          |
| \b        | Retroceso (Backspace).                                     |
| \e        | Carácter ESC, \x1b.                                        |
| \n        | Nueva línea.                                               |
| \r        | Retorno de carro.                                          |
| \f        | Salto de página, \x0c.                                     |
| \t        | Tabulación horizontal, \x09.                               |
| \v        | Tabulación vertical, \x0b.                                 |
| \oct      | Carácter especificado por un código octal de tres dígitos. |
| \xhex     | Carácter especificado por un código hexadecimal.           |
| \cchar    | Carácter de control nombrado.                              |

Representación de caracteres

## Clases de caracteres

| Secuencia | Descripción |
|----|----|
| \[...\] | Un solo carácter listado o contenido en un rango listado. Los rangos pueden ser combinados con los operadores `{+}` y `{-}`. Por ejemplo `[a-z]{+}[0-9]` es lo mismo que `[0-9a-z]` y `[a-z]{-}[aeiou]` es lo mismo que `[b-df-hj-np-tv-z]`. |
| \[^...\] | Un solo carácter no listado y no contenido en un rango listado. |
| . | Cualquier carácter, por omisión `[^\n].` |
| \d | Carácter numérico, `[0-9]`. |
| \D | Carácter no numérico, `[^0-9]`. |
| \s | Carácter de espacio en blanco, `[ \t\n\r\f\v]`. |
| \S | Carácter no de espacio en blanco, `[^ \t\n\r\f\v]`. |
| \w | Carácter de palabra, `[a-zA-Z0-9_]`. |
| \W | Carácter de no palabra, `[^a-zA-Z0-9_]`. |

Clases de caracteres

## Clases de caracteres Unicode

| Secuencia | Descripción                  |
|-----------|------------------------------|
| \p{C}     | Otro.                        |
| \p{Cc}    | Otro, control.               |
| \p{Cf}    | Otro, formato.               |
| \p{Co}    | Otro, uso privado.           |
| \p{Cs}    | Otro, sustituto.             |
| \p{L}     | Letra.                       |
| \p{LC}    | Letra, con casos.            |
| \p{Ll}    | Letra, minúscula.            |
| \p{Lm}    | Letra, modificada.           |
| \p{Lo}    | Letra, otra.                 |
| \p{Lt}    | Letra, de título.            |
| \p{Lu}    | Letra, mayúscula.            |
| \p{M}     | Marca.                       |
| \p{Mc}    | Marca, espacio combinado.    |
| \p{Me}    | Marca, encuadre.             |
| \p{Mn}    | Marca, no espaciada.         |
| \p{N}     | Número.                      |
| \p{Nd}    | Número, dígito decimal.      |
| \p{Nl}    | Número, letra.               |
| \p{No}    | Número, otro.                |
| \p{P}     | Puntuación.                  |
| \p{Pc}    | Puntuación, conector.        |
| \p{Pd}    | Puntuación, guion.           |
| \p{Pe}    | Puntuación, cierre.          |
| \p{Pf}    | Puntuación, comilla final.   |
| \p{Pi}    | Puntuación, comilla inicial. |
| \p{Po}    | Puntuación, otra.            |
| \p{Ps}    | Puntuación, apertura.        |
| \p{S}     | Símbolo.                     |
| \p{Sc}    | Símbolo, moneda.             |
| \p{Sk}    | Símbolo, modificado.         |
| \p{Sm}    | Símbolo, matemático.         |
| \p{So}    | Símbolo, otro.               |
| \p{Z}     | Separador.                   |
| \p{Zl}    | Separador, línea.            |
| \p{Zp}    | Separador, párrafo.          |
| \p{Zs}    | Separador, espacio.          |

Clases de caracteres Unicode

Estas clases de caracteres solo están disponibles si la opción --enable-parle-utf32 ha sido pasada durante la compilación.

## Alternancia y repetición

| Secuencia | Voraz | Descripción                                          |
|-----------|-------|------------------------------------------------------|
| ...\|...  | \-    | Probar los subpatrones en alternancia.               |
| \*        | sí    | Corresponde 0 o más veces.                           |
| \+        | sí    | Corresponde 1 o más veces.                           |
| ?         | sí    | Corresponde 0 o 1 vez.                               |
| {n}       | no    | Corresponde exactamente n veces.                     |
| {n,}      | no    | Corresponde al menos n veces.                        |
| {n,m}     | sí    | Corresponde al menos n veces pero no más de m veces. |
| \*?       | no    | Corresponde 0 o más veces.                           |
| +?        | no    | Corresponde 1 o más veces.                           |
| ??        | no    | Corresponde 0 o 1 vez.                               |
| {n,}?     | no    | Corresponde al menos n veces.                        |
| {n,m}?    | no    | Corresponde al menos n veces pero no más de m veces. |
| {MACRO}   | \-    | Incluye la regex MACRO en la regex actual.           |

Alternancia y repetición

## Ancla

| Secuencia | Descripción                                               |
|-----------|-----------------------------------------------------------|
| ^         | Comienza por una cadena o después de un retorno de línea. |
| \$        | Termina por una cadena o antes de un retorno de línea.    |

Ancla

## Agrupamiento

<table>
<caption>Agrupamiento</caption>
<thead>
<tr>
<th>Secuencia</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>(...)</td>
<td>Agrupa una expresión regular para modificar el orden de evaluación.</td>
</tr>
<tr>
<td>(?r-s:pattern)</td>
<td><p>Aplica la opción r y omite la opción s al interpretar el patrón. Las opciones pueden ser cero o más de los caracteres i, s o x.</p>
<p><code>i</code> significa insensible a mayúsculas y minúsculas.</p>
<p><code>-i</code> significa sensible a mayúsculas y minúsculas.</p>
<p><code>s</code> modifica el significado de <code>.</code> para que corresponda a cualquier carácter.</p>
<p><code>-s</code> modifica el significado de <code>.</code> para que corresponda a cualquier carácter excepto <code>\n</code>.</p>
<p><code>x</code> ignora los comentarios y los espacios en los patrones. Los espacios son ignorados excepto si están escapados por una barra invertida, contenidos en <code>""s</code>, o aparecen dentro de un rango de caracteres.</p>
<p>Estas opciones pueden ser aplicadas globalmente al nivel de las reglas pasando una combinación de los indicadores de bits al analizador léxico.</p></td>
</tr>
<tr>
<td>(?# comment )</td>
<td>Omite todo lo que está en (). El primer carácter ) encontrado termina el patrón. No es posible para el comentario contener un carácter ). El comentario puede extenderse sobre varias líneas.</td>
</tr>
</tbody>
</table>
