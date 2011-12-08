# main.py
import cherrypy
import wsgiref.handlers

class HelloWorld:
	@cherrypy.expose
	def index(self):
		return "Hello world!"


class GoodDay:
	@cherrypy.expose
	def index(self, num=None):
		reply = "Good Day!"
		if num is not None:
			for x in range(1, int(num)):
				reply += "Good Day!"
		return (reply)

def main():
	root = HelloWorld()
	root.reply = GoodDay()
	app = cherrypy.tree.mount(root, "/")
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
	main()
  