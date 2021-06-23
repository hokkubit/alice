"""
Simple script to define your aliases.
Also your .bash_aliases or .zsh_aliases file must be exist,
If it isn't Alice will create it for you

So, put this lines into your shell rc

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

You can wrap this script in a function in your command shell rc file as sample:
alice() {
    python3 ~/path/to/Alice $@
    source ~/.zshrc
}
Alice in Wonderland care your aliases
"""

__version__ = "0.1.0"

import curses
from curses import textpad

from collections import OrderedDict


class Menu:
    def __init__(self, menu, height, width):
        self.menu = menu
        self.height = height
        self.width = width

    def get_menu_list(self, stdscr, row_id: int, menu_mode: str):
        stdscr.clear()
        try:
            if menu_mode == 'main':

                for id, row in enumerate(self.menu):
                    x = self.width//2 - len(row)//2
                    y = self.height//2 - len(self.menu)//2 + id
                    if id == row_id:
                        stdscr.addstr(y, x, f'{row}', curses.color_pair(1))
                    else:
                        stdscr.addstr(y, x, f'{row}')

            elif menu_mode == 'aliases':
                for id, row in enumerate(self.menu):
                    alias_body = self.menu[row]
                    if (len(alias_body) >= 40):
                        formatted_body = alias_body.split()
                        alias_body = '\n\t'.join(formatted_body)
                    x = self.width // 5
                    y = int(self.height // 2.5) - len(self.menu) // 2 + id
                    if id == row_id:
                        # draw a container for alias <body> column
                        container = [[1, int(self.width / 2.5)], [self.height - 4, self.width - 3]]
                        textpad.rectangle(stdscr,
                                container[0][0],
                                container[0][1],
                                container[1][0],
                                container[1][1])
                        stdscr.setscrreg(0, self.height - 20)

                        stdscr.refresh()
                        stdscr.addstr(y, x - x // 2, row, curses.color_pair(2) )
                        for y, line in enumerate(alias_body.splitlines(), 2):
                            stdscr.addstr(y, x + self.width // 4, line, curses.A_DIM)
                    else:
                        stdscr.addstr(y, x - x // 2, row)
            stdscr.refresh()
        except Exception as e:
            if (str(e) == 'addwstr() returned ERR'):
                print("Sorry, screen too small")