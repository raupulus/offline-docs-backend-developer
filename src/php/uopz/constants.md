---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/uopz.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99160
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Los siguientes opcodes son definidos como constantes por uopz antes de 5.0.0:

`ZEND_EXIT` (`int`)  
Invoca exit() y die(); no recibe ningún argumento. Devuelve `true` para salir, `false` para continuar

`ZEND_NEW` (`int`)  
Invocado por la construcción de un objeto, recibe el objeto de la clase creada como único argumento

`ZEND_THROW` (`int`)  
Invocado por la estructura throw, recibe la excepción de la clase emitida como único argumento

`ZEND_FETCH_CLASS` (`int`)  
Invocado durante una composición, recibe la clase, el nombre de la clase recuperada como único argumento

`ZEND_ADD_TRAIT` (`int`)  
Invocado durante una composición, recibe la clase en la cual el trait será añadido, como primer argumento, y el nombre del trait como segundo argumento

`ZEND_ADD_INTERFACE` (`int`)  
Invocado durante una composición, recibe la clase en la cual la interfaz será añadida como primer argumento, y el nombre de la interfaz como segundo argumento

`ZEND_INSTANCEOF` (`int`)  
Invocado por el operador instanceof, recibe el objeto a verificar como primer argumento, y el nombre de la clase a la que pertenece el objeto como segundo argumento

Las siguientes constantes controlan el comportamiento del VM después de que un gestor usuario sea llamado; sea extremadamente cuidadoso! Estas constantes son eliminadas a partir de uopz 5.0.0.

`ZEND_USER_OPCODE_CONTINUE` (`int`)  
Avance de un opcode, y continúe

`ZEND_USER_OPCODE_ENTER` (`int`)  
Entrar en un nuevo op_array sin recursión

`ZEND_USER_OPCODE_LEAVE` (`int`)  
Retorna el op_array llamado en el mismo ejecutor

`ZEND_USER_OPCODE_DISPATCH` (`int`)  
Despacha el gestor opcode original

`ZEND_USER_OPCODE_DISPATCH_TO` (`int`)  
Despacha a un gestor específico (o combinado con la constante opcode de ZEND)

`ZEND_USER_OPCODE_RETURN` (`int`)  
Sale del ejecutor (retorna a la función)

Los siguientes modificadores están registrados como constantes por uopz

`ZEND_ACC_PUBLIC` (`int`)  
Marca una función como pública, el comportamiento por omisión

`ZEND_ACC_PROTECTED` (`int`)  
Marca una función como protegida

`ZEND_ACC_PRIVATE` (`int`)  
Marca una función como privada

`ZEND_ACC_STATIC` (`int`)  
Marca una función como estática

`ZEND_ACC_FINAL` (`int`)  
Marca una función como final

`ZEND_ACC_ABSTRACT` (`int`)  
Marca una función como abstracta

`ZEND_ACC_CLASS` (`int`)  
Registro ficticio para consistencia, el tipo de entrada de clase por omisión. Eliminada a partir de uopz 5.0.0.

`ZEND_ACC_INTERFACE` (`int`)  
Marca la clase como una interfaz. Eliminada a partir de uopz 5.0.0.

`ZEND_ACC_TRAIT` (`int`)  
Marca la clase como un trait. Eliminada a partir de uopz 5.0.0.

`ZEND_ACC_FETCH` (`int`)  
Utilizado para recuperar solo los flags. Eliminada a partir de uopz 5.0.0.
