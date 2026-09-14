---
title: Serializar objetos - objetos en sesión
source_url: https://www.php.net/manual/es/language.oop5.serialization.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/serialization.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 70f392045
order: 2590
---

## Serializar objetos - objetos en sesión

`serialize` devuelve un string que contiene una representación lineal de cualquier valor que puede ser almacenado en PHP. `unserialize` puede utilizar este string para recrear el valor original de la variable a partir de su representación lineal. Utilizar serialize para guardar un objeto conservará todas sus variables. Sus métodos no serán conservados, solo el nombre de la clase lo será.

Para poder deserializar (`unserialize`) un objeto, la clase del objeto debe estar definida, para permitir su reconstrucción. En otras palabras, si se tiene un objeto de la clase A y se serializa, la representación lineal obtenida hará referencia a la clase A y contendrá todas sus variables. Si se desea poder deserializar esta representación lineal en un lugar donde la clase A no esté definida (en otro fichero, por ejemplo), entonces se deberá redclarar la clase A antes de proceder a la deserialización de su representación lineal. Esto puede hacerse, por ejemplo, incluyendo el fichero de definición de la clase, o utilizando la función `spl_autoload_register`.

```php
<?php
// A.php :

  class A {
      public $one = 1;

      public function show_one() {
          echo $this->one;
      }
  }

// page1.php :

  include "A.php";

  $a = new A;
  $s = serialize($a);
  // guarda $s en algún lugar donde page2.php pueda encontrarlo
  file_put_contents('store', $s);

// page2.php :

  // se necesita la definición de la clase
  // para que unserialize() funcione
  include "A.php";

  $s = file_get_contents('store');
  $a = unserialize($s);

  // llamada a show_one() en el objeto $a, muestra 1
  $a->show_one();
?>

  
```

Si una aplicación serializa objetos, se recomienda encarecidamente, para su uso futuro, que la aplicación incluya las definiciones de las clases de los objetos serializados en cada página. No hacerlo podría resultar en un objeto deserializado sin su definición de clase. PHP asignaría entonces a este objeto una clase de tipo `__PHP_Incomplete_Class_Name`, que no tiene métodos, y produciría un objeto inútil.

Así, en el ejemplo anterior, si `$a` se registra en la sesión añadiendo una clave a la variable superglobal `$_SESSION`, se debería incluir el fichero `A.php` en todas las páginas, y no solo en `page1.php` y `page2.php`.

Tenga en cuenta que también se pueden utilizar los eventos de serialización y deserialización en un objeto utilizando los métodos [\_\_sleep()](#object.sleep) y [\_\_wakeup()](#object.wakeup). El uso de [\_\_sleep()](#object.sleep) permite también serializar solo una parte de las propiedades del objeto.
