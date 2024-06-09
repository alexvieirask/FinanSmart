import { Session } from "../../Utils/Session.JS";

async function signIn(useremail,
                      userpassword){
    const URL_REQUEST = `http://${Session.IP_ADDRESS}:5000/signin/auth` 
    let response = await fetch(URL_REQUEST, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body:  JSON.stringify({
            useremail               :       useremail,
            userpassword            :       userpassword,
        })
    });

    return response.json()
}

async function signUp(fullname,
                      username,
                      useremail,
                      userpassword,
                      userrepeatpassword){
    const URL_REQUEST = `http://${Session.IP_ADDRESS}:5000/signup/auth`
    let response = await fetch(URL_REQUEST, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization' : `Bearer '${Session.JWT}'`
        },
        body:  JSON.stringify({
            fullname                :      fullname,
            username                :      username,
            useremail               :      useremail,
            userpassword            :      userpassword,
            userrepeatpassword      :      userrepeatpassword 
        })
    });

    return response.json()
}

export { signIn, 
         signUp  }