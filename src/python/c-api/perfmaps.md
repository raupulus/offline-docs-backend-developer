---
title: Soporte para Mapeo Perf
source_url: https://docs.python.org/es/3
source_path: c-api/perfmaps.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 560
---

# Soporte para Mapeo Perf

En las plataformas soportadas (en el momento de escribir esto, sólo
Linux), el tiempo de ejecución puede aprovechar *perf map files* para
hacer que las funciones de Python sean visibles para una herramienta
externa de perfiles (como perf). Un proceso en ejecución puede crear
un fichero en el directorio "/tmp", que contiene entradas que pueden
asignar una sección de código ejecutable a un nombre. Esta interfaz se
describe en la documentación de la herramienta Perf de Linux.

En Python, estas API auxiliares pueden ser utilizadas por bibliotecas
y funciones que dependen de la generación de código de máquina sobre
la marcha.

Note that holding an *attached thread state* is not required for these
APIs.

int PyUnstable_PerfMapState_Init(void)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Abre el archivo "/tmp/perf-$pid.map", a menos que ya esté abierto,
   y crea un bloqueo para garantizar escrituras seguras para hilos en
   el archivo (siempre que las escrituras se realicen mediante
   "PyUnstable_WritePerfMapEntry()"). Normalmente, no es necesario
   llamar a esto explícitamente; solo use
   "PyUnstable_WritePerfMapEntry()" e inicializará el estado en la
   primera llamada.

   Retorna "0" en caso de éxito, "-1" en caso de fallo al crear/abrir
   el fichero perf map, o "-2" en caso de fallo al crear un bloqueo.
   Comprueba "errno" para más información sobre la causa de un fallo.

int PyUnstable_WritePerfMapEntry(const void *code_addr, unsigned int code_size, const char *entry_name)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Escribe una única entrada en el fichero "/tmp/perf-$pid.map". Esta
   función es segura para hilos. Aquí hay un ejemplo de entrada:

      # address      size  name
      7f3529fcf759 b     py::bar:/run/t.py

   Llamará a "PyUnstable_PerfMapState_Init()" antes de escribir la
   entrada, si el fichero perf map no está ya abierto. Retorna "0" en
   caso de éxito, o los mismos códigos de error que
   "PyUnstable_PerfMapState_Init()" en caso de fallo.

void PyUnstable_PerfMapState_Fini(void)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Cierra el fichero perf map abierto por
   "PyUnstable_PerfMapState_Init()". Esto es llamado por el propio
   tiempo de ejecución durante el cierre del intérprete. En general,
   no debería haber una razón para llamar explícitamente a esto,
   excepto para manejar escenarios específicos como la bifurcación.

int PyUnstable_CopyPerfMapFile(const char *parent_filename)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Open the "/tmp/perf-$pid.map" file and append the content of
   *parent_filename* to it.

   This function is available on all platforms but only generates
   output on platforms that support perf maps (currently only Linux).
   On other platforms, it does nothing.

   Added in version 3.13.

int PyUnstable_PerfTrampoline_CompileCode(PyCodeObject *code)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Compile the given code object using the current perf trampoline.

   The "current" trampoline is the one set by the runtime or the most
   recent "PyUnstable_PerfTrampoline_SetPersistAfterFork()" call.

   If no trampoline is set, falls back to normal compilation (no perf
   map entry).

   Parámetros:
      * **code** -- The code object to compile.

   Devuelve:
      0 on success, -1 on failure.

   Added in version 3.13.

int PyUnstable_PerfTrampoline_SetPersistAfterFork(int enable)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Set whether the perf trampoline should persist after a fork.

   * If "enable" is true (non-zero): perf map file remains open/valid
     post-fork. Child process inherits all existing perf map entries.

   * If "enable" is false (zero): perf map closes post-fork. Child
     process gets empty perf map.

   Default: false (clears on fork).

   Parámetros:
      * **enable** -- 1 to enable, 0 to disable.

   Devuelve:
      0 on success, -1 on failure.

   Added in version 3.13.
