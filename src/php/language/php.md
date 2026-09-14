---
title: php://
description: Acceso a los diversos flujos I/O
source_url: https://www.php.net/manual/es/wrappers.php.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/php.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: f56de7ebe
order: 4690
---

php://

Acceso a los diversos flujos I/O

## Descripción

PHP proporciona un número importante de flujos I/O que permiten acceder a los flujos de entrada y salida de PHP mismo, a los descriptores de ficheros de entrada, salida y error estándar, a flujos que representan ficheros temporales en memoria viva o en disco, así como a filtros que pueden manipular otros recursos de ficheros durante la lectura o escritura.

## php://stdin, php://stdout y php://stderr

`php://stdin`, `php://stdout` y `php://stderr` permiten acceso directo a los flujos de entrada o salida correspondientes del proceso PHP. El flujo hace referencia a una copia del descriptor de fichero, lo que significa que si se abre `php://stdin` y se cierra más tarde, solo se cierra la copia del descriptor; el flujo realmente referenciado por `STDIN` no se ve afectado. Se recomienda utilizar únicamente las constantes `STDIN`, `STDOUT` y `STDERR` en lugar de abrir manualmente los flujos utilizando estas envolturas.

`php://stdin` es de solo lectura, mientras que `php://stdout` y `php://stderr` son de solo escritura.

## php://input

