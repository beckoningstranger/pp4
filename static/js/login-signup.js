// Hide Form labels for username and password
var labels = document.getElementsByTagName('label')
labels[0].style.display = "none"
labels[1].style.display = "none"

// Apply classes to input elements I can't edit otherwise
var inputs = document.getElementsByTagName('input')

inputs[1].setAttribute("class", "form-control")
inputs[2].setAttribute("class", "form-control")