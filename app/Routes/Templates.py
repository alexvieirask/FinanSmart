from System.Config import *

class Templates:
    @app.route("/")
    def pages_login():
        return render_template("Pages/Login/login.html")