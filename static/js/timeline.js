// In the odd case where a user follows _every_ other user on the site, this will show a message on the user-list page.
var timeline = document.getElementById('posts')
if (!timeline.getElementsByTagName('*').length > 0) {
    var newElement = document.createElement("div")
    var userMessage = document.createTextNode("You're seeing this because you have not posted yet and you are not following anybody. Why don't you go to your Circle to start following people or create a post?")
    newElement.appendChild(userMessage)
    newElement.setAttribute("class", "container p-5 m-5 display-6")
    timeline.append(newElement)
}