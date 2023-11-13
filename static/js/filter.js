console.log("hellow world")

$(document).ready(function(){
    $(".filter-checkbox,#price-filter-btn").on("click", function(){
        console.log("A check box has been clicked");
        let filter_object = {}

        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price = min_price
        filter_object.max_price = max_price

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

  $("#max_price").on("blur", function(){
    let min_price =$(this).attr("min")
    let max_price =$(this).attr("max")
    let current_price = $(this).val()

    console.log("current_value",current_price);

    if (current_price < parseInt(min_price) || current_price > parseInt(max_price)){
        min_price  = Math.round( min_price * 100) /100
        max_price  = Math.round( max_price * 100) /100
        alert("The value muust be between $"+min_price +"and $"+max_price )

        $(this).val(min_price)
        $("#range").val(min_price)
        $(this).focus()


        return false

    }

  })  
})