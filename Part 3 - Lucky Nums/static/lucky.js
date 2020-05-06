/** processForm: get data from form and make AJAX call to our API. */

function processForm(evt) {
    evt.preventDefault();

    const name = document.getElementById("name").value;
    const year = document.getElementById("year").value;
    const email = document.getElementById("email").value;
    const color = document.getElementById("color").value;


}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    const results = document.getElementById("lucky-resutls");

}


$("#lucky-form").on("submit", processForm);