# Source
YouTube:
    Matering the Vim Language
    How to do 90% of What Plugins do (with just vim)
    vim + tmux - OMG!Code https://www.youtube.com/watch?v=5r6yzFEXajQ&t=813s

## Normal mode

All commands work as a word + noun (dw = delete word)

### Text objects

`w` words    
`s` sentances
`p` paragraphs  
`t` tags (available in XML/HTML files)
`i` indents (requires a plugin)
`l` lines (requires a plugin)
`e` entire (requires a plugin)

### Motions

`w` word forward
`b` word backward
`e` end of the word
`i` inner (selects just the word)
`a` all (selects word but also spaces/brackets if they exist)
`f_` find - go to first appearance of character _ in that line
`F_` same thing but backwards
`t_` till - go to a character before the first appearance of character _ in that line
`T_` same thing but backwards
`{/}` beginning/end of a paragraph
`''` go to previous location

### Commands:
`d` delete
`D` delete till the end of a line
`c` change (delete + insert)
`C` change till the end of a line
`I` move to beggining of the line and insert
`A` move to end of the line and insert
`o` insert below current line
`O` insert above current line
`p` paste below current line
`P` paste above current line
`>` indenti (works with hjkl operators)
`<` outdent 
`v` visually select
`V` visuall select lines
`y` yank/copy
`Y` yank whole line
`~` replace case upper --> lower
`r` replace character with what you type in
`J` add next line of the end of the current one
`*` search for word under the coursor


### Macros

`q<register>` start recortding
(do the things)
`q` stop recording
`@<register>`  apply the macro
`2@<register>` apply the macro to two lines below
Different way to apply to multiple lines
`V+j/k` to select desired lines
`:normal @<register` applies that macro to those lines

### Nouns:
`/` search for any character, word
`?` same thing but backwards
`m` set mark, eg. mq sets q mark on place where the cursor is
`{}` beggining/end of paragraph
`%` goes to next paren of brackets
`.` repeats the last command executed (whatever it is)
`diw` delete the whole word on which the coursor is on
`di"` delete everything inside the ""
`di]` delete everything inside of []
`dip` delete everythins indside of paragraph
`dit` delete everything inside of a tag eg `<html>___ </html>`
`d'q` delete everyting until the marker q
 same operations work with c, v, y
`daw|"|]` same as diw but with a it captures also the space that follows i
`gUw` change whole word to uppecrase
`guw` change whole word to lowercase
`gUU` whole line uppercase

### Registers

`:registers` or `:reg`shows the list of things in registry - basically clipboard
- `c` character text
- `l` line text
- `b` block text
`""` the unnamed register - everything that goes to clipboard ends here

#### Named Registers

`"` used to name a registry
`"cyy` yank whole line to registry named "c"
`"cp` paste from "c" registry

### Marks

`ma` sets mark "a" to the coursor position
`'a` jumps to position of mark "a"

## Commands:
`:find <file_name>` finds a file name in the current directory
`:read <file_name>` adds the content of the file to this document
`:ls` lists all files which are currently opened in vim
`:b <part_of_the_filename>` opens that file if it is already opened in vim
`:echo expand(%)` get the name of the currently opened file
`:reg` shows all registers, good place to paste stuff from
`g` at the end of the command means it applies to the whole document
`v` means an NOT to match the given pattern

## Control commands

### Normal Mode 

`ctrl + y` few lines up
`ctrl + e` few lines down
`ctrl + u` half page up
`ctrl + d` half page down
`ctrl + f` full page up
`ctrl + b` full page down
`ctrl + o` got to previous jump (list jumps with `:jumps` )
`ctrl + i` got to next jump
`ctrl + a` when on integer, it will increment it
`ctrl + x` when on integer, it will decrement it
`ctrl + ]` jump to a definition of a tag
`ctrl + g]` will show all the occurencies of this defined tag 
`ctrl + t` jump back up the tag stack
`ctrl + n` autocompletes a word, n is for next
`ctrl + p` autocompletes a word, p is for previous
`ctrl + w + s` split window horizontally
`ctrl + w + v` split window vertical
`ctrl + w + q` remove split
`ctrl + w + w` move to next window

### Insert Mode

`ctrl + x ctrl + n` autocomplete but with words only within this file
`ctrl + x ctrl + f` fzf complete path
`ctrl + x ctrl + k` fzf complete word (from whole dictionary)
`ctrl + x ctrl + j` fzf complete file with Ag (silver-searcher)
`ctrl + x ctrl + l` fzf complete line
`ctrl + x ctrl + ]` autocompletes a tag 

### Buffers

Buffers are used when more that one files are open within the same Vim
`:ls` show available files in buffer
`:bn` go to next file in buffed
`:bp` go to previous file in buffer
`:b<number>` go to specific buffer
`:b#` go to previous active buffer
`:bd` close current buffer
`sp #<number>` open buffer in horizontal split
`vsp #<number>` open buffer in vertical split

### Autocomplete

`ctrl + e` cancel autocomplete menu
`ctrl + j` move down in autocomplete menu
`ctrl + k` move up in autocomplete menu
`ctrl + l` select option from autocomplete menu
`tab` select option from autocomplete menu

## :Commands

`:!<command>` any shell command can be executed like this
