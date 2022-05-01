$(document).ready(function(){
    $('#loadMore').on('click', function(){
        var _currentProducts=$(".product-box").length;
        var _limit=$(this).attr('product-limit');
        var _total=$(this).attr('product-total');
        console.log(_currentProducts, _limit, _total)
        //Start Ajax
        $.ajax({
            url:'/load-more-data',
            data:{
                limit:_limit,
                offset:_currentProducts
            },
            dataType: 'json',
            beforeSend:function(){
                $("#loadMore").attr('disabled', true);
                $(".load-more-icon").addClass('fa-spin')
            },
            success:function(res){
                $("#filteredProducts").append(res.data);
                $("#loadMore").attr('disabled', false);
                $(".load-more-icon").removeClass('fa-spin');

                var _totalShowing=$(".product-box").length;
                if(_totalShowing==_total){
                    $("#loadMore").remove();
                }
            }
        })
        //End
    });
    //Product Variation
    $(".choose-size").hide();

    //show size according ro selected color
    $(".choose-color").on('click', function(){
        var _color=$(this).attr('data-color');
        $(".choose-size").hide()
        $(".color"+_color).show();
        $(".color"+_color).first().addClass('active');

    })
    //End

    //Show the price according to selected size
    $(".choose-color").on('click', function(){
        var _price=$(this).attr('data-price');
        $(".choose-size").removeClass('active');
        $(this).addClass('active');
        
        $(".product-price").text(_price);
    })

    // Show the first selected color
    var _color=$(".choose-color").first().attr('data-color');
    var _price=$(".choose-size").first().attr('data-price');
    $(".color"+_color).show()
    $(".color"+_color).first().addClass('active');
    $(".product-price").text(_price);

   
});