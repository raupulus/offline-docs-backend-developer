---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/opcache.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_revision: f2cdcd5af
order: 58650
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [opcache.enable](#ini.opcache.enable) | 1 | `INI_ALL` |  |
| [opcache.enable_cli](#ini.opcache.enable-cli) | 0 | `INI_SYSTEM` | Entre PHP 7.1.2 y 7.1.6 inclusive, el valor por omisión era 1 |
| [opcache.memory_consumption](#ini.opcache.memory-consumption) | "128" | `INI_SYSTEM` |  |
| [opcache.interned_strings_buffer](#ini.opcache.interned-strings-buffer) | "8" | `INI_SYSTEM` |  |
| [opcache.max_accelerated_files](#ini.opcache.max-accelerated-files) | "10000" | `INI_SYSTEM` |  |
| [opcache.max_wasted_percentage](#ini.opcache.max-wasted-percentage) | "5" | `INI_SYSTEM` |  |
| [opcache.use_cwd](#ini.opcache.use-cwd) | 1 | `INI_SYSTEM` |  |
| [opcache.validate_timestamps](#ini.opcache.validate-timestamps) | 1 | `INI_ALL` |  |
| [opcache.revalidate_freq](#ini.opcache.revalidate-freq) | "2" | `INI_ALL` |  |
| [opcache.revalidate_path](#ini.opcache.revalidate-path) | 0 | `INI_ALL` |  |
| [opcache.save_comments](#ini.opcache.save-comments) | 1 | `INI_SYSTEM` |  |
| [opcache.fast_shutdown](#ini.opcache.fast-shutdown) | 0 | `INI_SYSTEM` | Eliminado en PHP 7.2.0. |
| [opcache.enable_file_override](#ini.opcache.enable-file-override) | 0 | `INI_SYSTEM` |  |
| [opcache.optimization_level](#ini.opcache.optimization-level) | "0x7FFEBFFF" | `INI_SYSTEM` | Modificado desde 0x7FFFBFFF en PHP 7.3.0 |
| [opcache.inherited_hack](#ini.opcache.inherited-hack) | 1 | `INI_SYSTEM` | Eliminado en PHP 7.3.0 |
| [opcache.dups_fix](#ini.opcache.dups-fix) | 0 | `INI_ALL` |  |
| [opcache.blacklist_filename](#ini.opcache.blacklist-filename) | "" | `INI_SYSTEM` |  |
| [opcache.max_file_size](#ini.opcache.max-file-size) | 0 | `INI_SYSTEM` |  |
| [opcache.consistency_checks](#ini.opcache.consistency-checks) | 0 | `INI_ALL` | \>Desactivado a partir de PHP 8.1.18 y 8.2.5. Eliminado a partir de PHP 8.3.0. |
| [opcache.force_restart_timeout](#ini.opcache.force-restart-timeout) | "180" | `INI_SYSTEM` |  |
| [opcache.error_log](#ini.opcache.error-log) | "" | `INI_SYSTEM` |  |
| [opcache.log_verbosity_level](#ini.opcache.log-verbosity-level) | 1 | `INI_SYSTEM` |  |
| [opcache.record_warnings](#ini.opcache.record-warnings) | 0 | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0. |
| [opcache.preferred_memory_model](#ini.opcache.preferred-memory-model) | "" | `INI_SYSTEM` |  |
| [opcache.protect_memory](#ini.opcache.protect-memory) | 0 | `INI_SYSTEM` |  |
| [opcache.mmap_base](#ini.opcache.mmap-base) | `null` | `INI_SYSTEM` |  |
| [opcache.restrict_api](#ini.opcache.restrict-api) | "" | `INI_SYSTEM` |  |
| [opcache.file_update_protection](#ini.opcache.file_update_protection) | "2" | `INI_ALL` |  |
| [opcache.huge_code_pages](#ini.opcache.huge_code_pages) | 0 | `INI_SYSTEM` |  |
| [opcache.lockfile_path](#ini.opcache.lockfile_path) | "/tmp" | `INI_SYSTEM` |  |
| [opcache.opt_debug_level](#ini.opcache.opt_debug_level) | 0 | `INI_SYSTEM` | Disponible a partir de PHP 7.1.0 |
| [opcache.file_cache](#ini.opcache.file-cache) | NULL | `INI_SYSTEM` |  |
| [opcache.file_cache_only](#ini.opcache.file-cache-only) | 0 | `INI_SYSTEM` |  |
| [opcache.file_cache_consistency_checks](#ini.opcache.file-cache-consistency-checks) | 1 | `INI_SYSTEM` |  |
| [opcache.file_cache_fallback](#ini.opcache.file-cache-fallback) | 1 | `INI_SYSTEM` | Solo para Windows. |
| [opcache.validate_permission](#ini.opcache.validate-permission) | 0 | `INI_SYSTEM` | Disponible a partir de PHP 7.0.14 |
| [opcache.validate_root](#ini.opcache.validate-root) | 0 | `INI_SYSTEM` | Disponible a partir de PHP 7.0.14 |
| [opcache.preload](#ini.opcache.preload) | "" | `INI_SYSTEM` | Disponible a partir de PHP 7.4.0 |
| [opcache.preload_user](#ini.opcache.preload-user) | "" | `INI_SYSTEM` | Disponible a partir de PHP 7.4.0 |
| [opcache.cache_id](#ini.opcache.cache-id) | "" | `INI_SYSTEM` | Solo para Windows. Disponible a partir de PHP 7.4.0 |
| [opcache.jit](#ini.opcache.jit) | "disable" | `INI_ALL` | Disponible a partir de PHP 8.0.0. Antes de PHP 8.4.0, el valor predeterminado era "tracing". |
| [opcache.jit_buffer_size](#ini.opcache.jit-buffer-size) | 64M | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0. Antes de PHP 8.4.0, el valor predeterminado era 0. |
| [opcache.jit_debug](#ini.opcache.jit-debug) | 0 | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_bisect_limit](#ini.opcache.jit-bisect-limit) | 0 | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_prof_threshold](#ini.opcache.jit-prof-threshold) | "0.005" | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_max_root_traces](#ini.opcache.jit-max-root-traces) | "1024" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_max_side_traces](#ini.opcache.jit-max-side-traces) | "128" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_max_exit_counters](#ini.opcache.jit-max-exit-counters) | "8192" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_hot_loop](#ini.opcache.jit-hot-loop) | "61" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0. Antes de PHP 8.5.0, el valor predeterminado era 64. |
| [opcache.jit_hot_func](#ini.opcache.jit-hot-func) | "127" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_hot_return](#ini.opcache.jit-hot-return) | "8" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_hot_side_exit](#ini.opcache.jit-hot-side-exit) | "8" | `INI_SYSTEM` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_blacklist_root_trace](#ini.opcache.jit-blacklist-root-trace) | "16" | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_blacklist_side_trace](#ini.opcache.jit-blacklist-side-trace) | "8" | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_max_loop_unrolls](#ini.opcache.jit-max-loop-unrolls) | "8" | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_max_recursive_calls](#ini.opcache.jit-max-recursive-calls) | "2" | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_max_recursive_returns](#ini.opcache.jit-max-recursive-return) | "2" | `INI_ALL` | Disponible a partir de PHP 8.0.0 |
| [opcache.jit_max_polymorphic_calls](#ini.opcache.jit-max-polymorphic-calls) | "2" | `INI_ALL` | Disponible a partir de PHP 8.0.0 |

Opciones de configuración de OPcache

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`opcache.enable` `bool`  
Activa el cache de opcode. Cuando está desactivado, el código no es ni optimizado, ni almacenado en caché. La configuración de `opcache.enable` no puede ser activada durante la ejecución mediante la función `ini_set`, solo puede ser desactivada. Intentar activarla en un script generará una advertencia.

`opcache.enable_cli` `bool`  
Activa el cache de opcode para la versión CLI de PHP.

`opcache.memory_consumption` `int`  
El tamaño de la memoria compartida utilizada por OPcache, en megabytes. El valor mínimo permisible es `"8"`, que se fuerza si se define un valor más pequeño.

`opcache.interned_strings_buffer` `int`  
La cantidad de memoria utilizada para almacenar cadenas internas, en megabytes. El valor máximo es de 32767 en arquitecturas de 64 bits, y de 4095 en arquitecturas de 32 bits.

> [!NOTE]
> Antes de PHP 8.4.0, el valor máximo era de 4095 megabytes en todas las arquitecturas.

`opcache.max_accelerated_files` `int`  
El número máximo de claves (y por lo tanto, de scripts) en la tabla de hash de OPcache. El valor actualmente utilizado será el primer número del conjunto de números primos `{ 223, 463, 983, 1979, 3907, 7963, 16229, 32531, 65407, 130987, 262237, 524521, 1048793 }` que sea mayor o igual que el valor configurado. El valor mínimo es 200. El valor máximo es 100000 en PHP \< 5.5.6, y 1000000 en versiones posteriores. Los valores fuera de este intervalo se ajustan al intervalo permitido.

`opcache.max_wasted_percentage` `int`  
El porcentaje máximo de memoria desperdiciada permitido antes de que se programe un reinicio, si no hay suficiente memoria disponible. El valor máximo permisible es `"50"`, que se fuerza si se define un valor más grande.

`opcache.use_cwd` `bool`  
Si está activado, OPcache añade el directorio de trabajo actual a la clave del script, eliminando así posibles colisiones entre archivos con el mismo nombre base. Desactivar esta funcionalidad mejora el rendimiento, pero puede romper aplicaciones existentes.

`opcache.validate_timestamps` `bool`  
Si está activado, OPcache verificará las actualizaciones de los scripts cada [opcache.revalidate_freq](#ini.opcache.revalidate-freq) segundos. Cuando esta directiva está desactivada, debe reinicializarse OPcache manualmente mediante la función `opcache_reset`, la función `opcache_invalidate` o reiniciando el servidor web para que los cambios en el sistema de archivos surtan efecto.

> [!NOTE]
> OPcache puede validar siempre el timestamp de un archivo durante la compilación si las opciones [opcache.file_update_protection](#ini.opcache.file_update_protection) o [opcache.max_file_size](#ini.opcache.max-file-size) están definidas en valores no nulos.

`opcache.revalidate_freq` `int`  
La frecuencia de verificación del timestamp del script para detectar posibles actualizaciones, en segundos. El valor `0` hará que OPcache verifique las actualizaciones en cada petición.

Esta directiva de configuración se ignora si [opcache.validate_timestamps](#ini.opcache.validate-timestamps) está desactivado.

`opcache.revalidate_path` `bool`  
Si está desactivado, los archivos en caché existentes que usan el mismo [include_path](#ini.include-path) serán reutilizados. También, si un archivo con el mismo nombre está en otro lugar en el include_path, no será encontrado.

`opcache.save_comments` `bool`  
Si está desactivado, todos los comentarios de documentación serán eliminados del cache de opcode para reducir el tamaño del código optimizado. La desactivación de esta directiva puede romper aplicaciones y frameworks que dependen del análisis de comentarios para anotaciones, como Doctrine, Zend Framework 2 y PHPUnit.

`opcache.fast_shutdown` `bool`  
Si está activado, se utilizará una secuencia de cierre rápida, que no libera cada bloque asignado, sino que se basa en el gestor de memoria del Zend Engine para desasignar el conjunto entero de variables de la petición, en masa.

Esta directiva fue eliminada en PHP 7.2.0. Una variante de la secuencia de cierre rápido fue integrada en PHP y será utilizada automáticamente si es posible.

`opcache.enable_file_override` `bool`  
Cuando está activado, el cache de opcode será verificado para saber si un archivo ya ha sido almacenado en caché cuando se llaman a las funciones `file_exists`, `is_file` y `is_readable`. Esto puede aumentar el rendimiento de las aplicaciones que verifican la existencia y la legibilidad de los scripts PHP, pero puede devolver datos obsoletos si [opcache.validate_timestamps](#ini.opcache.validate-timestamps) está desactivado.

`opcache.optimization_level` `int`  
Una máscara de bits que controla qué pases de optimización se ejecutan. El valor por omisión es `0x7FFEBFFF`, que activa todas las optimizaciones seguras. Desactivar optimizaciones o activar optimizaciones no seguras es principalmente útil para depurar/desarrollar el optimizador.

Cada bit en la máscara de bits activa un pase de optimización específico:

| Bit | Nombre del pase | Descripción | Por omisión |
|----|----|----|----|
| 0 | PASS_1 | Optimizaciones peephole simples | On |
| 1 | PASS_2 | No utilizado (fusionado en PASS_1) | On |
| 2 | PASS_3 | Optimización de saltos simple | On |
| 3 | PASS_4 | Optimización de llamadas | On |
| 4 | PASS_5 | Optimización basada en el grafo de flujo de control | On |
| 5 | PASS_6 | Optimización basada en análisis de flujo de datos | On |
| 6 | PASS_7 | Si el grafo de llamadas debe utilizarse para optimizaciones basadas en SSA | On |
| 7 | PASS_8 | Propagación de constantes condicional dispersa | On |
| 8 | PASS_9 | Optimización de variables temporales | On |
| 9 | PASS_10 | Eliminación de opcodes NOP | On |
| 10 | PASS_11 | Compactación de literales | On |
| 11 | PASS_12 | Pre-cálculo del tamaño de la pila de llamadas | On |
| 12 | PASS_13 | Eliminación de variables no utilizadas | On |
| 13 | PASS_14 | Eliminación de código muerto | On |
| 14 | PASS_15 | Recopilación y sustitución de declaraciones de constantes (no seguro) | *Off* |
| 15 | PASS_16 | Inserción en línea de funciones triviales (parte de la optimización de llamadas) | On |
| 16 | (Flag) | Ignorar la posibilidad de sobrecarga de operadores (no seguro) | *Off* |

Máscara de bits de pases de optimización

> [!NOTE]
> Las *optimizaciones seguras* (activadas por omisión) preservan el comportamiento exacto del código PHP mientras mejoran el rendimiento. Incluyen la eliminación de código muerto, el plegado de constantes y la optimización de saltos.
>
> Las *optimizaciones no seguras* (desactivadas por omisión) pueden alterar el comportamiento en casos límite:
>
> - *Bit 14*: Recopilación de constantes. Las constantes se sustituyen en tiempo de compilación, ignorando el orden de declaración en tiempo de ejecución:
>
>   <div class="informalexample">
>
>   ```
>   <?php
>   echo getA();         // Outputs: "hello" instead of throwing an Error
>   const A = "hello";
>   function getA() { return A; }
>
>           
>   ```
>
>   </div>
>
> - *Bit 16*: Ignorar la sobrecarga de operadores. No seguro cuando se utilizan clases con `do_operation` (p. ej. [GMP](#book.gmp), [BCMath](#book.bc)) en operaciones aritméticas. Con declaraciones de tipo, el optimizador puede aplicar las mismas optimizaciones de forma segura.

`opcache.inherited_hack` `bool`  
Esta directiva de configuración se ignora.

`opcache.dups_fix` `bool`  
Este hack solo debe ser activado como solución de contorno para errores "Cannot redeclare class".

`opcache.blacklist_filename` `string`  
La ubicación de almacenamiento del archivo que gestiona la lista negra de OPcache. Un archivo de lista negra es un archivo de texto que contiene nombres de archivos que no deben ser acelerados; uno por línea. Se permiten comodines, y también se pueden proporcionar prefijos. Las líneas que comienzan con punto y coma se consideran comentarios y serán ignoradas.

Un archivo de lista negra simple se ve así:

    ; Coincide con un archivo específico.
    /var/www/broken.php
    ; Un prefijo que coincide con todos los archivos que comienzan con x.
    /var/www/x
    ; Una coincidencia con comodín.
    /var/www/*-broken.php

`opcache.max_file_size` `int`  
El tamaño máximo del archivo que puede ser almacenado en caché, en bytes. Si es `0`, todos los archivos podrán ser almacenados en caché.

`opcache.consistency_checks` `int`  
Si es diferente de cero, OPcache verificará la suma de comprobación del caché cada N peticiones, donde N es el valor de esta directiva de configuración. Esto solo debe ser activado durante el depurado, sabiendo que afecta significativamente al rendimiento.

> [!NOTE]
> Desactivado a partir de PHP 8.1.18 y 8.2.5. Eliminado a partir de PHP 8.3.0.

`opcache.force_restart_timeout` `int`  
La duración de espera para el inicio de un reinicio programado, si el caché no está activado, en segundos. Si este tiempo de espera se alcanza, entonces OPcache asume que algo está mal, y matará los procesos que gestionan los bloqueos en el caché para permitir un reinicio.

Si [opcache.log_verbosity_level](#ini.opcache.log-verbosity-level) es 2 o más, se registrará una advertencia en el registro de errores cuando ocurra este comportamiento.

Esta directiva no es soportada en Windows.

`opcache.error_log` `string`  
El registro de errores para errores de OPcache. Una cadena vacía será vista como `stderr`, y los errores serán enviados a la salida estándar de errores (que será el registro de errores del servidor web en la mayoría de los casos).

`opcache.log_verbosity_level` `int`  
El nivel de verbosidad de los registros. Por omisión, solo los errores fatales (nivel 0) y los errores (nivel 1) serán registrados. Los otros niveles disponibles son las alertas (nivel 2), los mensajes informativos (nivel 3), y los mensajes de depuración (nivel 4).

`opcache.record_warnings` `bool`  
Si esta opción está activada, OPcache registrará los avisos de compilación y los reproducirá en el próximo include, incluso si se sirve desde el caché.

`opcache.preferred_memory_model` `string`  
El modelo de memoria preferido para OPcache, a utilizar. Si se deja vacío, OPcache elegirá el modelo más apropiado, que es la mejor forma de hacerlo en la mayoría de los casos.

Los valores posibles son `mmap`, `shm`, `posix` y `win32`.

`opcache.protect_memory` `bool`  
Protege la memoria compartida de escrituras no autorizadas durante la ejecución de los scripts. Esto solo es útil para el depurado interno.

`opcache.mmap_base` `string`  
La base utilizada para los segmentos de memoria compartida en Windows. Todos los procesos PHP deben enlazar la memoria compartida en el mismo espacio de direcciones. El uso de esta directiva permite corregir los errores "Unable to reattach to base address".

`opcache.restrict_api` `string`  
Permite la llamada a las funciones de la API de OPcache solo desde scripts PHP cuyo camino comienza con una cadena específica. El valor por omisión, "", significa "sin restricciones".

`opcache.file_update_protection` `string`  
Impide el almacenamiento en caché de archivos que datan menos que este número de segundos. Esto protege del almacenamiento en caché de archivos actualizados incompletamente. Si todas las actualizaciones de archivos son atómicas, el rendimiento puede ser aumentado definiéndolo a `0`. Esto permitirá almacenar en caché los archivos inmediatamente.

`opcache.huge_code_pages` `bool`  
Activa o desactiva la copia de código PHP (segmento de texto) en HUGE PAGES. Esto debería mejorar el rendimiento, pero requiere una configuración adecuada del sistema operativo. Disponible en Linux a partir de PHP 7.0.0, y en FreeBSD a partir de PHP 7.4.0.

`opcache.lockfile_path` `string`  
Ruta absoluta utilizada para guardar los archivos de bloqueo compartidos (solo para \*nix)

`opcache.opt_debug_level` `string`  
Produce un volcado de opcode para depurar los diferentes pasos de optimización. 0x10000 mostrará los opcodes tal como el compilador los produce antes de que se produzca cualquier optimización, mientras que 0x20000 mostrará los códigos optimizados.

`opcache.file_cache` `string`  
Activa y define el directorio de caché de segundo nivel. Esto debería mejorar el rendimiento cuando la memoria SHM está llena, al reiniciar el servidor o reinicializar SMH. El valor por omisión "" desactiva el almacenamiento en caché basado en archivos.

`opcache.file_cache_only` `bool`  
Activa o desactiva el almacenamiento en caché del opcode en la memoria compartida.

> [!NOTE]
> Antes de PHP 8.1.0, desactivar esta directiva con un archivo de caché ya lleno requiere el vaciado manual de la caché.

`opcache.file_cache_consistency_checks` `bool`  
Activa o desactiva la validación de la suma de comprobación cuando el script se carga desde el caché de archivos.

`opcache.file_cache_fallback` `bool`  
Sugiere opcache.file_cache_only=1 para un proceso determinado que ha fallado al unirse a la memoria compartida (solo para Windows). Se requiere el caché de archivos activado explícitamente.

> [!CAUTION]
> Desactivar esta opción de configuración puede impedir que los procesos se inicien, y por lo tanto se desaconseja.

`opcache.validate_permission` `bool`  
Valida los permisos de los archivos almacenados en caché con respecto al usuario actual.

`opcache.validate_root` `bool`  
Impide las colisiones de nombres en entornos \`chroot\`. Esto debería ser activado en todos los entornos \`chroot\` para impedir el acceso a archivos fuera del chroot.

`opcache.preload` `string`  
Especifica un script PHP que será compilado y ejecutado al iniciar el servidor, y que puede precargar otros archivos, ya sea mediante `include` o utilizando la función `opcache_compile_file`. Todas las entidades (por ejemplo funciones y clases) definidas en estos archivos estarán disponibles para las peticiones listas para usar, hasta que el servidor se apague.

> [!NOTE]
> El precargado no es soportado en Windows.

`opcache.preload_user` `string`  
Permite que el precargado se ejecute como usuario del sistema especificado. Esto es útil para servidores que se inician como root antes de cambiar a un usuario del sistema no privilegiado. El precargado como root no está permitido por omisión por razones de seguridad, a menos que esta directiva esté explícitamente definida como `root`. A partir de PHP 8.3.0, esta directiva ya no necesita ser definida para permitir el precargado al ejecutarse como root con o [phpdbg SAPI](#book.phpdbg).

`opcache.cache_id` `string`  
En Windows, todos los procesos que ejecutan el mismo PHP SAPI bajo el mismo usuario con el mismo ID de caché comparten una instancia única de OPcache. El valor del ID de caché puede ser elegido libremente.

> [!TIP]
> Para IIS, diferentes grupos de aplicaciones pueden tener su propia instancia OPcache utilizando la variable de entorno `APP_POOL_ID` como `opcache.cache_id`. For IIS, different application pools can have their own OPcache instance by using the environment variable `APP_POOL_ID` as `opcache.cache_id`.

`opcache.jit` `stringint`  
Para un uso típico, esta opción acepta una de las cuatro siguientes valores string:

disable

: Desactivado completamente, no puede ser activado durante el tiempo de ejecución.

off

: Desactivado, pero puede ser activado durante el tiempo de ejecución.

tracing

/

on

: Utiliza el tracing JIT. Activado por omisión y recomendado para la mayoría de los usuarios.

function

: Utiliza el function JIT.

Para un uso avanzado, esta opción acepta un entero de 4 dígitos `CRTO`, donde los dígitos significan:

`C` (Banderas de optimización específica del CPU)  
0

: Desactiva las optimizaciones específicas del CPU.

1

: Activa el uso de AVX, si el CPU lo soporta.

`R` (asignación de registros)  
0

: No realiza ninguna asignación de registros

1

: Realiza asignaciones de registros a nivel de bloque.

2

: Realiza asignaciones de registros globales.

`T` (disparador)  
0

: Compila todas las funciones al cargar el script.

1

: Compila las funciones en su primera ejecución.

2

: Perfila las funciones en la primera petición y compila las funciones más calientes justo después.

3

: Perfila a la volada y compila las funciones calientes.

4

: Actualmente no utilizado.

5

: Utiliza el tracing JIT. Perfila a la volada y compila las trazas para los segmentos de código caliente.

`O` (nivel de optimización)  
0

: Sin JIT.

1

: JIT mínimo (llama a los manejadores estándar de la VM).

2

: Inlinea los manejadores de la VM.

3

: Utiliza la inferencia de tipos.

4

: Utiliza un grafo de llamadas.

5

: Optimiza el script entero.

El modo `"tracing"` corresponde a `CRTO = 1254`, el modo `"function"` corresponde a `CRTO = 1205`.

`opcache.jit_buffer_size` `int`  
La cantidad de memoria compartida reservada para código compilado JIT. Un valor de cero desactiva el JIT.

Cuando se utiliza un `int`, el valor se mide en bytes. También se puede usar la notación abreviada, como se describe en [esta FAQ](#faq.using.shorthandbytes).

`opcache.jit_debug` `int`  
Una máscara de bits que especifica qué salida de depuración de JIT activar Para los valores posibles, consulte [zend_jit.h](https://github.com/php/php-src/blob/master/ext/opcache/jit/zend_jit.h) (ver las definiciones de macro que comienzan con `ZEND_JIT_DEBUG`).

`opcache.jit_bisect_limit` `int`  
Opción de depuración que desactiva la compilación JIT después de la compilación de un cierto número de funciones. Esto puede ser útil para bisectar la fuente de una mala compilación JIT. Nota: esta opción solo funciona cuando el disparador JIT está definido a 0 (compilación al cargar el script) o 1 (compilación a la primera ejecución), por ejemplo, `opcache.jit=1215`. Ver más en la opción [opcache.jit](#ini.opcache.jit).

`opcache.jit_prof_threshold` `float`  
Al utilizar el modo de disparador "perfilar las funciones en la primera petición", este límite determina si una función es considerada caliente. El número de llamadas a la función dividido por el número de llamadas a todas las funciones debe ser superior a este límite. Por ejemplo, un límite de 0.005 significa que una función que corresponde a más de 0.5% de todas las llamadas será compilada JIT.

`opcache.jit_max_root_traces` `int`  
Número máximo de trazas raíz (root traces). La traza raíz es un flujo de ejecución que toma primero un camino a través del código, que es una unidad de la compilación JIT. JIT no compilara nuevo código si alcanza este límite.

`opcache.jit_max_side_traces` `int`  
Número máximo de trazas laterales (side trace) que una traza raíz puede tener. La traza lateral es otro flujo de ejecución que no sigue el camino de la traza raíz compilada. Las trazas laterales pertenecientes a la misma traza raíz no serán compiladas si se alcanza este límite.

`opcache.jit_max_exit_counters` `int`  
Número máximo de contadores de salida de traza lateral. Esto limita el número total de trazas laterales que puede haber, a través de todas las trazas raíz.

`opcache.jit_hot_loop` `int`  
Después de cuántas iteraciones un bucle es considerado caliente. El rango de valores válidos es `[0,255]` ; para cualquier parámetro fuera de este rango, por ejemplo -1 o 256, se utilizará el valor por omisión en su lugar. Especialmente, un valor nulo desactivará el JIT para trazar y compilar todos los bucles.

> [!NOTE]
> Se recomienda establecer este parámetro a un número primo, para evitar que sea un múltiplo de los contadores de iteraciones de bucle.

`opcache.jit_hot_func` `int`  
Después de cuántas llamadas una función es considerada caliente. El rango de valores válidos es `[0,255]` ; para cualquier parámetro fuera de este rango, por ejemplo -1 o 256, se utilizará el valor por omisión en su lugar. Especialmente, un valor nulo desactivará el JIT para trazar y compilar todas las funciones.

`opcache.jit_hot_return` `int`  
Después de cuántos retornos un retorno es considerado caliente. El rango de valores válidos es `[0,255]` ; para cualquier parámetro fuera de este rango, por ejemplo -1 o 256, se utilizará el valor por omisión en su lugar. Especialmente, un valor nulo desactivará el JIT para trazar y compilar todos los retornos.

`opcache.jit_hot_side_exit` `int`  
Después de cuántas salidas, una salida lateral es considerada caliente. El rango de valores válidos es `[0,255]` ; para cualquier parámetro fuera de este rango, por ejemplo -1 o 256, se utilizará el valor por omisión en su lugar. Especialmente, un valor nulo desactivará el JIT para trazar y compilar todas las salidas laterales.

`opcache.jit_blacklist_root_trace` `int`  
Número máximo de intentos de compilación de una traza raíz antes de que esta sea excluida.

`opcache.jit_blacklist_side_trace` `int`  
Número máximo de intentos de compilación de una traza lateral antes de que esta sea excluida.

`opcache.jit_max_loop_unrolls` `int`  
Número máximo de intentos para desenrollar un bucle en una traza lateral, intentando alcanzar la traza raíz y cerrar el bucle exterior.

`opcache.jit_max_recursive_calls` `int`  
Número máximo de llamadas recursivas desenrolladas en un bucle.

`opcache.jit_max_recursive_returns` `int`  
Número máximo de retornos recursivos desenrollados en un bucle.

`opcache.jit_max_polymorphic_calls` `int`  
Número máximo de intentos para inlinear una llamada polimórfica (dinámica o método). Llamadas por encima de este límite son tratadas como megamórficas y no son inlineadas.
