---
title: file_put_contents
description: Escribe datos en un fichero
source_url: https://www.php.net/manual/es/function.file-put-contents.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/file-put-contents.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: ea62fb831
order: 23480
---

file_put_contents

Escribe datos en un fichero

## Descripción

```php
file_put_contents(string $filename, mixed $data, [int $flags], [resource $context]): int
```php

Equivale a llamar a las funciones `fopen`, `fwrite` y `fclose` sucesivamente.

Si el fichero `filename` no existe, será creado. De lo contrario, el fichero existente será sobrescrito, a menos que la opción `FILE_APPEND` esté definida.

## Parámetros

`filename`  
Ruta de acceso al fichero en el que se deben escribir los datos.

`data`  
Los datos a escribir. Puede ser un string, un array o un recurso de flujo (explicación más abajo).

Si `data` es un recurso de tipo `stream`, el buffer restante de este flujo será copiado al fichero especificado. Esto equivale a utilizar la función `stream_copy_to_stream`.

Asimismo, puede especificarse el argumento `data` como un array de una sola dimensión. Esto equivale a `file_put_contents($filename, implode('', $array))`.

`flags`  
El valor del argumento `flags` puede ser cualquier combinación de los siguientes flags, unidos por el operador OR binario (`|`).

| Flag | Descripción |
|----|----|
| `FILE_USE_INCLUDE_PATH` | Busca el fichero `filename` en el directorio de inclusión. Ver [include_path](#ini.include-path) para más información. |
| `FILE_APPEND` | Si el fichero `filename` ya existe, esta opción permite añadir los datos al fichero en lugar de sobrescribirlo. |
| `LOCK_EX` | Adquiere un bloqueo exclusivo sobre el fichero durante la operación de escritura. En otras palabras, se realiza una llamada a la función `flock` entre la llamada a la función `fopen` y la llamada a la función `fwrite`. Este comportamiento no es idéntico a una llamada a la función `fopen` con el modo "x". |

Flags disponibles

`context`  
Un recurso de contexto válido creado con la función `stream_context_create`.

## Valores devueltos

Devuelve el número de bytes que han sido escritos al fichero, o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Uso simple de file_put_contents

```
<?php
$file = 'people.txt';
// Abre un fichero para leer un contenido existente
$current = file_get_contents($file);
// Añade una persona
$current .= "Jean Dupond\n";
// Escribe el resultado en el fichero
file_put_contents($file, $current);
?>

    
```php

Uso de opciones para file_put_contents

```
<?php
$file = 'people.txt';
// Una nueva persona a añadir
$person = "Jean Dupond\n";
// Escribe el contenido en el fichero, utilizando el flag
// FILE_APPEND para añadir al final del fichero y
// LOCK_EX para evitar que otros escriban en el fichero
// al mismo tiempo
file_put_contents($file, $person, FILE_APPEND | LOCK_EX);
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Véase también

`fopen`, `fwrite`, `file_get_contents`, `stream_context_create`
