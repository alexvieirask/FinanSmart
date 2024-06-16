import { RedirectTo } from "./Redirect.JS";
import { Session } from "./Session.JS";

RedirectTo.ButtonRedirectOnClick("#home-option",RedirectTo.Home)
RedirectTo.ButtonRedirectOnClick("#accountpayable-option",RedirectTo.AccountsPayable)
RedirectTo.ButtonRedirectOnClick("#accountreceivable-option",RedirectTo.AccountsReceivable)
RedirectTo.ButtonRedirectOnClick("#general-register-option",RedirectTo.GeneralRegister)
RedirectTo.ButtonRedirectOnClick("#settings-option",RedirectTo.Settings)
RedirectTo.ButtonRedirectOnClick("#leave-option",Session.destroy)

async function setHeaderData(){
    try{
        if (Session.USER){
            Session.USER.then(user=>{
                var headerUsername = document.querySelector("#header-username-span")
                headerUsername.textContent = `@${user.username}`
            }).catch(error=>{
                console.log(error)
            })
        }
       else{
            if (window.location != '/' ){
                RedirectTo.Login()
            }
        }
    }
    catch(error){
        console.log(error)
    }
}

setHeaderData()