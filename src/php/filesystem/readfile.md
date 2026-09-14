---
title: readfile
description: Muestra un fichero
source_url: https://www.php.net/manual/es/function.readfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/readfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: ea62fb831
order: 23940
---

readfile

Muestra un fichero

## Descripción

```php
readfile(string $filename, [bool $use_include_path], [resource $context]): int
```php

Lee un fichero y lo envía al buffer de salida.

## Parámetros

`filename`  
El fichero a leer.

`use_include_path`  
Puede utilizarse el segundo argumento opcional para explorar el directorio [include_path](#ini.include-path), pasando el valor de `true`.

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Devuelve el número de bytes leídos desde el fichero en caso de éxito, o `false` si ocurre un error

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Forzar la descarga utilizando `readfile`

```
<?php
$file = 'monkey.gif';

if (file_exists($file)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($file).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($file));
    readfile($file);
    exit;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Ventana de apertura / guardado](en/reference/filesystem/figures/readfile.png)

## Notas

> [!NOTE]
> `readfile` no presentará problemas de memoria, incluso al enviar ficheros grandes. Si se encuentran este tipo de problemas, asegúrese de que el buffer de salida está desactivado con la función `ob_get_level`.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Véase también

`fpassthru`, `file`, `fopen`, `include`, `require`, `virtual`, `file_get_contents`, [???](#wrappers)
