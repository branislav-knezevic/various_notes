## Plugin commands

### surround plugin
`ysiwX` surround word with X (.,[]{} whatever)
`cs"'` replace surrunding " with ' if text is already surrounded
`dsX` delete exisitng X surrundings

### comment plugin
`gcc` comment out a line
`gc2j` comment N number of lines below
`gcgc` uncomment adjacent commented lines

### vim-system-copy
`cpiw` copy word to system plugin
`cpi'` copy content inside of '' to system plugin
`cvi'` paste content of system clipboard inside of ''

### vim folding

`zi` switch folding on or off
`za` toggle current fold open/closed
`zc` close current fold
`zR` open all folds
`zM` close all folds
`zv` expand folds to reveal coursor

### FZF
`:FZF` starts a regular fuzzyfinder  
`:Files` searches for files in current git dir and shows preview
`:Rg` initiates ripgrep search, searches also for phrases within files
`:Ag` initiates silverSearcher, simlar to ripgrep
`:Blines` something like find (`/` ) in vim but it will show lines where it found it and you can jumb to that line
`:Lines` does search in all opened buffers
`:History:` command history
`:Buffers` serach opened buffers

`<leader>e` files edited in git
`<leader>b` files opened in buffer
`<leader>t` search for open tabs
`<leader>f` serch for files in current tree
  `<tab>` to select multiple files
  `<ctrl>v` open selected file in vertial split
  `<ctrl>x` open selected file in horizontal split
  `<ctrl>t` open selected file in new tab
`<leader>s` ripgrep in files (searches for phrases withing files)


in insert mode:  
`<ctrl>x<ctrl>k` find words (from dictionary)
`<ctrl>x<ctrl>f` fzf complete path
`<ctrl>x<ctrl>j` fzf complete path with silverearcher
`<ctrl>x<ctrl>l` fzf complete line

### Fugitive

`:G<git_command>` use git within vim
`<leader>gs` git status - same as `:G`
`<leader>gp` git push
`<leader>gl` git pull
`<leader>gh` take left side from merge
`<leader>g;` take right side from merge
  `s` when on a file to set it to staging 
  `u` when on a file to set it to unstage 
  `=` show changes
  `X` discards selected changes in conflict mode (unstaged are local changes)
  `dv` go to resolve conflict mode
  `<any_number>gI` adds selected file to .gitgnore
`:Gblame` shows who made changes on that file
  `o` once in `Gblame` will show which changes were made with specific commit
`:Glog` git log history


### Easymotion

`<leader>z` prefix for plugin, can be used with `w` `e` `b` `j` `k`...
`s<character>` searches for <character> anywhere in the document and highligts  it
`ss<character><character>` searches for <character><character> anywhere in the document and highligts them

### Unimpared

`[/]<space>` insert blank line before/after current line
`[/]n` go to previous/next git conflict marker
`[/]f` open to previous/next file in same directory

### Nerdtree

`<leader>n` toggle NerdTree
`<leader>a` go to NerdTree

### Auto-pairs

`<alt>p` toggle plugin
`<alt>e` when in insert mode to surround next word or words (if they are already surrounded) in desired things
`"|"{some text}` when in insert mode on position `|`, `<alt>e` will surround `{some text}` with quotes
pressing `<alt>e` multiple times will include next word each time
`<alt>b` when you FlyMode is enabled to insert a closed bracket where needed
`<alt>n` finds next closing paranthasis
