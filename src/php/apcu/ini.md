---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/apcu.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: ee1ce6a0e
order: 5110
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

Aunque los ajustes predeterminados de APCu funcionan correctamente en muchas instalaciones, es útil considerar ajustar estos parámetros de configuración.

Una cuestión importante para la configuración de APCu es cuál es el tamaño adecuado que debe asignarse en la memoria a APCu. La directiva ini que controla este parámetro es `apc.shm_size`. El párrafo a continuación es importante para responder a esta pregunta.

Una vez iniciado el servidor, el script `apc.php`, disponible con la extensión, puede ser copiado en el document root y ejecutado por el navegador. Este script proporciona un análisis detallado del funcionamiento interno de APCu. Si la biblioteca GD está activada en PHP, entonces el script puede mostrar gráficos pertinentes.

Si APCu está funcionando, el número de `Cache full count` (a la izquierda) mostrará el número de veces que el caché ha alcanzado su capacidad máxima y ha tenido que evacuar entradas para liberar memoria. Durante la evacuación, si `apc.ttl` ha sido especificado, APCu intentará primero eliminar las entradas expiradas, es decir, las entradas cuyo TTL ha expirado o las entradas que no tienen TTL definido y que no han sido consultadas en los últimos `apc.ttl` segundos. Si `apc.ttl` no ha sido definido o si la eliminación de las entradas expiradas no ha liberado suficiente espacio, APCu borrará la totalidad del caché.

El número de evacuaciones debe ser mínimo en un caché bien configurado. Si el caché está constantemente lleno y por lo tanto liberado a la fuerza, el removimiento resultante tendrá efectos perjudiciales en el rendimiento del script. La manera más sencilla de reducir este número es asignar más memoria a APCu.

