---
title: fann_create_train_from_callback
description: Crea una estructura de datos de entrenamiento desde una función proporcionada
  por el usuario
source_url: https://www.php.net/manual/es/function.fann-create-train-from-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-train-from-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 21010
---

fann_create_train_from_callback

Crea una estructura de datos de entrenamiento desde una función proporcionada por el usuario

## Descripción

```php
fann_create_train_from_callback(int $num_data, int $num_input, int $num_output, callable $user_function): resource
```php

Crea una estructura de datos de entrenamiento desde una función proporcionada por el usuario. Debido a que los datos de entrenamiento se numeran (datos 1, datos 2...), el usuario debe escribir una función que reciba el número del conjunto de datos de entrenamiento (entrada, salida) y que devuelva el conjunto.

## Parámetros

`num_data`  
El número de datos de entrenamiento

`num_input`  
El número de entradas por datos de entrenamiento

`num_output`  
El número de salidas por datos de entrenamiento

`user_function`  
La función proporcionada por elusuario con los siguientes parámetros: `num` - El número del conjunto de datos de entrenamiento, `num_input` - El número de entradas por datos de entrenamiento, `num_output` - El número de salidas por datos de entrenamiento

La función debería devolver un array asociativo con las claves `input` y `output` y con dos valores para la entrada y la salida.

## Valores devueltos

Devuelve un `resource` de datos de entrenamiento en caso de éxito, o `false` en caso de error.

## Ejemplos

Ejemplo de fann_create_train_from_callback

```
<?php
function create_train_callback($num_data, $num_input, $num_output) {
    return array(
        "input" => array_fill(0, $num_input, 1),
        "output" => array_fill(0, $num_output, 1),
    );
}

$num_data = 3;
$num_input = 2;
$num_output = 1;
$train_data = fann_create_train_from_callback($num_data, $num_input, $num_output, "create_train_callback");
if ($train_data) {
    // Hacer algo con $train_data
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_read_train_from_file`, `fann_train_on_data`, `fann_destroy_train`, `fann_save_train`
