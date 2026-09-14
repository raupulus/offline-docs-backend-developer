---
title: Ejemplos
source_url: https://www.php.net/manual/es/fann.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: c2aeb63e3
order: 20830
---

## Ejemplos

## Entrenamiento XOR

Este ejemplo muestra cómo entrenar datos para una función XOR

Fichero xor.data

```php
4 2 1
-1 -1
-1
-1 1
1
1 -1
1
1 1
-1

    
```

Entrenamiento sencillo

```php
<?php
$num_entradas = 2;
$num_salidas = 1;
$num_capas = 3;
$num_neuronas_ocultas = 3;
$error_deseado = 0.001;
$máx_épocas = 500000;
$épocas_entre_informes = 1000;

$rna = fann_create_standard($num_capas, $num_entradas, $num_neuronas_ocultas, $num_salidas);

if ($rna) {
    fann_set_activation_function_hidden($rna, FANN_SIGMOID_SYMMETRIC);
    fann_set_activation_function_output($rna, FANN_SIGMOID_SYMMETRIC);

    $nombre_fichero = dirname(__FILE__) . "/xor.data";
    if (fann_train_on_file($rna, $nombre_fichero, $máx_épocas, $épocas_entre_informes, $error_deseado))
        fann_save($rna, dirname(__FILE__) . "/xor_float.net");

    fann_destroy($rna);
}
?>

    
```

Este ejemplo muestra cómo leer y ejecutar datos para una función XOR

Prueba sencilla

```php
<?php
$fichero_entrenamiento = (dirname(__FILE__) . "/xor_float.net");
if (!is_file($fichero_entrenamiento))
    die("El fichero xor_float.net no ha sido creado. Ejecute simple_train.php para generarlo");

$rna = fann_create_from_file($fichero_entrenamiento);
if (!$rna)
    die("No se pudo crear ANN");

$entrada = array(-1, 1);
$calc_out = fann_run($rna, $entrada);
printf("xor test (%f,%f) -> %f\n", $entrada[0], $entrada[1], $calc_out[0]);
fann_destroy($rna);
?>

    
```
