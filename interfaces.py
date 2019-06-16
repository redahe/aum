class ThreadTreeNode():

    def __init__(self, parent, reply_num, prev_thread, title, content):
        self.children = []
        self.parent = parent
        self.reply_num = reply_num

        self.prev_thread = prev_thread
        self.next_thread = None

        self.title = title
        self.content = content


class NavigationComponent():

    def next_reply(self):
        pass

    def back_reply(self):
        pass

    def next_subthread(self):
        pass

    def prev_subthread(self):
        pass

    def next_thread(self):
        pass

    def prev_thread(self):
        pass




class ViewerComponent():

    def show(self):
        pass

    def hide(self):
        pass

    def view_file(self, filepath):
        pass

    def view_url(self, url):
        pass

    def view_document(self, doc):
        pass

    def view_html(self, doc):
        pass

    def scroll_line_down(self):
        pass

    def scroll_line_up(self):
        pass

    def go_begin(self):
        pass

    def go_end(self):
        pass

    def close(self):
        pass
