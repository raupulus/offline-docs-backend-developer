---
title: uopz_set_mock
description: Utiliza una simulación en lugar de una clase para nuevos objetos
source_url: https://www.php.net/manual/es/function.uopz-set-mock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-set-mock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 0545e305c
order: 99390
---

uopz_set_mock

Utiliza una simulación en lugar de una clase para nuevos objetos

## Descripción

```php
uopz_set_mock(string $class, mixed $mock): void
```php

Si `mock` es una cadena que contiene el nombre de una clase, se instanciará en lugar de `class`. `mock` también puede ser un objeto.

> [!NOTE]
> Solo el acceso dinámico a las propiedades y métodos usará el objeto `mock`. El acceso estático sigue utilizando la `class` original. Consulte el [ejemplo](#uopz_set_mock.example.static) a continuación.

## Parámetros

`class`  
El nombre de la clase que se va a simular.

`mock`  
La simulación a usar en forma de cadena que contiene el nombre de la clase a usar o un objeto. Si se pasa una cadena, debe ser el nombre totalmente calificado de la clase. Se recomienda usar la constante mágica `::class` en este caso.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL uopz 6.0.0 | La simulación de miembros estáticos ya no es compatible con esta función. `uopz_redefine` y `uopz_set_return`, o [Componere](#book.componere) pueden ser utilizados en su lugar. |

## Ejemplos

Ejemplo de `uopz_set_mock`

```
<?php
class A {
    public function who() {
        echo "A";
    }
}

class mockA {
    public function who() {
        echo "mockA";
    }
}

uopz_set_mock(A::class, mockA::class);
(new A)->who();
?>

   
```php

El ejemplo anterior mostrará:

    mockA

Ejemplo de `uopz_set_mock`

```
<?php
class A {
    public function who() {
        echo "A";
    }
}

uopz_set_mock(A::class, new class {
                            public function who() {
                                echo "mockA";
                            }
                        });
(new A)->who();
?>

   
```php

El ejemplo anterior mostrará:

    mockA

`uopz_set_mock` y miembros estáticos

Desde uopz 6.0.0, la simulación de miembros estáticos ya no es compatible.

```
<?php
class A {
    const CON = 'A';
    public static function who() {
        echo "A";
    }
}

uopz_set_mock(A::class, new class {
                            const CON = 'mockA';
                            public static function who() {
                                echo "mockA";
                            }
                        });
echo A::CON, PHP_EOL;
A::who();
?>

   
```php

El ejemplo anterior mostrará:

    A
    A

       

El ejemplo anterior muestra con uopz 5:

    mockA
    mockA

## Véase también

uopz_get_mock

uopz_unset_mock
