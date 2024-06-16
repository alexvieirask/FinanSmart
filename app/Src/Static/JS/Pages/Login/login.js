import { Session } from "../../Utils/Session.JS";
import { SKForm } from '../../Utils/SKForm.js';
import { SKToastr } from '../../Utils/SKToastr.js';
import *  as api from "./api.js"

class VSKFormSignUp extends SKForm { 
    constructor(formID) {
        super(formID);

        this.onSubmit(async () => {
            const responseData = await api.signUp(this.FieldByName('user-fullname'),
                                                  this.FieldByName('user-name'),
                                                  this.FieldByName('user-email'),
                                                  this.FieldByName('user-pass'),
                                                  this.FieldByName('user-repeatpass'));
            
            if (responseData.status != 200){
                SKToastr.error(responseData.details);
            }
            else{
                SKToastr.success('Conta criada com sucesso.');
                this.Reset();
                $('.form-signup').toggle(); 
                $('.form-signin').toggle(); 
            }
        });

        this.ButtonOnClick('#logreg-forms #btn-signup', ()=>{
            $('#logreg-forms .form-signin').toggle(); 
            $('#logreg-forms .form-signup').toggle(); 
        })

        this.ButtonOnClick('#logreg-forms #cancel_signup', ()=>{
            $('#logreg-forms .form-signin').toggle(); 
            $('#logreg-forms .form-signup').toggle(); 
        })

    }
}

class VSKFormSignIn extends SKForm { 
    constructor(formID) {
        super(formID);
        this.onSubmit(async () => {
            const responseData = await api.signIn(this.FieldByName('inputEmail'),
                                                  this.FieldByName('inputPassword'));
        
            if (responseData.status != 200){
                SKToastr.error(responseData.details);
            } else{
                Session.JWT = responseData.details;
                await Session.CURRENT_USER();
                window.location = "/home"
            }
        });
    }
}

new VSKFormSignIn('.form-signin');
new VSKFormSignUp('.form-signup');