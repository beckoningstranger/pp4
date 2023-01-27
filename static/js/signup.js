// Hide Form labels for username and password
var labels = document.getElementsByTagName('label')
for (let label of labels) {
    label.style.display = "none"
}

// Hide Email field, we don't do password resets anyway at this point
var emailField = document.getElementById('id_email')
emailField.style.display = "none"

// Apply classes to input elements I can't edit otherwise
var inputs = document.getElementsByTagName('input')
for (let input of inputs) {
    input.setAttribute("class", "form-control")
}
document.getElementById('id_email').setAttribute('placeholder', "E-Mail (optional)")