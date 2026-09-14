---
title: Readline Init File
source_url: https://www.gnu.org/software/bash/manual
source_path: 042-readline-init-file.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 420
---

## Readline Init File

initialization file, readline

Although the Readline library comes with a set of Emacs-like keybindings installed by default, it is possible to use a different set of keybindings. Any user can customize programs that use Readline by putting commands in an inputrc file, conventionally in their home directory. The name of this file is taken from the value of the shell variable `INPUTRC`. If that variable is unset, the default is `~/.inputrc`. If that file does not exist or cannot be read, Readline looks for `/etc/inputrc`. The `bind` builtin command can also be used to set Readline keybindings and variables. See [Bash Builtins](#Bash-Builtins).

When a program that uses the Readline library starts up, Readline reads the init file and sets any variables and key bindings it contains.

In addition, the `C-x C-r` command re-reads this init file, thus incorporating any changes that you might have made to it.

### Readline Init File Syntax

There are only a few basic constructs allowed in the Readline init file. Blank lines are ignored. Lines beginning with a ‘`#`’ are comments. Lines beginning with a ‘`$`’ indicate conditional constructs (see [Conditional Init Constructs](#Conditional-Init-Constructs)). Other lines denote variable settings and key bindings.

Variable Settings  
You can modify the run-time behavior of Readline by altering the values of variables in Readline using the `set` command within the init file. The syntax is simple:

    set variable value

Here, for example, is how to change from the default Emacs-like key binding to use `vi` line editing commands:

    set editing-mode vi

Variable names and values, where appropriate, are recognized without regard to case. Unrecognized variable names are ignored.

Boolean variables (those that can be set to on or off) are set to on if the value is null or empty, \<on\> (case-insensitive), or 1. Any other value results in the variable being set to off.

The `bind&#160;-V` command lists the current Readline variable names and values. See [Bash Builtins](#Bash-Builtins).

A great deal of run-time behavior is changeable with the following variables.

variables, readline

`active-region-start-color`  

active-region-start-color

A string variable that controls the text color and background when displaying the text in the active region (see the description of `enable-active-region` below). This string must not take up any physical character positions on the display, so it should consist only of terminal escape sequences. It is output to the terminal before displaying the text in the active region. This variable is reset to the default value whenever the terminal type changes. The default value is the string that puts the terminal in standout mode, as obtained from the terminal’s terminfo description. A sample value might be ‘`\e[01;33m`’.

`active-region-end-color`  

active-region-end-color

A string variable that “undoes” the effects of `active-region-start-color` and restores “normal” terminal display appearance after displaying text in the active region. This string must not take up any physical character positions on the display, so it should consist only of terminal escape sequences. It is output to the terminal after displaying the text in the active region. This variable is reset to the default value whenever the terminal type changes. The default value is the string that restores the terminal from standout mode, as obtained from the terminal’s terminfo description. A sample value might be ‘`\e[0m`’.

`bell-style`  

bell-style

Controls what happens when Readline wants to ring the terminal bell. If set to ‘`none`’, Readline never rings the bell. If set to ‘`visible`’, Readline uses a visible bell if one is available. If set to ‘`audible`’ (the default), Readline attempts to ring the terminal’s bell.

`bind-tty-special-chars`  

bind-tty-special-chars

If set to ‘`on`’ (the default), Readline attempts to bind the control characters that are treated specially by the kernel’s terminal driver to their Readline equivalents. These override the default Readline bindings described here. Type ‘`stty -a`’ at a Bash prompt to see your current terminal settings, including the special control characters (usually `cchars`).

`blink-matching-paren`  

blink-matching-paren

If set to ‘`on`’, Readline attempts to briefly move the cursor to an opening parenthesis when a closing parenthesis is inserted. The default is ‘`off`’.

`colored-completion-prefix`  

colored-completion-prefix

If set to ‘`on`’, when listing completions, Readline displays the common prefix of the set of possible completions using a different color. The color definitions are taken from the value of the `LS_COLORS` environment variable. If there is a color definition in `LS_COLORS` for the custom suffix ‘`readline-colored-completion-prefix`’, Readline uses this color for the common prefix instead of its default. The default is ‘`off`’.

`colored-stats`  

colored-stats

If set to ‘`on`’, Readline displays possible completions using different colors to indicate their file type. The color definitions are taken from the value of the `LS_COLORS` environment variable. The default is ‘`off`’.

`comment-begin`  

comment-begin

The string to insert at the beginning of the line by the `insert-comment` command. The default value is `"#"`.

`completion-display-width`  

completion-display-width

The number of screen columns used to display possible matches when performing completion. The value is ignored if it is less than 0 or greater than the terminal screen width. A value of 0 causes matches to be displayed one per line. The default value is -1.

`completion-ignore-case`  

completion-ignore-case

If set to ‘`on`’, Readline performs filename matching and completion in a case-insensitive fashion. The default value is ‘`off`’.

`completion-map-case`  

completion-map-case

If set to ‘`on`’, and \<completion-ignore-case\> is enabled, Readline treats hyphens (‘`-`’) and underscores (‘`_`’) as equivalent when performing case-insensitive filename matching and completion. The default value is ‘`off`’.

`completion-prefix-display-length`  

completion-prefix-display-length

The maximum length in characters of the common prefix of a list of possible completions that is displayed without modification. When set to a value greater than zero, Readline replaces common prefixes longer than this value with an ellipsis when displaying possible completions. If a completion begins with a period, and Readline is completing filenames, it uses three underscores instead of an ellipsis.

`completion-query-items`  

completion-query-items

The number of possible completions that determines when the user is asked whether the list of possibilities should be displayed. If the number of possible completions is greater than or equal to this value, Readline asks whether or not the user wishes to view them; otherwise, Readline simply lists the completions. This variable must be set to an integer value greater than or equal to zero. A zero value means Readline should never ask; negative values are treated as zero. The default limit is `100`.

`convert-meta`  

convert-meta

If set to ‘`on`’, Readline converts characters it reads that have the eighth bit set to an ASCII key sequence by clearing the eighth bit and prefixing an ESC character, converting them to a meta-prefixed key sequence. The default value is ‘`on`’, but Readline sets it to ‘`off`’ if the locale contains characters whose encodings may include bytes with the eighth bit set. This variable is dependent on the `LC_CTYPE` locale category, and may change if the locale changes. This variable also affects key bindings; see the description of `force-meta-prefix` below.

`disable-completion`  

disable-completion

If set to ‘`On`’, Readline inhibits word completion. Completion characters are inserted into the line as if they had been mapped to `self-insert`. The default is ‘`off`’.

`echo-control-characters`  

echo-control-characters

When set to ‘`on`’, on operating systems that indicate they support it, Readline echoes a character corresponding to a signal generated from the keyboard. The default is ‘`on`’.

`editing-mode`  

editing-mode

The `editing-mode` variable controls the default set of key bindings. By default, Readline starts up in emacs editing mode, where the keystrokes are most similar to Emacs. This variable can be set to either ‘`emacs`’ or ‘`vi`’.

`emacs-mode-string`  

emacs-mode-string

If the \<show-mode-in-prompt\> variable is enabled, this string is displayed immediately before the last line of the primary prompt when emacs editing mode is active. The value is expanded like a key binding, so the standard set of meta- and control- prefixes and backslash escape sequences is available. The ‘`\1`’ and ‘`\2`’ escapes begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. The default is ‘`@`’.

`enable-active-region`  

enable-active-region The

point is the current cursor position, and mark refers to a saved cursor position (see [Commands For Moving](#Commands-For-Moving)). The text between the point and mark is referred to as the region. When this variable is set to ‘`On`’, Readline allows certain commands to designate the region as active. When the region is active, Readline highlights the text in the region using the value of the `active-region-start-color`, which defaults to the string that enables the terminal’s standout mode. The active region shows the text inserted by bracketed-paste and any matching text found by incremental and non-incremental history searches. The default is ‘`On`’.

`enable-bracketed-paste`  

enable-bracketed-paste

When set to ‘`On`’, Readline configures the terminal to insert each paste into the editing buffer as a single string of characters, instead of treating each character as if it had been read from the keyboard. This is called putting the terminal into bracketed paste mode; it prevents Readline from executing any editing commands bound to key sequences appearing in the pasted text. The default is ‘`On`’.

`enable-keypad`  

enable-keypad

When set to ‘`on`’, Readline tries to enable the application keypad when it is called. Some systems need this to enable the arrow keys. The default is ‘`off`’.

`enable-meta-key`  

enable-meta-key

When set to ‘`on`’, Readline tries to enable any meta modifier key the terminal claims to support when it is called. On many terminals, the Meta key is used to send eight-bit characters; this variable checks for the terminal capability that indicates the terminal can enable and disable a mode that sets the eighth bit of a character (0200) if the Meta key is held down when the character is typed (a meta character). The default is ‘`on`’.

`expand-tilde`  

expand-tilde

If set to ‘`on`’, Readline attempts tilde expansion when it attempts word completion. The default is ‘`off`’.

`force-meta-prefix`  

force-meta-prefix

If set to ‘`on`’, Readline modifies its behavior when binding key sequences containing `\M-` or `Meta-` (see `Key Bindings` in [Readline Init File Syntax](#Readline-Init-File-Syntax)) by converting a key sequence of the form `\M-`\<C\> or `Meta-`\<C\> to the two-character sequence `ESC` \<C\> (adding the meta prefix). If `force-meta-prefix` is set to ‘`off`’ (the default), Readline uses the value of the `convert-meta` variable to determine whether to perform this conversion: if `convert-meta` is ‘`on`’, Readline performs the conversion described above; if it is ‘`off`’, Readline converts \<C\> to a meta character by setting the eighth bit (0200). The default is ‘`off`’.

`history-preserve-point`  

history-preserve-point

If set to ‘`on`’, the history code attempts to place the point (the current cursor position) at the same location on each history line retrieved with `previous-history` or `next-history`. The default is ‘`off`’.

`history-size`  

history-size

Set the maximum number of history entries saved in the history list. If set to zero, any existing history entries are deleted and no new entries are saved. If set to a value less than zero, the number of history entries is not limited. By default, Bash sets the maximum number of history entries to the value of the `HISTSIZE` shell variable. If you try to set \<history-size\> to a non-numeric value, the maximum number of history entries will be set to 500.

`horizontal-scroll-mode`  

horizontal-scroll-mode

Setting this variable to ‘`on`’ means that the text of the lines being edited will scroll horizontally on a single screen line when the lines are longer than the width of the screen, instead of wrapping onto a new screen line. This variable is automatically set to ‘`on`’ for terminals of height 1. By default, this variable is set to ‘`off`’.

`input-meta`  

input-meta

meta-flag

If set to ‘`on`’, Readline enables eight-bit input (that is, it does not clear the eighth bit in the characters it reads), regardless of what the terminal claims it can support. The default value is ‘`off`’, but Readline sets it to ‘`on`’ if the locale contains characters whose encodings may include bytes with the eighth bit set. This variable is dependent on the `LC_CTYPE` locale category, and its value may change if the locale changes. The name `meta-flag` is a synonym for `input-meta`.

`isearch-terminators`  

isearch-terminators

The string of characters that should terminate an incremental search without subsequently executing the character as a command (see [Searching](#Searching)). If this variable has not been given a value, the characters ESC and `C-j` terminate an incremental search.

`keymap`  

keymap

Sets Readline’s idea of the current keymap for key binding commands. Built-in `keymap` names are `emacs`, `emacs-standard`, `emacs-meta`, `emacs-ctlx`, `vi`, `vi-move`, `vi-command`, and `vi-insert`. `vi` is equivalent to `vi-command` (`vi-move` is also a synonym); `emacs` is equivalent to `emacs-standard`. Applications may add additional names. The default value is `emacs`; the value of the `editing-mode` variable also affects the default keymap.

`keyseq-timeout`  
Specifies the duration Readline will wait for a character when reading an ambiguous key sequence (one that can form a complete key sequence using the input read so far, or can take additional input to complete a longer key sequence). If Readline doesn’t receive any input within the timeout, it uses the shorter but complete key sequence. Readline uses this value to determine whether or not input is available on the current input source (`rl_instream` by default). The value is specified in milliseconds, so a value of 1000 means that Readline will wait one second for additional input. If this variable is set to a value less than or equal to zero, or to a non-numeric value, Readline waits until another key is pressed to decide which key sequence to complete. The default value is `500`.

`mark-directories`  
If set to ‘`on`’, completed directory names have a slash appended. The default is ‘`on`’.

`mark-modified-lines`  

mark-modified-lines

When this variable is set to ‘`on`’, Readline displays an asterisk (‘`*`’) at the start of history lines which have been modified. This variable is ‘`off`’ by default.

`mark-symlinked-directories`  

mark-symlinked-directories

If set to ‘`on`’, completed names which are symbolic links to directories have a slash appended, subject to the value of `mark-directories`. The default is ‘`off`’.

`match-hidden-files`  

match-hidden-files

This variable, when set to ‘`on`’, forces Readline to match files whose names begin with a ‘`.`’ (hidden files) when performing filename completion. If set to ‘`off`’, the user must include the leading ‘`.`’ in the filename to be completed. This variable is ‘`on`’ by default.

`menu-complete-display-prefix`  

menu-complete-display-prefix

If set to ‘`on`’, menu completion displays the common prefix of the list of possible completions (which may be empty) before cycling through the list. The default is ‘`off`’.

`output-meta`  

output-meta

If set to ‘`on`’, Readline displays characters with the eighth bit set directly rather than as a meta-prefixed escape sequence. The default is ‘`off`’, but Readline sets it to ‘`on`’ if the locale contains characters whose encodings may include bytes with the eighth bit set. This variable is dependent on the `LC_CTYPE` locale category, and its value may change if the locale changes.

`page-completions`  

page-completions

If set to ‘`on`’, Readline uses an internal pager resembling *more*(1) to display a screenful of possible completions at a time. This variable is ‘`on`’ by default.

`prefer-visible-bell`  
See `bell-style`.

`print-completions-horizontally`  
If set to ‘`on`’, Readline displays completions with matches sorted horizontally in alphabetical order, rather than down the screen. The default is ‘`off`’.

`revert-all-at-newline`  

revert-all-at-newline

If set to ‘`on`’, Readline will undo all changes to history lines before returning when executing `accept-line`. By default, history lines may be modified and retain individual undo lists across calls to `readline()`. The default is ‘`off`’.

`search-ignore-case`  

search-ignore-case

If set to ‘`on`’, Readline performs incremental and non-incremental history list searches in a case-insensitive fashion. The default value is ‘`off`’.

`show-all-if-ambiguous`  

show-all-if-ambiguous

This alters the default behavior of the completion functions. If set to ‘`on`’, words which have more than one possible completion cause the matches to be listed immediately instead of ringing the bell. The default value is ‘`off`’.

`show-all-if-unmodified`  

show-all-if-unmodified

This alters the default behavior of the completion functions in a fashion similar to \<show-all-if-ambiguous\>. If set to ‘`on`’, words which have more than one possible completion without any possible partial completion (the possible completions don’t share a common prefix) cause the matches to be listed immediately instead of ringing the bell. The default value is ‘`off`’.

`show-mode-in-prompt`  

show-mode-in-prompt

If set to ‘`on`’, add a string to the beginning of the prompt indicating the editing mode: emacs, vi command, or vi insertion. The mode strings are user-settable (e.g., \<emacs-mode-string\>). The default value is ‘`off`’.

`skip-completed-text`  

skip-completed-text

If set to ‘`on`’, this alters the default completion behavior when inserting a single match into the line. It’s only active when performing completion in the middle of a word. If enabled, Readline does not insert characters from the completion that match characters after point in the word being completed, so portions of the word following the cursor are not duplicated. For instance, if this is enabled, attempting completion when the cursor is after the first ‘`e`’ in ‘`Makefile`’ will result in ‘`Makefile`’ rather than ‘`Makefilefile`’, assuming there is a single possible completion. The default value is ‘`off`’.

`vi-cmd-mode-string`  

vi-cmd-mode-string

If the \<show-mode-in-prompt\> variable is enabled, this string is displayed immediately before the last line of the primary prompt when vi editing mode is active and in command mode. The value is expanded like a key binding, so the standard set of meta- and control- prefixes and backslash escape sequences is available. The ‘`\1`’ and ‘`\2`’ escapes begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. The default is ‘`(cmd)`’.

`vi-ins-mode-string`  

vi-ins-mode-string

If the \<show-mode-in-prompt\> variable is enabled, this string is displayed immediately before the last line of the primary prompt when vi editing mode is active and in insertion mode. The value is expanded like a key binding, so the standard set of meta- and control- prefixes and backslash escape sequences is available. The ‘`\1`’ and ‘`\2`’ escapes begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. The default is ‘`(ins)`’.

`visible-stats`  

visible-stats

If set to ‘`on`’, a character denoting a file’s type is appended to the filename when listing possible completions. The default is ‘`off`’.

Key Bindings  
The syntax for controlling key bindings in the init file is simple. First you need to find the name of the command that you want to change. The following sections contain tables of the command name, the default keybinding, if any, and a short description of what the command does.

Once you know the name of the command, simply place on a line in the init file the name of the key you wish to bind the command to, a colon, and then the name of the command. There can be no space between the key name and the colon – that will be interpreted as part of the key name. The name of the key can be expressed in different ways, depending on what you find most comfortable.

In addition to command names, Readline allows keys to be bound to a string that is inserted when the key is pressed (a \<macro\>). The difference between a macro and a command is that a macro is enclosed in single or double quotes.

The `bind&#160;-p` command displays Readline function names and bindings in a format that can be put directly into an initialization file. See [Bash Builtins](#Bash-Builtins).

\<keyname\>:\&#160;\<function-name\>\&#160;or\&#160;\<macro\>  
\<keyname\> is the name of a key spelled out in English. For example:

    Control-u: universal-argument
    Meta-Rubout: backward-kill-word
    Control-o: "> output"

In the example above, `C-u` is bound to the function `universal-argument`, `M-DEL` is bound to the function `backward-kill-word`, and `C-o` is bound to run the macro expressed on the right hand side (that is, to insert the text ‘`> output`’ into the line).

This key binding syntax recognizes a number of symbolic character names: \<DEL\>, \<ESC\>, \<ESCAPE\>, \<LFD\>, \<NEWLINE\>, \<RET\>, \<RETURN\>, \<RUBOUT\> (a destructive backspace), \<SPACE\>, \<SPC\>, and \<TAB\>.

"\<keyseq\>":\&#160;\<function-name\>\&#160;or\&#160;\<macro\>  
\<keyseq\> differs from \<keyname\> above in that strings denoting an entire key sequence can be specified, by placing the key sequence in double quotes. Some GNU Emacs style key escapes can be used, as in the following example, but none of the special character names are recognized.

    "\C-u": universal-argument
    "\C-x\C-r": re-read-init-file
    "\e[11~": "Function Key 1"

In the above example, `C-u` is again bound to the function `universal-argument` (just as it was in the first example), ‘`C-x C-r`’ is bound to the function `re-read-init-file`, and ‘`ESC [ 1 1 ~`’ is bound to insert the text ‘`Function Key 1`’.

The following GNU Emacs style escape sequences are available when specifying key sequences:

`\C-`  
A control prefix.

`\M-`  
Adding the meta prefix or converting the following character to a meta character, as described above under `force-meta-prefix` (see `Variable Settings` in [Readline Init File Syntax](#Readline-Init-File-Syntax)).

`\e`  
An escape character.

`\\`  
Backslash.

`\"`  
", a double quotation mark.

`\'`  
', a single quote or apostrophe.

In addition to the GNU Emacs style escape sequences, a second set of backslash escapes is available:

`\a`  
alert (bell)

`\b`  
backspace

`\d`  
delete

`\f`  
form feed

`\n`  
newline

`\r`  
carriage return

`\t`  
horizontal tab

`\v`  
vertical tab

`\nnn`  
The eight-bit character whose value is the octal value \<nnn\> (one to three digits).

`\xHH`  
The eight-bit character whose value is the hexadecimal value \<HH\> (one or two hex digits).

When entering the text of a macro, single or double quotes must be used to indicate a macro definition. Unquoted text is assumed to be a function name. The backslash escapes described above are expanded in the macro body. Backslash will quote any other character in the macro text, including ‘`"`’ and ‘`'`’. For example, the following binding will make ‘`C-x \`’ insert a single ‘`\`’ into the line:

    "\C-x\\": "\\"

### Conditional Init Constructs

Readline implements a facility similar in spirit to the conditional compilation features of the C preprocessor which allows key bindings and variable settings to be performed as the result of tests. There are four parser directives available.

`$if`  
The `$if` construct allows bindings to be made based on the editing mode, the terminal being used, or the application using Readline. The text of the test, after any comparison operator, extends to the end of the line; unless otherwise noted, no characters are required to isolate it.

`mode`  
The `mode=` form of the `$if` directive is used to test whether Readline is in `emacs` or `vi` mode. This may be used in conjunction with the ‘`set keymap`’ command, for instance, to set bindings in the `emacs-standard` and `emacs-ctlx` keymaps only if Readline is starting out in `emacs` mode.

`term`  
The `term=` form may be used to include terminal-specific key bindings, perhaps to bind the key sequences output by the terminal’s function keys. The word on the right side of the ‘`=`’ is tested against both the full name of the terminal and the portion of the terminal name before the first ‘`-`’. This allows `xterm` to match both `xterm` and `xterm-256color`, for instance.

`version`  
The `version` test may be used to perform comparisons against specific Readline versions. The `version` expands to the current Readline version. The set of comparison operators includes ‘`=`’ (and ‘`==`’), ‘`!=`’, ‘`<=`’, ‘`>=`’, ‘`<`’, and ‘`>`’. The version number supplied on the right side of the operator consists of a major version number, an optional decimal point, and an optional minor version (e.g., ‘`7.1`’). If the minor version is omitted, it defaults to ‘`0`’. The operator may be separated from the string `version` and from the version number argument by whitespace. The following example sets a variable if the Readline version being used is 7.0 or newer:

    $if version >= 7.0
    set show-mode-in-prompt on
    $endif

`application`  
The \<application\> construct is used to include application-specific settings. Each program using the Readline library sets the \<application name\>, and you can test for a particular value. This could be used to bind key sequences to functions useful for a specific program. For instance, the following command adds a key sequence that quotes the current or previous word in Bash:

    $if Bash
    # Quote the current or previous word
    "\C-xq": "\eb\"\ef\""
    $endif

`variable`  
The \<variable\> construct provides simple equality tests for Readline variables and values. The permitted comparison operators are ‘`=`’, ‘`==`’, and ‘`!=`’. The variable name must be separated from the comparison operator by whitespace; the operator may be separated from the value on the right hand side by whitespace. String and boolean variables may be tested. Boolean variables must be tested against the values \<on\> and \<off\>. The following example is equivalent to the `mode=emacs` test described above:

    $if editing-mode == emacs
    set show-mode-in-prompt on
    $endif

`$else`  
Commands in this branch of the `$if` directive are executed if the test fails.

`$endif`  
This command, as seen in the previous example, terminates an `$if` command.

`$include`  
This directive takes a single filename as an argument and reads commands and key bindings from that file. For example, the following directive reads from `/etc/inputrc`:

    $include /etc/inputrc

### Sample Init File

Here is an example of an \<inputrc\> file. This illustrates key binding, variable assignment, and conditional syntax.

    # This file controls the behavior of line input editing for
    # programs that use the GNU Readline library.  Existing
    # programs include FTP, Bash, and GDB.
    #
    # You can re-read the inputrc file with C-x C-r.
    # Lines beginning with '#' are comments.
    #
    # First, include any system-wide bindings and variable
    # assignments from /etc/Inputrc
    $include /etc/Inputrc

    #
    # Set various bindings for emacs mode.

    set editing-mode emacs 

    $if mode=emacs

    Meta-Control-h: backward-kill-word  Text after the function name is ignored

    #
    # Arrow keys in keypad mode
    #
    #"\M-OD":        backward-char
    #"\M-OC":        forward-char
    #"\M-OA":        previous-history
    #"\M-OB":        next-history
    #
    # Arrow keys in ANSI mode
    #
    "\M-[D":        backward-char
    "\M-[C":        forward-char
    "\M-[A":        previous-history
    "\M-[B":        next-history
    #
    # Arrow keys in 8 bit keypad mode
    #
    #"\M-\C-OD":       backward-char
    #"\M-\C-OC":       forward-char
    #"\M-\C-OA":       previous-history
    #"\M-\C-OB":       next-history
    #
    # Arrow keys in 8 bit ANSI mode
    #
    #"\M-\C-[D":       backward-char
    #"\M-\C-[C":       forward-char
    #"\M-\C-[A":       previous-history
    #"\M-\C-[B":       next-history

    C-q: quoted-insert

    $endif

    # An old-style binding.  This happens to be the default.
    TAB: complete

    # Macros that are convenient for shell interaction
    $if Bash
    # edit the path
    "\C-xp": "PATH=${PATH}\e\C-e\C-a\ef\C-f"
    # prepare to type a quoted word --
    # insert open and close double quotes
    # and move to just after the open quote
    "\C-x\"": "\"\"\C-b"
    # insert a backslash (testing backslash escapes
    # in sequences and macros)
    "\C-x\\": "\\"
    # Quote the current or previous word
    "\C-xq": "\eb\"\ef\""
    # Add a binding to refresh the line, which is unbound
    "\C-xr": redraw-current-line
    # Edit variable on current line.
    "\M-\C-v": "\C-a\C-k$\C-y\M-\C-e\C-a\C-y="
    $endif

    # use a visible bell if one is available
    set bell-style visible

    # don't strip characters to 7 bits when reading
    set input-meta on

    # allow iso-latin1 characters to be inserted rather
    # than converted to prefix-meta sequences
    set convert-meta off

    # display characters with the eighth bit set directly
    # rather than as meta-prefixed characters
    set output-meta on

    # if there are 150 or more possible completions for a word,
    # ask whether or not the user wants to see all of them
    set completion-query-items 150

    # For FTP
    $if Ftp
    "\C-xg": "get \M-?"
    "\C-xt": "put \M-?"
    "\M-.": yank-last-arg
    $endif
