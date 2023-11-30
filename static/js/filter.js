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


//Add to cart 



$(".add-to-cart-btn").on("click", function(event){
    console.log("hellow world")
    event.preventDefault();

    let this_val = $(this)
    let index = this_val.attr("data-index")
    let quantity = $(".product-quantity-" + index).val()  
    let product_title = $(".product-title-" + index).val()
    let product_id = $(".product-id-" + index).val()
    let product_price = $(".product__prices-" + index).text()
    let product_pid = $(".product-pid-" + index).val()
    let product_image = $(".product-image-" + index).val()
    

    console.log("quanity:",quantity);
    console.log("title",product_title);
    console.log("id",product_id);
    console.log("price:",product_price);
    console.log("pid:",product_pid);
    console.log("image:",product_image);
    console.log("index",index);
    console.log("this:",this_val);

    
    $.ajax({
        url:'/add-to-cart',
        data:{
            'id':product_id,
            'pid':product_pid,
            'image':product_image,
            'qty':quantity,
            'title':product_title,
            'price':product_price
        },
        dataType:'json',
        beforeSend:function(){
            console.log("adding prodcut to cart");
        },
        success:function(res){
            this_val.html("✔")

            console.log("added prodcut to cart");
            $(".cart-item-count").text(res.totalcartitem)
        }
    })

})

//   $("#add-to-cart").on("click", function(event){
//     console.log("hellow world")
//     event.preventDefault();
//     let quantity = $("#product-quantity").val()  
//     let product_title = $(".product-title").val()
//     let product_id = $(".product-id").val()
//     let product_price = $(".product__prices").text()
//     let this_val = $(this)

//     console.log("qua:",quantity);
//     console.log("title",product_title);
//     console.log("id",product_id);
//     console.log("price:",product_price);
//     console.log("this:",this_val);
//     $.ajax({
//         url:'/add-to-cart',
//         data:{
//             'id':product_id,
//             'qty':quantity,
//             'title':product_title,
//             'price':product_price
//         },
//         dataType:'json',
//         beforeSend:function(){
//             console.log("adding prodcut to cart");
//         },
//         success:function(res){
//             this_val.html("Item added successfully")

//             console.log("added prodcut to cart");
//             $(".cart-item-count").text(res.totalcartitem)
//         }
//     })

// })
})




