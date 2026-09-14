---
title: fann_read_train_from_file
description: Lee un fichero que almacena datos de entrenamiento
source_url: https://www.php.net/manual/es/function.fann-read-train-from-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-read-train-from-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 9ee27f088
order: 21650
---

fann_read_train_from_file

Lee un fichero que almacena datos de entrenamiento

## Descripción

```php
fann_read_train_from_file(string $filename): resource
```php

Lee un fichero que almacena datos de entrenamiento.

## Parámetros

`filename`  
El fichero de entrada con el siguiente formato:

```
número_datos_entrenamiento número_entradas número_salidas
datos de entrada separados por un espacio
datos de salida separados por un espacio

.
.
.

datos de entrada separados por un espacio
datos de salida separados por un espacio

     
```php

## Valores devueltos

Devuelve un `resource` de datos de entrenamiento en caso de éxito, o `false` en caso de error.

## Ejemplos

Ejemplo de fann_read_train_from_file

```
<?php
$train_data = fann_read_train_from_file("xor.data");
if ($train_data) {
    // Hacer algo con $train_data para la función XOR
}
?>

    
```php

Contenido de xor.data

```
4 2 1
-1 -1
-1
-1 1
1
1 -1
1
1 1
-1

    
```php

## Véase también

`fann_train_on_data`, `fann_destroy_train`, `fann_save_train`
