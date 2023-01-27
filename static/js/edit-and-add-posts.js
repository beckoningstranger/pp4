var urls = ""
var insert_pics_here = document.querySelector('#uploaded_pics')

// Hide the image input field in the Add Post form that the user is not supposed to touch
if (document.title == "Create a new post") {
    var imagesInputFields = document.getElementsByTagName('p');
    imagesInputFields[3].style.display = "none"
}

// Hide form labels
var labels = document.getElementsByTagName('label')
for (let label of labels) {
    label.style.display = "none"
}

// Add classes to input fields
var inputs = document.getElementsByTagName('input')
for (let input of inputs) {
    input.setAttribute('class', 'form-control')
}
document.getElementById('id_title').setAttribute('placeholder', 'Enter a title for your post')
document.getElementById('id_content').setAttribute('placeholder', 'Compose your post here')
document.getElementById('id_content').setAttribute('class', 'form-control')

if (document.title == "Update your post") {
    urls = document.getElementById('id_images')
    let spaced_urls = urls.value.replaceAll(',', ' ')
    urls.setAttribute("value", spaced_urls)
    // Hide the image input field in the Edit Post form that the user is not supposed to touch
    var imagesInputFields = document.getElementsByTagName('p');
    imagesInputFields[3].style.display = "none"

    // Get all post images and assign eventListeners to them so users can remove them with a click
    postImages = document.getElementsByClassName(
        'user-image'
    )
    for (let image of postImages) {
        image.addEventListener("click", function() {
            newUrlsValue = urls.value.replace(image.src, 'deleted')
            urls.setAttribute("value", newUrlsValue)
            image.remove()
        })
    }

}

// Cloudinary Upload Widget
var myWidget = cloudinary.createUploadWidget(
    {
        cloudName: "dpeawwegg",
        uploadPreset: "upload-preset"
    },
    (error, result) => {
        if (!error && result && result.event === "success") {
            let new_img = document.createElement('img')
            // The widget returns a url leading with http instead of https, but that's easily replaced
            let receivedUrl = result.info.url.replace('http', 'https')
            // Now the newly created image element is formatted and inserted into the DOM
            new_img.setAttribute("src", receivedUrl)
            new_img.setAttribute("width", "150")
            new_img.setAttribute("height", "150")
            new_img.setAttribute("class", "rounded m-1 user-image")
            new_img.addEventListener("click", function () {
                newUrlsValue = urls.value.replace(new_img.src, '')
                urls.setAttribute("value", newUrlsValue)
                new_img.remove()
            });
            insert_pics_here.insertAdjacentElement("beforeend", new_img);

            // The uploaded image's received url is inserted into the  hidden input field in the form
            urls = document.getElementById('id_images')
            if (urls.value === "") {
                urls.setAttribute("value", receivedUrl)
            }
            else {
                urls.setAttribute("value", urls.value + " " + receivedUrl);
            }
        }
    }
);

// Event Listener for Cloudinary widget
document.getElementById("upload_widget").addEventListener(
    "click",
    function () {
        myWidget.open();
    },
    false
);