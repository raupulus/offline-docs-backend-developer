---
title: Readline Interaction
source_url: https://www.gnu.org/software/bash/manual
source_path: 041-readline-interaction.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 410
---

## Readline Interaction

interaction, readline

Often during an interactive session you type in a long line of text, only to notice that the first word on the line is misspelled. The Readline library gives you a set of commands for manipulating the text as you type it in, allowing you to just fix your typo, and not forcing you to retype the majority of the line. Using these editing commands, you move the cursor to the place that needs correction, and delete or insert the text of the corrections. Then, when you are satisfied with the line, you simply press RET. You do not have to be at the end of the line to press RET; the entire line is accepted regardless of the location of the cursor within the line.

### Readline Bare Essentials

notation, readline

command editing

editing command lines

In order to enter characters into the line, simply type them. The typed character appears where the cursor was, and then the cursor moves one space to the right. If you mistype a character, you can use your erase character to back up and delete the mistyped character.

Sometimes you may mistype a character, and not notice the error until you have typed several other characters. In that case, you can type `C-b` to move the cursor to the left, and then correct your mistake. Afterwards, you can move the cursor to the right with `C-f`.

When you add text in the middle of a line, you will notice that characters to the right of the cursor are ‘pushed over’ to make room for the text that you have inserted. Likewise, when you delete text behind the cursor, characters to the right of the cursor are ‘pulled back’ to fill in the blank space created by the removal of the text. These are the bare essentials for editing the text of an input line:

`C-b`  
Move back one character.

`C-f`  
Move forward one character.

DEL or Backspace  
Delete the character to the left of the cursor.

`C-d`  
Delete the character underneath the cursor.

Printing\&#160;characters  
Insert the character into the line at the cursor.

`C-_` or `C-x C-u`  
Undo the last editing command. You can undo all the way back to an empty line.

Depending on your configuration, the Backspace key might be set to delete the character to the left of the cursor and the DEL key set to delete the character underneath the cursor, like `C-d`, rather than the character to the left of the cursor.

### Readline Movement Commands

The above table describes the most basic keystrokes that you need in order to do editing of the input line. For your convenience, many other commands are available in addition to `C-b`, `C-f`, `C-d`, and DEL. Here are some commands for moving more rapidly within the line.

`C-a`  
Move to the start of the line.

`C-e`  
Move to the end of the line.

`M-f`  
Move forward a word, where a word is composed of letters and digits.

`M-b`  
Move backward a word.

`C-l`  
Clear the screen, reprinting the current line at the top.

Notice how `C-f` moves forward a character, while `M-f` moves forward a word. It is a loose convention that control keystrokes operate on characters while meta keystrokes operate on words.

### Readline Killing Commands

killing text

yanking text

Killing text means to delete the text from the line, but to save it away for later use, usually by yanking (re-inserting) it back into the line. (‘Cut’ and ‘paste’ are more recent jargon for ‘kill’ and ‘yank’.)

If the description for a command says that it ‘kills’ text, then you can be sure that you can get the text back in a different (or the same) place later.

When you use a kill command, the text is saved in a kill-ring. Any number of consecutive kills save all of the killed text together, so that when you yank it back, you get it all. The kill ring is not line specific; the text that you killed on a previously typed line is available to be yanked back later, when you are typing another line. <span class="indexterm cp" role="cp"></span>

Here is the list of commands for killing text.

`C-k`  
Kill the text from the current cursor position to the end of the line.

`M-d`  
Kill from the cursor to the end of the current word, or, if between words, to the end of the next word. Word boundaries are the same as those used by `M-f`.

`M-DEL`  
Kill from the cursor to the start of the current word, or, if between words, to the start of the previous word. Word boundaries are the same as those used by `M-b`.

`C-w`  
Kill from the cursor to the previous whitespace. This is different than `M-DEL` because the word boundaries differ.

Here is how to yank the text back into the line. Yanking means to copy the most-recently-killed text from the kill buffer into the line at the current cursor position.

`C-y`  
Yank the most recently killed text back into the buffer at the cursor.

`M-y`  
Rotate the kill-ring, and yank the new top. You can only do this if the prior command is `C-y` or `M-y`.

### Readline Arguments

You can pass numeric arguments to Readline commands. Sometimes the argument acts as a repeat count, other times it is the *sign* of the argument that is significant. If you pass a negative argument to a command which normally acts in a forward direction, that command will act in a backward direction. For example, to kill text back to the start of the line, you might type ‘`M-- C-k`’.

The general way to pass numeric arguments to a command is to type meta digits before the command. If the first ‘digit’ typed is a minus sign (‘`-`’), then the sign of the argument will be negative. Once you have typed one meta digit to get the argument started, you can type the remainder of the digits, and then the command. For example, to give the `C-d` command an argument of 10, you could type ‘`M-1 0 C-d`’, which will delete the next ten characters on the input line.

### Searching for Commands in the History

Readline provides commands for searching through the command history (see [Bash History Facilities](#Bash-History-Facilities)) for lines containing a specified string. There are two search modes: incremental and non-incremental.

Incremental searches begin before the user has finished typing the search string. As each character of the search string is typed, Readline displays the next entry from the history matching the string typed so far. An incremental search requires only as many characters as needed to find the desired history entry. When using emacs editing mode, type `C-r` to search backward in the history for a particular string. Typing `C-s` searches forward through the history. The characters present in the value of the `isearch-terminators` variable are used to terminate an incremental search. If that variable has not been assigned a value, the ESC and `C-j` characters terminate an incremental search. `C-g` aborts an incremental search and restores the original line. When the search is terminated, the history entry containing the search string becomes the current line.

To find other matching entries in the history list, type `C-r` or `C-s` as appropriate. This searches backward or forward in the history for the next entry matching the search string typed so far. Any other key sequence bound to a Readline command terminates the search and executes that command. For instance, a RET terminates the search and accepts the line, thereby executing the command from the history list. A movement command will terminate the search, make the last line found the current line, and begin editing.

Readline remembers the last incremental search string. If two `C-r`s are typed without any intervening characters defining a new search string, Readline uses any remembered search string.

Non-incremental searches read the entire search string before starting to search for matching history entries. The search string may be typed by the user or be part of the contents of the current line.
