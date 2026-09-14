---
title: file_get_contents
description: Lee todo un fichero en una cadena
source_url: https://www.php.net/manual/es/function.file-get-contents.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/file-get-contents.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 3abd17e61
order: 23470
---

file_get_contents

Lee todo un fichero en una cadena

## Descripción

```php
file_get_contents(string $filename, [bool $use_include_path], [resource $context], [int $offset], [int $length]): string
```php

Similar a la función `file`, excepto que `file_get_contents` devuelve el fichero `filename` en una cadena, comenzando desde la posición `offset` y hasta `length` bytes. En caso de error, `file_get_contents` devuelve `false`.

`file_get_contents` es el método recomendado para leer el contenido de un fichero en una `string`. Utilizará un buffer en memoria si este mecanismo es soportado por el sistema, con el fin de mejorar el rendimiento.

> [!NOTE]
> Si se abre una URI con caracteres especiales, como espacios, es necesario codificar esta URI con la función `urlencode`.

## Parámetros

`filename`  
Nombre del fichero a leer.

`use_include_path`  
> [!NOTE]
> La constante `FILE_USE_INCLUDE_PATH` puede ser utilizada para activar la búsqueda en el [ruta de inclusión](#ini.include-path). Esto no es posible si [strict typing](#language.types.declarations.strict) está activado, ya que `FILE_USE_INCLUDE_PATH` es un `int`. Utilice `true` en su lugar.

`context`  
Un recurso de contexto válido, creado con la función `stream_context_create`. Si no es necesario utilizar un contexto específico, este parámetro puede ser omitido asignándole el valor `null`.

`offset`  
La posición desde la cual se comienza a leer en el flujo original. Una posición negativa cuenta desde el final del flujo.

El desplazamiento en el fichero (`offset`) no es soportado en ficheros remotos. Si se intenta desplazarse en un fichero que no es local puede funcionar en pequeños desplazamientos, pero el comportamiento puede no ser el esperado ya que el proceso utiliza el flujo del buffer.

`length`  
El tamaño máximo de datos a leer. El comportamiento por defecto es leer hasta el final del fichero. Este parámetro se aplica al flujo procesado por los filtros.

## Valores devueltos

Devuelve los datos leídos o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

Genera una advertencia de tipo `E_WARNING` si, `filename` no puede ser encontrado, si el parámetro `length` es menor que cero, o si el desplazamiento a la posición `offset` especificado en el flujo falla.

Cuando `file_get_contents` es llamado sobre un directorio, se genera un error de nivel `E_WARNING` en Windows, y a partir de PHP 7.4 en otros sistemas operativos también.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.0.0   | `length` ahora es nullable.                          |
| 7.1.0   | Se añade soporte para posiciones `offset` negativas. |

## Ejemplos

Lee y muestra el código HTML de un sitio web

```
<?php
$homepage = file_get_contents('http://www.example.com/');
echo $homepage;
?>

    
```php

Busca un fichero en el include_path

```
<?php
// Si el tipado estricto está activado c.à.d. declare(strict_types=1);
$file = file_get_contents('./people.txt', true);
// De lo contrario
$file = file_get_contents('./people.txt', FILE_USE_INCLUDE_PATH);
?>

    
```php

Lee una sección de un fichero

```
<?php
// Lee 14 caracteres a partir del 21º carácter
$section = file_get_contents('./people.txt', FALSE, NULL, 20, 14);
var_dump($section);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(14) "lle Bjori Ro"

Uso de contextos de flujo

```
<?php
// Creación de un flujo
$opts = [
  'http'=> [
    'method'=>"GET",
    'header'=>"Accept-language: en\r\n" .
              "Cookie: foo=bar\r\n",
  ]
];

$context = stream_context_create($opts);

// Acceso a un fichero HTTP con los encabezados HTTP indicados arriba
$file = file_get_contents('http://www.example.com/', false, $context);
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

> [!WARNING]
> Cuando SSL es utilizado, el servidor IIS de Microsoft violará el protocolo al cerrar la conexión sin enviar un indicador `close_notify`. PHP lo reportará como "SSL: Fatal Protocol Error" cuando se llegue al final de los datos. Para evitar esto, el nivel de la directiva [error_reporting](#ini.error-reporting) debe ser bajado para no incluir los avisos. PHP puede detectar automáticamente los servidores IIS defectuosos al abrir el flujo utilizando `https://` y suprimirá el aviso. Al utilizar `fsockopen` para crear un socket `ssl://`, es responsabilidad del desarrollador detectar y suprimir el aviso.

## Véase también

`file`, `fgets`, `fread`, `readfile`, `file_put_contents`, `stream_get_contents`, `stream_context_create`, [\$http_response_header](#reserved.variables.httpresponseheader)
