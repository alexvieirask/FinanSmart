class SKToastr {
    static error(message) {
        if (!document.querySelector('.toast-error')) {
            toastr.error(message);
        }
    }

    static success(message) {
        if (!document.querySelector('.toast-success')) {
            toastr.success(message);
        }
    }

    static warning(message) {
        if (!document.querySelector('.toast-warning')) {
            toastr.warning(message);
        }
    }
}

export { SKToastr };