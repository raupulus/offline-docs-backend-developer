---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/fann.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 6a8c8a94c
order: 20820
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`FANN_TRAIN_INCREMENTAL` (`int`)  
Algoritmo de retropropagación estándar, donde los pesos se actualizan después de cada patrón de entrenamiento. Esto significa que los pesos se actualizan muchas veces durante una única época. Por este motivo, algunos problemas entrenarán muy rápido con este algoritmo, mientras que problemas más avanzados no entrenarán muy bien.

`FANN_TRAIN_BATCH` (`int`)  
Algoritmo de retropropagación estándar, donde los pesos se actualizan después de calcular el error cuadrático medio para el conjunto de entrenamiento completo. Esto significa que los pesos solamente se actualizan una vez durante una época. Por este motivo, algunos problemas entrenarán más lento con este algoritmo. Aunque debido a que el error cuadrático medio se calcula más correctamente que en el entrenamiento incremental, algunos probleamas alcanzarán soluciones mejores con este algoritmo.

`FANN_TRAIN_RPROP` (`int`)  
Un algoritmo de entrenamiento por lotes más avanzado que alcanza buenos resultados para muchos problemas. El algoritmo de entrenamiento RPROP es adaptativo, por lo que no emplea learning_rate. Sin embargo, se pueden establecer otros parámetros para cambiar la manera en que funciona el algoritmo RPROP, aunque solamente se recomienda para usuarios que sepan cómo funciona el algoritmo de entrenamiento RPROP. El algoritmo de entrenamiento RPROP está descrito por \[Riedmiller y Braun, 1993\], aunque el algoritmo real de aprendizaje utilizado aquí es el algoritmo de entrenamiento iRPROP-, el cual está descrito por \[Igel y Husken, 2000\], y es una variedad del algoritmo de entrenamiento RPROP estándar.

`FANN_TRAIN_QUICKPROP` (`int`)  
Un algoritmo de entrenamiento por lotes más avanzado que alcanza buenos resultados para muchos problemas. El algoritmo de entrenamiento quickprop emplea el parámetro learning_rate junto con otros parámetros más avanzados, aunque solamente se recomienda cambiar estos parámetros avanzados a usuarios que sepan cómo funciona el algoritmo de entrenamiento quickprop. El algoritmo de entrenamiento quickprop está descrito por \[Fahlman, 1988\].

`FANN_TRAIN_SARPROP` (`int`)  
Algoritmo de entrenamiento más avanzado aún. Solamente para la versión 2.2

<!-- -->

`FANN_LINEAR` (`int`)  
Función de activación lineal.

`FANN_THRESHOLD` (`int`)  
Función de activación de umbral.

`FANN_THRESHOLD_SYMMETRIC` (`int`)  
Función de activación de umbral.

`FANN_SIGMOID` (`int`)  
Función de activación sigmoide.

`FANN_SIGMOID_STEPWISE` (`int`)  
Aproximación lineal escalonada a la sigmoide.

`FANN_SIGMOID_SYMMETRIC` (`int`)  
Función de activación sigmoide simétrica, también conocida como tanh.

`FANN_SIGMOID_SYMMETRIC_STEPWISE` (`int`)  
Aproximación lineal escalonada a la sigmoide simétrica.

`FANN_GAUSSIAN` (`int`)  
Función de activación gaussiana.

`FANN_GAUSSIAN_SYMMETRIC` (`int`)  
Función de activación gaussiana simétrica.

`FANN_GAUSSIAN_STEPWISE` (`int`)  
Función de activación gaussiana escalonada.

`FANN_ELLIOT` (`int`)  
Función de activación rápida (igual que la sigmoide) definida por David Elliott.

`FANN_ELLIOT_SYMMETRIC` (`int`)  
Función de activación rápida (igual que la sigmoide simétrica) definida por David Elliott.

`FANN_LINEAR_PIECE` (`int`)  
Función de activación lineal acotada.

`FANN_LINEAR_PIECE_SYMMETRIC` (`int`)  
Función de activación lineal acotada.

`FANN_SIN_SYMMETRIC` (`int`)  
Función de activación sinusal periódica.

`FANN_COS_SYMMETRIC` (`int`)  
Función de activación cosinusal periódica.

