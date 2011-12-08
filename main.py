#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import feedparser
from google.appengine.api import urlfetch
from google.appengine.ext import webapp



class MainHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write('Hello world!')


class FetchHandler(webapp.RequestHandler):
	def get(self):
		url = self.request.get('url')
		doc = feedparser.parse(url)
		self.response.out.write("<h1>")
		self.response.out.write(doc.feed.title)
		self.response.out.write("</h1>")
		self.response.out.write("<ul>")
		for entry in doc.entries:
			self.response.out.write("<li>")
			self.response.out.write("<a href=%s>%s</a> " % (entry.link, entry.title))
			self.response.out.write("</li>")
		self.response.out.write("</ul>")

handlers = [
	('/', MainHandler),
	(r'/fetch', FetchHandler),
]

app = webapp.WSGIApplication(handlers, debug=True)


