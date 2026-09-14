---
title: Phar::copy
description: Copia un fichero perteneciente a un archivo hacia otro fichero del mismo
  archivo
source_url: https://www.php.net/manual/es/phar.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 8d09722b6
order: 64000
---

Phar::copy

Copia un fichero perteneciente a un archivo hacia otro fichero del mismo archivo

## Descripción

```php
public Phar::copy(string $from, string $to): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Copia un fichero perteneciente a un archivo hacia un nuevo fichero del mismo archivo. Es una alternativa orientada a objetos al uso de `copy` con un flujo phar.

## Parámetros

`from`  

`to`  

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Levanta una excepción `UnexpectedValueException` si el fichero origen no existe, si el fichero destino ya existe, si el acceso en escritura está desactivado, si abrir uno u otro de los ficheros falla, si la lectura del fichero origen falla, o levanta una excepción `PharException` si la escritura de los cambios en el phar falla.

## Ejemplos

Ejemplo con `Phar::copy`

Este ejemplo muestra cómo utilizar `Phar::copy` y la comparación en términos de rendimiento con el equivalente utilizando el flujo phar. La diferencia principal entre los dos métodos concierne la gestión de errores. Todos los métodos Phar levantan excepciones, mientras que las funciones de flujo utilizan `trigger_error`.

```
<?php

try {
    $phar = new Phar('monphar.phar');

    $phar['a'] = 'salut';
    $phar->copy('a', 'b');

    echo $phar['b']; // Muestra "phar://myphar.phar/b"
} catch (Exception $e) {
    // Maneja los errores
}

// El equivalente en términos de flujo del código anterior
// se devuelven E_WARNING en lugar de excepciones
copy('phar://monphar.phar/a', 'phar//monphar.phar/c');
echo file_get_contents('phar://monphar.phar/c'); // Muestra "salut"

?>

    
```php
