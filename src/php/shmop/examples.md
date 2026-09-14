---
title: Ejemplos
source_url: https://www.php.net/manual/es/shmop.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/shmop/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: shmop
translation_status: ready
translation_reviewed: false
translation_revision: 6ce09e409
order: 74190
---

## Ejemplos

## Uso básico

Resumen de las operaciones con Memoria Compartida

```php
<?php

// Crear un segmento de memoria compartida de 100 bytes con un identificador igual a 0xff3
$shm_id = shmop_open(0xff3, "c", 0644, 100);
if (!$shm_id) {
    echo "Couldn't create shared memory segment\n";
}

// Obtener tamaño del segmento de memoria compartida
$shm_size = shmop_size($shm_id);
echo "SHM Block Size: " . $shm_size . " has been created.\n";

// Escribir una cadena de prueba en la memoria compartida
$shm_bytes_written = shmop_write($shm_id, "my shared memory block", 0);
if ($shm_bytes_written != strlen("my shared memory block")) {
    echo "Couldn't write the entire length of data\n";
}

// Ahora vamos a leer la cadena de texto
$my_string = shmop_read($shm_id, 0, $shm_size);
if (!$my_string) {
    echo "Couldn't read from shared memory block\n";
}
echo "The data inside shared memory was: " . $my_string . "\n";

//Ahora vamos a eliminar y cerrar el segmento de memoria compartida
if (!shmop_delete($shm_id)) {
    echo "Couldn't mark shared memory block for deletion.";
}
shmop_close($shm_id);

?>

   
```
