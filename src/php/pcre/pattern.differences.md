---
title: Diferencias con Perl
source_url: https://www.php.net/manual/es/reference.pcre.pattern.differences.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/pattern.differences.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_revision: 96c9d88ba
order: 61690
---

Las diferencias descritas aquí se refieren a las que hay con Perl 5.005.

1.  Por defecto, un carácter espacio en blanco es cualquier carácter que la función isspace() de la biblioteca C reconoce, aunque es posible compilar PCRE con tablas de tipo de caracteres alternativas. Normalmente isspace() coincide con un espacio, salto de página, nueva línea, retorno de carro, tabulador horizontal y tabulador vertical. Perl 5 ya no incluye el tabulador vertical en su juego caracteres de espacios en blanco. De hecho, el carácter de escape \v, el cual estuvo en la documentación de Perl durante mucho tiempo, nunca fue reconocido. Sin embargo, el carácter mismo fue tratado como espacio en blanco al menos hasta 5.002. En 5.004 y 5.005 no coincide con \s.

2.  PCRE no permite los cuantificadores de repetición en declaraciones de búsqueda hacia delante. Perl las permite, pero no significan lo que se puede estar pensando. Por ejemplo, (?!a){3} no afirma que los tres caracteres siguientes no son "a". Simplemente afirma que el siguiente carácter no es "a" tres veces.

3.  Los sub-patrones de captura que tienen lugar dentro de declaraciones de búsqueda hacia delante negativas se cuentan, pero sus entradas en los índices del vector nunca se establecen. Perl establece sus variables numéricas desde cualquiera de los patrones que han coincidido antes de que la declaración falle al coincidir con algo (de ese modo teniendo éxito), pero sólo si la declaración de búsqueda hacia delante negativa contiene sólo una rama.

4.  Aunque los caracteres cero binario están soportados en la cadena objetivo, no están permitidos en un patrón de cadena porque es pasado como una cadena C normal, finalizada por cero. La secuencia de escape "\x00" se puede usar para representar un cero binario en un patrón.

5.  Las siguientes secuencias de escape de Perl no estás soportadas: \l, \u, \L, \U. De hecho, éstas están implementadas por el manejo de cadenas general de Perl y no son parte de su motor de comparación de patrones.

6.  La declaración \G de Perl no está soportada y no es relevante para las comparaciones de patrones individuales.

7.  Obviamente, PCRE no soporta la construcción de (?{código}) y (??{código}). Sin embargo, tiene soporte para patrones recursivos.

8.  Hay, a la hora de escribir, algunas singularidades en Perl 5.005_02 concernientes con la configuración de las cadenas capturadas cuando una parte de un patrón se repite. Por ejemplo, al comparar "aba" con el patrón /^(a(b)?)+\$/ establece \$2 con el valor "b", pero al comparar "aabbaa" con /^(aa(bb)?)+\$/ deja \$2 sin establecer. Sin embargo, si el patrón se cambia a /^(aa(b(b))?)+\$/ entonces \$2 (y \$3) se establecen. En Perl 5.004 \$2 es establecido en ambos casos, y esto también es `true` en PCRE. Si en el futuro Perl cambia a un estado de consistencia que es diferente, PCRE puede cambiar para seguir su ejemplo.

9.  Una discrepancia todavía no resuelta es que en Perl 5.005_02 el patrón /^(a)?(?(1)a\|b)+\$/ coincide con la cadena "a", mientras que en PCRE no lo hace. Sin embargo, en Perl y en PCRE /^(a)?a/ coincide con "a" dejando \$1 sin establecer.

10. PCRE proporciona algunas extensiones para las herramientas de expresiones regulares de Perl:

    1.  Aunque las declaraciones de búsqueda hacia atrás deben coincidir con cadenas de longitud fija, cada rama alternativa de una declaración de búsqueda hacia atrás puede coincidir con una longitud de cadena diferente. Perl 5.005 requiere que todas ellas tengan la misma longitud.

    2.  Si se aplica [PCRE_DOLLAR_ENDONLY](#reference.pcre.pattern.modifiers) y no se aplica [PCRE_MULTILINE](#reference.pcre.pattern.modifiers), el meta-carácter \$ coincide sólo con el final absoluto de la cadena.

    3.  Si se aplica [PCRE_EXTRA](#reference.pcre.pattern.modifiers), una barra invertida seguida de una letra sin ningún significado especial fallará.

    4.  Si se aplica [PCRE_UNGREEDY](#reference.pcre.pattern.modifiers), la codicia de los cuantificadores de repetición se invierte, es decir, por defecto dejan de ser codiciosos, pero si son seguidos por un signo de interrogación lo serán.
