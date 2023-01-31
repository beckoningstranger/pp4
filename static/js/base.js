// Get the current URL
var url = window.location.pathname
// Find who the currently logged in user is
var currentUser = document.getElementById('navbarDarkDropdownMenuLink').innerText.trim()

// Extract the part after the last '/' from the URL
function getSlugOrPk() {
    let urlBeforeSlashReversed = ""
    let urlBeforeSlash = ""
    // Trace the URL from its end to the first appearing '/' and write the result down, resulting in a reversed word
    for (let i = url.length - 1; url[i] != "/"; i--) {
        urlBeforeSlashReversed += url[i]
    }
    // Reverse the just generated variable so the word is readable again
    for (let i = urlBeforeSlashReversed.length - 1; i > -1; i--) {
        urlBeforeSlash += urlBeforeSlashReversed[i]
    }
    return urlBeforeSlash
}

// Timeline page:
if (document.title == "Timeline") {
    addPost = document.getElementById('add-post')
    addPost.style.display = 'block'
}


// Posts:
if (url.includes('/post')) {
    var postAuthorElement = document.getElementById('post-author')
    var postAuthor = postAuthorElement.innerText.trim()
    if (postAuthor == currentUser) {
        editPost = document.getElementById('edit-post')
        editPost.style.display = 'block'
        editPost.children[0].setAttribute('href', '/' + 'update-post/' + getSlugOrPk())
        deletePost = document.getElementById('delete-post')
        deletePost.style.display = 'block'
        deletePost.children[0].setAttribute('href', '/' + 'delete-post/' + getSlugOrPk())
    }

}

// Profiles:
if (url.includes('profile')) {
    // Find who owns the profile that's being displayed
    var profileOwnerexists = document.getElementById('profile-owner')
    if (profileOwnerexists) {
        var profileOwner = document.getElementById('profile-owner').innerText.trim()
        if (profileOwner == currentUser) {
            editProfile = document.getElementById('edit-profile')
            editProfile.style.display = 'block'
            editProfile.children[0].setAttribute('href', '/' + 'profile/edit/' + getSlugOrPk())
        }
    }
}

// Circle:
if (url.includes('mycircle')) {
    followPeople = document.getElementById('follow-people')
    followPeople.style.display = 'block'
}

