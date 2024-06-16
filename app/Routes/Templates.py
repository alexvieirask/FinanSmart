from System.Config import *

class Templates:
    @app.route("/")
    def SKIndex():
        return render_template("Pages/Login/login.html")
    
    @app.route("/home")
    def SKHome():
        return render_template("Pages/Home/home.html")
    
    @app.route("/general_register")
    def SKGeneralRegister():
       return render_template("Pages/GeneralRegister/GeneralRegister.html")