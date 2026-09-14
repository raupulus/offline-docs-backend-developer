---
title: '"abc" --- Abstract Base Classes'
source_url: https://docs.python.org/es/3
source_path: library/abc.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1490
---

# "abc" --- Abstract Base Classes

**Código fuente:** Lib/abc.py

======================================================================

Este módulo proporciona la infraestructura para definir *clases de
base abstracta* (CBAs) en Python, como se describe en **PEP 3119**;
consulte en el PEP el porqué fue agregado a Python. (Véase también
**PEP 3141** y el módulo "numbers" con respecto a una jerarquía de
tipos para números basados en CBAs.)

The "collections" module has some concrete classes that derive from
ABCs; these can, of course, be further derived. In addition, the
"collections.abc" submodule has some ABCs that can be used to test
whether a class or instance provides a particular interface, for
example, if it is *hashable* or if it is a *mapping*.

Este módulo provee la metaclase "ABCMeta" para definir CBAs y una
clase auxiliar "ABC" para definir CBAs alternativamente a través de
herencia:

class abc.ABC

   A helper class that has "ABCMeta" as its metaclass.  With this
   class, an abstract base class can be created by simply deriving
   from "ABC" avoiding sometimes confusing metaclass usage, for
   example:

      from abc import ABC

      class MyABC(ABC):
          pass

   Note that the type of "ABC" is still "ABCMeta", therefore
   inheriting from "ABC" requires the usual precautions regarding
   metaclass usage, as multiple inheritance may lead to metaclass
   conflicts. One may also define an abstract base class by passing
   the metaclass keyword and using "ABCMeta" directly, for example:

      from abc import ABCMeta

      class MyABC(metaclass=ABCMeta):
          pass

   Added in version 3.4.

class abc.ABCMeta

   Metaclases para definir Clases de Base Abstracta (CBAs).

   Utilice esta metaclase para crear una CBA.  Una CBA puede ser
   heredada directamente y así, actuar como una clase mixta.  También
   se puede registrar clases concretas no relacionadas (incluso clases
   integradas) y CBAs no relacionadas como "subclases virtuales" --
   estas y sus descendientes serán consideradas subclases del CBA
   registrado por la función integrada "issubclass()", pero la CBA
   registrada no aparecerá en su *MRO* (Orden de Resolución de
   Métodos) ni las implementaciones de método definidas por la CBA
   registrada serán invocables (ni siquiera a través de "super()").
   [1]

   Classes created with a metaclass of "ABCMeta" have the following
   method:

   register(subclass)

      Registre la *subclase* como una "subclase virtual" de esta CBA.
      Por ejemplo:

         from abc import ABC

         class MyABC(ABC):
             pass

         MyABC.register(tuple)

         assert issubclass(tuple, MyABC)
         assert isinstance((), MyABC)

      Distinto en la versión 3.3: Retorna la subclase registrada, para
      permitir su uso como decorador de clase.

      Distinto en la versión 3.4: To detect calls to "register()", you
      can use the "get_cache_token()" function.

   También se puede redefinir este método en una clase de base
   abstracta:

   __subclasshook__(subclass)

      (Debe ser definido como un método de clase.)

      Check whether *subclass* is considered a subclass of this ABC.
      This means that you can customize the behavior of "issubclass()"
      further without the need to call "register()" on every class you
      want to consider a subclass of the ABC.  (This class method is
      called from the "__subclasscheck__()" method of the ABC.)

      This method should return "True", "False" or "NotImplemented".
      If it returns "True", the *subclass* is considered a subclass of
      this ABC. If it returns "False", the *subclass* is not
      considered a subclass of this ABC, even if it would normally be
      one.  If it returns "NotImplemented", the subclass check is
      continued with the usual mechanism.

   Para una demostración de estos conceptos, vea este ejemplo de la
   definición CBA:

      class Foo:
          def __getitem__(self, index):
              ...
          def __len__(self):
              ...
          def get_iterator(self):
              return iter(self)

      class MyIterable(ABC):

          @abstractmethod
          def __iter__(self):
              while False:
                  yield None

          def get_iterator(self):
              return self.__iter__()

          @classmethod
          def __subclasshook__(cls, C):
              if cls is MyIterable:
                  if any("__iter__" in B.__dict__ for B in C.__mro__):
                      return True
              return NotImplemented

      MyIterable.register(Foo)

   The ABC "MyIterable" defines the standard iterable method,
   "__iter__()", as an abstract method.  The implementation given here
   can still be called from subclasses.  The "get_iterator()" method
   is also part of the "MyIterable" abstract base class, but it does
   not have to be overridden in non-abstract derived classes.

   The "__subclasshook__()" class method defined here says that any
   class that has an "__iter__()" method in its "__dict__" (or in that
   of one of its base classes, accessed via the "__mro__" list) is
   considered a "MyIterable" too.

   Finally, the last line makes "Foo" a virtual subclass of
   "MyIterable", even though it does not define an "__iter__()" method
   (it uses the old-style iterable protocol, defined in terms of
   "__len__()" and "__getitem__()").  Note that this will not make
   "get_iterator" available as a method of "Foo", so it is provided
   separately.

The "abc" module also provides the following decorator:

