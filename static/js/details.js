// Main Image and Image Picker behavior

// Check if the image picker was loaded because there are multiple images for the post
if (document.getElementById('image-picker') != null) {
    var images = document.getElementById('image-picker').children
    var mainImage = document.getElementById('main-image')

    for (let image of images) {
        // When user click an image in the image picker, it should become the main image
        image.addEventListener("click", function () {
            // Reset borders on all thumbnails
            for (let image of images) {
                image.style.border = "none"
            }
            // Mark clicked image as active one
            image.style.border = "4px solid white"
            // Make clicked image main image
            mainImage.setAttribute('src', image.src)
        })
    }
    // On load, mark the first image as the active one
    images[0].style.border = "4px solid white"
    images[0].style.borderRadius = "10px"
}

// Comments behavior

var commentCards = document.getElementsByClassName('comment-card')
var commentCardButtons = document.getElementsByClassName('comment-buttons')
for (let commentCard of commentCards) {
    commentCard.addEventListener("mouseover", function () {
        for (let cCB of commentCardButtons) {
            cCB.style.visibility = "visible"
        }
    })
    commentCard.addEventListener("mouseout", function () {
        for (let cCB of commentCardButtons) {
            cCB.style.visibility = "hidden"
        }
    })
}