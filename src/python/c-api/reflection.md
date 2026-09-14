---
title: Reflexión
source_url: https://docs.python.org/es/3
source_path: c-api/reflection.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 600
---

# Reflexión

PyObject *PyEval_GetBuiltins(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Obsoleto desde la versión 3.13: Utilice "PyEval_GetFrameBuiltins()"
   en su lugar.

   Retorna un diccionario de los builtins en el marco de ejecución
   actual, o el intérprete del estado del hilo si no hay ningún marco
   en ejecución actualmente.

PyObject *PyEval_GetLocals(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Obsoleto desde la versión 3.13: Utilice "PyEval_GetFrameLocals()"
   para obtener el mismo comportamiento que llamando a "locals()" en
   código Python, o bien llama a "PyFrame_GetLocals()" sobre el
   resultado de "PyEval_GetFrame()" para acceder al atributo
   "f_locals" del frame actualmente en ejecución.

   Retorna un diccionario de las variables locales en el marco de
   ejecución actual, o "NULL" si actualmente no se está ejecutando
   ningún marco.

   Consulte "locals()" para obtener más información sobre el mapeo
   retornado en diferentes ámbitos.

   Como esta función retorna una *referencia prestada*, el diccionario
   retornado para *ámbitos optimizados* se almacena en caché en el
   objeto marco y permanecerá vivo mientras lo haga el marco del
   objeto. A diferencia de "PyEval_GetFrameLocals()" y "locals()", las
   llamadas posteriores a esta función en el mismo marco actualizarán
   el contenido del diccionario en caché para reflejar los cambios en
   el estado de las variables locales en lugar de retornar una nueva
   instantánea.

   Distinto en la versión 3.13: Como parte de **PEP 667**,
   "PyFrame_GetLocals()", "locals()", y "FrameType.f_locals" ya no
   utilizan el diccionario de caché compartido. Consulte la entrada
   What's New para más detalles.

PyObject *PyEval_GetGlobals(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Obsoleto desde la versión 3.13: Utilice "PyEval_GetFrameGlobals()"
   en su lugar.

   Retorna un diccionario de las variables globales en el marco de
   ejecución actual, o "NULL" si actualmente no se está ejecutando
   ningún marco.

PyFrameObject *PyEval_GetFrame(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Return the *attached thread state*'s frame, which is "NULL" if no
   frame is currently executing.

   Vea también "PyThreadState_GetFrame()".

PyObject *PyEval_GetFrameBuiltins(void)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.13.*

   Retorna un diccionario de los builtins en el marco de ejecución
   actual, o el intérprete del estado del hilo si no hay ningún marco
   en ejecución actualmente.

   Added in version 3.13.

PyObject *PyEval_GetFrameLocals(void)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.13.*

   Retorna un diccionario de las variables locales en el marco de
   ejecución actual, o "NULL" si no se está ejecutando ningún marco.
   Equivale a llamar a "locals()" en código Python.

   Para acceder a "f_locals" en el marco actual sin hacer una captura
   independiente en *ámbitos optimizados*, llame a
   "PyFrame_GetLocals()" sobre el resultado de "PyEval_GetFrame()".

   Added in version 3.13.

PyObject *PyEval_GetFrameGlobals(void)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.13.*

   Retorna un diccionario de las variables locales en el marco de
   ejecución actual, o "NULL" si no se está ejecutando ningún marco.
   Equivale a llamar a "globals()" en código Python.

   Added in version 3.13.

const char *PyEval_GetFuncName(PyObject *func)
    * Part of the Stable ABI.*

   Retorna el nombre de *func* si es una función, clase u objeto de
   instancia; de lo contrario, el nombre del tipo *func*s.

const char *PyEval_GetFuncDesc(PyObject *func)
    * Part of the Stable ABI.*

   Retorna una cadena de caracteres de descripción, según el tipo de
   *func*. Los valores de retorno incluyen "()" para funciones y
   métodos, "constructor", "instancia" y "objeto". Concatenado con el
   resultado de "PyEval_GetFuncName()", el resultado será una
   descripción de *func*.
