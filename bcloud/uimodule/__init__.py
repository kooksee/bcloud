import tornado
from tornado import web


class EntryModule(web.UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)


class SidebarModule(web.UIModule):
    def render(self):
        return self.render_string("modules/sidebar.html")

    def embedded_css(self):
        return '''
         .content > .wireframe.image {
        opacity: 0.5 !important;
    }

    .launch.button .icon {
        margin-left: 0px;
    }

    .minimal.basic > .launch.button {
        display: block;
    }

    .fixed.launch.button {
        display: none;
        position: fixed;
        top: 10.5em;
        left: 0px;
        width: 55px;
        height: auto;
        white-space: nowrap;
        overflow: hidden;

        -webkit-transition: 0.3s width ease, 0.5s transform ease;
        -moz-transition: 0.3s width ease, 0.5s transform ease;
        -o-transition: 0.3s width ease, 0.5s transform ease;
        -ms-transition: 0.3s width ease, 0.5s transform ease;
        transition: 0.3s width ease, 0.5s transform ease;
    }

    .fixed.launch.button .text {
        position: absolute;
        white-space: nowrap;
        top: auto;
        left: 54px;
        opacity: 0;

        -webkit-transition: 0.3s opacity 0.3s;
        -moz-transition: 0.3s opacity 0.3s;
        -o-transition: 0.3s opacity 0.3s;
        -ms-transition: 0.3s opacity 0.3s;
        transition: 0.3s opacity 0.3s;
        '''

    def embedded_javascript(self):
        return '''
         // create sidebar and attach to menu open
      $('.ui.sidebar')
        .sidebar('attach events', '.toc.item');

       $('.ui.sidebar')
        .sidebar('attach events', '.ui.launch');
        '''


class EntryModule1(web.UIModule):
    def render(self, entry, show_comments=False):
        if show_comments:
            self.show_comments = True
        else:
            self.show_count = True
        return self.render_string("modules/entry.html", entry=entry,
                                  show_comments=show_comments)

    def embedded_javascript(self):
        if getattr(self, "show_count", False):
            return self.render_string("disquscount.js")
        return None

    def javascript_files(self):
        if getattr(self, "show_comments", False):
            return ["http://disqus.com/forums/brettaylor/embed.js"]
        return None