`FANN_SIN` (`int`)  
Función de activación sinusal periódica.

`FANN_COS` (`int`)  
Función de activación cosinusal periódica.

<!-- -->

`FANN_ERRORFUNC_LINEAR` (`int`)  
Función de error lineal estándar.

`FANN_ERRORFUNC_TANH` (`int`)  
Función de erorr tanh, normalmente mejor, aunque puede requerir un índice de aprendizaje menor. Esta función de error dirige de forma agresiva las salidas que difieren mucho de las deseadas, mientras que no dirige las salidas que únicamente difieren más bien poco. No se recomienda para el entrenamiento en cascada o incremental.

<!-- -->

`FANN_STOPFUNC_MSE` (`int`)  
El criterio de parada el es valor del Error Cuadrático Medio (ECM - MSE por sus siglas en inglés).

`FANN_STOPFUNC_BIT` (`int`)  
El criterio de parada es el número de bit que fallan. El número de bit significa el número de neuronas de salida que difieren más del límite de fallo de bit (véanse fann_get_bit_fail_limit y fann_set_bit_fail_limit). Los bit se cuentan en todos los datos de entrenamiento, por lo que este número puede ser mayor que el número de datos de entrenamiento.

<!-- -->

`FANN_NETTYPE_LAYER` (`int`)  
Cada capa únicamente posee conexiones a la siguiente capa.

`FANN_NETTYPE_SHORTCUT` (`int`)  
Cada capa posee conexiones a todas las capas siguientes.

<!-- -->

`FANN_E_NO_ERROR` (`int`)  
Sin errores.

`FANN_E_CANT_OPEN_CONFIG_R` (`int`)  
No se puede abrir el fichero de configuración para lectura.

`FANN_E_CANT_OPEN_CONFIG_W` (`int`)  
No se puede abrir el fichero de configuración para escritura.

`FANN_E_WRONG_CONFIG_VERSION` (`int`)  
Versión errónea del fichero de configuración.

`FANN_E_CANT_READ_CONFIG` (`int`)  
Error al leer información del fichero de configuración.

`FANN_E_CANT_READ_NEURON` (`int`)  
Error al leer información de neuronas desde el fichero de configuración.

`FANN_E_CANT_READ_CONNECTIONS` (`int`)  
Error al leer conexiones desde el fichero de configuración.

`FANN_E_WRONG_NUM_CONNECTIONS` (`int`)  
Número de conexiones diferente del esperado.

`FANN_E_CANT_OPEN_TD_W` (`int`)  
No se puede abrir el fichero de datos de entrenamiento para escritura.

`FANN_E_CANT_OPEN_TD_R` (`int`)  
No se puede abrir el fichero de datos de entrenamiento para lectura.

`FANN_E_CANT_READ_TD` (`int`)  
Error al leer datos de entrenamiento desde el fichero.

`FANN_E_CANT_ALLOCATE_MEM` (`int`)  
No se puede asignar memoria.

`FANN_E_CANT_TRAIN_ACTIVATION` (`int`)  
No se puede entrenar con la función de activación seleccionada.

`FANN_E_CANT_USE_ACTIVATION` (`int`)  
No se puede utilizar la función de activación seleccionada.

`FANN_E_TRAIN_DATA_MISMATCH` (`int`)  
Diferencias irreconciliables entre dos estructuras fann_train_data.

`FANN_E_CANT_USE_TRAIN_ALG` (`int`)  
No se puede utilizar el algoritmo de entrenamiento seleccionado.

`FANN_E_TRAIN_DATA_SUBSET` (`int`)  
Intento de tomar un subconjunto que no está dentro del conjunto de entrenamiento.

`FANN_E_INDEX_OUT_OF_BOUND` (`int`)  
Índice fuera de los límites.

`FANN_E_SCALE_NOT_PRESENT` (`int`)  
No están presentes los parámetro de escala.

`FANN_E_INPUT_NO_MATCH` (`int`)  
El número de neuronas de entrada en los datos de la Red Neuronal Artificial (RNA - ANN por sus siglas en inglés) no coinciden.

`FANN_E_OUTPUT_NO_MATCH` (`int`)  
El número de neuronas de salida en los datos de la Red Neuronal Artificial (RNA - ANN por sus siglas en inglés) no coinciden.
