---
title: Ds\Hashable::hash
description: Devuelve un valor escalar para usar como valor de hash
source_url: https://www.php.net/manual/es/ds-hashable.hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/hashable/hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14800
---

Ds\Hashable::hash

Devuelve un valor escalar para usar como valor de hash

## Descripción

```php
abstract public Ds\Hashable::hash(): mixed
```php

Devuelve un valor escalar para usar como valor de hash de los objetos.

Mientras que el valor de hash no defina la igualdad, todos los objetos que son iguales según `Ds\Hashable::equals` deben tener el mismo valor de hash. Los valores de hash de los objetos iguales no tienen que ser únicos, por ejemplo se podría simplemente devolver `true` para todos los objetos y nada se rompería - la única implicación sería que las tablas de hash se convertirían en listas enlazadas porque todos los objetos serían hasheados en el mismo cubo. Es por lo tanto muy importante que se elija un buen valor de hash, como un ID o una dirección de correo electrónico.

Este método permite usar objetos como claves en estructuras tales como `Ds\Map` y `Ds\Set`, o cualquier otra estructura de búsqueda que respete esta interfaz.

> [!CAUTION]
> No elija un valor que podría cambiar en el objeto, como una propiedad pública. Las búsquedas en las tablas de hash fallarían porque el hash ha cambiado.

> [!CAUTION]
> Todos los objetos que son iguales deben tener el mismo valor de hash.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un valor escalar para usar como valor de hash de este objeto.

## Ejemplos

Ejemplo de `Ds\Hashable::hash`

```
<?php
class HashableObject implements \Ds\Hashable
{
    private $name;
    private $email;

    public function __construct($name, $email)
    {
        $this->name  = $name;
        $this->email = $email;
    }

    /**
     * Debe devolver el mismo valor para todos los objetos iguales, pero no tiene que
     * ser único. Este valor no será utilizado para determinar la igualdad.
     */
    public function hash()
    {
        return $this->email;
    }

    /**
     * Determina la igualdad, generalmente durante una búsqueda en una tabla de hash para determinar
     * si la clave del cubo coincide con la clave de búsqueda. El hash debe ser igual si
     * los objetos son iguales, de lo contrario esta determinación no se alcanzaría.
     */
    public function equals($obj): bool
    {
        return $this->name  === $obj->name
            && $this->email === $obj->email;
    }
}
?>

   
```php
