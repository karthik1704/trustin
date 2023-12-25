console.log('hi');




$(document).ready(function () {



    $('#myTable').on('click', '.move-up', function () {
        var row = $(this).closest('tr');
        if (row.index() > 0) {
            var prevRow = row.prev();
            row.find('.order').val(prevRow.find('.order').val());
            prevRow.find('.order').val(row.index() + 1);
            row.slideUp('fast', function () {
                row.insertBefore(row.prev()).slideDown('fast');
                updateButtonState();
            });
        }
    });

    // Move row down
    $('#myTable').on('click', '.move-down', function () {
        var row = $(this).closest('tr');
        if (row.index() < $('#myTable tbody tr').length - 1) {
            var nextRow = row.next();
            row.find('.order').val(nextRow.find('.order').val());
            nextRow.find('.order').val(row.index() + 1);
            row.slideUp('fast', function () {
                row.insertAfter(row.next()).slideDown('fast');
                updateButtonState();
            });
        }
    });

    // Remove Row
    $('#myTable').on('click', '.remove-row', function () {
        var row = $(this).closest('tr');
        var removedOrder = parseInt(row.find('.order').val(), 10);
        row.slideUp('fast', function () {
            row.remove();
            updateOrderAfterRemoval(removedOrder);
            updateButtonState();
        });
    });
    // Update order when remove Row
    function updateOrderAfterRemoval(removedOrder) {
        $('#myTable tbody tr').each(function () {
            var order = parseInt($(this).find('.order').val(), 10);
            if (order > removedOrder) {
                $(this).find('.order').val(order - 1);
            }
        });
    }
    // diable last and first down and up button 
    function updateButtonState() {
        $('#myTable tbody tr').each(function (index) {
            var moveUpButton = $(this).find('.move-up');
            var moveDownButton = $(this).find('.move-down');

            if (index === 0) {
                moveUpButton.prop('disabled', true).addClass('disabled');
            } else {
                moveUpButton.prop('disabled', false).removeClass('disabled');
            }

            if (index === $('#myTable tbody tr').length - 1) {
                moveDownButton.prop('disabled', true).addClass('disabled');
            } else {
                moveDownButton.prop('disabled', false).removeClass('disabled');
            }
        });
    }

    // Initial button state
    updateButtonState();



    $('#id_product, #id_test_type').on('change', function () {
        let product = $('#id_product').val();
        let test_type = '';
        let checkTestType = []
        $("input[name='test_type']:checked").each(function () {
            checkTestType.push($(this).val());
        });

        console.log(checkTestType)


        // $.ajax({
        //     url: `/samples/tests/${product}/`,
        //     type: 'GET',
        //     dataType: 'json',
        //     success: function (data) {
        //         var tbody = $("#myTable tbody");

        //         var rows = $.map(data, (d, idx) => {


        //             var newRow = $("<tr>");

        //             var cell1 = $("<td>").text(idx + 1);
        //             var cell2 = $("<td>").text(d.testing_parameters).append(
        //             `
        //             <input type="text"  name="testing-${idx}-test" id="id_testing-${idx}-test" value="${d.id}" />
        //             <input type="hidden" name="testing-${idx}-id" id="id_testing-${idx}-id">

        //             `
        //             );
        //             var cell3 = $("<td>").text(d.method_or_spec);
        //             var cell4 = $("<td>").text(d.test_type);
        //             var cell5 = $("<td>").append('<button type="button" class="btn btn-primary remove-row" id="remove-button">Remove</button>');
        //             var cell5 = $("<td>").append('<button type="button" class="btn btn-primary remove-row" id="remove-button">Remove</button>');
        //             var cell6 = $("<td>").append(` <button type="button" class="btn btn-primary move-up" id="up-button">Up</button>
        //             <button type="button" class="btn btn-primary move-down"
        //                 id="down-button">Down</button>
        //             <input type="text" name="testing-${idx}-priority_order" id="id_testing-${idx}-priority_order" class="order" value="${idx + 1}" />
                 
        //             `);

        //             return newRow.append(cell1, cell2, cell3, cell4, cell5, cell6);


        //         })
        //         $('#id_testing-TOTAL_FORMS').val(rows.length)
        //         tbody.empty().append(rows);
        //         console.log(data)
        //     },
        //     error: function (error) {
        //         console.error('Error fetching data:', error);
        //     }
        // });

       getTestParameters(product, checkTestType)

    })

    function getTestParameters(product, test_type){

         $.ajax({
            url: `/samples/tests/${product}/?test_type=${test_type.join(',')}`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                var tbody = $("#myTable tbody");
                tbody.empty().text('Loading...');
                var rows = $.map(data, (d, idx) => {


                    var newRow = $("<tr>");

                    var cell1 = $("<td>").text(idx + 1);
                    var cell2 = $("<td>").text(d.testing_parameters).append(
                    `
                    <input type="text"  name="testing-${idx}-test" id="id_testing-${idx}-test" value="${d.id}" />
                    <input type="hidden" name="testing-${idx}-id" id="id_testing-${idx}-id">

                    `
                    );
                    var cell3 = $("<td>").text(d.method_or_spec);
                    var cell4 = $("<td>").text(d.test_type);
                    var cell5 = $("<td>").append('<button type="button" class="btn btn-primary remove-row" id="remove-button">Remove</button>');
                    var cell5 = $("<td>").append('<button type="button" class="btn btn-primary remove-row" id="remove-button">Remove</button>');
                    var cell6 = $("<td>").append(` <button type="button" class="btn btn-primary move-up" id="up-button">Up</button>
                    <button type="button" class="btn btn-primary move-down"
                        id="down-button">Down</button>
                    <input type="text" name="testing-${idx}-priority_order" id="id_testing-${idx}-priority_order" class="order" value="${idx + 1}" />
                 
                    `);

                    return newRow.append(cell1, cell2, cell3, cell4, cell5, cell6);


                })
                $('#id_testing-TOTAL_FORMS').val(rows.length)
                tbody.empty().append(rows);
                console.log(data)
            },
            error: function (error) {
                console.error('Error fetching data:', error);
            }
        });
    }

})


