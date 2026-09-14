---
title: '"readline" --- GNU readline interface'
source_url: https://docs.python.org/es/3
source_path: library/readline.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3650
---

# "readline" --- GNU readline interface

======================================================================

The "readline" module defines a number of functions to facilitate
completion and reading/writing of history files from the Python
interpreter. This module can be used directly, or via the
"rlcompleter" module, which supports completion of Python identifiers
at the interactive prompt.  Settings made using  this module affect
the behaviour of both the interpreter's interactive prompt  and the
prompts offered by the built-in "input()" function.

Las combinaciones de teclas de Readline se pueden configurar mediante
un archivo de inicialización, generalmente ".inputrc" en su directorio
de inicio. Consulte Readline Init File en el manual de GNU Readline
para obtener información sobre el formato y las construcciones
permitidas de ese archivo, y las capacidades de la biblioteca Readline
en general.

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

Availability: Unix.

Nota:

  The underlying Readline library API may be implemented by the
  "editline" ("libedit") library instead of GNU readline. On macOS the
  "readline" module detects which library is being used at run
  time.The configuration file for "editline" is different from that of
  GNU readline. If you programmatically load configuration strings you
  can use "backend" to determine which library is being used.If you
  use "editline"/"libedit" readline emulation on macOS, the
  initialization file located in your home directory is named
  ".editrc". For example, the following content in "~/.editrc" will
  turn ON *vi* keybindings and TAB completion:

     python:bind -v
     python:bind ^I rl_complete

  Also note that different libraries may use different history file
  formats. When switching the underlying library, existing history
  files may become unusable.

readline.backend

   The name of the underlying Readline library being used, either
   ""readline"" or ""editline"".

   Added in version 3.13.

## Archivo de inicio

Las siguientes funciones se relacionan con el archivo de inicio y la
configuración del usuario:

readline.parse_and_bind(string)

   Execute the init line provided in the *string* argument. This calls
   "rl_parse_and_bind()" in the underlying library.

readline.read_init_file([filename])

   Execute a readline initialization file. The default filename is the
   last filename used. This calls "rl_read_init_file()" in the
   underlying library. It raises an auditing event "open" with the
   file name if given, and ""<readline_init_file>"" otherwise,
   regardless of which file the library resolves.

   Distinto en la versión 3.14: The auditing event was added.

## Búfer de línea

Las siguientes funciones operan en el búfer de línea:

readline.get_line_buffer()

   Return the current contents of the line buffer ("rl_line_buffer" in
   the underlying library).

readline.insert_text(string)

   Insert text into the line buffer at the cursor position.  This
   calls "rl_insert_text()" in the underlying library, but ignores the
   return value.

readline.redisplay()

   Change what's displayed on the screen to reflect the current
   contents of the line buffer.  This calls "rl_redisplay()" in the
   underlying library.

## Archivo de historial

Las siguientes funciones operan en un archivo de historial:

readline.read_history_file([filename])

   Load a readline history file, and append it to the history list.
   The default filename is "~/.history".  This calls "read_history()"
   in the underlying library and raises an auditing event "open" with
   the file name if given and ""~/.history"" otherwise.

   Distinto en la versión 3.14: The auditing event was added.

readline.write_history_file([filename])

   Save the history list to a readline history file, overwriting any
   existing file.  The default filename is "~/.history".  This calls
   "write_history()" in the underlying library and raises an auditing
   event "open" with the file name if given and ""~/.history""
   otherwise.

   Distinto en la versión 3.14: The auditing event was added.

readline.append_history_file(nelements[, filename])

   Append the last *nelements* items of history to a file.  The
   default filename is "~/.history".  The file must already exist.
   This calls "append_history()" in the underlying library.  This
   function only exists if Python was compiled for a version of the
   library that supports it. It raises an auditing event "open" with
   the file name if given and ""~/.history"" otherwise.

   Added in version 3.5.

   Distinto en la versión 3.14: The auditing event was added.

readline.get_history_length()
readline.set_history_length(length)

   Set or return the desired number of lines to save in the history
   file. The "write_history_file()" function uses this value to
   truncate the history file, by calling "history_truncate_file()" in
   the underlying library.  Negative values imply unlimited history
   file size.

## Lista del historial

Las siguientes funciones operan en una lista de historial global:

readline.clear_history()

   Clear the current history.  This calls "clear_history()" in the
   underlying library.  The Python function only exists if Python was
   compiled for a version of the library that supports it.

readline.get_current_history_length()

   Retorna el número de elementos actuales en el historial. (Esto es
   diferente de la función "get_history_length()", que retorna el
   número máximo de líneas que se escribirán en un archivo de
   historial).

readline.get_history_item(index)

   Return the current contents of history item at *index*.  The item
   index is one-based.  This calls "history_get()" in the underlying
   library.

readline.remove_history_item(pos)

   Remove history item specified by its position from the history. The
   position is zero-based.  This calls "remove_history()" in the
   underlying library.

readline.replace_history_item(pos, line)

   Replace history item specified by its position with *line*. The
   position is zero-based.  This calls "replace_history_entry()" in
   the underlying library.

readline.add_history(line)

   Append *line* to the history buffer, as if it was the last line
   typed. This calls "add_history()" in the underlying library.

readline.set_auto_history(enabled)

   Enable or disable automatic calls to "add_history()" when reading
   input via readline.  The *enabled* argument should be a Boolean
   value that when true, enables auto history, and that when false,
   disables auto history.

   Added in version 3.6.

   *Auto history* está habilitado de forma predeterminada, y cambiarlo
   no hará que persista en múltiples sesiones.

