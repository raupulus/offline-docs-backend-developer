---
title: ¿Qué hace que un phar sea un phar y no un tar o un zip?
source_url: https://www.php.net/manual/es/phar.fileformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/fileformat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f9c4a68ef
order: 64890
---

## ¿Qué hace que un phar sea un phar y no un tar o un zip?

## Los componentes de todas las archivos Phar, independientemente del formato de archivo

Todos los archivos Phar contienen de tres a cuatro secciones:

1.  Un contenedor

2.  Un manifiesto que describe el contenido

3.  El contenido del archivo

4.  Una firma (opcional) para verificar la integridad (solo con el formato de archivo phar)

## El contenedor de archivo Phar

Un contenedor Phar es un simple archivo PHP. El contenedor mínimo contiene:

```php
<?php __HALT_COMPILER();
   
```

Un contenedor debe contener al menos el token `__HALT_COMPILER();` como conclusión. Típicamente, un contenedor contendrá las siguientes funcionalidades de carga:

```php
<?php
Phar::mapPhar();
include 'phar://monphar.phar/index.php';
__HALT_COMPILER();
   
   
```

No hay restricciones sobre el contenido de un contenedor Phar, excepto la necesidad de concluir con `__HALT_COMPILER();`. La etiqueta de cierre PHP `?>` puede ser incluida u omitida, pero no puede haber más de un espacio entre el `;` y la etiqueta de cierre `?>`, de lo contrario la extensión phar no será capaz de leer el manifiesto del archivo.

En un archivo phar basado en tar o zip, el contenedor se almacena en el archivo `.phar/stub.php`. El contenedor por defecto de los archivos Phar basados en phar contiene aproximadamente 7ko de código para extraer el contenido del phar y ejecutarlo. Consulte la función `Phar::createDefaultStub` para más detalles.

El alias phar se almacena, en el caso de un archivo phar basado en tar o zip, en el archivo `.phar/alias.txt` como texto plano.

## Comparación entre Phar, Tar y Zip

¿Cuáles son las ventajas y desventajas de cada uno de los tres formatos soportados por la extensión phar? Esta tabla intenta responder a esta pregunta.

