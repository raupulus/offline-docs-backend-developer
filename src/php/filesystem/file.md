---
title: file
description: Lee el fichero y devuelve el resultado en un array
source_url: https://www.php.net/manual/es/function.file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: 89b506b5b
order: 23490
---

file

Lee el fichero y devuelve el resultado en un array

## Descripción

```php
file(string $filename, [int $flags], [resource $context]): array
```php

Lee el fichero y devuelve el resultado en un array.

> [!NOTE]
> Puede utilizarse la función `file_get_contents` para devolver el contenido de un fichero en un `string`.

## Parámetros

`filename`  
Ruta de acceso al fichero.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

`flags`  
El argumento opcional `flags` puede ser una o más de las siguientes constantes:

`FILE_USE_INCLUDE_PATH`  
Busca el fichero en el [include_path](#ini.include-path).

`FILE_IGNORE_NEW_LINES`  
No añade nueva línea al final de cada elemento del array.

`FILE_SKIP_EMPTY_LINES`  
Ignora las líneas vacías.

`FILE_NO_DEFAULT_CONTEXT`  
No utiliza el contexto por omisión.

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Devuelve el fichero en un array. Cada elemento del array corresponde a una línea del fichero, y los retornos de carro se colocan al final de la línea. Si ocurre un error, `file` devolverá `false`.

> [!NOTE]
> Cada línea del array resultante incluirá un final de línea, a menos que se utilice `FILE_IGNORE_NEW_LINES`.

> [!NOTE]
> Si PHP no reconoce correctamente los finales de línea al leer ficheros que han sido creados o leídos en un Macintosh, la activación de la opción de configuración [auto_detect_line_endings](#ini.auto-detect-line-endings) puede resolver el problema.

## Errores/Excepciones

A partir de PHP 8.3.0, se lanza una excepción ValueError si el `flags` contiene valores inválidos, como `FILE_APPEND`.

Emite un error de nivel `E_WARNING` si el fichero no existe.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Se lanza una excepción ValueError para cualquier valor inválido del `flags`. |

## Ejemplos

Ejemplo con `file`

```
<?php
// Lee una página web en un array.
$lines = file('http://www.example.com/');

// Muestra todas las líneas del array como código HTML, con los números de línea
foreach ($lines as $line_num => $line) {
    echo "Line #<b>{$line_num}</b> : " . htmlspecialchars($line) . "<br />\n";
}

// Uso de flag
$trimmed = file('somefile.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
?>

    
```php

## Notas

> [!WARNING]
> Cuando SSL es utilizado, el servidor IIS de Microsoft violará el protocolo al cerrar la conexión sin enviar un indicador `close_notify`. PHP lo reportará como "SSL: Fatal Protocol Error" cuando se llegue al final de los datos. Para evitar esto, el nivel de la directiva [error_reporting](#ini.error-reporting) debe ser bajado para no incluir los avisos. PHP puede detectar automáticamente los servidores IIS defectuosos al abrir el flujo utilizando `https://` y suprimirá el aviso. Al utilizar `fsockopen` para crear un socket `ssl://`, es responsabilidad del desarrollador detectar y suprimir el aviso.

## Véase también

`file_get_contents`, `readfile`, `fopen`, `fsockopen`, `popen`, `include`, `stream_context_create`
