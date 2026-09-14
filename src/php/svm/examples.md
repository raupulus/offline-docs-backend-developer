---
title: Ejemplos
source_url: https://www.php.net/manual/es/svm.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89660
---

## Ejemplos

El proceso básico consiste en definir argumentos, someter datos de entrenamiento para la generación de un modelo y, posteriormente, realizar predicciones basadas en este modelo. Existe un conjunto predeterminado de argumentos que deberían proporcionar resultados con la mayoría de las entradas, por lo que se comenzará examinando estos datos.

Los datos se someten a través de un fichero, un flujo o un array. Si se proporcionan a través de un fichero o un flujo, deben contener una línea por ejemplo de entrenamiento, la cual debe estar formateada como una clase entera (generalmente 1 y -1), seguida de una serie de pares clave/característica en orden creciente de características. Las características son enteros y los valores son números de punto flotante en el rango 0-1. Por ejemplo:

-1 1:0.43 3:0.12 9284:0.2

En un problema de clasificación de documentos, por ejemplo, relacionado con el spam, cada línea debe representar un documento. Debe haber 2 clases, -1 para el spam y 1 para el ham. Cada característica representa palabras y los valores representan la importancia de estas palabras en el documento (por ejemplo, la frecuencia de aparición de estas palabras en el documento, con el total en el rango adecuado). Las características con valor 0 (es decir, la palabra no aparece en absoluto en el documento) simplemente no se incluirán.

En el modo array, los datos deben pasarse en forma de arrays de arrays. Cada subarray debe tener la clase como primer elemento, más pares clave =\> valor para las características/valor.

Estos datos se pasan a la función de entrenamiento de la clase SVM, que devolverá un modelo SVM en caso de éxito.

Una vez generado el modelo, puede utilizarse para realizar predicciones sobre datos no vistos previamente. Estos pueden pasarse en forma de array a la función de predicción del modelo, en el mismo formato que antes, pero sin la etiqueta. La respuesta será la clase.

Los modelos pueden guardarse y restaurarse según sea necesario, utilizando las funciones de guardado y carga, que toman como argumento la ruta al fichero correspondiente.

Entrenamiento desde un array

```php
    
<?php
$data = array(
 array(-1, 1 => 0.43, 3 => 0.12, 9284 => 0.2),
 array(1, 1 => 0.22, 5 => 0.01, 94 => 0.11),
);

$svm = new SVM();
$model = $svm->train($data);

$data = array(1 => 0.43, 3 => 0.12, 9284 => 0.2);
$result = $model->predict($data);
var_dump($result);
$model->save('model.svm');
?>

   
```

Resultado del ejemplo anterior es similar a:

        
    int(-1)

Entrenamiento desde un fichero

```php
    
<?php
 $svm = new SVM();
 $model = $svm->train("traindata.txt");
?>

   
```