Cuando APCu es compilado con mmap (Memory Mapping), solo utilizará un segmento de memoria, a diferencia del caso en que APCu es construido con SHM (SysV Shared Memory) que utiliza varios segmentos de memoria. MMAP no tiene un límite máximo como SHM en `/proc/sys/kernel/shmmax`. En general, el uso de MMAP es recomendado ya que reclama la memoria más rápidamente cuando el servidor web es reiniciado y reduce el impacto en la asignación de memoria al inicio.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [apc.enabled](#ini.apcu.enabled) | "1" | `INI_SYSTEM` |  |
| [apc.shm_segments](#ini.apcu.shm-segments) | "1" | `INI_SYSTEM` |  |
| [apc.shm_size](#ini.apcu.shm-size) | "32M" | `INI_SYSTEM` |  |
| [apc.entries_hint](#ini.apcu.entries-hint) | 512 \* apc.shm_size | `INI_SYSTEM` | Anteriormente a APCu 5.1.25, el valor predeterminado era 4096 |
| [apc.ttl](#ini.apcu.ttl) | "0" | `INI_SYSTEM` |  |
| [apc.gc_ttl](#ini.apcu.gc-ttl) | "3600" | `INI_SYSTEM` |  |
| [apc.mmap_file_mask](#ini.apcu.mmap-file-mask) | NULL | `INI_SYSTEM` |  |
| [apc.slam_defense](#ini.apcu.slam-defense) | "0" | `INI_SYSTEM` |  |
| [apc.enable_cli](#ini.apcu.enable-cli) | "0" | `INI_SYSTEM` |  |
| [apc.use_request_time](#ini.apcu.use-request-time) | "0" | `INI_ALL` | Anteriormente a APCu 5.1.19, el valor predeterminado era `1`. |
| [apc.serializer](#ini.apcu.serializer) | "php" | `INI_SYSTEM` | Anteriormente a APCu 5.1.15, el valor predeterminado era `"default"`. |
| [apc.coredump_unmap](#ini.apcu.coredump-unmap) | "0" | `INI_SYSTEM` |  |
| [apc.preload_path](#ini.apcu.preload-path) | NULL | `INI_SYSTEM` |  |

Opciones de configuración de APCu

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`apc.enabled` `bool`  
`apc.enabled` puede ser puesto a 0 para desactivar APC. Esto puede ser útil cuando APC es compilado estáticamente en PHP ya que no hay otra manera de desactivarlo (cuando APC es compilado como DSO, la línea `extension` en el fichero `php.ini` puede simplemente ser comentada).

`apc.shm_segments` `int`  
El número de segmentos de memoria compartida a asignar al caché de compilación Si APC carece de memoria compartida pero que `apc.shm_size` está puesto al valor máximo permitido por el sistema, entonces aumentar este valor puede evitar que APC agote su memoria.

`apc.shm_size` `string`  
El tamaño de cada segmento de memoria compartida dado en notación abreviada como se indica en esta [FAQ](#faq.using.shorthandbytes). Por defecto, algunos sistemas (incluyendo la mayoría de las variantes de BSD) tienen un límite muy bajo para el tamaño de un segmento de memoria compartida.

`apc.entries_hint` `int`  
Un "indicio" sobre el número de variables distintas que pueden ser almacenadas. Poner a cero o en caso de duda omitir.

`apc.ttl` `int`  
Considerar que las entradas de caché sin TTL explícito son expiradas si no han sido consultadas desde hace tantos segundos. En efecto, esto permite que estas entradas sean oportunamente eliminadas durante una inserción en el caché, o antes de una eliminación completa. Tenga en cuenta que debido a que la eliminación es oportunista, las entradas pueden seguir siendo legibles incluso si son más antiguas que `apc.ttl` segundos. Este parámetro no tiene ningún efecto sobre las entradas de caché para las cuales un TTL explícito está especificado.

`apc.gc_ttl` `int`  
El número de segundos durante los cuales una entrada de caché puede permanecer en la lista de recolección de basura después de haber sido retirada o invalidada. Las entradas son elegibles para eliminación si su número de referencias es cero, o si exceden este límite de tiempo. Si se establece en `0`, la limpieza basada en el tiempo está desactivada, y las entradas solo se eliminan cuando su número de referencias cae a cero.

`apc.mmap_file_mask` `string`  
Si APCu ha sido compilado con la opción MMAP usando `--enable-mmap`, este parámetro recibe la máscara de fichero de tipo mktemp-style a pasar al módulo mmap para determinar si la región de la memoria usando mmap será guardada a través de un fichero o por la de la memoria compartida. En el caso de que el guardado se haga a través de un fichero, la máscara será de la forma `/tmp/apc.XXXXXX` (con exactamente 6 `X`). Para usar shm_open/mmap de la norma POSIX, la máscara debe contener `.shm`, como en el siguiente ejemplo: `/apc.shm.XXXXXX`. Este parámetro puede ser definido por `/dev/zero` para usar la interfaz `/dev/zero` del núcleo con una memoria usando mmap anónimamente. Dejar este parámetro indefinido forzará un mmap anónimo.

`apc.slam_defense` `bool`  
Al inicio o durante la modificación de un fichero en un servidor muy ocupado, varios procesos pueden entrar en competencia para poner en caché el mismo fichero al mismo tiempo. Configurar `apc.slam_defense` en `1` puede ayudar a evitar que varios procesos pongan en caché el mismo fichero simultáneamente introduciendo un mecanismo de probabilidad. Si la misma clave es intentada ser puesta en caché en un corto lapso de tiempo por diferentes procesos, salta la puesta en caché para el proceso actual para mitigar los posibles problemas de puesta en caché.

`apc.enable_cli` `int`  
Principalmente usado para pruebas y depuración. Definir este parámetro permite activar APC en la versión CLI de PHP. Normalmente, no es ideal crear, alimentar y destruir el caché APC en cada solicitud CLI. Sin embargo, en muchos escenarios de prueba es útil poder activar fácilmente APC en la versión CLI de PHP.

`apc.serializer` `string`  
Este parámetro permite a APC usar un serializador de terceros

`apc.coredump_unmap` `bool`  
Activa la gestión por APC de señales, tales como SIGSEGV, que provocan la escritura de ficheros core dump cuando son recibidas. Cuando estas señales son recibidas, APC intentará desasignar el segmento de memoria compartida reservado a mmap con el objetivo de excluirlo del fichero core dump. Esta opción puede mejorar la estabilidad del sistema cuando se reciben señales fatales y APC está configurado con un largo segmento de memoria compartida.

> [!WARNING]
> Esta opción es potencialmente peligrosa. Desasignar un segmento de memoria compartida usado por mmap en el gestor de señales fatales puede causar un comportamiento impredecible si ocurre un error fatal.

> [!NOTE]
> Aunque algunos núcleos pueden proporcionar la posibilidad de ignorar muchos tipos de memoria compartida cuando generan un fichero core dump, estas implementaciones también pueden ignorar importantes segmentos de memoria compartida como el tablero de Apache.

`apc.preload_path` `string`  
Opcional, define una ruta hacia el directorio donde APC cargará los datos del caché al inicio.

`apc.use_request_time` `bool`  
Usa el tiempo de inicio de la solicitud de la interfaz SAPI para la duración de vida (TTL).
