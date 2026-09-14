---
title: Closure::bind
description: Duplicar un cierre con un objeto vinculado y ámbito de clase especificados
source_url: https://www.php.net/manual/es/closure.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/closure/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 9c74079f1
order: 3040
---

Closure::bind

Duplicar un cierre con un objeto vinculado y ámbito de clase especificados

## Descripción

```php
public static Closure::bind(Closure $closure, object $newThis, [object $newScope]): Closure
```php

Este método es una versión estática de Closure::bindTo. Véase la documentación de ese método para más información.

## Parámetros

`closure`  
La función anónima a vincular.

`newThis`  
El objeto al que la función anónima dada debería ser vinculado, o `null` para que el cierre sea desvinculado.

`newScope`  
El ámbito de clase a la que asociar el cierre, o 'static' para mantener el actual. Si se proporciona un objeto, el tipo del mismo se usará en su lugar. Esto determina la visibilidad de métodos protegidos y privados del objeto vinculado. No se permite pasar (un objeto de) una clase interna a este parámetro.

## Valores devueltos

Devuelve un nuevo objeto `Closure` object, o `null` en caso de error.

## Ejemplos

Ejemplo de `Closure::bind`

```
<?php
class A {
    private static $sfoo = 1;
    private $ifoo = 2;
}
$cl1 = static function() {
    return A::$sfoo;
};
$cl2 = function() {
    return $this->ifoo;
};

$bcl1 = Closure::bind($cl1, null, 'A');
$bcl2 = Closure::bind($cl2, new A(), 'A');
echo $bcl1(), "\n";
echo $bcl2(), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    1
    2

## Véase también

Funciones anónimas

Closure::bindTo
