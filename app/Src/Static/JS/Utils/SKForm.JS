import { SKToastr } from "./SKToastr.JS";

class SKForm {
    constructor(formID) {
        this.formID = formID;
    }

    async handleRequest(event, processRequest) {
        try {
            await this.#BeforePost(event);
            await processRequest();
            await this.#AfterPost(event);
        } 
        catch (error) {
            console.log(error);
        }
    }

    onSubmit(processRequest) {
        document.querySelector(this.formID).addEventListener("submit", (event) => {
            event.preventDefault();
            this.handleRequest(event, processRequest);
        });
    }

    ButtonOnClick(ButtonComponent,processRequest){
        document.querySelector(ButtonComponent).addEventListener("click",processRequest)
    }
    
    Reset() {
        var form = document.querySelector(this.formID);
        form.reset();
    }

    inputTypeNumber() {
        var valor = this.value;
        valor = valor.replace(/[^0-9.]/g, '');
        valor = valor.replace(/(\..*?)\./g, '$1');
        this.value = valor;
    }

    async #BeforePost(event) {
        event.preventDefault();
        this.#disableButtonForm();
    }

    async #AfterPost(event) {
        event.preventDefault();
        this.#enableButtonForm();
    }

    #disableButtonForm() {
        var form = document.querySelector(this.formID);
        var submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = true;
    } 

    #enableButtonForm() {
        var form = document.querySelector(this.formID);
        var submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = false;
    }

    FieldByName(Field){
        const form = document.querySelector(this.formID);
        for (const element of form.elements) {
            if (!element.name && 
                ['text', 'email', 'password'].includes(element.type)){
                SKToastr.error('Nome do Elemento do Formulário não definido. ID:'+element.id)
            }

            if (element.name == Field && 
               ['text', 'email', 'password'].includes(element.type)) {
                return element.value;
            }
        }
    }
}

export { SKForm };