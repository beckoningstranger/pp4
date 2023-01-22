var urls = ""
var insert_pics_here = document.querySelector('#uploaded_pics')

// Hide the image input field in the Add Post form that the user is not supposed to touch
if (document.title == "Create a new post") {
    var imagesInputFields = document.getElementsByTagName('p');
    imagesInputFields[4].style.display = "none"
}

if (document.title == "Update your post") {
    urls = document.getElementById('id_images')
    let spaced_urls = urls.value.replaceAll(',', ' ')
    urls.setAttribute("value", spaced_urls)
    // Hide the image input field in the Edit Post form that the user is not supposed to touch
    var imagesInputFields = document.getElementsByTagName('p');
    imagesInputFields[4].style.display = "none"

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
            new_img.setAttribute("src", result.info.url)
            new_img.setAttribute("width", "200")
            new_img.setAttribute("height", "200")
            new_img.addEventListener("click", function () {
                newUrlsValue = urls.value.replace(new_img.src, '')
                urls.setAttribute("value", newUrlsValue)
                new_img.remove()
            });
            insert_pics_here.insertAdjacentElement("beforeend", new_img);

            urls = document.getElementById('id_images')
            if (urls.value === "") {
                urls.setAttribute("value", result.info.url)
            }
            else {
                urls.setAttribute("value", urls.value + " " + result.info.url);
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