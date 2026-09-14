---
title: Integración del manual de PHP
source_url: https://www.php.net/manual/es/chm.integration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: chmonly/integration.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: chmonly
translation_status: ready
translation_revision: 7cecc752c
order: 1390
---

## Integración del manual de PHP

> [!NOTE]
> La información ofrecida aquí está dirigida principalmente a autores de IDEs, o usuarios avanzados que quisieran integrar éste archivo CHM con sus IDEs favoritos u otros componentes de entornos de producción.

Existen varios editores en la actualidad que ofrecen integración con CHM, pero puede que necesite saber algunas cosas sobre los contenidos CHM para integrar satisfactoriamente el manual a su entorno.

El documento CHM es construido usando tablas de estilos XSL a partir de fuentes XML. Este hecho es único actualmente en la familia del Manual de PHP, ya que todas las otras versiones son generadas usando tablas de estilo DSSSL. Esto también quiere decir que pueden surgir algunas diferencias de visualización no intencionales. Un script especial de conversión es ejecutado sobre la salida XSLT, agregando varias características interesantes, y empaquetando el manual con los archivos de preferencias y muestras de skins.

Si nunca ha trabajado con CHMs, puede pensar en ellos como archivos comprimidos con soporte integrado del SO para el acceso a archivos y soporte adicional para búsquedas e índices. Aunque los archivos CHM sólo pueden consultarse usando el Visor de Ayuda HTML, se puede acceder directamente a archivos al interior de documentos CHM usando un prefijo de URL especial, el nombre del archivo CHM y el archivo que desea en el interior. Ya que todo el contenido de la ayuda es almacenado en archivos HTML, puede desplegar páginas del CHM en Internet Explorer.

Asumiendo que usted colocó su archivo `php_manual_en.chm` en `c:\phpmanual`, el archivo índice del manual (aquel que ve la primera vez) puede ser consultado con la siguiente URL: `mk:@MSITStore:C:\phpmanual\php_manual_en.chm::/_index.html`. Aquí, `mk:@MSITStore:` es el "protocolo" especial, `C:\phpmanual\php_manual_en.chm` es el documento CHM con su ruta completa. La parte `/_index.html` es la ruta al archivo índice dentro del CHM y `::` es simplemente lo que necesita colocar entre la ruta CHM y ésta ruta de archivo.

> [!NOTE]
> Todos los archivos se encuentran en el directorio raíz del CHM, a diferencia de versiones previas de CHM que incluían un directorio de lenguaje. Las imágenes, tables de estilos y otros archivos suplementarios tienen nombres que inician con un caracter de subrayado (como ocurre con el índice principal mostrado anteriormente), para evitar colisiones de nombres.

Los nombres de los archivos generados siguen las mismas reglas que el manual en línea, excepto que la extensión es `.html` y no `.php`. La más importante es que los archivos de documentación de funciones reciben nombres de la forma `function.FUNCNAME.html`, en donde `FUNCNAME` es el nombre de la función, con todos los signos de subrayado convertidos en guiones. Algunos ejemplos son `function.echo.html`, `function.mysql-close.html`, `function.imagecopy.html`.

Usando toda esta información, usted puede mostrar una página del manual para una función solicitada por un usuario. Un ejemplo simple es incluido en la distribución, llamado `php_quickref.hta`. ésta es una [Aplicación HTML](http://msdn.microsoft.com/workshop/author/hta/hta_node_entry.asp) parA demostrar el simple proceso de mostrar una página del manual que hace referencia a una función. La función `quickRef()` definida allí cumple con esta tarea.

Si se quiere integrar el manual en un IDE sin soporte directo para el manual de PHP (en realidad, la conversión de signos de subrayado en guiones), puede usar el archivo `_function.html` incluido para acceder a una página de función, Este archivo es simplemente un enrutador, y puede ser parametrizado a través de la URL, como `_function.html#mysql_close`. Esta página le redireccionará a la página de la función mysql_close (`function.mysql-close.html`) automáticamente. Puede proveer la ruta completa de este archivo si su IDE soporta la ayuda sensible a contexto, y proveer la cadena especificada por el IDE como el parámetro. Un ejemplo de esto es la integración de UltraEdit 9 (vea la página web de edición).

El índice del manual (asequible a través de la pestaña de índice en el panel de navegación) puede ser usado también para propósitos de integración. Todas las páginas HTML son incluidas en el índice con sus títulos como términos de indexación (incluyendo páginas de descripción de funciones).

Si usted es un desarrollador de aplicaciones de escritorio y quiesiera integrar profundamente el CHM con su programa (como por ejemplo desplegando el árbol de la tabla de contenidos en el cuadro de ayuda de su IDE), puede encontrar más información en <http://www.helpware.net/>, así como en otros recursos útiles. El sitio oficial del formato HTML Help se encuentra en <http://www.microsoft.com/download/en/details.aspx?id=21138>.
