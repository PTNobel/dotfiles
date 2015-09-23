set nocompatible
filetype off
execute pathogen#infect()
execute pathogen#helptags()
filetype plugin indent on
syntax on
set ruler
set number
set vb
set nocp
set autoindent
set expandtab
set softtabstop=2
set shiftwidth=2
set cindent
set ts=2
set scrolloff=2
set clipboard=unnamedplus
let g:SuperTabDefaultCompletionType = "context"
let g:jedi#popup_on_dot = 0  " disables the autocomplete to popup whenever you press .

set cursorline
set colorcolumn=81
highlight ColorColumn ctermbg=darkgrey
"execute "set colorcolumn=" . join(range(80,335), ',')

au BufRead /tmp/mutt-* set tw=72
au BufRead /tmp/mutt-* set spell
au BufRead /tmp/mutt-* set cursorline
au BufRead /tmp/mutt-* set colorcolumn=73
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let g:syntastic_tex_checkers = ["chktex"]

set grepprg=grep\ -nH\ $*
let g:tex_flavor = "latex"
" use pdflatex
let g:Tex_DefaultTargetFormat='pdf'
let g:Tex_MultipleCompileFormats='pdf,dvi'
let g:Tex_CompileRule_pdf = 'mkdir -p tmp; pdflatex -output-directory tmp -interaction=nonstopmode $*; cp tmp/*.pdf .'

map <F6> :setlocal spell! spelllang=en_us<CR>
map <F8> :setlocal spell! spelllang=es<CR>
autocmd BufNewFile,BufRead *.tex set spell
autocmd BufNewFile,BufRead *.tex let g:indentLine_enabled=0
autocmd BufNewFile,BufRead *.md let g:indentLine_enabled=0
autocmd BufNewFile,BufRead *.java set ts=4
autocmd BufNewFile,BufRead *.java set softtabstop=4
autocmd BufNewFile,BufRead *.java set shiftwidth=4

set incsearch
set hlsearch

syntax enable


autocmd StdinReadPre * let s:std_in=1

let g:pymode_rope_lookup_project = 0
let g:pymode_rope = 0
let g:pymode_python = 'python3'
let g:pymode_lint_options_mccabe = {'complexity': 30}
set undofile
set undodir=~/.vim/undodir

let g:pymode_rope=0

set backspace=indent,eol,start
set complete-=i
set smarttab

if &t_Co == 8 && $TERM !~# '^linux'
  set t_Co=16
endif

let g:ycm_semantic_triggers = {
\  'tex'  : ['\ref{', '\cref{', '\cite{', '\autocite{', '\mlacite{',],
\ }

let g:jedi#force_py_version = 3
let g:calendar_google_calendar = 1
let g:calendar_google_task = 1

" vertical line indentation
let g:indentLine_color_term = 239
let g:indentLine_color_gui = '#09AA08'
let g:indentLine_char = '│'
let g:tex_comment_nospell= 1
let g:LatexBox_quickfix = 4
let g:LatexBox_viewer = "zathura"
let g:LatexBox_latexmk_preview_continuously = 1
let g:LatexBox_build_dir = '/tmp/parth-LaTeX'
let g:LatexBox_latexmk_options = "-cd -outdir='/tmp/parth-LaTeX'"

let g:powerline_pycmd = 'py3'
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline, even if there is only one tab
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set smartcase
