---
title: Closure::bindTo
description: Duplica la cierre con un nuevo objeto vinculado y un nuevo contexto de
  clase.
source_url: https://www.php.net/manual/es/closure.bindto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/closure/bindto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 80720e59f
order: 3050
---

Closure::bindTo

Duplica la cierre con un nuevo objeto vinculado y un nuevo contexto de clase.

## Descripción

```php
public Closure::bindTo(object $newThis, [object $newScope]): Closure
```php

Crea y devuelve una nueva [función anónima ](#functions.anonymous) con el mismo cuerpo y las mismas variables vinculadas que la original, pero con un objeto vinculado que puede ser diferente, y un nuevo contexto de clase.

El objeto vinculado determina el valor que `$this` tendrá en el cuerpo de la función, y el contexto de clase representa una clase que determina a qué miembros privados y protegidos la función anónima tendrá acceso. En otras palabras, las propiedades que serán visibles serán las mismas que si la función anónima fuera un método de la clase pasada a través del argumento `newScope`.

Las cierres estáticas no pueden tener un objeto vinculado (el valor del argumento `newThis` debería ser `null`), pero este método puede utilizarse para cambiar su ámbito de clase.

Este método verificará que una cierre no estática a la que se le pase un contexto de objeto se vincule a este objeto (y ya no sea no estática), y viceversa. Con este fin, las cierres no estáticas a las que se les pase un contexto de clase pero `null` como contexto de objeto serán convertidas en estáticas, y viceversa.

> [!NOTE]
> Si solo se desea duplicar la función anónima, puede utilizarse [el clonado](#language.oop5.cloning) en su lugar.

## Parámetros

`newThis`  
El objeto al que vincular la función anónima, o `null` para una cierre estática.

`newScope`  
El contexto de clase a asociar con la cierre, o 'static' para conservar el contexto actual. Si se pasa un objeto, su tipo será utilizado. Esto determina la visibilidad de los métodos protegidos y privados del objeto vinculado. No está permitido pasar (un objeto de) una clase interna para este argumento.

## Valores devueltos

Devuelve la nueva cierre en forma de objeto `Closure`, o `null` en caso de error.

## Ejemplos

Ejemplo `Closure::bindTo`

```
<?php

class A
{
    private $val;

    public function __construct($val)
    {
        $this->val = $val;
    }

    public function getClosure()
    {
        //Retorna una cierre vinculada a este objeto y contexto
        return function() {
            return $this->val;
        };
    }
}

$ob1 = new A(1);
$ob2 = new A(2);

$cl = $ob1->getClosure();
echo $cl(), "\n";
$cl = $cl->bindTo($ob2);
echo $cl(), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    1
    2

## Véase también

Funciones anónimas

Closure::bind
