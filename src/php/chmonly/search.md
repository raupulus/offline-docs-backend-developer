---
title: La Búsqueda de Texto Completo
source_url: https://www.php.net/manual/es/chm.search.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: chmonly/search.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: chmonly
translation_status: ready
translation_reviewed: false
translation_revision: dcd544828
order: 1400
---

## La Búsqueda de Texto Completo

Esta edición del Manual PHP incluye una posibilidad de búsqueda de texto completo avanzada proporcionada por la aplicación de visualización. Esto permite a los usuarios buscar cada palabra en el fichero de ayuda para encontrar una correspondencia. Por ejemplo, si un usuario realiza una búsqueda sobre la palabra "Apache", cada tema que contenga la palabra "Apache" será listado. La búsqueda de texto completo avanzada permite a un usuario buscar utilizando booleanos, patrones de expresión y expresiones anidadas. Un usuario puede también limitar la búsqueda a los resultados anteriores, hacer coincidir palabras similares, o buscar solo los títulos de los temas.

El uso de la función de búsqueda es bastante simple. Haga clic en la pestaña de búsqueda, escriba las palabras deseadas y presione ENTRAR (o haga clic en "Listar Temas"). Recibirá entonces una lista de correspondencias del Manual PHP (y de las notas). Puede utilizar el botón con una flecha hacia la derecha para añadir operadores booleanos a su búsqueda (o puede escribirlos). A medida que ve los resultados, puede utilizar los encabezados de columna (Título, Ubicación y Rango) para ordenar la lista de temas. El orden por defecto es por Rango. También puede ajustar algunos parámetros en la parte inferior de esta pestaña.

Las palabras encontradas se resaltan en la página actual en el panel de tema por defecto. Puede desactivar esta función seleccionando el elemento de menú "Desactivar Resaltado de Búsqueda" en el menú Opciones. Puede tener esta funcionalidad de la misma manera. Si está consultando un tema largo, solo las primeras 500 ocurrencias de una palabra o frase de búsqueda serán resaltadas, debido a una limitación del visualizador.

## Reglas Generales de Búsqueda

Una búsqueda básica consiste en la palabra o frase que se desea encontrar. Se pueden utilizar expresiones de patrón, expresiones anidadas, operadores booleanos, coincidencias de palabras similares, una lista de resultados anteriores, o títulos de temas para definir aún más la búsqueda.

Las reglas básicas para formular consultas son las siguientes:

- Las búsquedas no distinguen entre mayúsculas y minúsculas, por lo que se puede escribir la búsqueda en mayúsculas o en minúsculas.

- Se puede buscar cualquier combinación de letras (a-z) y números (0-9). No se puede buscar letras solas (a, b, c, etc.) y palabras comunes, como: an, and, as, at, be, but, by, do, for, from, have, he, in, it, not, of, on, or, she, that, the, there, they, this, to, we, which, with, you.

- Los caracteres de puntuación como el punto (.), los dos puntos (:), el punto y coma (;), la coma (,) y el guion (-) son ignorados durante una búsqueda.

- Agrupar los elementos de la búsqueda utilizando comillas dobles o paréntesis para separar cada elemento. No se puede buscar comillas.

> [!NOTE]
> Si se busca un nombre de fichero con una extensión, se debe agrupar toda la cadena en comillas dobles ("nombredefichero.ext"). De lo contrario, el punto romperá el nombre de fichero en dos términos distintos. La operación por defecto entre los términos es Y, por lo que se creará el equivalente lógico de "nombredefichero Y ext".

## Búsqueda de palabras o frases

Se pueden buscar palabras o frases y utilizar expresiones de patrón. Las expresiones de patrón permiten buscar uno o más caracteres utilizando un signo de interrogación o un asterisco. La tabla a continuación describe los resultados de estos diferentes tipos de búsquedas.