## Ganchos (*hooks*) de inicialización

readline.set_startup_hook([function])

   Set or remove the function invoked by the "rl_startup_hook"
   callback of the underlying library.  If *function* is specified, it
   will be used as the new hook function; if omitted or "None", any
   function already installed is removed.  The hook is called with no
   arguments just before readline prints the first prompt.

readline.set_pre_input_hook([function])

   Set or remove the function invoked by the "rl_pre_input_hook"
   callback of the underlying library.  If *function* is specified, it
   will be used as the new hook function; if omitted or "None", any
   function already installed is removed.  The hook is called with no
   arguments after the first prompt has been printed and just before
   readline starts reading input characters.  This function only
   exists if Python was compiled for a version of the library that
   supports it.

## Terminación

The following functions relate to implementing a custom word
completion function.  This is typically operated by the Tab key, and
can suggest and automatically complete a word being typed.  By
default, Readline is set up to be used by "rlcompleter" to complete
Python identifiers for the interactive interpreter.  If the "readline"
module is to be used with a custom completer, a different set of word
delimiters should be set.

readline.set_completer([function])

   Establece o elimina la función de finalización. Si se especifica
   *function*, se usará como la nueva función de finalización; Si se
   omite o es "None", se elimina cualquier función de finalización ya
   instalada. La función completa se llama como "function(text,
   state)", para *state* en "0", "1", "2", ..., hasta que retorna un
   valor que no es una cadena de caracteres. Debería retornar las
   siguientes terminaciones posibles comenzando con *text*.

   The installed completer function is invoked by the *entry_func*
   callback passed to "rl_completion_matches()" in the underlying
   library. The *text* string comes from the first parameter to the
   "rl_attempted_completion_function" callback of the underlying
   library.

readline.get_completer()

   Obtiene la función de finalización o "None" si no se ha definido
   ninguna función de finalización.

readline.get_completion_type()

   Get the type of completion being attempted.  This returns the
   "rl_completion_type" variable in the underlying library as an
   integer.

readline.get_begidx()
readline.get_endidx()

   Get the beginning or ending index of the completion scope. These
   indexes are the *start* and *end* arguments passed to the
   "rl_attempted_completion_function" callback of the underlying
   library.  The values may be different in the same input editing
   scenario based on the underlying C readline implementation. Ex:
   libedit is known to behave differently than libreadline.

readline.set_completer_delims(string)
readline.get_completer_delims()

   Set or get the word delimiters for completion.  These determine the
   start of the word to be considered for completion (the completion
   scope). These functions access the
   "rl_completer_word_break_characters" variable in the underlying
   library.

readline.set_completion_display_matches_hook([function])

   Set or remove the completion display function.  If *function* is
   specified, it will be used as the new completion display function;
   if omitted or "None", any completion display function already
   installed is removed.  This sets or clears the
   "rl_completion_display_matches_hook" callback in the underlying
   library.  The completion display function is called as
   "function(substitution, [matches], longest_match_length)" once each
   time matches need to be displayed.

## Ejemplo

The following example demonstrates how to use the "readline" module's
history reading and writing functions to automatically load and save a
history file named ".python_history" from the user's home directory.
The code below would normally be executed automatically during
interactive sessions from the user's "PYTHONSTARTUP" file.

   import atexit
   import os
   import readline

   histfile = os.path.join(os.path.expanduser("~"), ".python_history")
   try:
       readline.read_history_file(histfile)
       # default history len is -1 (infinite), which may grow unruly
       readline.set_history_length(1000)
   except FileNotFoundError:
       pass

   atexit.register(readline.write_history_file, histfile)

Este código se ejecuta automáticamente cuando Python se ejecuta en
modo interactivo (ver Configuración de Readline).

El siguiente ejemplo logra el mismo objetivo pero administra sesiones
interactivas concurrentes, agregando solo el nuevo historial.

   import atexit
   import os
   import readline
   histfile = os.path.join(os.path.expanduser("~"), ".python_history")

   try:
       readline.read_history_file(histfile)
       h_len = readline.get_current_history_length()
   except FileNotFoundError:
       open(histfile, 'wb').close()
       h_len = 0

   def save(prev_h_len, histfile):
       new_h_len = readline.get_current_history_length()
       readline.set_history_length(1000)
       readline.append_history_file(new_h_len - prev_h_len, histfile)
   atexit.register(save, h_len, histfile)

El siguiente ejemplo amplía la clase "code.InteractiveConsole" para
administrar el guardado/restauración del historial.

   import atexit
   import code
   import os
   import readline

   class HistoryConsole(code.InteractiveConsole):
       def __init__(self, locals=None, filename="<console>",
                    histfile=os.path.expanduser("~/.console-history")):
           code.InteractiveConsole.__init__(self, locals, filename)
           self.init_history(histfile)

       def init_history(self, histfile):
           readline.parse_and_bind("tab: complete")
           if hasattr(readline, "read_history_file"):
               try:
                   readline.read_history_file(histfile)
               except FileNotFoundError:
                   pass
               atexit.register(self.save_history, histfile)

       def save_history(self, histfile):
           readline.set_history_length(1000)
           readline.write_history_file(histfile)

Nota:

  The new *REPL* introduced in version 3.13 doesn't support readline.
  However, readline can still be used by setting the
  "PYTHON_BASIC_REPL" environment variable.
