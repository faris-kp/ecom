console.log("working")



$("#commentForm_review").submit(function(e) {
    e.preventDefault(); // Prevent the default form submission
    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(response){
            console.log("saved to DB...",response)


            if(response.bool == true){
                $("#review-add-text").html("Review Added Successfully")
            }
        }
    });


});
