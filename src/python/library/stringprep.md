---
title: '"stringprep" --- Internet String Preparation'
source_url: https://docs.python.org/es/3
source_path: library/stringprep.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3940
---

# "stringprep" --- Internet String Preparation

**Código fuente:** Lib/stringprep.py

======================================================================

Cuando se quiere identificar cosas (como nombres de host) en internet,
generalmente es necesario comparar tales identificaciones para
"igualdad". La manera en la que esta comparación se ejecuta dependerá
del dominio de la aplicación, ej. si tiene o no tiene que distinguir
entre mayúsculas y minúsculas. Además, en algunos casos será necesario
restringir las posibles identificaciones, de tal manera que solo se
permitan identificadores de caracteres que se puedan "imprimir".

**RFC 3454** define el proceso para la "preparación" de cadenas
Unicode para protocolos de internet. Antes de pasar cadenas a un
cable, se procesan con el proceso de preparación, después del cual
tienen una forma normalizada. El RFC define un conjunto de tablas, que
pueden ser combinadas en perfiles. Cada perfil debe definir qué tablas
usa, y que partes opcionales del proceso "stringprep" son parte del
perfil. Un ejemplo de perfil de "stringprep" es "nameprep", que se usa
para nombres de dominios internacionalizados.

The module "stringprep" only exposes the tables from **RFC 3454**. As
these tables would be very large to represent as dictionaries or
lists, the module uses the Unicode character database internally. The
module source code itself was generated using the "mkstringprep.py"
utility.

As a result, these tables are exposed as functions, not as data
structures. There are two kinds of tables in the RFC: sets and
mappings. For a set, "stringprep" provides the "characteristic
function", i.e. a function that returns "True" if the parameter is
part of the set. For mappings, it provides the mapping function: given
the key, it returns the associated value. Below is a list of all
functions available in the module.

stringprep.in_table_a1(code)

   Determina si *code* está en la tablaA.1 (Puntos de Código sin
   asignar en Unicode 3.2).

stringprep.in_table_b1(code)

   Determina si *code* está en la tablaB.1 (Generalmente mapeado a
   nada).

stringprep.map_table_b2(code)

   Retorna el valor mapeado para *code* de acuerdo a la tablaB.2
   (Mapeo para *case-folding* usado con NFKC).

stringprep.map_table_b3(code)

   Retorna el valor mapeado para *code* de acuerdo a tablaB.3 (Mapeo
   para *case-folding* usado sin normalización).

stringprep.in_table_c11(code)

   Determina si *code* está en la tablaC.1.1 (Caracteres de espacio
   ASCII).

stringprep.in_table_c12(code)

   Determina si *code* está en la tablaC.1.2 (Caracteres de espacio
   no-ASCII).

stringprep.in_table_c11_c12(code)

   Determina si *code* está en la tablaC.1 (Caracteres de espacio,
   unión de C.1.1 y C.1.2).

stringprep.in_table_c21(code)

   Determina si *code* está en la tablaC.2.1 (Caracteres de control
   ASCII).

stringprep.in_table_c22(code)

   Determina si *code* está en la tablaC.2.2 (Caracteres de control no
   ASCII).

stringprep.in_table_c21_c22(code)

   Determina si *code* está en la tablaC.2 (Caracteres de control,
   unión de C.2.1 y C.2.2).

stringprep.in_table_c3(code)

   Determina si *code* está en la tablaC.3 (Uso privado).

stringprep.in_table_c4(code)

   Determina si *code* está en la tablaC.4 (Puntos de código sin
   caracteres)

stringprep.in_table_c5(code)

   Determina si *code* está en la tablaC.5 (Códigos surrogados).

stringprep.in_table_c6(code)

   Determina si *code* está en la tablaC.6 (Inadecuado para texto
   plano).

stringprep.in_table_c7(code)

   Determina si *code* está en la tablaC.7 (Inadecuado para la
   representación canónica).

stringprep.in_table_c8(code)

   Determina si *code* está en la tablaC.8 (Cambia las propiedades de
   apariencia o están obsoletas).

stringprep.in_table_c9(code)

   Determina si *code* está en la tablaC.9 (Caracteres de etiquetado).

stringprep.in_table_d1(code)

   Determina si *code* está en la tablaD.1 (Caracteres con propiedad
   bidireccional "R" o "AL").

stringprep.in_table_d2(code)

   Determina si *code* está en la tablaD.2 (Caracteres con propiedad
   bidireccional "L").
