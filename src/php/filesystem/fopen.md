---
title: fopen
description: Abre un fichero o un URL
source_url: https://www.php.net/manual/es/function.fopen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fopen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 18bac8389
order: 23610
---

fopen

Abre un fichero o un URL

## Descripción

```php
fopen(string $filename, string $mode, [bool $use_include_path], [resource $context]): resource
```php

`fopen` asocia un recurso con nombre, especificado por `filename`, a un flujo.

## Parámetros

`filename`  
Si `filename` está en la forma "esquema://...", se asume que será un URL y PHP buscará un gestor de protocolos (también conocido como envoltura) para ese protocolo. Si no está registrada ninguna envoltura para ese protocolo, PHP emitirá un aviso para ayudar a rastrear problemas potenciales en el script y continuará como si `filename` especificara un fichero normal.

Si PHP ha decidido que `filename` especifica un fichero local, intentará abrir un flujo para ese fichero. El fichero debe ser accesible para PHP, por lo que es necesario asegurarse de que los permisos de acceso del fichero permiten este acceso. Si está habilitado [open_basedir](#ini.open-basedir) se pueden aplicar más restricciones.

Si PHP ha decidido que `filename` especifica un protocolo registrado, y ese protocolo está registrado como un URL de red, PHP se asegurará de que [allow_url_fopen](#ini.allow-url-fopen) está habilitado. Si es desactivado, PHP emitirá un aviso y la llamada a fopen fallará.

> [!NOTE]
> La lista de protocolos soportados se puede encontrar en [???](#wrappers). Algunos protocolos (también descritos como `envolturas`) soportan `contexto` y/u opciones de `php.ini`. Consulte la página específica del protocolo en uso para una lista de opciones que se pueden establecer. (p.ej. el valor `user_agent` en `php.ini` usado por la envoltura `http`).

En la plataforma Windows, asegúrese de escapar cualquier barra invertida usada en la ruta de fichero, o use barras hacia delante.

```
<?php
$handle = fopen("c:\\folder\\resource.txt", "r");
?>

        
```php

`mode`  
El parámetro `mode` especifica el tipo de acceso que se necesita para el flujo. Puede ser cualquiera de los siguientes:

| `mode` | Descripción |
|----|----|
| `'r'` | Apertura para sólo lectura; coloca el puntero al fichero al principio del fichero. |
| `'r+'` | Apertura para lectura y escritura; coloca el puntero al fichero al principio del fichero. |
| `'w'` | Apertura para sólo escritura; coloca el puntero al fichero al principio del fichero y trunca el fichero a longitud cero. Si el fichero no existe se intenta crear. |
| `'w+'` | Abre para lectura y escritura; de otro modo, tiene el mismo comportamiento que `'w'`. |
| `'a'` | Apertura para sólo escritura; coloca el puntero del fichero al final del mismo. Si el fichero no existe, se intenta crear. En este modo, `fseek` no tiene efecto, escribe siempre agregando. |
| `'a+'` | Apertura para lectura y escritura; coloca el puntero del fichero al final del mismo. Si el fichero no existe, se intenta crear. En este modo, `fseek` solo afecta a la posición de lectura, escribe siempre agregando. |
| `'x'` | Creación y apertura para sólo escritura; coloca el puntero del fichero al principio del mismo. Si el fichero ya existe, la llamada a `fopen` fallará devolviendo `false` y generando un error de nivel `E_WARNING`. Si el fichero no existe se intenta crear. Esto es equivalente a especificar las flags `O_EXCL|O_CREAT` para la llamada al sistema de `open(2)` subyacente. |
| `'x+'` | Creación y apertura para lectura y escritura; de otro modo tiene el mismo comportamiento que `'x'`. |
| `'c'` | Abre el fichero para sólo escritura. Si el fichero no existe, se crea. Si existe no es truncado (a diferencia de `'w'`), ni la llamada a esta función falla (como en el caso con `'x'`). El puntero al fichero se posiciona en el principio del fichero. Esto puede ser útil si se desea obtener un bloqueo asistido (véase `flock`) antes de intentar modificar el fichero, ya que al usar `'w'` se podría truncar el fichero antes de haber obtenido el bloqueo (si se desea truncar el fichero, se puede usar `ftruncate` después de solicitar el bloqueo). |
| `'c+'` | Abre el fichero para lectura y escritura; de otro modo tiene el mismo comportamiento que `'c'`. |
| `'e'` | Establece el flag 'close-on-exec' en el descriptor de fichero abierto. Disponible solamente en PHP compilado en sistemas compatibles con POSIX.1-2008. |
| `'n'` | Establecer el flag de no bloqueo en el descriptor de fichero abierto. Disponible solamente en PHP compilado en sistemas compatibles con POSIX.1-2008. |

Una lista de los modos posibles de `fopen` usando `mode`

> [!NOTE]
> Diferentes familias de sistemas operativos tienen diferentes convenciones para el final de línea. Cuando escribe un fichero de texto y quiere insertar un salto de línea, necesita usar el carácter o caracteres correctos de final de línea para su sistema operativo. Los sistemas basados en Unix usan `\n` como el carácter de final de línea, los sistemas basados en Windows usan `\r\n` como caracteres de final de línea y los sistemas basados en Macintosh usan `\r` como carácter de final de línea.
>
> Si usa los caracteres de final de línea erróneos cuando escribe sus ficheros, se podrá encontrar con que otras aplicaciones que abran esos ficheros "parecerán raras".
>
> Windows ofrece un flag de trasnformación en modo texto (`'t'`) que transformará de manera transparente `\n` a `\r\n` cuando se trabaja con el fichero. En contraste, puede usar `'b'` para forzar el modo binario, lo cual no transformará su información. Para usar estas flags, especifique `'b'` o `'t'` como el último carácter del parámetro `mode`.
>
> El modo de transformación por omición es `'b'`. Puede usar el modo `'t'` si está trabajando con ficheros de texto plano y usa `\n` para delimitar los finales de línea es su script, pero espera que sus ficheros sean legibles con aplicaciones como versiones antiguas de notepad. Debería usar el `'b'` en todos los demás casos.
>
> Si especifica el flag 't' cuando trabaja con archivos binarios, puede experimentar problemas extraños con sus datos, incluyendo archivos de imagen rotos y problemas extraños con los caracteres `\r\n`.

> [!NOTE]
> Por portabilidad, También se recomienda encarecidamente que reescriba el código que usa o se basa en el modo `'t'` para que use las terminaciones de línea correctas y el modo `'b'` en su lugar.

> [!NOTE]
> El `mode` modo es ignorado para `php://output`, `php://input`, `php://stdin`, `php://stdout`, `php://stderr` Y envoluturas de flujo `php://fd`.

`use_include_path`  
El tercer parámetro opcional `use_include_path` puede ser establecido a '1' o `true` si se desea buscar un fichero también en [include_path](#ini.include-path).

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Devuelve un recurso de puntero a fichero si tiene éxito, o `false` si ocurre un error

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Historial de cambios

| Versión       | Descripción                |
|---------------|----------------------------|
| 7.0.16, 7.1.2 | Se añadió la opción `'e'`. |

## Ejemplos

Ejemplos de `fopen`

```
<?php
$handle = fopen("/home/rasmus/fichero.txt", "r");
$handle = fopen("/home/rasmus/fichero.gif", "wb");
$handle = fopen("http://www.ejemplo.com/", "r");
$handle = fopen("ftp://user:password@example.com/fichero.txt", "w");
?>

    
```php

## Notas

> [!WARNING]
> Cuando SSL es utilizado, el servidor IIS de Microsoft violará el protocolo al cerrar la conexión sin enviar un indicador `close_notify`. PHP lo reportará como "SSL: Fatal Protocol Error" cuando se llegue al final de los datos. Para evitar esto, el nivel de la directiva [error_reporting](#ini.error-reporting) debe ser bajado para no incluir los avisos. PHP puede detectar automáticamente los servidores IIS defectuosos al abrir el flujo utilizando `https://` y suprimirá el aviso. Al utilizar `fsockopen` para crear un socket `ssl://`, es responsabilidad del desarrollador detectar y suprimir el aviso.

> [!NOTE]
> Si está experimentando problemas al leer y escribir ficheros y está usando la versión de módulo de servidor de PHP, asegúrese de que los ficheros y directorios que está usando sean accesibles por el proceso del servidor.

> [!NOTE]
> Esta función también podría tener éxito cuando `filename` es un directorio. Si no se está seguro de que `filename` sea un fichero o un directorio, podría ser necesario utilzar la función `is_dir` antes de llamar a `fopen`.

## Véase también

[???](#wrappers), `fclose`, `fgets`, `fread`, `fwrite`, `fsockopen`, `file`, `file_exists`, `is_readable`, `stream_set_timeout`, `popen`, `stream_context_create`, `umask`, `SplFileObject`