| Funcionalidad | Phar | Tar | Zip |
|----|----|----|----|
| Formato de archivo estándar | No | Sí | Sí |
| Puede ser ejecutado sin la extensión Phar [\[1\]](#phar.fileformat.phartip) | Sí | No | No |
| Compresión por archivo | Sí | No | Sí |
| Compresión para todo el archivo | Sí | Sí | No |
| Validación por firma de todo el archivo | Sí | Sí | Sí |
| Soporte de aplicaciones específicamente web | Sí | Sí | Sí |
| Metadatos por archivo | Sí | Sí | Sí |
| Metadatos para todo el archivo | Sí | Sí | Sí |
| Creación/modificación de archivo [\[2\]](#phar.fileformat.phartip2) | Sí | Sí | Sí |
| Soporte completo de todas las funciones de flujo | Sí | Sí | Sí |
| Puede ser creado/modificado incluso si phar.readonly=1 [\[3\]](#phar.fileformat.phartip3) | No | Sí | Sí |

Tabla comparativa: Phar, Tar y Zip

> [!TIP]
> \[1\] PHP no puede acceder directamente al contenido de un archivo Phar sin que la extensión Phar esté instalada si utiliza un `contenedor` que extrae el contenido del archivo phar. El contenedor creado por `Phar::createDefaultStub` extrae el archivo phar y ejecuta su contenido desde un directorio temporal si no se encuentra ninguna extensión phar.

> [!TIP]
> \[2\] Todos los accesos en escritura requieren que `phar.readonly` esté desactivado en el php.ini o directamente desde la línea de comandos.

> [!TIP]
> \[3\] Solo los archivos tar o zip sin `.phar` en su nombre y sin contenedor ejecutable `.phar/stub.php` pueden ser creados si phar.readonly=1.

## Los phars basados en Tar

Los archivos basados en el formato de archivo tar son conformes al formato moderno USTAR. El diseño de los encabezados del archivo tar lo hace más eficiente que el formato de archivo zip y tan eficiente como el formato de archivo phar cuando se trata de acceder a los datos. Los nombres de archivos están limitados a 255 bytes, incluyendo la ruta completa dentro del archivo phar basado en tar. Estos archivos pueden ser completamente comprimidos en formato gzip o bzip2 mientras siguen siendo ejecutables por la extensión Phar.

Hay un soporte limitado para leer los tarballs en el formato pax interchangeable, pero todos los encabezados pax reconocidos (actualmente, typeflag `x` y `g`) son silenciosamente ignorados. También hay un soporte limitado para los archivos GNU Tar; actualmente, los encabezados `././@LongLink` son resueltos.

Para comprimir un archivo completo, utilice `Phar::compress`. Para descomprimir un archivo completo, utilice `Phar::decompress`.

## Los phars basados en Zip

Los archivos basados en el formato de archivo zip soportan numerosas funcionalidades incluidas en el formato zip. Los metadatos por archivo o sobre todo el archivo se almacenan en los comentarios del archivo zip y del archivo zip como una cadena de caracteres serializada. Los comentarios zip ya existentes serán leídos sin problemas como una cadena. Las lecturas/escrituras comprimidas son soportadas por la compresión zlib DEFLATE, y solo las lecturas comprimidas por la compresión bzip2. No hay límite en el número de archivos dentro de un archivo phar basado en zip. Los directorios vacíos se almacenan en el archivo zip como archivos con una barra final, como `mi/directorio/`

## El formato de archivo Phar

El formato de archivo phar está compuesto por contenedor/manifiesto/contenido/firma, y almacena las informaciones cruciales de lo que está contenido en el archivo phar en su `manifiesto`.

El manifiesto Phar es un formato altamente optimizado que permite la especificación archivo por archivo de la compresión, los permisos y hasta metadatos de usuario tales como el usuario o el grupo propietario. Todos los valores de más de un byte son almacenados en formato little-endian, A excepción de la versión de la API que es almacenada por razones históricas en 3 trozos big-endian.

Todos los flags no utilizados están reservados para un uso futuro y no deben ser utilizados para almacenar informaciones personalizadas. Utilice los metadatos por archivo para almacenar metadatos personalizados sobre archivos particulares.

El formato de archivo básico del manifiesto de un archivo Phar es el siguiente:

| Tamaño en bytes | Descripción |
|----|----|
| 4 bytes | Longitud del manifiesto en bytes (limitada a 1 MB) |
| 4 bytes | Número de archivos en el Phar |
| 2 bytes | Versión de la API del manifiesto Phar (actualmente 1.0.0) |
| 4 bytes | Flags "bitmapped" globales del Phar |
| 4 bytes | Longitud del alias Phar |
| ?? | El alias Phar (longitud basada en el valor anterior) |
| 4 bytes | Longitud de los metadatos Phar (`0` si no hay) |
| ?? | Metadatos Phar serializados, almacenados en un formato `serialize` |
| al menos 24 \* bytes de las entradas | Entradas para cada archivo |

Formato global del manifiesto Phar

## Flags "bitmapped" globales del Phar

Estos son los flags "bitmapped" actualmente reconocidos por la extensión Phar para el bitmap completo global de Phar:

| Valor | Descripción |
|----|----|
| `0x00010000` | Si está presente, el Phar contiene una firma de verificación |
| `0x00001000` | Si está presente, el Phar contiene al menos 1 archivo que es comprimido mediante zlib DEFLATE |
| `0x00002000` | Si está presente, el Phar contiene al menos 1 archivo que es comprimido mediante bzip2 |

Valores de bitmap reconocidos

## Definición de las entradas del manifiesto Phar

Cada archivo del manifiesto contiene las siguientes informaciones:

| Tamaño en bytes | Descripción |
|----|----|
| 4 bytes | Longitud del nombre de archivo en bytes |
| ?? | Nombre de archivo (longitud basada en el valor anterior) |
| 4 bytes | Tamaño del archivo descomprimido en bytes |
| 4 bytes | Timestamp Unix del archivo |
| 4 bytes | Tamaño del archivo comprimido en bytes |
| 4 bytes | Suma de control CRC32 del contenido descomprimido del archivo |
| 4 bytes | Flags bitmapped específicos del archivo |
| 4 bytes | Longitud de los metadatos del archivo serializados (`0` si no hay) |
| ?? | Metadatos del archivo serializados, almacenados en un formato `serialize` |

Entrada del manifiesto Phar

Se debe notar que a partir de la API 1.1.1, los directorios vacíos son almacenados como nombres de archivo con una barra final como `mi/directorio/`

Los valores reconocidos de flags bitmapped específicos del archivo son:

| Valor | Descripción |
|----|----|
| `0x000001FF` | Estos bits están reservados para definir permisos específicos del archivo. Estos son utilizados para `fstat` y pueden ser utilizados para recrear los permisos deseados en caso de extracción. |
| `0x00001000` | Si está presente, el archivo es comprimido mediante zlib DEFLATE |
| `0x00002000` | Si está presente, el archivo es comprimido mediante bzip2 |

Valores reconocidos de bitmap

## Formato de firma Phar

Los Phar que contienen una firma siempre tienen la firma añadida al final del Phar, después del cargador, el manifiesto y el contenido. Los tipos de firma soportados hasta la fecha son MD5, SHA1, SHA256, SHA512, y OPENSSL.

| Longitud en bytes | Descripción |
|----|----|
| variante | La firma actual, 20 bytes para una SHA1, 16 bytes para una MD5, 32 bytes para una SHA256, y 64 bytes para una SHA512. La longitud de una firma OPENSSL depende del tamaño de la clave privada. |
| 4 bytes | Los flags de firma. `0x0001` es utilizado para definir una firma MD5, `0x0002` para una SHA1, `0x0003` para una SHA256 y `0x0004` para una SHA512. El soporte para las firmas SHA256 y SHA512 está disponible a partir de la versión 1.1.0 de la API. `0x0010` es utilizado para definir una firma OPENSSL, que está disponible a partir de la versión 1.1.1 de la API, si OpenSSL está disponible. |
| 4 bytes | `GBMB` mágico utilizado para definir la presencia de una firma. |

Formato de firma
