---
title: Uso de la Edición CHM del Manual de PHP
source_url: https://www.php.net/manual/es/chm.using.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: chmonly/usingchm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: chmonly
translation_status: ready
translation_reviewed: true
translation_revision: eee245cdb
order: 1410
---

## Uso de la Edición CHM del Manual de PHP

Al hacer doble clic en un CHM, se abre una ventana de visualización de la ayuda HTML con tres paneles. En el lado izquierdo de la ventana se encuentra el panel de navegación. Contiene cuatro pestañas de navegación: las pestañas Contenido, Índice, Búsqueda y Favoritos. En el lado derecho de la ventana se encuentra el panel de temas. Muestra el tema de ayuda seleccionado, o el tema de ayuda predeterminado al inicio. Las páginas de ayuda son todas ficheros HTML separados, el Internet Explorer muestra las páginas en el panel de temas. El tercer panel es la barra de herramientas, que se encuentra debajo de la barra de título de la ventana de ayuda. Se puede ajustar la disposición horizontal arrastrando el borde vertical entre el panel de navegación y el panel de temas.

Es importante tener en cuenta que cuando se abre el CHM por primera vez, puede aparecer en una posición y tamaño extraños. A partir de ahí, Windows recuerda la posición de la ventana, el tamaño y la pestaña abierta por última vez. Todos estos elementos, incluyendo los favoritos, se almacenan en un fichero llamado `hh.dat`. Si se mueve el fichero a otro directorio, todos estos parámetros memorizados se perderán (incluyendo la lista de favoritos!). Si se reemplaza el fichero CHM por uno nuevo, con el mismo nombre, no es un problema. Los nombres de ficheros y los valores de ruta se almacenan en `hh.dat`.

## La barra de herramientas de la ayuda HTML

La barra de herramientas de la ayuda HTML contiene los siguientes iconos, al visualizar el Manual PHP:

- Ocultar/Mostrar - Oculta/Muestra el panel de navegación.

- Localizar - Localiza un tema en la pestaña de contenido (en caso de que se haya llegado a un tema con la búsqueda, el índice o los favoritos, y se desee ver dónde se encuentra en la estructura de la tabla de contenidos).

- Atrás - Vuelve atrás en el historial.

- Adelante - Avanza en el historial.

- Actualizar - Recarga la página actual.

- Inicio - Abre la página de inicio del CHM.

- Imprimir - Abre el cuadro de diálogo de impresión.

- Opciones - Proporciona una lista desplegable con más opciones.

Utilizar esta barra de herramientas es realmente fácil, muchos de los iconos de la barra de herramientas están fuertemente relacionados con sus equivalentes en Internet Explorer.

## El panel de navegación

El panel de navegación contiene cuatro pestañas de navegación: las pestañas Contenido, Índice, Búsqueda y Favoritos. Todas proporcionan métodos diferentes para acceder a un tema en el fichero de ayuda.

- La pestaña Contenido revela una tabla de contenidos en forma de árbol, donde se puede navegar al tema deseado abriendo y cerrando partes del árbol. Incluso se puede acceder a las secciones más profundas utilizando esta tabla de contenidos. Si se hace clic derecho en un elemento aquí y se elige "Imprimir...", se tendrá la opción de imprimir el tema seleccionado o el tema seleccionado y todos los subtemas. Sin embargo, la impresión no es el objetivo inicial de esta representación del manual (la versión PDF es adecuada para la impresión).

- La pestaña Índice lista un gran número de "palabras clave" (en realidad los títulos de las páginas del manual). Se puede elegir una, o comenzar a escribir una palabra clave, ver la lista ajustarse a la entrada, y luego hacer clic en un tema, o presionar Entrar si el tema seleccionado es el que se desea ver.

- La pestaña Búsqueda muestra una de las funcionalidades más potentes de la ayuda HTML, la búsqueda de texto completo (también conocida como FTS). Aquí, se puede escribir la expresión de búsqueda, conectando eventualmente palabras con AND/OR/NEAR/NOT. Antes de hacer clic en 'Lista de temas', también se pueden definir algunas opciones en la parte inferior. Después de mostrar los resultados de la búsqueda, se dará cuenta de que los resultados de los textos manuales y las notas de usuario están separados. Para ordenar los dos tipos, haga clic en el encabezado de columna 'Ubicación'. Ahora, desde la lista de resultados de la búsqueda, se puede elegir un tema, y ver su página. Las palabras clave que se han buscado están resaltadas en la página.

- La pestaña Favoritos permite almacenar los temas más utilizados en una lista, fácilmente accesible. Aquí, se puede ver la lista, añadir el tema actual, eliminar uno, o mostrar un elemento seleccionado. También se puede especificar el propio título para el favorito, escribiéndolo en el campo 'Temas actuales :'. Los títulos de las páginas de notas de usuario están precedidos por una cadena 'N:' para que se puedan distinguir de las páginas de manual normales en la lista de favoritos.

