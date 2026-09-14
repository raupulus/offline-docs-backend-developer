---
title: Soporte para Windows
source_url: https://www.php.net/manual/es/migration71.windows-support.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration71/windows-support.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 3cd337b4d
order: 510
---

## Soporte para Windows

## Soporte para rutas largas y UTF-8

Si una aplicación web es conforme a UTF-8, no se requiere ninguna acción adicional. Para aplicaciones que dependen de rutas en una codificación diferente a UTF-8 para la E/S, se debe definir explícitamente una directiva INI. El orden de alternativa para la comprobación de los ajustes de codificación INI es:

- internal_encoding

- default_charset

- zend.multibyte

Se han introducido varias funciones para la gestión de las páginas de códigos:

- sapi_windows_cp_set() para establecer la página de códigos predeterminada

- sapi_windows_cp_get() para recuperar la página de códigos actual

- sapi_windows_cp_is_utf8()

- sapi_windows_cp_conv() para convertir entre páginas de códigos, utilizando una firma compatible con iconv()

Estas funciones son seguras para subprocesos múltiples.

La salida de la página de códigos de la consola se ajusta en función de la codificación utilizada en PHP. Dependiendo de la página de códigos OEM del sistema concreto, la salida visible podría o no ser correcta. Por ejemplo, con cmd.exe por defecto y en un sistema con la página de códigos OEM 437, las salidas en las páginas de códigos 1251, 1252, 1253 y otras pueden mostrarse correctamente utilizando UTF-8. En los mismos sistemas, los caracteres en páginas de códigos como 20932 probablemente no se mostrarán correctamente. Esto se refiere a las reglas del sistema para páginas de códigos, la compatibilidad de la fuente y la elección del programa de consola utilizado. PHP define automáticamente la página de códigos de la consola de acuerdo con las reglas de codificación desde php.ini. Utilizar consolas alternativas en lugar de cmd.exe directamente podría ofrecer una mejor experiencia en algunos casos.

Sin embargo, tenga en cuenta que cambiar la página de códigos después de que la solicitud haya comenzado puede causar efectos secundarios inesperados en CLI. La manera preferible es a través de php.ini. Cuando PHP CLI se utiliza en un emulador de consola que no admita Unicode, podría ser necesario evitar cambiar la página de códigos de la consola. La mejor manera de lograr esto es definir la codificación interna o predeterminada para que coincida con la página de códigos ANSI. Otro método es establecer las directivas INI output_encoding e input_encoding en la página de códigos requerida; sin embargo, en este caso la diferencia entre las páginas de códigos internas y de E/S puede causar mojibake. En raros casos, si PHP falla de forma limpia, la página de códigos original de la consola puede no ser restaurada. En este caso, se puede utilizar el comando chcp para restaurarla manualmente.

Especial atención a los sistemas DBCS - el cambio de página de códigos durante la ejecución utilizando `ini_set` puede causar problemas de visualización. A diferencia de los sistemas no DBCS, los caracteres de ancho doble requieren dos celdas de la consola para mostrarse. En algunos casos, solo puede ocurrir la coincidencia de caracteres en el conjunto de glifos de la fuente, sin cambio de fuente. Esta es la naturaleza de los sistemas DBCS; la manera más simple de prevenir problemas de visualización es evitar el uso de `ini_set` para el cambio de página de códigos.

Como consecuencia del soporte de UTF-8 en los flujos, los scripts PHP ya no están limitados a nombres de ficheros ASCII o ANSI. Esto está listo para su uso en CLI. Para otros SAPI, la documentación para el servidor correspondiente es útil.

El soporte para rutas largas es transparente. Las rutas de más de 260 caracteres se prefijan automáticamente con `\\?\`. La longitud máxima de la ruta se limita a 2048 caracteres. Tenga en cuenta que el límite de los segmentos de ruta (longitud del basename) persiste.

Para una mejor portabilidad, se recomienda encarecidamente gestionar los nombres de ficheros, E/S y otros temas relacionados en UTF-8. Además, para las aplicaciones de consola, el uso de una fuente TrueType es preferible y se desaconseja el uso de ini_set() para el cambio de página de códigos.

## readline

La [extensión readline](#book.readline) se admite a través de la [biblioteca WinEditLine](http://mingweditline.sourceforge.net/). Así, la interfaz de sistema interactiva CLI también se admite (`php.exe -a`).

## PHP_FCGI_CHILDREN

`PHP_FCGI_CHILDREN` es ahora respetado. Si esta variable de entorno está definida, el primer proceso `php-cgi.exe` ejecutará el número especificado de hijos. Estos compartirán el mismo socket TCP.

## ftok()

Se ha añadido soporte para `ftok`
