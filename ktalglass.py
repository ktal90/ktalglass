#! /usr/bin/env python
#timeline_item = {'text': 'Hello world'}
#service.timeline().insert(body=timeline_item).execute()
import webapp2
print "Hello, World!"


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)