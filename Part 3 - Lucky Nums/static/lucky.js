/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault();
    const API_URL = "/api/get-lucky-num";

    const name = document.getElementById("name").value;
    const year = document.getElementById("year").value;
    const email = document.getElementById("email").value;
    const color = document.getElementById("color").value;

    // POST request to API
    const resp = await axios.post(API_URL, {
        name,
        year,
        email,
        color
    });

    // store response data and pass to handler
    const data = resp.data;
    handleResponse(data);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    const results = document.getElementById("lucky-results");

    let html = `
    <p>Your lucky number is ${resp.num.num} (${resp.num.fact}).</p>
    <p>Your birth year (${resp.year.year}) fact is ${resp.year.fact}.</p>
    `;

    results.innerHTML = html;
}


$("#lucky-form").on("submit", processForm);