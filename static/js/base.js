var url = window.location.pathname

function getSlugOrPk() {
    let urlBeforeSlashReversed = ""
    let urlBeforeSlash = ""
    for (let i = url.length - 1; url[i] != "/"; i--) {
        urlBeforeSlashReversed += url[i]
    }
    for (let i = urlBeforeSlashReversed.length - 1; i > -1; i--) {
        urlBeforeSlash += urlBeforeSlashReversed[i]
    }
    return urlBeforeSlash
}

getSlugOrPk();

// Timeline page:
if (document.title == "Timeline") {
    addPost = document.getElementById('add-post')
    addPost.style.display = 'block'
}


// Posts:
var currentUser = document.getElementById('navbarDropdownMenuLink').innerText.trim()

if (url.includes('post')) {
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
    var profileOwner = document.getElementById('profile-owner').innerText.trim()
    console.log(profileOwner)
    if (profileOwner == currentUser) {
        editProfile = document.getElementById('edit-profile')
        editProfile.style.display = 'block'
        editProfile.children[0].setAttribute('href', '/' + 'profile/edit/' + getSlugOrPk())
    }
}

