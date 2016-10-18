# coding:utf-8
# -*- coding:utf-8 -*-
import functools

from tornado import web


def auth(method):
    """Decorate with this method to restrict to site admins."""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.request.method == "GET":
                self.redirect(self.get_login_url())
                return
            raise web.HTTPError(403)
        elif not self.current_user.administrator:
            if self.request.method == "GET":
                self.redirect("/")
                return
            raise web.HTTPError(403)
        else:
            return method(self, *args, **kwargs)

    return wrapper


class BaseHandler(web.RequestHandler):
    """Implements Google Accounts authentication methods."""

    def get_current_user(self):
        user = self.get_current_user()
        if user:
            user.administrator = self.is_current_user_admin()
        return user

    def get_login_url(self):
        return self.create_login_url(self.request.uri)

    def render_string(self, template_name, **kwargs):
        # Let the templates access the users module to generate login URLs
        return web.RequestHandler.render_string(
            self, template_name, users='', **kwargs)


class FeedHandler(BaseHandler):
    def get(self):
        # entries = db.Query(Entry).order('-published').fetch(limit=10)
        self.set_header("Content-Type", "application/atom+xml")
        self.render("feed.xml", entries='')


class EntryHandler(BaseHandler):

    @web.removeslash
    def get(self, slug):
        entry = ''#db.Query(Entry).filter("slug =", slug).get()
        if not entry:
            raise web.HTTPError(404)
        self.render("entry.html", entry=entry)


class AboutHandler(BaseHandler):

    def get(self):
        self.render("about.html")