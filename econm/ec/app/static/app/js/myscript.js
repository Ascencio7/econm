
$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log("pid =",id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data = ",data);
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})

//Para decrementar los productos
$(' .minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount

        }
    })
})


$(' .remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})


function updateWishlist(action) {
    $('.' + action + '-wishlist').click(function() {
        var id = $(this).attr("pid").toString();
        $.ajax({
            type: "GET",
            url: `/${action}wishlist`,
            data: {
                prod_id: id
            },
            success: function(data) {
                window.location.href = `${window.location.origin}/product-detail/${id}`;
            }
        });
    });
}

updateWishlist('plus');
updateWishlist('minus');
