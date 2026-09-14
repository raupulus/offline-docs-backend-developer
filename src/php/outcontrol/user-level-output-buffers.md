---
title: Búferes de salida a nivel de usuario
source_url: https://www.php.net/manual/es/outcontrol.user-level-output-buffers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/user-level-output-buffers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 59920
---

## Búferes de salida a nivel de usuario

La bufferización de salida a nivel de usuario de PHP puede iniciarse, manipularse y finalizar desde el código PHP. Cada uno de estos búferes incluye un búfer de salida y una función de gestión de salida asociada.

## ¿Qué salida está bufferizada?

Los búferes de salida a nivel de usuario de PHP bufferizan toda la salida después de su inicio hasta que sean desactivados o el script finalice. La salida en el contexto de los búferes de salida a nivel de usuario de PHP es todo lo que PHP mostraría o enviaría al navegador. En términos prácticos, la salida es cualquier dato de longitud no nula que sea:

> [!NOTE]
> Los datos escritos directamente en `stdout` o pasados a una función SAPI con una funcionalidad similar no serán capturados por los búferes de salida a nivel de usuario. Esto incluye la escritura de datos en `stdout` con `fwrite` o el envío de encabezados con `header` o `setcookie`.

## Iniciar un búfer de salida

Los búferes de salida a nivel de usuario pueden iniciarse utilizando la función `ob_start` o definiendo los parámetros [output_buffering](#ini.output-buffering) y [output_handler](#ini.output-handler) de `php.ini`. Tanto uno como otro pueden crear búferes de salida, `ob_start` es más flexible ya que acepta funciones definidas por el usuario como gestores de salida y las operaciones permitidas en el búfer (flush, clean, remove) pueden definirse también. Los búferes de salida iniciados con `ob_start` estarán activos a partir de la línea donde se llamó a la función, mientras que los iniciados con [output_buffering](#ini.output-buffering) bufferizarán la salida desde la primera línea del script.

PHP también incluye un gestor de salida interno `"URL-Rewriter"` que inicia su propio búfer de salida y solo permite dos instancias del mismo funcionando al mismo tiempo (una para la reescritura de URL a nivel de usuario y otra para el soporte transparente de identificadores de sesión). Estos búferes pueden iniciarse llamando a la función `output_add_rewrite_var` y/o activando el parámetro [session.use_trans_sid](#ini.session.use-trans-sid) de `php.ini`.

La extensión `zlib` tiene su propio búfer de salida que puede activarse utilizando el parámetro [zlib.output_compression](#ini.zlib.output-compression) de `php.ini`.

> [!NOTE]
> Mientras que `"URL-Rewriter"` es especial en cuanto a que solo permite dos instancias del mismo funcionando al mismo tiempo, todos los búferes de salida a nivel de usuario utilizan los mismos búferes subyacentes usados por `ob_start` con su funcionalidad implementada por una función de gestión de salida personalizada. Como tal, toda su funcionalidad puede emularse con código de usuario.

## Anidamiento de búferes de salida

Si un búfer de salida está activo cuando se inicia un nuevo búfer, el nuevo búfer se anidará dentro del búfer previamente activo. El búfer interno se comportará de la misma manera, ya esté anidado o no, pero la salida bufferizada por este no será bufferizada por el búfer externo. Solo la salida vaciada por el búfer interno será bufferizada por el búfer externo.

La mayoría de las funciones `ob_*` solo funcionan con el búfer de salida activo (el último iniciado) por lo que solo el búfer activo puede vaciarse, limpiarse y desactivarse. Las funciones que funcionan con otros búferes son `ob_list_handlers` que devuelve la lista de todos los gestores de salida en uso y `ob_get_status` que puede devolver información sobre el búfer activo únicamente o sobre todos los búferes en uso.

Llamar a `ob_get_level` o `ob_get_status` devolverá el nivel de anidamiento del búfer de salida activo.

> [!CAUTION]
> El valor para los niveles idénticos entre `ob_get_level` y `ob_get_status` difiere en uno. Para `ob_get_level` el primer nivel es `1`, mientras que para `ob_get_status` el primer nivel es `0`.

## Tamaño del búfer

Los tamaños de los búferes de salida se expresan mediante enteros y representan el número de bytes que el búfer puede almacenar sin vaciarse. Cuando el tamaño de la salida en el búfer excede el tamaño del búfer, el contenido del búfer se envía al gestor de salida, su valor de retorno se lava y el búfer se vacía.

Con la excepción de `"URL-Rewriter"`, el tamaño de los búferes de salida puede definirse cuando el búfer se inicia. Si se define como `0`, el búfer de salida solo está limitado por la memoria disponible para PHP. Si se define como `1`, el búfer se lava después de cada bloque de código que produce una salida de longitud no nula.

El tamaño de los búferes de salida puede recuperarse llamando a `ob_get_status`.

Los búferes de salida iniciados con `ob_start` tendrán su tamaño de búfer definido al valor entero pasado al segundo parámetro `chunk_size` de la función. Si se omite, se define como `0`.

El búfer de salida iniciado con [output_buffering](#ini.output-buffering) definido como `"On"` tendrá su tamaño de búfer definido como `0`. Si se define como un entero, el tamaño del búfer corresponderá a ese número.

El tamaño del búfer de salida de `"URL-Rewriter"` se define como `0`, por lo que solo está limitado por la memoria disponible para PHP.

El tamaño del búfer de salida de `zlib` está controlado por el parámetro [zlib.output_compression](#ini.zlib.output-compression) de `php.ini`. Si se define como `"On"`, el tamaño del búfer será `"16K"`/`16384`. Si se define como un entero, el tamaño del búfer corresponderá a ese número en bytes.

## Operaciones permitidas en los búferes

Las operaciones permitidas en los búferes pueden controlarse pasando uno de los [flags de control de búfer](#outcontrol.constants.buffer-control-flags) al tercer parámetro `flags` de `ob_start`. Si se omite, todas las operaciones están permitidas por defecto. Si se usa `0` en su lugar, el búfer no puede vaciarse, limpiarse ni desactivarse pero su contenido puede recuperarse.

`PHP_OUTPUT_HANDLER_CLEANABLE` permite a `ob_clean` limpiar el contenido del búfer.

> [!WARNING]
> La ausencia del flag `PHP_OUTPUT_HANDLER_CLEANABLE` no evitará que `ob_end_clean` o `ob_get_clean` limpien el contenido del búfer.

`PHP_OUTPUT_HANDLER_FLUSHABLE` permite a `ob_flush` vaciar el contenido del búfer.

> [!WARNING]
> La ausencia del flag `PHP_OUTPUT_HANDLER_FLUSHABLE` no evitará que `ob_end_flush` o `ob_get_flush` vacíen el contenido del búfer.

`PHP_OUTPUT_HANDLER_REMOVABLE` permite a `ob_end_clean`, `ob_end_flush`, `ob_get_clean` o `ob_get_flush` desactivar el búfer.

`PHP_OUTPUT_HANDLER_STDFLAGS`, la combinación de los tres flags, permite que cada una de las tres operaciones se realice en el búfer.

## Lavar, acceder y limpiar el contenido del búfer

Lavar envía y elimina el contenido del búfer activo. Los búferes de salida se lavan cuando el tamaño de la salida excede el tamaño del búfer, el script finaliza o se llama a `ob_flush`, `ob_end_flush`, o `ob_get_flush`.

> [!CAUTION]
> Llamar a `ob_end_flush` o `ob_get_flush` desactivará el búfer activo.

> [!CAUTION]
> Lavar los búferes lavará el valor de retorno del gestor de salida que puede diferir del contenido del búfer. Por ejemplo, usar `ob_gzhandler` comprimirá la salida y lavará la salida comprimida.

El contenido del búfer activo puede recuperarse llamando a `ob_get_contents` o `ob_get_flush`.

Si solo se necesita la longitud del contenido del búfer, `ob_get_length` o `ob_get_status` devolverá la longitud del contenido en bytes.

> [!CAUTION]
> Llamar a `ob_get_clean` o `ob_get_flush` desactivará el búfer activo después de devolver su contenido.

El contenido del búfer activo puede limpiarse llamando a `ob_clean`, `ob_end_clean` o `ob_get_clean`.

> [!CAUTION]
> Llamar a `ob_end_clean` o `ob_get_clean` desactivará el búfer activo.

## Desactivar los búferes

Los búferes de salida pueden desactivarse llamando a `ob_end_clean`, `ob_end_flush`, `ob_get_flush` o `ob_get_clean`.

> [!WARNING]
> Los búferes de salida iniciados sin el flag `PHP_OUTPUT_HANDLER_REMOVABLE` no pueden desactivarse y generarán un `E_NOTICE`.

Cada búfer de salida que no haya sido desactivado al final del script o cuando se llama a `exit` será lavado y desactivado por el proceso de terminación de PHP. Los búferes se lavarán y desactivarán en orden inverso a su inicio. El último búfer iniciado será el primero, el primer búfer iniciado será el último en lavarse y desactivarse.

> [!CAUTION]
> Si no se desea el lavado del contenido del búfer, debe usarse un gestor de salida personalizado para evitar el lavado al cerrar.

## Gestores de salida

Los gestores de salida son `callable`s asociados a los búferes de salida que se invocan al llamar a `ob_clean`, `ob_flush`, `ob_end_flush`, `ob_get_flush`, `ob_end_clean`, `ob_get_clean` o durante el proceso de terminación de PHP.

> [!NOTE]
> El proceso de terminación lavará los valores de retorno de los gestores de salida

Si se omite o es `null` al iniciar el búfer de salida se utilizará el gestor de salida interno `"gestor de salida por defecto"` que devuelve el contenido del búfer sin modificar cuando se invoca. Los gestores de salida pueden usarse para devolver una versión modificada del contenido del búfer y/o tener efectos secundarios (por ejemplo, enviar encabezados).

PHP incluye dos gestores de salida internos: `"default output handler"` (el gestor de salida por defecto) y `"URL-Rewriter"` (que está integrado en su propio búfer de salida y solo hasta dos instancias del mismo pueden iniciarse).

La extensión agrupada incluye cuatro gestores de salida adicionales: `mb_output_handler`, `ob_gzhandler`, `ob_iconv_handler`, `ob_tidyhandler`.

## Trabajar con los gestores de salida

Al ser invocados, los gestores de salida reciben el contenido del búfer y una máscara que indica el estado de la bufferización de salida.

```php
handler(string $buffer, [int $phase]): string
```php

`buffer`  
El contenido del búfer.

`phase`  
Una máscara de bits de las [ constantes `PHP_OUTPUT_HANDLER_*` ](#constant.php-output-handler-start).

> [!WARNING]
> Llamar a cualquiera de las siguientes funciones desde un gestor de salida resultará en un error fatal: `ob_clean`, `ob_end_clean`, `ob_end_flush`, `ob_flush`, `ob_get_clean`, `ob_get_flush`, `ob_start`.

> [!NOTE]
> Si el `PHP_OUTPUT_HANDLER_DISABLED` de un gestor está definido, el gestor no será invocado al llamar a `ob_end_clean`, `ob_end_flush`, `ob_get_clean`, `ob_get_flush` `ob_get_clean`, `ob_get_flush`, `ob_clean`, `ob_flush` o durante el proceso de terminación de PHP. Antes de PHP 8.4.0, este flag no tenía ningún efecto al llamar a las funciones `ob_clean` o `ob_flush`.

> [!NOTE]
> El directorio de trabajo del script puede cambiar dentro de la función de parada bajo ciertos servidores web, por ejemplo Apache o el servidor web integrado.

## Flags pasados a los gestores de salida

La máscara de bits pasada al segundo parámetro `phase` del gestor de salida proporciona información sobre la invocación del gestor.

> [!NOTE]
> La máscara de bits puede incluir más de un flag y el operador `&` debe usarse para verificar si un flag está definido.

> [!WARNING]
> El valor de `PHP_OUTPUT_HANDLER_WRITE` y su alias `PHP_OUTPUT_HANDLER_CONT` es `0` por lo que si está definido no puede determinarse excepto usando un [operador de igualdad](#language.operators.comparison) (`==` o `===`).

Los siguientes flags están definidos en una fase específica del ciclo de vida del gestor: `PHP_OUTPUT_HANDLER_START` está definido cuando un gestor es invocado por primera vez. `PHP_OUTPUT_HANDLER_FINAL` o su alias `PHP_OUTPUT_HANDLER_END` está definido cuando un gestor es invocado por última vez, es decir, cuando se desactiva. Este flag también está definido cuando los búferes son desactivados por el proceso de terminación de PHP.

Los siguientes flags están definidos por una invocación específica del gestor: `PHP_OUTPUT_HANDLER_FLUSH` está definido cuando un gestor es invocado al llamar a `ob_flush`. `PHP_OUTPUT_HANDLER_WRITE` o su alias `PHP_OUTPUT_HANDLER_CONT` está definido cuando el tamaño de su contenido es igual o excede el tamaño del búfer y el gestor es invocado mientras el búfer se lava automáticamente. `PHP_OUTPUT_HANDLER_FLUSH` está definido cuando un gestor es invocado al llamar a `ob_clean`, `ob_end_clean` o `ob_get_clean`. Cuando se llama a `ob_end_clean` o `ob_get_clean` también se define `PHP_OUTPUT_HANDLER_FINAL`.

> [!NOTE]
> Cuando se llama a `ob_end_flush` o `ob_get_flush` se define `PHP_OUTPUT_HANDLER_FINAL` pero `PHP_OUTPUT_HANDLER_FLUSH` no.

## Valores de retorno de los gestores de salida

El valor de retorno del gestor de salida se convierte internamente a una cadena siguiendo las semánticas de tipo estándar de PHP, con dos excepciones: los `array`s y los `bool`eanos.

Los arrays se convierten en la cadena `"Array"` pero el mensaje de advertencia `"Conversión de un array a cadena"` no se dispara.

Si el gestor de salida devuelve `false` se devuelve el contenido del búfer. Si el gestor devuelve `true` se devuelve una cadena vacía.

> [!NOTE]
> Si un gestor devuelve `false` o lanza una excepción su flag `PHP_OUTPUT_HANDLER_DISABLED` está definido.

## Excepciones lanzadas en los gestores de salida

Si una excepción no capturada es lanzada en un gestor de salida el programa termina y el gestor es invocado por el proceso de terminación después de lo cual se devuelve el mensaje de error `"Excepción no capturada"`.

Si la excepción no capturada es lanzada en un gestor invocado por `ob_flush`, `ob_end_flush` o `ob_get_flush`, el contenido del búfer se lava antes del mensaje de error.

Si una excepción no capturada es lanzada en un gestor de salida durante la terminación, el gestor termina y ni el contenido del búfer ni el mensaje de error son lavados.

> [!NOTE]
> Si un gestor lanza una excepción su flag `PHP_OUTPUT_HANDLER_DISABLED` está definido.

## Errores generados en los gestores de salida

Si un error no fatal es generado en un gestor de salida el programa continúa su ejecución.

Si un error no fatal es generado en un gestor invocado por `ob_flush`, `ob_end_flush` o `ob_get_flush`, el búfer vacía algunos datos dependiendo del valor de retorno del gestor. Si el gestor devuelve `false` el búfer y el mensaje de error son lavados. Si el gestor devuelve otra cosa, el valor de retorno del gestor es lavado pero no el mensaje de error.

> [!NOTE]
> Si un gestor devuelve `false` su flag `PHP_OUTPUT_HANDLER_DISABLED` está definido.

Si un error fatal es generado en un gestor de salida el programa termina y el gestor es invocado por el proceso de terminación después de lo cual el mensaje de error es lavado.

Si el error fatal es generado en un gestor invocado por `ob_flush`, `ob_end_flush` o `ob_get_flush`, el contenido del búfer es lavado antes del mensaje de error.

Si un error fatal es generado en un gestor de salida durante la terminación el programa termina sin lavar el contenido del búfer o el mensaje de error.

## Salida en los gestores de salida

En circunstancias específicas, la salida producida en el gestor es lavada con el contenido del búfer. Esta salida no se añade al búfer y no forma parte de la cadena devuelta por `ob_get_flush`.

Durante las operaciones de lavado de búfer (llamada a `ob_flush`, `ob_end_flush`, `ob_get_flush` y durante la terminación) si el valor de retorno de un gestor es `false` el contenido del búfer es lavado seguido de la salida. Si el gestor no es invocado durante la terminación el gestor lanzando una excepción o la llamada a `exit` resulta en el mismo comportamiento.

> [!NOTE]
> Si un gestor devuelve `false` su flag `PHP_OUTPUT_HANDLER_DISABLED` está definido.

## Flags de estado de los gestores de salida

Los [ flags de estado de los gestores ](#outcontrol.constants.flags-returned-by-handler) de la máscara de bits `flags` del búfer están definidos en cada invocación del gestor de salida y forman parte de la máscara de bits `flags` devuelta por `ob_get_status`. Si el gestor se ejecuta con éxito y no devuelve `false`, `PHP_OUTPUT_HANDLER_STARTED` y `PHP_OUTPUT_HANDLER_PROCESSED` están definidos. Si el gestor devuelve `false` o lanza una excepción durante la ejecución, `PHP_OUTPUT_HANDLER_STARTED` y `PHP_OUTPUT_HANDLER_DISABLED` están definidos.

> [!NOTE]
> Si `PHP_OUTPUT_HANDLER_DISABLED` de un gestor está definido, el gestor no será invocado al llamar a `ob_end_clean`, `ob_end_flush`, `ob_get_clean`, `ob_get_flush` `ob_get_clean`, `ob_get_flush`, `ob_clean`, `ob_flush` o durante el proceso de terminación de PHP. Antes de PHP 8.4.0, este flag no tenía ningún efecto al llamar a las funciones `ob_clean` o `ob_flush`.
