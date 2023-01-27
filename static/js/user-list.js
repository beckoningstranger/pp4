// In the odd case where a user follows _every_ other user on the site, this will show a message on the user-list page.
var userList = document.getElementById('users-left-to-follow')
if (!userList.getElementsByTagName('*').length > 0) {
    var newElement = document.createElement("p")
    var userMessage = document.createTextNode("You are following everybody. How do you keep up with the reading? ;-)")
    newElement.appendChild(userMessage)
    userList.append(newElement)
}