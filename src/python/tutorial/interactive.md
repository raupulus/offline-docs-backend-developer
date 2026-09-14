---
title: 14. Edición de entrada interactiva y sustitución de historial
source_url: https://docs.python.org/es/3
source_path: tutorial/interactive.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4950
---

# 14. Edición de entrada interactiva y sustitución de historial

Algunas versiones del intérprete de Python permiten editar la línea de
entrada actual, y sustituir en base al historial, de forma similar a
las capacidades del intérprete de comandos *Korn* y el GNU bash.  Esto
se implementa con la biblioteca GNU Readline, que soporta varios
estilos de edición.  Esta biblioteca tiene su propia documentación la
cuál no vamos a duplicar aquí.

## 14.1. Autocompletado con tab e historial de edición

El autocompletado de variables y nombres de módulos es automatically
enabled al iniciar el intérprete, por lo tanto la tecla "Tab" invoca
la función de autocompletado; ésta mira en los nombres de sentencia,
las variables locales y los nombres de módulos disponibles. Para
expresiones con puntos como "string.a", va a evaluar la expresión
hasta el "'.'" final y entonces sugerir autocompletado para los
atributos del objeto resultante. Nota que esto quizás ejecute código
de aplicaciones definidas si un objeto con un método "__getattr__()"
es parte de la expresión. La configuración por omisión también guarda
tu historial en un archivo llamado ".python_history" en tu directorio
de usuario. El historial estará disponible durante la próxima sesión
interactiva del intérprete.

## 14.2. Alternativas al intérprete interactivo

This facility is an enormous step forward compared to earlier versions
of the interpreter; however, some wishes are left: It would be nice if
the proper indentation were suggested on continuation lines (the
parser knows if an "INDENT" token is required next).  The completion
mechanism might use the interpreter's symbol table.  A command to
check (or even suggest) matching parentheses, quotes, etc., would also
be useful.

Un intérprete interactivo mejorado alternativo que está dando vueltas
desde hace rato es IPython, que ofrece completado por tab, exploración
de objetos, y administración avanzada del historial.  También puede
ser configurado en profundidad, e integrarse en otras aplicaciones.
Otro entorno interactivo mejorado similar es bpython.
