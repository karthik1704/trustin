'use strict';


(function($){

    $('#id_customer').on('change',function(){
        const id = this.value

        $.ajax({
            url: `/customers/retrieve/${id}`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Display the received data on the page
               Object.keys(data).map((key)=>{
                const className = `.field-${key} .readonly`
                $(className).text(data[key])
               })
            },
            error: function (error) {
                console.error('Error fetching data:', error);
            }
        });

    })

    console.log($('#id_mail_send').checked)
    if (!$('#id_mail_send').checked){
        $('#id_subject').hide()
        $('#id_body').hide()
        $('label[for="id_subject"]').hide();
        $('label[for="id_body"]').hide();
    }

    $('#id_mail_send').on('change', function(){
     
            $('#id_subject').toggle()
            $('label[for="id_subject"]').toggle();
            $('#id_body').toggle()
            $('label[for="id_body"]').toggle();
        
    
    })

}(django.jQuery));