$(document).ready(function(){
        var trf_code = $('#id_trf_code').val();
        $.ajax({
           url: `/trf/tdetail/${trf_code}/`,
           type: 'GET',
           dataType: 'json',
           success: function (data) {
               var tbody = $("#myTable tbody");

               var rows = $.map(data, (d, idx) => {


                   var newRow = $("<tr>");

                   var cell1 = $("<td>").text(idx + 1);
                   var cell2 = $("<td>").text(d.test.testing_parameters).append(
                   `
                   <input type="text"  name="testing-${idx}-test" id="id_testing-${idx}-test" value="${d.test.id}" />
                   <input type="hidden" name="testing-${idx}-id" id="id_testing-${idx}-id">

                   `
                   );
                   var cell3 = $("<td>").text(d.test.method_or_spec);
                   var cell4 = $("<td>").text(d.test.test_type);
                   var cell5 = $("<td>").append('<button type="button" class="btn btn-primary remove-row" id="remove-button">Remove</button>');
                   var cell5 = $("<td>").append('<button type="button" class="btn btn-primary remove-row" id="remove-button">Remove</button>');
                   var cell6 = $("<td>").append(` <button type="button" class="btn btn-primary move-up" id="up-button">Up</button>
                   <button type="button" class="btn btn-primary move-down"
                       id="down-button">Down</button>
                   <input type="text" name="testing-${idx}-priority_order" id="id_testing-${idx}-priority_order" class="order" value="${d.priority_order}" />
                
                   `);

                   return newRow.append(cell1, cell2, cell3, cell4, cell5, cell6);


               })
               $('#id_testing-TOTAL_FORMS').val(rows.length)
               tbody.empty().append(rows);
               console.log(data)
           },
           error: function (error) {
               console.error('Error fetching data:', error);
           }
       });
})


