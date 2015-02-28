set nocompatible

set vb
filetype plugin indent on 
set nocp
set autoindent
set expandtab
set softtabstop=4
set shiftwidth=4
set cindent
set ts=4
set scrolloff=2
set clipboard=unnamedplus
execute pathogen#infect()
"syntax on
let g:SuperTabDefaultCompletionType = "context"
let g:jedi#popup_on_dot = 0  " disables the autocomplete to popup whenever you press .
au BufRead /tmp/mutt-* set tw=72
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

set grepprg=grep\ -nH\ $*
let g:tex_flavor = "latex"
map <F6> :setlocal spell! spelllang=en_us<CR>

set incsearch
set hlsearch

syntax enable

set cursorline
set colorcolumn=80
