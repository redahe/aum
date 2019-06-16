#!/usr/bin/env python
# -*- coding: UTF-8 -*-.


import curses
import sys

import npyscreen


def exit(arg):
    sys.exit(0)

class MainForm(npyscreen.FormBaseNew):


    def set_status(self, status):
        self.text.value = status
        self.text.display()

    def create(self):
        column_height = terminal_dimensions()[0] - 9
        self.sources = self.add(
            Column,
            name       = "SOURCES",
            relx       = 2,
            rely       = 2,
            max_width  = 20,
            max_height = column_height
        )
        self.topics = self.add(
            Column,
            name       = "TOPICS",
            relx       = 23,
            rely       = 2,
            max_height = column_height
        )
        self.text = self.add(npyscreen.FixedText, relx=14, rely=35)
        self.text.value = '-----------'

        self.add_handlers({"q": exit})

        self.sources.entry_widget.handlers[ord('l')] = self.select_source
        self.sources.entry_widget.handlers[ord('\n')] = self.select_source
        self.sources.entry_widget.handlers[ord('/')] = self.sources.entry_widget.h_set_filter

        self.topics.entry_widget.handlers[ord('l')] = self.select_topic
        self.topics.entry_widget.handlers[ord('\n')] = self.select_topic
        self.topics.entry_widget.handlers[ord('/')] = self.topics.entry_widget.h_set_filter

        self.sources.values  = ["GMAIL",
                                "MASTODON",
                                "USENET"]

        self.topics.values  = ["2016-09-19T2001Z    aaaa\n message",
                               "2018-09-19T2002Z    Анатолий Обросков",
                               "2018-09-19T2002Z    another message"]

    def select_source(self, ch):
        self.sources.entry_widget.h_select_exit(ch)
        self.sources.editing=False
        self.sources.entry_widget.editing=False
        self.sources.how_exited=True
        self.editw=1
        self.set_status('selected')

    def select_topic(self, ch):
        self.set_status(self.topics.entry_widget.get_selected_objects())
        self.parentApp.switchForm('Viewer')
        self.parentApp.pager_form.lines=7


class ViewForm(npyscreen.FormBaseNew):

    def create(self):
        self.pager = self.add(npyscreen.Pager,
                          name="msg", relx=2, rely=6)
        self.pager.values = [str(i)+'spell'*(i%3)+' words'*(i%4)+' some about'*3
                            for i in range(40)]

        self.pager.handlers[ord("q")] = self.close
        self.pager.handlers[ord("h")] = self.close
        self.pager.handlers[ord("l")] = self.close

    def close(self, ch):
        self.parentApp.switchForm('MAIN')
        self.parentApp.main_form.display()


class App(npyscreen.NPSAppManaged):

    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.TransparentThemeLightText)

        self.main_form = self.addForm('MAIN', MainForm, name= '[0] Main Form')
        self.pager_form = self.addForm("Viewer",
                                       ViewForm,
                                       lines=terminal_dimensions()[0] - 9,
                                       columns=terminal_dimensions()[1] - 9,
                                       name='[1] Topic')

        self.pager_form2 = self.addForm("Viewer2",
                                        ViewForm,
                                        lines=terminal_dimensions()[0] - 10,
                                        columns=terminal_dimensions()[1] - 10,
                                        name='[2] Some....')
        self.pager_form.show_aty=1
        self.pager_form.show_atx=1
        self.pager_form2.show_aty=2
        self.pager_form2.show_atx=2

    def disp_pager(self, arg):
        self.switchForm("Viewer")


class Column(npyscreen.BoxTitle):

    def __init__(self, *args, **kwargs):
        npyscreen.BoxTitle.__init__(self, *args, **kwargs)
        self.how_exited=False

    def resize(self):
        self.max_height = int(0.73 * terminal_dimensions()[0])


def terminal_dimensions():
    return curses.initscr().getmaxyx()


if __name__ == "__main__":
    app = App()
    app.run()
