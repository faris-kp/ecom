document.getElementById("departments__button").addEventListener("click", function () {
    var categories = document.querySelectorAll(".departments__body");
    categories.forEach(function (category) {
        // Check if the display property is set, and toggle it
        if (category.style.display === "none" || category.style.display === "") {
            category.style.display = "block"; // Display the category
        } else {
            category.style.display = "none"; // Hide the category
        }
    });
});

$(document).ready(function() {
    setTimeout(() => {
        $(".alert").alert("close");
    }, 3000);
});
