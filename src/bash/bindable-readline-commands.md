---
title: Bindable Readline Commands
source_url: https://www.gnu.org/software/bash/manual
source_path: 043-bindable-readline-commands.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 430
---

## Bindable Readline Commands

This section describes Readline commands that may be bound to key sequences. You can list your key bindings by executing `bind&#160;-P` or, for a more terse format, suitable for an \<inputrc\> file, `bind&#160;-p`. (See [Bash Builtins](#Bash-Builtins).) Command names without an accompanying key sequence are unbound by default.

In the following descriptions, point refers to the current cursor position, and mark refers to a cursor position saved by the `set-mark` command. The text between the point and mark is referred to as the region. Readline has the concept of an *active region*: when the region is active, Readline redisplay highlights the region using the value of the `active-region-start-color` variable. The `enable-active-region` variable turns this on and off. Several commands set the region to active; those are noted below.

### Commands For Moving

<span class="indexterm fn" role="fn"></span>`beginning-of-line (C-a)`  
Move to the start of the current line. This may also be bound to the Home key on some keyboards.

<span class="indexterm fn" role="fn"></span>`end-of-line (C-e)`  
Move to the end of the line. This may also be bound to the End key on some keyboards.

<span class="indexterm fn" role="fn"></span>`forward-char (C-f)`  
Move forward a character. This may also be bound to the right arrow key on some keyboards.

<span class="indexterm fn" role="fn"></span>`backward-char (C-b)`  
Move back a character. This may also be bound to the left arrow key on some keyboards.

<span class="indexterm fn" role="fn"></span>`forward-word (M-f)`  
Move forward to the end of the next word. Words are composed of letters and digits.

<span class="indexterm fn" role="fn"></span>`backward-word (M-b)`  
Move back to the start of the current or previous word. Words are composed of letters and digits.

<span class="indexterm fn" role="fn"></span>`shell-forward-word (M-C-f)`  
Move forward to the end of the next word. Words are delimited by non-quoted shell metacharacters.

<span class="indexterm fn" role="fn"></span>`shell-backward-word (M-C-b)`  
Move back to the start of the current or previous word. Words are delimited by non-quoted shell metacharacters.

<span class="indexterm fn" role="fn"></span>`previous-screen-line ()`  
Attempt to move point to the same physical screen column on the previous physical screen line. This will not have the desired effect if the current Readline line does not take up more than one physical line or if point is not greater than the length of the prompt plus the screen width.

<span class="indexterm fn" role="fn"></span>`next-screen-line ()`  
Attempt to move point to the same physical screen column on the next physical screen line. This will not have the desired effect if the current Readline line does not take up more than one physical line or if the length of the current Readline line is not greater than the length of the prompt plus the screen width.

<span class="indexterm fn" role="fn"></span>`clear-display (M-C-l)`  
Clear the screen and, if possible, the terminal’s scrollback buffer, then redraw the current line, leaving the current line at the top of the screen.

<span class="indexterm fn" role="fn"></span>`clear-screen (C-l)`  
Clear the screen, then redraw the current line, leaving the current line at the top of the screen. If given a numeric argument, this refreshes the current line without clearing the screen.

<span class="indexterm fn" role="fn"></span>`redraw-current-line ()`  
Refresh the current line. By default, this is unbound.

### Commands For Manipulating The History

<span class="indexterm fn" role="fn"></span>`accept-line (Newline or Return)`  
Accept the line regardless of where the cursor is. If this line is non-empty, add it to the history list according to the setting of the `HISTCONTROL` and `HISTIGNORE` variables. If this line is a modified history line, then restore the history line to its original state.

<span class="indexterm fn" role="fn"></span>`previous-history (C-p)`  
Move ‘back’ through the history list, fetching the previous command. This may also be bound to the up arrow key on some keyboards.

<span class="indexterm fn" role="fn"></span>`next-history (C-n)`  
Move ‘forward’ through the history list, fetching the next command. This may also be bound to the down arrow key on some keyboards.

<span class="indexterm fn" role="fn"></span>`beginning-of-history (M-<)`  
Move to the first line in the history.

<span class="indexterm fn" role="fn"></span>`end-of-history (M->)`  
Move to the end of the input history, i.e., the line currently being entered.

<span class="indexterm fn" role="fn"></span>`reverse-search-history (C-r)`  
Search backward starting at the current line and moving ‘up’ through the history as necessary. This is an incremental search. This command sets the region to the matched text and activates the region.

<span class="indexterm fn" role="fn"></span>`forward-search-history (C-s)`  
Search forward starting at the current line and moving ‘down’ through the history as necessary. This is an incremental search. This command sets the region to the matched text and activates the region.

<span class="indexterm fn" role="fn"></span>`non-incremental-reverse-search-history (M-p)`  
Search backward starting at the current line and moving ‘up’ through the history as necessary using a non-incremental search for a string supplied by the user. The search string may match anywhere in a history line.

<span class="indexterm fn" role="fn"></span>`non-incremental-forward-search-history (M-n)`  
Search forward starting at the current line and moving ‘down’ through the history as necessary using a non-incremental search for a string supplied by the user. The search string may match anywhere in a history line.

<span class="indexterm fn" role="fn"></span>`history-search-backward ()`  
Search backward through the history for the string of characters between the start of the current line and the point. The search string must match at the beginning of a history line. This is a non-incremental search. By default, this command is unbound, but may be bound to the Page Down key on some keyboards.

<span class="indexterm fn" role="fn"></span>`history-search-forward ()`  
Search forward through the history for the string of characters between the start of the current line and the point. The search string must match at the beginning of a history line. This is a non-incremental search. By default, this command is unbound, but may be bound to the Page Up key on some keyboards.

<span class="indexterm fn" role="fn"></span>`history-substring-search-backward ()`  
Search backward through the history for the string of characters between the start of the current line and the point. The search string may match anywhere in a history line. This is a non-incremental search. By default, this command is unbound.

<span class="indexterm fn" role="fn"></span>`history-substring-search-forward ()`  
Search forward through the history for the string of characters between the start of the current line and the point. The search string may match anywhere in a history line. This is a non-incremental search. By default, this command is unbound.

<span class="indexterm fn" role="fn"></span>`yank-nth-arg (M-C-y)`  
Insert the first argument to the previous command (usually the second word on the previous line) at point. With an argument \<n\>, insert the \<n\>th word from the previous command (the words in the previous command begin with word 0). A negative argument inserts the \<n\>th word from the end of the previous command. Once the argument \<n\> is computed, this uses the history expansion facilities to extract the \<n\>th word, as if the ‘`!n`’ history expansion had been specified.

<span class="indexterm fn" role="fn"></span>`yank-last-arg (M-. or M-_)`  
Insert last argument to the previous command (the last word of the previous history entry). With a numeric argument, behave exactly like `yank-nth-arg`. Successive calls to `yank-last-arg` move back through the history list, inserting the last word (or the word specified by the argument to the first call) of each line in turn. Any numeric argument supplied to these successive calls determines the direction to move through the history. A negative argument switches the direction through the history (back or forward). This uses the history expansion facilities to extract the last word, as if the ‘`!$`’ history expansion had been specified.

<span class="indexterm fn" role="fn"></span>`operate-and-get-next (C-o)`  
Accept the current line for return to the calling application as if a newline had been entered, and fetch the next line relative to the current line from the history for editing. A numeric argument, if supplied, specifies the history entry to use instead of the current line.

<span class="indexterm fn" role="fn"></span>`fetch-history ()`  
With a numeric argument, fetch that entry from the history list and make it the current line. Without an argument, move back to the first entry in the history list.

### Commands For Changing Text

<span class="indexterm fn" role="fn"></span>`end-of-file (usually C-d)`  
The character indicating end-of-file as set, for example, by `stty`. If this character is read when there are no characters on the line, and point is at the beginning of the line, Readline interprets it as the end of input and returns EOF.

<span class="indexterm fn" role="fn"></span>`delete-char (C-d)`  
Delete the character at point. If this function is bound to the same character as the tty EOF character, as `C-d` commonly is, see above for the effects. This may also be bound to the Delete key on some keyboards.

<span class="indexterm fn" role="fn"></span>`backward-delete-char (Rubout)`  
Delete the character behind the cursor. A numeric argument means to kill the characters, saving them on the kill ring, instead of deleting them.

<span class="indexterm fn" role="fn"></span>`forward-backward-delete-char ()`  
Delete the character under the cursor, unless the cursor is at the end of the line, in which case the character behind the cursor is deleted. By default, this is not bound to a key.

<span class="indexterm fn" role="fn"></span>`quoted-insert (C-q or C-v)`  
Add the next character typed to the line verbatim. This is how to insert key sequences like `C-q`, for example.

<span class="indexterm fn" role="fn"></span>`self-insert (a, b, A, 1, !, …)`  
Insert the character typed.

<span class="indexterm fn" role="fn"></span>`bracketed-paste-begin ()`  
This function is intended to be bound to the "bracketed paste" escape sequence sent by some terminals, and such a binding is assigned by default. It allows Readline to insert the pasted text as a single unit without treating each character as if it had been read from the keyboard. The characters are inserted as if each one was bound to `self-insert` instead of executing any editing commands.

Bracketed paste sets the region (the characters between point and the mark) to the inserted text. It sets the *active region*.

<span class="indexterm fn" role="fn"></span>`transpose-chars (C-t)`  
Drag the character before the cursor forward over the character at the cursor, moving the cursor forward as well. If the insertion point is at the end of the line, then this transposes the last two characters of the line. Negative arguments have no effect.

<span class="indexterm fn" role="fn"></span>`transpose-words (M-t)`  
Drag the word before point past the word after point, moving point past that word as well. If the insertion point is at the end of the line, this transposes the last two words on the line.

<span class="indexterm fn" role="fn"></span>`shell-transpose-words (M-C-t)`  
Drag the word before point past the word after point, moving point past that word as well. If the insertion point is at the end of the line, this transposes the last two words on the line. Word boundaries are the same as `shell-forward-word` and `shell-backward-word`.

<span class="indexterm fn" role="fn"></span>`upcase-word (M-u)`  
Uppercase the current (or following) word. With a negative argument, uppercase the previous word, but do not move the cursor.

<span class="indexterm fn" role="fn"></span>`downcase-word (M-l)`  
Lowercase the current (or following) word. With a negative argument, lowercase the previous word, but do not move the cursor.

<span class="indexterm fn" role="fn"></span>`capitalize-word (M-c)`  
Capitalize the current (or following) word. With a negative argument, capitalize the previous word, but do not move the cursor.

<span class="indexterm fn" role="fn"></span>`overwrite-mode ()`  
Toggle overwrite mode. With an explicit positive numeric argument, switches to overwrite mode. With an explicit non-positive numeric argument, switches to insert mode. This command affects only `emacs` mode; `vi` mode does overwrite differently. Each call to `readline()` starts in insert mode.

In overwrite mode, characters bound to `self-insert` replace the text at point rather than pushing the text to the right. Characters bound to `backward-delete-char` replace the character before point with a space.

By default, this command is unbound, but may be bound to the Insert key on some keyboards.

### Killing And Yanking

<span class="indexterm fn" role="fn"></span>`kill-line (C-k)`  
Kill the text from point to the end of the current line. With a negative numeric argument, kill backward from the cursor to the beginning of the line.

<span class="indexterm fn" role="fn"></span>`backward-kill-line (C-x Rubout)`  
Kill backward from the cursor to the beginning of the current line. With a negative numeric argument, kill forward from the cursor to the end of the line.

<span class="indexterm fn" role="fn"></span>`unix-line-discard (C-u)`  
Kill backward from the cursor to the beginning of the current line.

<span class="indexterm fn" role="fn"></span>`kill-whole-line ()`  
Kill all characters on the current line, no matter where point is. By default, this is unbound.

<span class="indexterm fn" role="fn"></span>`kill-word (M-d)`  
Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as `forward-word`.

<span class="indexterm fn" role="fn"></span>`backward-kill-word (M-DEL)`  
Kill the word behind point. Word boundaries are the same as `backward-word`.

<span class="indexterm fn" role="fn"></span>`shell-kill-word (M-C-d)`  
Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as `shell-forward-word`.

<span class="indexterm fn" role="fn"></span>`shell-backward-kill-word ()`  
Kill the word behind point. Word boundaries are the same as `shell-backward-word`.

<span class="indexterm fn" role="fn"></span>`unix-word-rubout (C-w)`  
Kill the word behind point, using white space as a word boundary, saving the killed text on the kill-ring.

<span class="indexterm fn" role="fn"></span>`unix-filename-rubout ()`  
Kill the word behind point, using white space and the slash character as the word boundaries, saving the killed text on the kill-ring.

<span class="indexterm fn" role="fn"></span>`delete-horizontal-space ()`  
Delete all spaces and tabs around point. By default, this is unbound.

<span class="indexterm fn" role="fn"></span>`kill-region ()`  
Kill the text in the current region. By default, this command is unbound.

<span class="indexterm fn" role="fn"></span>`copy-region-as-kill ()`  
Copy the text in the region to the kill buffer, so it can be yanked right away. By default, this command is unbound.

<span class="indexterm fn" role="fn"></span>`copy-backward-word ()`  
Copy the word before point to the kill buffer. The word boundaries are the same as `backward-word`. By default, this command is unbound.

<span class="indexterm fn" role="fn"></span>`copy-forward-word ()`  
Copy the word following point to the kill buffer. The word boundaries are the same as `forward-word`. By default, this command is unbound.

<span class="indexterm fn" role="fn"></span>`yank (C-y)`  
Yank the top of the kill ring into the buffer at point.

<span class="indexterm fn" role="fn"></span>`yank-pop (M-y)`  
Rotate the kill-ring, and yank the new top. You can only do this if the prior command is `yank` or `yank-pop`.

### Specifying Numeric Arguments

<span class="indexterm fn" role="fn"></span>`digit-argument (M-0, M-1, … M--)`  
Add this digit to the argument already accumulating, or start a new argument. `M--` starts a negative argument.

<span class="indexterm fn" role="fn"></span>`universal-argument ()`  
This is another way to specify an argument. If this command is followed by one or more digits, optionally with a leading minus sign, those digits define the argument. If the command is followed by digits, executing `universal-argument` again ends the numeric argument, but is otherwise ignored. As a special case, if this command is immediately followed by a character that is neither a digit nor minus sign, the argument count for the next command is multiplied by four. The argument count is initially one, so executing this function the first time makes the argument count four, a second time makes the argument count sixteen, and so on. By default, this is not bound to a key.

### Letting Readline Type For You

<span class="indexterm fn" role="fn"></span>`complete (TAB)`  
Attempt to perform completion on the text before point. The actual completion performed is application-specific. Bash attempts completion by first checking for any programmable completions for the command word (see [Programmable Completion](#Programmable-Completion)), otherwise treating the text as a variable (if the text begins with ‘`$`’), username (if the text begins with ‘`~`’), hostname (if the text begins with ‘`@`’), or command (including aliases, functions, and builtins) in turn. If none of these produces a match, it falls back to filename completion.

<span class="indexterm fn" role="fn"></span>`possible-completions (M-?)`  
List the possible completions of the text before point. When displaying completions, Readline sets the number of columns used for display to the value of `completion-display-width`, the value of the environment variable `COLUMNS`, or the screen width, in that order.

<span class="indexterm fn" role="fn"></span>`insert-completions (M-*)`  
Insert all completions of the text before point that would have been generated by `possible-completions`, separated by a space.

<span class="indexterm fn" role="fn"></span>`menu-complete ()`  
Similar to `complete`, but replaces the word to be completed with a single match from the list of possible completions. Repeatedly executing `menu-complete` steps through the list of possible completions, inserting each match in turn. At the end of the list of completions, `menu-complete` rings the bell (subject to the setting of `bell-style`) and restores the original text. An argument of \<n\> moves \<n\> positions forward in the list of matches; a negative argument moves backward through the list. This command is intended to be bound to TAB, but is unbound by default.

<span class="indexterm fn" role="fn"></span>`menu-complete-backward ()`  
Identical to `menu-complete`, but moves backward through the list of possible completions, as if `menu-complete` had been given a negative argument. This command is unbound by default.

<span class="indexterm fn" role="fn"></span>`export-completions ()`  
Perform completion on the word before point as described above and write the list of possible completions to Readline’s output stream using the following format, writing information on separate lines:

- the number of matches \<N\>;

- the word being completed;

- \<S\>:\<E\>, where \<S\> and \<E\> are the start and end offsets of the word in the Readline line buffer; then

- each match, one per line

If there are no matches, the first line will be “0”, and this command does not print any output after the \<S\>:\<E\>. If there is only a single match, this prints a single line containing it. If there is more than one match, this prints the common prefix of the matches, which may be empty, on the first line after the \<S\>:\<E\>, then the matches on subsequent lines. In this case, \<N\> will include the first line with the common prefix.

The user or application should be able to accommodate the possibility of a blank line. The intent is that the user or application reads \<N\> lines after the line containing \<S\>:\<E\> to obtain the match list. This command is unbound by default.

<span class="indexterm fn" role="fn"></span>`delete-char-or-list ()`  
Deletes the character under the cursor if not at the beginning or end of the line (like `delete-char`). At the end of the line, it behaves identically to `possible-completions`. This command is unbound by default.

<span class="indexterm fn" role="fn"></span>`complete-filename (M-/)`  
Attempt filename completion on the text before point.

<span class="indexterm fn" role="fn"></span>`possible-filename-completions (C-x /)`  
List the possible completions of the text before point, treating it as a filename.

<span class="indexterm fn" role="fn"></span>`complete-username (M-~)`  
Attempt completion on the text before point, treating it as a username.

<span class="indexterm fn" role="fn"></span>`possible-username-completions (C-x ~)`  
List the possible completions of the text before point, treating it as a username.

<span class="indexterm fn" role="fn"></span>`complete-variable (M-$)`  
Attempt completion on the text before point, treating it as a shell variable.

<span class="indexterm fn" role="fn"></span>`possible-variable-completions (C-x $)`  
List the possible completions of the text before point, treating it as a shell variable.

<span class="indexterm fn" role="fn"></span>`complete-hostname (M-@)`  
Attempt completion on the text before point, treating it as a hostname.

<span class="indexterm fn" role="fn"></span>`possible-hostname-completions (C-x @)`  
List the possible completions of the text before point, treating it as a hostname.

<span class="indexterm fn" role="fn"></span>`complete-command (M-!)`  
Attempt completion on the text before point, treating it as a command name. Command completion attempts to match the text against aliases, reserved words, shell functions, shell builtins, and finally executable filenames, in that order.

<span class="indexterm fn" role="fn"></span>`possible-command-completions (C-x !)`  
List the possible completions of the text before point, treating it as a command name.

<span class="indexterm fn" role="fn"></span>`dynamic-complete-history (M-TAB)`  
Attempt completion on the text before point, comparing the text against history list entries for possible completion matches.

<span class="indexterm fn" role="fn"></span>`dabbrev-expand ()`  
Attempt menu completion on the text before point, comparing the text against lines from the history list for possible completion matches.

<span class="indexterm fn" role="fn"></span>`complete-into-braces (M-{)`  
Perform filename completion and insert the list of possible completions enclosed within braces so the list is available to the shell (see [Brace Expansion](#Brace-Expansion)).

### Keyboard Macros

<span class="indexterm fn" role="fn"></span>`start-kbd-macro (C-x ()`  
Begin saving the characters typed into the current keyboard macro.

<span class="indexterm fn" role="fn"></span>`end-kbd-macro (C-x ))`  
Stop saving the characters typed into the current keyboard macro and save the definition.

<span class="indexterm fn" role="fn"></span>`call-last-kbd-macro (C-x e)`  
Re-execute the last keyboard macro defined, by making the characters in the macro appear as if typed at the keyboard.

<span class="indexterm fn" role="fn"></span>`print-last-kbd-macro ()`  
Print the last keyboard macro defined in a format suitable for the \<inputrc\> file.

### Some Miscellaneous Commands

<span class="indexterm fn" role="fn"></span>`re-read-init-file (C-x C-r)`  
Read in the contents of the \<inputrc\> file, and incorporate any bindings or variable assignments found there.

<span class="indexterm fn" role="fn"></span>`abort (C-g)`  
Abort the current editing command and ring the terminal’s bell (subject to the setting of `bell-style`).

<span class="indexterm fn" role="fn"></span>`do-lowercase-version (M-A, M-B, M-x, …)`  
If the metafied character \<x\> is upper case, run the command that is bound to the corresponding metafied lower case character. The behavior is undefined if \<x\> is already lower case.

<span class="indexterm fn" role="fn"></span>`prefix-meta (ESC)`  
Metafy the next character typed. Typing ‘`ESC f`’ is equivalent to typing `M-f`.

<span class="indexterm fn" role="fn"></span>`undo (C-_ or C-x C-u)`  
Incremental undo, separately remembered for each line.

<span class="indexterm fn" role="fn"></span>`revert-line (M-r)`  
Undo all changes made to this line. This is like executing the `undo` command enough times to get back to the initial state.

<span class="indexterm fn" role="fn"></span>`tilde-expand (M-&)`  
Perform tilde expansion on the current word.

<span class="indexterm fn" role="fn"></span>`set-mark (C-@)`  
Set the mark to the point. If a numeric argument is supplied, set the mark to that position.

<span class="indexterm fn" role="fn"></span>`exchange-point-and-mark (C-x C-x)`  
Swap the point with the mark. Set the current cursor position to the saved position, then set the mark to the old cursor position.

<span class="indexterm fn" role="fn"></span>`character-search (C-])`  
Read a character and move point to the next occurrence of that character. A negative argument searches for previous occurrences.

<span class="indexterm fn" role="fn"></span>`character-search-backward (M-C-])`  
Read a character and move point to the previous occurrence of that character. A negative argument searches for subsequent occurrences.

<span class="indexterm fn" role="fn"></span>`skip-csi-sequence ()`  
Read enough characters to consume a multi-key sequence such as those defined for keys like Home and End. CSI sequences begin with a Control Sequence Indicator (CSI), usually `ESC [`. If this sequence is bound to "\e\[", keys producing CSI sequences have no effect unless explicitly bound to a Readline command, instead of inserting stray characters into the editing buffer. This is unbound by default, but usually bound to `ESC [`.

<span class="indexterm fn" role="fn"></span>`insert-comment (M-#)`  
Without a numeric argument, insert the value of the `comment-begin` variable at the beginning of the current line. If a numeric argument is supplied, this command acts as a toggle: if the characters at the beginning of the line do not match the value of `comment-begin`, insert the value; otherwise delete the characters in `comment-begin` from the beginning of the line. In either case, the line is accepted as if a newline had been typed. The default value of `comment-begin` causes this command to make the current line a shell comment. If a numeric argument causes the comment character to be removed, the line will be executed by the shell.

<span class="indexterm fn" role="fn"></span>`dump-functions ()`  
Print all of the functions and their key bindings to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an \<inputrc\> file. This command is unbound by default.

<span class="indexterm fn" role="fn"></span>`dump-variables ()`  
Print all of the settable variables and their values to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an \<inputrc\> file. This command is unbound by default.

<span class="indexterm fn" role="fn"></span>`dump-macros ()`  
Print all of the Readline key sequences bound to macros and the strings they output to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an \<inputrc\> file. This command is unbound by default.

<span class="indexterm fn" role="fn"></span>`execute-named-command (M-x)`  
Read a bindable Readline command name from the input and execute the function to which it’s bound, as if the key sequence to which it was bound appeared in the input. If this function is supplied with a numeric argument, it passes that argument to the function it executes.

<span class="indexterm fn" role="fn"></span>`spell-correct-word (C-x s)`  
Perform spelling correction on the current word, treating it as a directory or filename, in the same way as the `cdspell` shell option. Word boundaries are the same as those used by `shell-forward-word`.

<span class="indexterm fn" role="fn"></span>`glob-complete-word (M-g)`  
Treat the word before point as a pattern for pathname expansion, with an asterisk implicitly appended, then use the pattern to generate a list of matching file names for possible completions.

<span class="indexterm fn" role="fn"></span>`glob-expand-word (C-x *)`  
Treat the word before point as a pattern for pathname expansion, and insert the list of matching file names, replacing the word. If a numeric argument is supplied, append a ‘`*`’ before pathname expansion.

<span class="indexterm fn" role="fn"></span>`glob-list-expansions (C-x g)`  
Display the list of expansions that would have been generated by `glob-expand-word`, and redisplay the line. If a numeric argument is supplied, append a ‘`*`’ before pathname expansion.

<span class="indexterm fn" role="fn"></span>`shell-expand-line (M-C-e)`  
Expand the line by performing shell word expansions. This performs alias and history expansion, \$’\<string\>’ and \$"\<string\>" quoting, tilde expansion, parameter and variable expansion, arithmetic expansion, command and process substitution, word splitting, and quote removal. An explicit argument suppresses command and process substitution.

<span class="indexterm fn" role="fn"></span>`history-expand-line (M-^)`  
Perform history expansion on the current line.

<span class="indexterm fn" role="fn"></span>`magic-space ()`  
Perform history expansion on the current line and insert a space (see [History Interaction](#History-Interaction)).

<span class="indexterm fn" role="fn"></span>`alias-expand-line ()`  
Perform alias expansion on the current line (see [Aliases](#Aliases)).

<span class="indexterm fn" role="fn"></span>`history-and-alias-expand-line ()`  
Perform history and alias expansion on the current line.

<span class="indexterm fn" role="fn"></span>`insert-last-argument (M-. or M-_)`  
A synonym for `yank-last-arg`.

<span class="indexterm fn" role="fn"></span>`edit-and-execute-command (C-x C-e)`  
Invoke an editor on the current command line, and execute the result as shell commands. Bash attempts to invoke `$VISUAL`, `$EDITOR`, and `emacs` as the editor, in that order.

<span class="indexterm fn" role="fn"></span>`display-shell-version (C-x C-v)`  
Display version information about the current instance of Bash.
