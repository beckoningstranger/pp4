var insert_pics_here = document.querySelector('#uploaded_pics')
var image_url = document.getElementById('id_profile_image')

// Hide the image input field so user can't touch it
var imagesInputFields = document.getElementsByTagName('p');
imagesInputFields[4].style.display = "none"

// Get the profile image and assign eventListeners to it so users can remove it with a click
if (document.getElementById('profile-image') != null) {
    let previous_img = document.getElementById('profile-image')
    previous_img.addEventListener("click", function () {
        image_url.setAttribute("value", "placeholder")
        previous_img.remove()
    });
}
else {
    previous_img = false;
}




// Cloudinary upload widget

var myWidget = cloudinary.createUploadWidget(
    {
        cloudName: "dpeawwegg",
        uploadPreset: "upload-preset"
    },
    (error, result) => {
        if (!error && result && result.event === "success") {
            if (previous_img) {
                previous_img.remove()
            }
            let profile_img = document.createElement('img')
            profile_img.setAttribute("src", result.info.url)
            profile_img.setAttribute("width", "200")
            profile_img.setAttribute("height", "200")
            profile_img.addEventListener("click", function () {
                urls.setAttribute("value", 'placeholder')
                profile_img.remove()
            });
            insert_pics_here.insertAdjacentElement("beforeend", profile_img);
            image_url = document.getElementById('id_profile_image')
            image_url.setAttribute("value", result.info.url)
        }
    }
);

// Event Listener for Cloudinary upload widget
document.getElementById("upload_widget").addEventListener(
    "click",
    function () {
        myWidget.open();
    },
    false
);