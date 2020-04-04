#!/usr/bin/env python3.8
""" This is an ncurses CLI for NotationalVelocity.  It handles HTTP(S?) calls to a lambda up in AWS
    to get or set data.
    Things to think about:
    * lookahead - as user types, after 3 or 4 chars, start querying for matches
    * curses - make a nice interface to show both possible existing matches for title and an
    editable field for a new note.

    The UI will have three 'windows'.
    * The first window is a single line, user text entry.
    * The second window displays the top X notes that match text in window 1.  This could be a 'pad'
      https://docs.python.org/3/howto/curses.html#windows-and-pads.
    * The third window displays a text box with notes or blank if no note matches.  This could be a 'pad'
      https://docs.python.org/3/howto/curses.html#windows-and-pads.
    The user can cycle through the three windows using Tab.  Scrolling over notes in window 2 loads
    that note's text in window 3.
"""
import curses
import boto3

class NotationalMomentum(object):
    def __init__(self):
        # prepare the screen
        self._prepare_screen()
        self._print_message("This string gets printed at position(0,0)", 0, 0, False)
        self._print_message("Try Russian text: Привет", 3, 1, True)

    def __del__(self):
        self._end_screen()

    def _prepare_screen(self):
        self.screen = curses.initscr()
        self.text_entry = curses.newpad(100, 100)

    def _print_message(self, msg, scnX, scnY, refreshFlag=False):
        self.num_rows, self.num_cols = self.screen.getmaxyx()

        # Update the buffer, adding text at different locations
        self.screen.addstr(scnX, scnY, msg)
        if refreshFlag:
            self.screen.refresh()
            curses.napms(2000)


    def _end_screen(self):
        curses.endwin()

if __name__ == '__main__':
    nm = NotationalMomentum()
