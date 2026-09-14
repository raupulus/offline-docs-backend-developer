---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/outcontrol.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_revision: e2f2172bf
order: 59890
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [output_buffering](#ini.output-buffering) | `"0"` | `INI_PERDIR` |  |
| [output_handler](#ini.output-handler) | `null` | `INI_PERDIR` |  |
| [implicit_flush](#ini.implicit-flush) | `"0"` | `INI_ALL` |  |
| [url_rewriter.tags](#ini.url-rewriter.tags) | `"form="` | `INI_ALL` | A partir de PHP 7.1.0, este parámetro INI solo tiene efecto en `output_add_rewrite_var`. Anterior a PHP 7.1.0, este parámetro INI activaba el soporte transparente del ID de sesión (ver [session.trans_sid_tags](#ini.session.trans-sid-tags)). |
| [url_rewriter.hosts](#ini.url-rewriter.hosts) | `$_SERVER['HTTP_HOST']` se utiliza por omisión. | `INI_ALL` | Disponible a partir de PHP 7.1.0 |

Opciones de configuración de los buffers de salida

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`output_buffering` `bool`/`int`  
La memoria intermedia de la salida para todos los ficheros puede ser activada al definir esta directiva en `"On"`. Para limitar el tamaño del buffer, un número/cantidad correspondiente al número máximo de bytes permitidos puede ser utilizado en lugar de `"On"` para el valor de esta directiva. Por ejemplo, `output_buffering=4096`.

`output_handler` `string`  
La salida de los scripts puede ser redirigida hacia una función. Por ejemplo, al definir `output_handler` en `mb_output_handler`, la codificación de los caracteres será convertida de manera transparente hacia la codificación especificada. La configuración de cualquier manejador de salida activa automáticamente la memoria intermedia de la salida.

> [!NOTE]
> `mb_output_handler` y `ob_iconv_handler` no pueden ser utilizados juntos, y `ob_gzhandler` y [zlib.output_compression](#ini.zlib.output-compression) no pueden ser utilizados con alguno de los siguientes elementos: `mb_output_handler`, `ob_gzhandler`, [zlib.output_compression](#ini.zlib.output-compression), el manejador 'URL-Rewriter' (ver [session.use_trans_sid](#ini.session.use-trans-sid) y `output_add_rewrite_var`).

> [!NOTE]
> Solo las funciones internas pueden ser utilizadas con esta directiva. Para las funciones de usuario, utilice `ob_start`.

`implicit_flush` `bool`  
`false` por omisión. Al cambiar este valor a `true` se indica a PHP que el buffer de salida debe ser vaciado automáticamente después de cada función de visualización. Esto equivale a llamar a la función `flush` después de cada llamada a cualquier función que produzca una salida (como `print` o `echo`) y cada bloque HTML.

Cuando se utiliza PHP en un entorno web, activar esta opción tiene serias implicaciones y generalmente solo se recomienda para depuración. Este valor está por omisión en `true` cuando PHP funciona en modo `CLI SAPI`.

Ver también `ob_implicit_flush`.

`url_rewriter.tags` `string`  
`url_rewriter.tags` especifica las etiquetas HTML y los atributos en los cuales las URLs son reescritas por los valores de `output_add_rewrite_var`. Por omisión, es `"form="`.

Añadir `"form="` o cualquier atributo `form` añadirá un elemento `input` oculto en el `form` con un atributo de nombre y valor para cada par nombre-valor pasado a `output_add_rewrite_var`.

> [!CAUTION]
> Añadir la misma etiqueta más de una vez a `url_rewriter.tags` utilizará únicamente la primera ocurrencia durante el proceso de reescritura de URL.

> [!NOTE]
> Anterior a PHP 7.1.0, [url_rewriter.tags](#ini.url-rewriter.tags) era utilizado para especificar [session.trans_sid_tags](#ini.session.trans-sid-tags).

`url_rewriter.hosts` `string`  
`url_rewriter.hosts` especifica los hosts que son reescritos para incluir los valores de la función `output_add_rewrite_var`. Por omisión `$_SERVER['HTTP_HOST']`. Varios hosts pueden ser especificados separados por una coma, no se permite ningún espacio entre los hosts. Por ejemplo: `php.net,wiki.php.net,bugs.php.net`