## Atajos de teclado

Existen numerosos atajos de teclado que se pueden utilizar para aumentar la productividad. Muchos usuarios encuentran más apropiado utilizar estos atajos de teclado para acceder a los temas, en lugar de hacer clic.

| Para | Pulsar |
|----|----|
| Cerrar el visor de ayuda | <span class="keycombo"> +ALT+ +F4+ </span> |
| Mostrar el menú Opciones | <span class="keycombo"> +ALT+ +O+ </span> |
| Ocultar o mostrar el panel de navegación | <span class="keycombo"> +ALT+ +O+ </span>, y luego T |
| Imprimir un tema | <span class="keycombo"> +ALT+ +O+ </span>, y luego P |
| Volver al tema anterior | <span class="keycombo"> +ALT+ +Flecha izquierda+ </span> |
| Avanzar al tema siguiente (si se ha visto justo antes) | <span class="keycombo"> +ALT+ +Flecha derecha+ </span> |
| Activar o desactivar el resaltado de búsqueda | <span class="keycombo"> +ALT+ +O+ </span>, y luego O |
| Volver a la página de inicio de la ayuda | <span class="keycombo"> +ALT+ +O+ </span>, y luego H |
| Cambiar entre el panel de navegación y el panel de temas | F6 |
| Desplazarse a través de todos los enlaces en un tema o a través de todas las opciones en una pestaña del panel de navegación | TAB |
| Mostrar el menú contextual (clic derecho) | <span class="keycombo"> +SHIFT+ +F10+ </span> |

Atajos de teclado generales del visor de ayuda

| Para | Pulsar |
|----|----|
| Mostrar la pestaña Contenido | <span class="keycombo"> +ALT+ +C+ </span> |
| Abrir y cerrar un libro o una carpeta | \+ y - o Flecha izquierda y Flecha derecha |
| Seleccionar un tema | Flecha abajo y Flecha arriba |
| Activar el tema seleccionado | Entrar |

Atajos de teclado de la pestaña Contenido

| Para | Pulsar |
|----|----|
| Mostrar la pestaña Índice | <span class="keycombo"> +ALT+ +N+ </span> |
| Escribir una palabra clave para buscar | <span class="keycombo"> +ALT+ +W+ </span>, y luego escribir la palabra |
| Seleccionar una palabra clave en la lista | Flecha arriba y Flecha abajo |
| Mostrar la palabra clave seleccionada | Entrar o <span class="keycombo"> +ALT+ +D+ </span> |

Atajos de teclado de la pestaña Índice

| Para | Pulsar |
|----|----|
| Mostrar la pestaña Búsqueda | <span class="keycombo"> +ALT+ +S+ </span> |
| Escribir una palabra clave para buscar | <span class="keycombo"> +ALT+ +W+ </span>, y luego escribir la palabra |
| Iniciar la búsqueda | <span class="keycombo"> +ALT+ +L+ </span> |
| Seleccionar un tema en la lista de resultados | <span class="keycombo"> +ALT+ +T+ </span>, y luego Flecha arriba y Flecha abajo |
| Mostrar el tema seleccionado | Entrar o <span class="keycombo"> +ALT+ +D+ </span> |
| Buscar una palabra clave en la lista de resultados | <span class="keycombo"> +ALT+ +U+ </span> |
| Búsqueda de palabras similares a la palabra clave. Por ejemplo, para encontrar palabras como "correr" y "corto" para la palabra clave "correr" | <span class="keycombo"> +ALT+ +M+ </span> |
| Buscar solo en los títulos de los temas | <span class="keycombo"> +ALT+ +R+ </span> |

Atajos de teclado de la pestaña Búsqueda

| Para | Pulsar |
|----|----|
| Mostrar la pestaña Favoritos | <span class="keycombo"> +ALT+ +I+ </span> |
| Añadir el tema actual a la lista de favoritos | <span class="keycombo"> +ALT+ +A+ </span> |
| Seleccionar un tema en la lista de favoritos | <span class="keycombo"> +ALT+ +P+ </span>, y luego Flecha arriba y Flecha abajo |
| Mostrar el tema seleccionado | Entrar o <span class="keycombo"> +ALT+ +D+ </span> |
| Eliminar el tema seleccionado de la lista de favoritos | <span class="keycombo"> +ALT+ +R+ </span> |

Atajos de teclado de la pestaña Favoritos

| Para | Pulsar |
|----|----|
| Búsqueda por índice | Seleccionar las palabras que se desean buscar y pulsar F1 |
| Búsqueda en una página | <span class="keycombo"> +CTRL+ +F+ </span>, y luego ajustar las opciones |
| Recargar la página | F5 |

Atajos de teclado de la pestaña Tema