@abc.abstractmethod

   Un decorador que indica métodos abstractos.

   Using this decorator requires that the class's metaclass is
   "ABCMeta" or is derived from it.  A class that has a metaclass
   derived from "ABCMeta" cannot be instantiated unless all of its
   abstract methods and properties are overridden.  The abstract
   methods can be called using any of the normal 'super' call
   mechanisms.  "@abstractmethod" may be used to declare abstract
   methods for properties and descriptors.

   Dynamically adding abstract methods to a class, or attempting to
   modify the abstraction status of a method or class once it is
   created, are only supported using the "update_abstractmethods()"
   function.  The "@abstractmethod" only affects subclasses derived
   using regular inheritance; "virtual subclasses" registered with the
   ABC's "register()" method are not affected.

   When "@abstractmethod" is applied in combination with other method
   descriptors, it should be applied as the innermost decorator, as
   shown in the following usage examples:

      class C(ABC):
          @abstractmethod
          def my_abstract_method(self, arg1):
              ...
          @classmethod
          @abstractmethod
          def my_abstract_classmethod(cls, arg2):
              ...
          @staticmethod
          @abstractmethod
          def my_abstract_staticmethod(arg3):
              ...

          @property
          @abstractmethod
          def my_abstract_property(self):
              ...
          @my_abstract_property.setter
          @abstractmethod
          def my_abstract_property(self, val):
              ...

          @abstractmethod
          def _get_x(self):
              ...
          @abstractmethod
          def _set_x(self, val):
              ...
          x = property(_get_x, _set_x)

   In order to correctly interoperate with the abstract base class
   machinery, the descriptor must identify itself as abstract using
   "__isabstractmethod__". In general, this attribute should be "True"
   if any of the methods used to compose the descriptor are abstract.
   For example, Python's built-in "@property" does the equivalent of:

      class Descriptor:
          ...
          @property
          def __isabstractmethod__(self):
              return any(getattr(f, '__isabstractmethod__', False) for
                         f in (self._fget, self._fset, self._fdel))

   Nota:

     A diferencia de los métodos abstractos de Java, estos métodos
     abstractos pueden tener una implementación. Esta implementación
     se puede llamar a través del mecanismo "super()" de la clase que
     lo invalida.  Esto podría ser útil como un *end-point* para una
     super llamada en un *framework* que use herencia múltiple
     cooperativa.

The "abc" module also supports the following legacy decorators:

@abc.abstractclassmethod

   Added in version 3.2.

   Obsoleto desde la versión 3.3: It is now possible to use
   "@classmethod" with "@abstractmethod", making this decorator
   redundant.

   A subclass of the built-in "classmethod", indicating an abstract
   classmethod. Otherwise it is similar to "@abstractmethod".

   This special case is deprecated, as the "@classmethod" decorator is
   now correctly identified as abstract when applied to an abstract
   method:

      class C(ABC):
          @classmethod
          @abstractmethod
          def my_abstract_classmethod(cls, arg):
              ...

@abc.abstractstaticmethod

   Added in version 3.2.

   Obsoleto desde la versión 3.3: It is now possible to use
   "@staticmethod" with "@abstractmethod", making this decorator
   redundant.

   A subclass of the built-in "staticmethod", indicating an abstract
   staticmethod. Otherwise it is similar to "@abstractmethod".

   This special case is deprecated, as the "@staticmethod" decorator
   is now correctly identified as abstract when applied to an abstract
   method:

      class C(ABC):
          @staticmethod
          @abstractmethod
          def my_abstract_staticmethod(arg):
              ...

@abc.abstractproperty

   Obsoleto desde la versión 3.3: It is now possible to use
   "@property", "@property.getter", "@property.setter" and
   "@property.deleter" with "@abstractmethod", making this decorator
   redundant.

   A subclass of the built-in "property", indicating an abstract
   property.

   This special case is deprecated, as the "@property" decorator is
   now correctly identified as abstract when applied to an abstract
   method:

      class C(ABC):
          @property
          @abstractmethod
          def my_abstract_property(self):
              ...

   En el ejemplo anterior se define una propiedad de solo lectura;
   también se puede definir una propiedad abstracta de lectura y
   escritura marcando adecuadamente uno o varios de los métodos
   subyacentes como abstractos:

      class C(ABC):
          @property
          def x(self):
              ...

          @x.setter
          @abstractmethod
          def x(self, val):
              ...

   Si solo algunos componentes son abstractos, solo estos componentes
   necesitan ser actualizados para crear una propiedad concreta en una
   subclase:

      class D(C):
          @C.x.setter
          def x(self, val):
              ...

The "abc" module also provides the following functions:

abc.get_cache_token()

   Retorna el token de caché de la clase base abstracta actual.

   El token es un objeto opaco (que admite pruebas de igualdad) que
   identifica la versión actual de la caché de clases de base
   abstractas para subclases virtuales. El token cambia con cada
   llamada a "ABCMeta.register()" en cualquier CBA.

   Added in version 3.4.

abc.update_abstractmethods(cls)

   Una función para recalcular el estado de abstracción de una clase
   abstracta. Se debe llamar a esta función si los métodos abstractos
   de una clase se han implementado o cambiado después de su creación.
   Por lo general, esta función debe llamarse desde dentro de un
   decorador de clases.

   Retorna *cls*, para permitir su uso como decorador de clases.

   Si *cls* no es una instancia de "ABCMeta", no hace nada.

   Nota:

     Esta función asume que las superclases de *cls* ya están
     actualizadas. No actualiza subclases.

   Added in version 3.10.

-[ Notas al pie ]-

[1] Los desarrolladores de C++ pueden notar que el concepto de clase
    base virtual de Python no es el mismo que en C++.