`php://input` es un flujo de solo lectura que permite leer datos sin tratar desde el cuerpo de la petición. `php://input` no está disponible en las peticiones POST con `enctype="multipart/form-data"` si la opción [enable_post_data_reading](#ini.enable-post-data-reading) está activada.

## php://output

`php://output` es un flujo de solo escritura, que permite escribir en el mecanismo de buffer de salida de la misma manera que las funciones `print` y `echo`.

## php://fd

`php://fd` permite acceso directo al descriptor de fichero especificado. Por ejemplo, `php://fd/3` corresponde al descriptor de fichero número 3.

## php://memory y php://temp

`php://memory` y `php://temp` son flujos de lectura/escritura que permiten almacenar datos temporales en una envoltura de ficheros. Una diferencia entre estos dos flujos es que `php://memory` almacenará siempre sus datos en memoria, mientras que `php://temp` utilizará un fichero temporal una vez que la cantidad de datos almacenados haya superado un límite predefinido (por omisión, 2 Mo). La ubicación de este fichero temporal se determina de la misma manera que para la función `sys_get_temp_dir`.

El límite de memoria de `php://temp` puede ser controlado añadiendo `/maxmemory:NN`, donde `NN` es la cantidad máxima de datos a conservar en memoria antes de utilizar un fichero temporal, en bytes.

> [!CAUTION]
> Algunas extensiones PHP pueden requerir un flujo IO estándar, y pueden intentar convertir un flujo dado a un flujo IO estándar. Esta conversión puede fallar para los flujos de memoria, ya que la función C `fopencookie` debe estar disponible. Esta función C *no está* disponible en Windows.

## php://filter

`php://filter` es una especie de envoltura prevista para permitir la aplicación de [filtros](#filters) sobre un flujo en el momento de su apertura. Esto es muy práctico con funciones sobre ficheros todas-en-una como las funciones `readfile`, `file` y `file_get_contents`, donde no existe otro mecanismo que permita aplicar un filtro al flujo antes de que el contenido sea leído.

La meta de `php://filter` toma los parámetros siguientes bajo la forma de componentes de su ruta. Varios filtros encadenados pueden ser especificados en una sola ruta. Consúltese los ejemplos para un uso correcto de estos parámetros.

| Nombre | Descripción |
|----|----|
| `resource=<flujo a filtrar>` | Este parámetro es requerido. Especifica el flujo que se desea filtrar. |
| `read=<lista de filtros a aplicar a la lectura>` | Este parámetro es opcional. Uno o más nombres de filtros pueden ser proporcionados aquí, separados por un carácter pipe (`|`). |
| `write=<lista de filtros a aplicar a la escritura>` | Este parámetro es opcional. Uno o más nombres de filtros pueden ser proporcionados aquí, separados por un carácter pipe (`|`). |
| `<lista de filtros a aplicar tanto a la lectura como a la escritura>` | Todos los filtros proporcionados sin ser prefijados por `read=` o `write=` serán aplicados tanto a la lectura como a la escritura. |

Parámetros de php://filter {role="stream_wrapper"}

## Opciones

| Atributo | Soportado |
|----|----|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen) | No |
| Restringido por [allow_url_include](#ini.allow-url-include) | `php://input`, `php://stdin`, `php://memory` y `php://temp` únicamente. |
| Permite la lectura | `php://stdin`, `php://input`, `php://fd`, `php://memory` y `php://temp` únicamente. |
| Permite la escritura | `php://stdout`, `php://stderr`, `php://output`, `php://fd`, `php://memory` y `php://temp` únicamente. |
| Permite la adición | `php://stdout`, `php://stderr`, `php://output`, `php://fd`, `php://memory` y `php://temp` únicamente. (Equivalente a la escritura) |
| Permite tanto la lectura como la escritura | `php://fd`, `php://memory` y `php://temp` únicamente. |
| Soporte de la función `stat` | No. Sin embargo, `php://memory` y `php://temp` soportan `fstat`. |
| Soporte de la función `unlink` | No |
| Soporte de la función `rename` | No |
| Soporte de la función `mkdir` | No |
| Soporte de la función `rmdir` | No |
| Soporte de la función `stream_select` | `php://stdin`, `php://stdout`, `php://stderr`, `php://fd` y `php://temp` únicamente. |

Resumen de la envoltura (para `php://filter`, consúltese el resumen de la envoltura a filtrar) {role="stream_wrapper"}

## Ejemplos

php://temp/maxmemory

Este parámetro opcional permite configurar el límite de memoria antes de que `php://temp` comience a utilizar un fichero temporal.

```php
<?php
// Define el límite a 5 Mo.
$fiveMBs = 5 * 1024 * 1024;
$fp = fopen("php://temp/maxmemory:$fiveMBs", 'r+');

fputs($fp, "hello\n");

// Lee lo que acabamos de escribir.
rewind($fp);
echo stream_get_contents($fp);
?>

   
```

php://filter/resource=\<flujo a filtrar\>

Este parámetro debe ser colocado al final de la especificación de `php://filter` y debe apuntar al flujo que se desea filtrar.

```php
<?php
/* Esto es equivalente a
  readfile("http://www.example.com");
  ya que no se especifica ningún filtro */

readfile("php://filter/resource=http://www.example.com");
?>

   
```

php://filter/read=\<lista de filtros a aplicar a la lectura\>

Este parámetro toma uno o más nombres de filtros separados por un carácter pipe `|`.

```php
<?php
/* Esto mostrará el contenido de
  www.example.com completamente en mayúsculas */
readfile("php://filter/read=string.toupper/resource=http://www.example.com");

/* Esto hará lo mismo que el anterior,
  pero codificará además el resultado en ROT13 */
readfile("php://filter/read=string.toupper|string.rot13/resource=http://www.example.com");
?>

   
```

php://filter/write=\<lista de filtros a aplicar a la escritura\>

Este parámetro toma uno o más nombres de filtros separados por un carácter pipe `|`.

```php
<?php
/* Esto filtrará la cadena "Hello World"
  a través del filtro rot13, y luego escribirá el resultado
  en el fichero example.txt del directorio actual */
file_put_contents("php://filter/write=string.rot13/resource=example.txt","Hello World");
?>

   
```

php://memory y php://temp no son reutilizables

`php://memory` y `php://temp` no son reutilizables, es decir, después de que los flujos hayan sido cerrados no hay manera de referenciarlos nuevamente.

```php
<?php
file_put_contents('php://memory', 'PHP');
echo file_get_contents('php://memory'); // no muestra nada

   
```

php://input para leer datos JSON del cuerpo de la solicitud

Este ejemplo demuestra cómo leer datos JSON sin procesar de solicitudes POST, PUT y PATCH usando `php://input`.

```php
<?php
$input = file_get_contents("php://input");
$json_array = json_decode(
  json: $input,
  associative: true,
  flags: JSON_THROW_ON_ERROR
);

echo "Datos JSON recibidos: ";
print_r($json_array);
?>

   
```
