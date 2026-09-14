---
title: SplFileObject::__construct
description: Construye un nuevo objeto de fichero
source_url: https://www.php.net/manual/es/splfileobject.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 84310
---

SplFileObject::\_\_construct

Construye un nuevo objeto de fichero

## Descripción

```php
public SplFileObject::__construct(string $filename, [string $mode], [bool $useIncludePath], [resource $context])
```php

Construye un nuevo objeto de fichero.

## Parámetros

`filename`  
El fichero a leer.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

`mode`  
El modo en el que abrir el fichero. Véase `fopen` para una lista de los modos permitidos.

`useIncludePath`  
Si se va a buscar `filename` en el [include_path](#ini.include-path).

`context`  
Un contexto válido creado con `stream_context_create`.

## Errores/Excepciones

Lanza una `RuntimeException` si `filename` no se puede abrir.

Lanza una `LogicException` si `filename` es un directorio.

## Ejemplos

Ejemplo de SplFileObject::\_\_construct

Este ejemplo abre el fichero actual y recorre su contenido, línea por línea.

```
<?php
$fichero = new SplFileObject(__FILE__);
foreach ($fichero as $num_línea => $línea) {
    echo "La línea $num_línea es $línea";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    La línea 0 es <?php
    La línea 1 es $fichero = new SplFileObject(__FILE__);
    La línea 2 es foreach ($fichero as $num_línea => $línea) {
    La línea 3 es     echo "La línea $num_línea es $línea";
    La línea 4 es }
    La línea 5 es ?>

## Véase también

SplFileInfo::openFile, `fopen`
