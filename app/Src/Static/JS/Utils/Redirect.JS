class RedirectTo{
    static Login(){
        window.location = "/"
    }
    
    static Home(){
        window.location = "/home"
    }
    
    static Settings(){
        window.location = "/settings"
    }

    static GeneralRegister(){
        window.location = "/general_register"
    }

    static ButtonRedirectOnClick(id_button,redirect_function,){
        document.querySelector(id_button).addEventListener("click",redirect_function)
    }
}

export { RedirectTo }