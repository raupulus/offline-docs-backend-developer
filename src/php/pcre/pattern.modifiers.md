---
title: Opciones de búsqueda
source_url: https://www.php.net/manual/es/reference.pcre.pattern.modifiers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/pattern.modifiers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: false
translation_revision: b5aa3464c
order: 61700
---

Las opciones de PCRE se listan a continuación. Los nombres entre paréntesis son los nombres internos a PCRE. Los espacios y los caracteres de nueva línea son ignorados en los modificadores, los otros caracteres causan errores.

> *i* (`PCRE_CASELESS`)  
> Realiza una búsqueda insensible a mayúsculas o minúsculas.
>
> *m* (`PCRE_MULTILINE`)  
> Por omisión, PCRE trata la cadena sujeto como una sola línea (aunque esta cadena contenga retornos de carro). El metacarácter "inicio de línea" (^) solo será válido una vez, al inicio de la línea, y el metacarácter "fin de línea" (\$) solo será válido al final de la cadena, o antes del retorno de carro final (a menos que se active la opción *D*). Es el mismo funcionamiento que en Perl.
>
> Cuando esta opción está activada, "inicio de línea" y "fin de línea" corresponderán entonces a los caracteres siguiente y precedente inmediatamente a un carácter de nueva línea, además del inicio y del final de la cadena. Es el mismo funcionamiento que la opción Perl /m. Si no hay ningún carácter de nueva línea "\n" en la cadena sujeto, o si no hay ninguna ocurrencia de ^ o \$ en el patrón, esta opción no sirve de nada.
>
> *s* (`PCRE_DOTALL`)  
> Con esta opción, el metacarácter punto (.) reemplaza cualquier carácter, incluyendo las nuevas líneas. Sin esta opción, el carácter punto no reemplaza las nuevas líneas. Esta opción es equivalente a la opción Perl /s. Una clase de caracteres negativa como \[^a\] aceptará siempre los caracteres de nuevas líneas, independientemente de esta opción.
>
> *x* (`PCRE_EXTENDED`)  
> Con esta opción, los caracteres de espacio son ignorados, excepto cuando están escapados, o dentro de una clase de caracteres, y todos los caracteres entre \# no escapados y fuera de una clase de caracteres, y el próximo carácter de nueva línea son ignorados. Es el equivalente Perl de la opción /x: permite añadir comentarios en los patrones complicados. Tenga en cuenta, sin embargo, que esto solo se aplica a los caracteres de datos. Los caracteres de espacio nunca deben aparecer en las secuencias especiales de un patrón, por ejemplo en la secuencia (?( que introduce un paréntesis condicional.
>
> *A* (`PCRE_ANCHORED`)  
> Con esta opción, el patrón está anclado de forma forzada, es decir que el patrón debe aplicarse justo al inicio de la cadena sujeto para ser considerado encontrado. Es posible realizar el mismo efecto añadiendo los metacaracteres adecuados, lo cual es la única manera de hacerlo en Perl.
>
> *D* (`PCRE_DOLLAR_ENDONLY`)  
> Con esta opción, el metacarácter \$ solo será válido al final de la cadena sujeto. Sin esta opción, \$ también es válido antes de una nueva línea, si esta última es el último carácter de la cadena. Esta opción es ignorada si la opción *m* está activada. No hay equivalente en Perl.
>
> *S*  
> Cuando un patrón se utiliza varias veces, vale la pena pasar unos instantes más para analizarlo y optimizar el código para acelerar los tratamientos posteriores. Esta opción fuerza este análisis más exhaustivo. Actualmente, este análisis solo es útil para los patrones no anclados, que no comienzan por un carácter fijo. Desde PHP 7.3.0, esta bandera ya no tiene efecto.
>
> *U* (`PCRE_UNGREEDY`)  
> Esta opción invierte la tendencia a la gula de las expresiones regulares. También puede invertirse esta tendencia caso por caso con un `?` pero esto hará gula la secuencia. Esta opción no es compatible con Perl. También puede ponerse en el patrón con la opción `(?U)` en el [patrón](#regexp.reference.internal-options) o por un punto de interrogación antes del cuantificador (.e.g. `.*?`).
>
> > [!NOTE]
> > No es generalmente posible hacer coincidir más que el límite de [pcre.backtrack_limit](#ini.pcre.backtrack-limit) caracteres en modo no gula.
>
> *X* (`PCRE_EXTRA`)  
> Esta opción añade otras funcionalidades incompatibles con el PCRE de Perl. Todos los backslash seguidos de una letra que no tendría un significado particular causan un error, permitiendo la reserva de estas combinaciones para futuras funcionalidades. Por omisión, como en Perl, los backslash seguidos de una letra sin significado particular son tratados como valores literales. Actualmente, esta opción no activa otras funciones.
>
> *J* (`PCRE_INFO_JCHANGED`)  
> La opción interna de configuración (?J) modifica la opción local `PCRE_DUPNAMES`. Permite la duplicación de nombres para los subpatrones. A partir de PHP 7.2.0 `J` también es soportado como modificador.
>
> *u* (`PCRE_UTF8`)  
> Esta opción activa funcionalidades adicionales de PCRE que no son compatibles con Perl. La cadena de entrada y el patrón son tratados como cadenas UTF-8. Una cadena de entrada inválida tendrá como consecuencia una ausencia de coincidencia en las funciones preg\_\*. Un patrón inválido levantará un error de nivel E_WARNING. Las secuencias UTF-8 de cinco y seis octetos son consideradas inválidas.
>
> *n* (`PCRE_NO_AUTO_CAPTURE`)  
> Este modificador hace que los grupos simples `(xyz)` no sean capturantes. Solo los grupos nombrados como `(?<name>xyz)` son capturantes. Esto afecta únicamente a los grupos capturantes, siempre es posible utilizar referencias de subpatrón numeradas, y el array de coincidencias contendrá siempre resultados numerados. Disponible a partir de PHP 8.2.0
>
> *r* (`PCRE2_EXTRA_CASELESS_RESTRICT`)  
> Cuando *u* (`PCRE_UTF8`) y *i* (`PCRE_CASELESS`) están activos, este modificador impide la coincidencia entre los caracteres ASCII y no-ASCII.
>
> Por ejemplo, `preg_match('/\x{212A}/iu', "K")` coincide con el símbolo Kelvin `K` (U+212A). Cuando *r* es utilizado (`preg_match('/\x{212A}/iur', "K")`, esto no coincide.
>
> Disponible a partir de PHP 8.4.0.
