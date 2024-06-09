from System.Config import *

class Templates:
    @app.route("/")
    def SKIndex():
        return render_template("Pages/Login/login.html")