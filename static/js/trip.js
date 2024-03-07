$(function(){
    $('#addbtn').click(function(){
        c = $('#waypnt').children().length;
        html =`
        <ul class="list-group list-group-horizontal" id="p${c}">
        <li class="list-group-item"><input type="text" name="point${c}" id="point${c}" class="form-control points"  placeholder="Enter Place"></li>
        <li class="list-group-item"><input type="number" name="km${c}" style="width: 70px;" id="km${c}" class="form-control kilometers" placeholder="Km"></li>
        <li class="list-group-item"><button class="btn btn-danger btn-sm rmbtn" data="p${c}"><i class="bi bi-dash-circle"></i></button></li>
        </ul>
        `;
        $('#waypnt').append(html)
    })

    $('#waypnt').on('click', '.rmbtn', function(){
        id = '#'+$(this).attr('data');
        $(id).remove()
    })

    $('#submit').click(function(){
        var pnts = [];
        pnts = $.map($(".points"),function(select){
            return $(select).val();
        });
        var kms = [];
        kms = $.map($(".kilometers"),function(select){
            return $(select).val();
        });
        if($('#from').val() == '' || $('#to').val() == '' || $('#departure_time').val() == '' || $('#amount').val() == ''){
            alert('Please fill the field first !')
        }
        else{
            data = {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'from': $('#from').val(),
                'to': $('#to').val(),
                'd_time': $('#departure_time').val(),
                'e_time': $('#estimated_time').val(),
                'preference': $('#preference').val(),
                'amount': $('#amount').val(),
                'desc': $('#desc').val(),
                'points': pnts+'',
                'kilometers': kms+''
            }
            data = JSON.parse(JSON.stringify(data))
            $.post("/pooler/ride/", data, function(res){
                if(res.success){
                    window.alert('successfully added trip');
                    window.location.href='/pooler/'
                }
            })
        }
    })

})