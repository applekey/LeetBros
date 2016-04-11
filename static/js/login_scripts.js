function onLoad() {
    gapi.load('auth2', function() {
        gapi.auth2.init();
    });
}

function demoSignIn(){
    $.ajax({
        url : '/',
        method : 'POST',
        contentType : 'application/json',
        data : {
            'name' : 'demoName', 
            'email' : 'demo@demoEmail.com'
        },
        complete : function(response) {
            console.log('here')
            console.log(response)

            window.location = "/start"
        }
    });
}

function login(data)
{
    $.ajax({
        url : '/',
        method : 'POST',
        contentType : 'application/json',
        data : data,
        complete : function(response) {
            window.location = '/start'
        }
    });
}

function customlogin()
{
    formVals = $('#loginform').serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});

    data = {
            'email' : formVals.inputEmail,
            'passw' : formVals.inputPassword,
            'customlogin' : 'true'
        };

    login(data);

    return false;
}

function register(data)
{
    $.ajax({
        url : '/register',
        method : 'POST',
        contentType : 'application/json',
        data : data,
        complete : function(response) {
            window.location = '/login'
        }
    });
}

function registerUser()
{
    formVals = $('#registerform').serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});

    data = {
        'email' : formVals.inputEmail,
        'passw' : formVals.inputPassword,
        'confirmpass' : formVals.confirmPassword
    }

    register(data)

    return false;
}

function onGoogleSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    /*console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail());*/

    data = {
            'auth_token' : googleUser.getAuthResponse().id_token, 
            'name' : profile.getName(), 
            'email' : profile.getEmail(),
            'bigGlogin' : 'true'
        };

    login(data);
}

function signOut() {
    deleteCookie('sessionId')
    window.location = "/"
}

function googleSignOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
      signOut()
    });
}

function deleteCookie(name) {
    createCookie('sessionId', '', -1);
}

function createCookie(name, value, days) {
    var expires;

    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = encodeURIComponent(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
    return null;
}