<table>
<caption>Búsqueda de palabras y frases</caption>
<thead>
<tr>
<th>Buscar</th>
<th>Ejemplo</th>
<th>Resultados</th>
</tr>
</thead>
<tbody>
<tr>
<td>Una simple palabra</td>
<td>select</td>
<td>Los temas que contienen la palabra "select". (También se encontrarán sus variaciones gramaticales, como "selector" y "selection".)</td>
</tr>
<tr>
<td>Una frase</td>
<td>"nuevo operador" o nuevo operador</td>
<td><p>Los temas que contienen la frase literal "nuevo operador" y todas sus variaciones gramaticales.</p>
<p>Sin las comillas, la consulta es equivalente a especificar "nuevo Y operador", que encontrará los temas que contienen las dos palabras individuales, en lugar de la frase.</p></td>
</tr>
<tr>
<td>Expresión de patrón</td>
<td>esc* o HT??</td>
<td><p>Los resultados para el primer ejemplo incluyen los temas que contienen los términos "ESC", "escape", "escalation", etc. El asterisco no puede ser el único carácter en el término.</p>
<p>Los resultados para el segundo ejemplo incluyen los temas que contienen los términos "HTTP", "HTML", etc. El signo de interrogación no puede ser el único carácter en el término.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Seleccione la casilla de verificación Coincidencia de palabras similares para incluir variaciones gramaticales menores para la frase que se está buscando. Esta funcionalidad solo localiza las variaciones del término con sufijos comunes. Por ejemplo, una búsqueda de la palabra "add" encontrará "added", pero no encontrará "additive". Esta opción es independiente de otras opciones o sintaxis. Si se realiza una búsqueda solo en los títulos, se encontrarán las variaciones en los títulos. Si se utilizan comillas (o cualquier otro operador de consulta), cualquier variación del término puede aparecer; por ejemplo, "búsqueda truncada" también encontrará "búsqueda truncada".

## Definir los términos de búsqueda

Los operadores AND, OR, NOT y NEAR permiten definir con precisión la búsqueda creando una relación entre los términos de búsqueda. La tabla siguiente muestra cómo se pueden utilizar cada uno de estos operadores. Si no se especifica ningún operador, se utiliza AND. Por ejemplo, la consulta "servidor cgi seguridad" es equivalente a "servidor Y cgi Y seguridad".

| Buscar | Ejemplo | Resultados |
|----|----|----|
| Ambos términos en el mismo tema | http AND apache | Los temas que contienen las palabras "http" y "apache". |
| Cualquiera de los términos en un tema | ming OR swflib | Los temas que contienen la palabra "ming" o la palabra "swflib", o ambas. |
| El primer término sin el segundo término | xml NOT expat | Los temas que contienen la palabra "xml" pero no la palabra "expat". |
| Ambos términos en el mismo tema, cerca el uno del otro | base de datos NEAR seguridad | Los temas que contienen la palabra "base de datos" a ocho palabras de la palabra "seguridad". |

Operador de búsqueda

> [!NOTE]
> Los caracteres \|, & y ! también pueden ser utilizados en lugar de OR, AND y NOT respectivamente. Esto puede no funcionar si se utiliza una versión muy antigua del visualizador.

## Uso de expresiones anidadas en la búsqueda

Las expresiones anidadas permiten crear búsquedas complejas para encontrar información. Por ejemplo, "html AND ((smtp OR pop3) NEAR mail)" encuentra los temas que contienen la palabra "html" con las palabras "smtp" y "mail" cerca una de la otra, o que contienen "html" con las palabras "pop3" y "mail" cerca una de la otra.

Las reglas básicas para buscar temas de ayuda utilizando expresiones anidadas son las siguientes:

- Se pueden utilizar paréntesis para anidar expresiones en una consulta. Las expresiones entre paréntesis se evalúan antes que el resto de la consulta.

- Si una consulta no contiene una expresión anidada, se evalúa de izquierda a derecha. Por ejemplo: "mail NOT pop3 OR smtp" encuentra los temas que contienen la palabra "mail" sin la palabra "pop3" o los temas que contienen la palabra "smtp". Por otro lado, "mail NOT (pop3 OR smtp)" encuentra los temas que contienen la palabra "mail" sin las palabras "pop3" o "smtp".

- No se pueden anidar expresiones más de cinco niveles.
