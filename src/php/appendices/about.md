---
title: Acerca del manual
source_url: https://www.php.net/manual/es/about.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/about.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 10
---

## Acerca del manual

## Formatos

El manual de PHP se proporciona en diferentes formatos. Estos formatos se dividen en dos grupos: los que están disponibles en línea y los que se pueden descargar.

> [!NOTE]
> Algunos editores han proporcionado versiones impresas de este manual. No se recomienda ninguna, ya que se vuelven obsoletas rápidamente.

El manual puede ser leído en línea en el sitio [php.net](https://www.php.net/). La versión en línea del manual de PHP tiene actualmente dos renderizados CSS: uno agradable a la vista y otro práctico para la impresión.

Dos ventajas del manual en línea sobre la mayoría de los formatos descargables son la integración de las [notas de los usuarios](#about.notes) y los [URL de acceso directo](https://www.php.net/urlhowto.php) que se pueden utilizar para acceder rápidamente a una parte del manual. Una desventaja evidente es que se debe estar en línea para disfrutar de este formato.

Hay muchos formatos del manual para la consulta fuera de línea, y el formato más adecuado depende de su sistema operativo y de sus gustos personales. Para saber cómo se genera el manual, lea la sección ['Cómo se genera el manual'](#about.generate) de este apéndice.

El formato más portable es el HTML. El manual se proporciona en un formato de una sola página HTML, o como un conjunto de ficheros de tamaño reducido (pero un buen millar de ficheros en total). Proporcionamos este formato en una forma comprimida, por lo que se necesitará una utilidad de descompresión para extraer los ficheros del archivo.

Para las plataformas Windows, el formato Windows HTML Help proporciona una versión HTML del manual para usar con la aplicación Windows HTML Help: incluye un motor de búsqueda completo, un índice y marcadores. Muchos IDE en Windows proporcionan enlaces con este formato para una mejor integración. También existen visualizadores de CHM para Linux. Visite [xCHM](http://xchm.sourceforge.net/) o [GnoCHM](http://gnochm.sourceforge.net/).

También existe una [versión CHM extendida](https://www.php.net/docs-echm.php), que se actualiza con menos frecuencia pero que proporciona más funcionalidades. Solo funcionará en Microsoft Windows debido a las tecnologías utilizadas para construir estas páginas.

## Acerca de las notas de los usuarios

Las notas de los usuarios juegan un papel muy importante en el desarrollo de este manual. Al permitir a los lectores contribuir con ejemplos, comentarios y críticas, o aclaraciones, se integran aspectos muy importantes del lenguaje en el manual. Hasta que las notas más importantes se integren en la documentación, están disponibles en el sitio mismo, y en algunos formatos fuera de línea.

> [!NOTE]
> Las notas de los usuarios no son moderadas antes de aparecer en el sitio, y aunque lo sean, su veracidad no puede ser garantizada, al igual que no existe garantía en cuanto a la exactitud del manual mismo.

> [!NOTE]
> Por cuestiones de alcance de la licencia, las notas de los usuarios se consideran parte del manual de PHP, y por lo tanto están cubiertas por la misma licencia que cubre esta documentación (Creative Commons Attribution hasta la fecha). Para más detalles, lea la página [Derechos de autor del manual](#copyright).

## Cómo leer la definición de una función (prototipo)

Cada función en el manual está documentada para permitir una comprensión rápida. Saber descifrar el texto facilitará su aprendizaje. En lugar de depender de ejemplos listos para copiar/pegar, es más útil saber leer la definición de una función (prototipo). Así es cómo:

> [!NOTE]
> Aunque PHP es un lenguaje sin tipado fuerte, un conocimiento básico de los [tipos](#language.types) es esencial, ya que tienen significados importantes.

Las definiciones de funciones indican qué tipo de datos es [devuelto](#functions.returning-values). Examinemos la función `strlen` como ejemplo:

```php
strlen

(PHP 4, PHP 5, PHP 7)
strlen -- Devuelve el tamaño de la cadena

Descripción
strlen ( string $string ) : int

Devuelve el tamaño de la cadena $string.

   
```

| Parte | Descripción |
|----|----|
| strlen | El nombre de la función. |
| (PHP 4, PHP 5, PHP 7) | strlen() está presente en todas las versiones de PHP 4, 5 y 7. |
| ( string \$string ) | El primer (y aquí el único) parámetro a proporcionar a esta función es el parámetro `string`, que debe ser del tipo `string`. |
| int | Tipo de valor devuelto por esta función, que es, en este caso, un `int` (es decir, el tamaño de una cadena se mide por un número). |

Explicaciones de la definición de la función

Podríamos reescribir este prototipo con una versión más genérica:

          nombre de la función    ( tipo del parámetro   nombre del parámetro ) : tipo de retorno

       

Varias funciones necesitan varios parámetros, como `in_array`. Su prototipo es el siguiente:

          in_array ( mixed $needle, array $haystack , bool $strict = false ) : bool

       

¿Qué significa esto? in_array() devuelve un [booléano](#language.types.boolean) `true` en caso de éxito (el parámetro `needle` se encontró en el array `haystack`) o `false` si ocurre un error (el parámetro `needle` no se encontró en el array `haystack`). El primer parámetro se llama `needle` y puede ser de diferentes [tipos](#language.types): por lo tanto, lleva la mención *mixed*. El parámetro `needle` (lo que estamos buscando) puede ser un valor escalar ( `string`, `int`, o [float](#language.types.float)), o incluso un [array](#language.types.array). `haystack` (el array, en el que estamos buscando) es el segundo parámetro. El tercer parámetro, *opcional*, `strict`, es opcional. Todos los parámetros opcionales tienen un valor por defecto; si el valor por defecto es desconocido, se muestra como `?`. El manual indica que el parámetro `strict` vale por defecto `false`. Consulte el manual de cada función para saber cómo funciona.

Además, el signo & (e comercial) añadido al principio del parámetro de una función permite pasar este parámetro por [referencia](#language.references.pass), como en este ejemplo:

           preg_match ( string $pattern , string $subject , array &$matches = null,
           int $flags = 0 , int $offset = 0 ) : int|false

         

En este ejemplo, se puede ver que el tercer parámetro opcional `&$matches` será pasado por referencia.

También hay funciones con información más compleja sobre las versiones de PHP. Tomemos `html_entity_decode` como ejemplo:

    (PHP 4 >= 4.3.0, PHP 5, PHP 7)

       

Esto significa que esta función solo está disponible desde PHP 4.3.0.

## Versiones de PHP documentadas en este manual

Este manual contiene información sobre las versiones antiguas, actuales y futuras de PHP. Los cambios de comportamiento están documentados en forma de notas, historiales de versiones, pero también en las páginas del manual. La versión documentada más antigua es la versión 7.0.0.

Cuando la documentación existe para las últimas versiones de desarrollo (no publicadas) de PHP, se titulará "disponible en Git" o "versión de desarrollo." Estos cambios están previstos, pero aún pueden evolucionar en raros casos.

Todos los desarrollos están versionados en el depósito Git y pueden ser recuperados como se describe en [acceso anónimo Git](https://www.php.net/git.php).

Y por cuestiones de claridad, el manual hará referencia a las versiones mayores, menores y revisiones de PHP. Por ejemplo, PHP `7.3.1`, el *7* es la versión mayor, *3* la menor, y *1* la revisión. Típicamente, PHP solo agrega nuevas funcionalidades en las versiones mayores o menores, y corrige errores en las revisiones. Sin embargo, esta convención no siempre se verifica.

Tenga en cuenta también que el manual se refiere al PHP presente y no futuro, incluso para las funcionalidades documentadas y que aún no están disponibles. Así, el manual puede perdurar en el tiempo y no requiere actualizaciones importantes con cada lanzamiento de PHP.

En varias ocasiones, el manual de PHP enumera los valores por defecto de las directivas de PHP. Estos valores se basan en el comportamiento de PHP sin archivo de configuración `php.ini`, por lo que pueden cambiar de los valores encontrados en los archivos distribuidos `php.ini-development` y `php.ini-production`. Los valores indicados son también los de la última versión de PHP, un registro de cambios indica los valores previamente empleados. Vea [el apéndice sobre las directivas PHP ](#ini.list) para más detalles sobre estos valores y sus evoluciones.

## Dónde encontrar más información sobre PHP ?

Este manual no tiene como objetivo proporcionar presentaciones sobre las prácticas de programación. Si es un completo novato, o incluso un programador principiante, puede encontrar difícil aprender la programación PHP con solo este manual: sería mejor encontrar recursos más orientados al aprendizaje.

Hay un buen número de listas de difusión activas, que tratan todos los aspectos del lenguaje y la programación PHP. Si está bloqueado por un problema, probablemente pueda encontrar ayuda en estas listas. Existe un recuento de las listas de difusión en [la página de soporte de php.net](https://www.php.net/support.php).

## Cómo ayudar a mejorar la documentación ?

Hay varias formas de participar en la mejora de la documentación.

Si se encuentra un error, en cualquier traducción de la documentación, informe del error en el gestor de incidencias del depósito de idioma respectivo en <https://github.com/php/>;; por ejemplo, los errores en el manual en inglés deben ser reportados a <https://github.com/php/doc-en/issues>; Todas las incidencias relacionadas con la documentación, así como sus formatos, deben ser enviadas como errores.

> [!NOTE]
> No abuse del gestor de incidencias para enviar solicitudes de ayuda. Utilice más bien una de las opciones propuestas por el [soporte](https://www.php.net/support.php).

Al contribuir con notas, se pueden proporcionar nuevos ejemplos, destacar efectos secundarios y aportar aclaraciones para los demás lectores. Pero no tome el sistema de anotación como un sistema de envío de errores. Puede obtener más información sobre las anotaciones en la sección ['Acerca de las notas de los usuarios'](#about.notes)

También es posible enviar solicitudes de extracción al [espejo Github del repositorio de la documentación](https://github.com/php/doc-en).

El manual de PHP está traducido a muchos idiomas. El conocimiento del inglés así como de otro idioma puede permitir ayudar a la documentación de PHP trabajando con un equipo de traducción. Para más información sobre cómo comenzar una traducción, o sobre cómo ayudar a una versión ya traducida, comience por leer <https://doc.php.net/guide/>.

El proyecto de documentación de PHP tiene un canal IRC donde se puede venir y hablar con los autores del manual o encontrar un cierto aspecto del manual con el cual se podría ayudar. Las coordenadas: `#php.doc` en `irc.efnet.org`.

## Cómo se generan las documentaciones

Este manual está escrito en XML, utilizando la [DTD de DocBook XML](http://www.oasis-open.org/docbook/xml/), y [PhD](https://wiki.php.net/doc/phd/) (El motor \[PH\]P de visualización \[D\]ocBook) para el mantenimiento y el formateo.

Gracias al formato XML como fuente, se tiene la posibilidad de generar muchos formatos teniendo una sola fuente para todos los formatos. La herramienta utilizada para formatear el manual en línea es [PhD](https://wiki.php.net/doc/phd/). Se utiliza [Microsoft HTML Help Workshop](http://msdn.microsoft.com/library/en-us/htmlhelp/html/vsconhh1start.asp) para generar el formato Windows HTML Help del manual, y, por supuesto, PHP mismo para realizar conversiones y formateo.

El manual de PHP se genera en muchos idiomas y formatos, lea <https://www.php.net/docs.php> para más información. El código fuente XML puede ser descargado desde git y visualizado en <https://github.com/php/doc-en>.

## Traducciones

El manual de PHP está disponible no solo en inglés, sino también en diferentes idiomas. El texto del manual se escribe primero en inglés, luego equipos de todo el mundo aseguran la traducción del manual a su idioma nativo. Si la traducción de una sección aún no está disponible, el sistema de creación de la documentación presentará entonces la versión en inglés.

Los contribuyentes a la documentación parten de los códigos fuente XML disponibles en <https://github.com/php/doc-en>. luego traducen a su idioma. *No* utilizan las versiones generadas (como el HTML o el texto plano) ya que es el sistema de edición el que se encarga de hacer las conversiones del formato XML a un formato legible.

> [!NOTE]
> Si desea ayudar con la traducción de la documentación, póngase en contacto con el equipo de documentación inscribiéndose en la lista de difusión: <phpdoc+subscribe@lists.php.net>. La dirección de la lista de difusión es `phpdoc@lists.php.net`. Indique en el mensaje que está interesado en la traducción de la documentación a un nuevo idioma, y alguien vendrá a ayudar a comenzar una nueva traducción, o unirse al equipo que ha tomado a cargo esta traducción.

Actualmente, el manual está disponible, parcial o totalmente, en más de 10 idiomas.

Todos pueden ser descargados aquí: <https://www.php.net/docs.php>.
