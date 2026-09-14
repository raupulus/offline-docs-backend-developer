---
title: 9. Componentes de nivel superior
source_url: https://docs.python.org/es/3
source_path: reference/toplevel_components.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: reference
order: 4850
---

# 9. Componentes de nivel superior

El intérprete de Python puede obtener su entrada de varias fuentes: de
un script que se le pasa como entrada estándar o como argumento del
programa, escrito interactivamente, de un archivo fuente de módulo,
etc. Este capítulo proporciona la sintaxis utilizada en estos casos.

## 9.1. Programas completos de Python

Si bien una especificación de lenguaje no necesita prescribir cómo se
invoca al intérprete de lenguaje, es útil tener una noción de un
programa completo de Python. Un programa completo de Python se ejecuta
en un entorno mínimamente inicializado: todos los módulos estándar e
integrados están disponibles, pero ninguno ha sido inicializado,
excepto "sys" (varios servicios del sistema), "builtins" (funciones
integradas, excepciones y "Ninguno") y "__main__". Este último se
utiliza para proporcionar el espacio de nombres local y global para la
ejecución del programa completo.

La sintaxis de un programa completo de Python es la entrada de
archivos, que se describe en la siguiente sección.

El intérprete también puede invocarse en modo interactivo; en este
caso, no lee ni ejecuta un programa completo, sino que lee y ejecuta
una instrucción (posiblemente compuesta) a la vez. El entorno inicial
es idéntico al de un programa completo; cada instrucción se ejecuta en
el espacio de nombres de "__main__".

Se puede pasar un programa completo al intérprete en tres formas: con
la opción "-c" *string* de línea de comando, como un archivo pasado
como primer argumento de línea de comando o como entrada estándar. Si
el archivo o la entrada estándar es un dispositivo tty, el intérprete
ingresa al modo interactivo; de lo contrario, ejecuta el archivo como
un programa completo.

## 9.2. Entrada de archivo

Todas las entradas leídas de archivos no interactivos tienen la misma
forma:

   file_input: (NEWLINE | statement)* ENDMARKER

Esta sintaxis se utiliza en las siguientes situaciones:

* al analizar un programa completo de Python (desde un archivo o desde
  una cadena);

* al analizar un módulo;

* al analizar una cadena pasada a la función: "exec()";

## 9.3. Entrada interactiva

La entrada en modo interactivo se analiza utilizando la siguiente
gramática:

   interactive_input: [stmt_list] NEWLINE | compound_stmt NEWLINE | ENDMARKER

Tenga en cuenta que una declaración compuesta (de nivel superior) debe
ir seguida de una línea en blanco en modo interactivo; esto es
necesario para ayudar al analizador sintáctico a detectar el final de
la entrada.

## 9.4. Entrada de expresión

"eval()" se utiliza para la entrada de expresiones. Ignora los
espacios en blanco iniciales. El argumento de cadena para "eval()"
debe tener la siguiente forma:

   eval_input: expression_list NEWLINE* ENDMARKER
