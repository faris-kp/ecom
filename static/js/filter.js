console.log("hellow world")

$(document).ready(function(){
    $(".filter-checkbox").on("click", function(){
        console.log("A check box has been clicked");
        let filter_object = {}

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter='+ filter_key +']:checked')).map(function(element){
                return element.value
            })
        })
        console.log("filter-object",filter_object);
        $.ajax({
            url: '/filter-product',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("Trying to filter");
            },
            success : function(responce){
                console.log(responce);
                console.log("Data filtered succesfully");
                $("#filtered-products").html(responce.data)

            }

        })
    })
})