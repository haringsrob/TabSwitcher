import sublime
import sublime_plugin
import datetime

class SwitchTabsCommand(sublime_plugin.TextCommand):

    def activate_tab(self, index):
        if index == -1:
            return

        view = self.view.window().sheets()[index].view();

        if view != None:
            self.view.window().focus_view(view);

    def run(self, edit):
        self.list = []

        active_view = self.view.window().active_view();
        active_view_index: int = 0;

        for index, sheet in enumerate(self.view.window().sheets()):
            self.list.append(sheet.view().name() or sheet.view().file_name())

            # If the view is active set the active index.
            if (active_view.id() == sheet.view().id()):
              active_view_index = index;

        self.view.window().show_quick_panel(self.list, self.activate_tab, 1, active_view_index)