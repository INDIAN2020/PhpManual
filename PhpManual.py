import sublime, sublime_plugin

class PhpManual(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                url = "http://www.php.net/manual-lookup.php?pattern="\
                        "%s&scope=quickref" % self.view.substr(word)
                sublime.active_window().run_command('open_url', {"url": url})
