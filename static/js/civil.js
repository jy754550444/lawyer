//$.ajax({
//    type: "GET",
//    cache: false,
//    url: '/civiliagents?law_name=' + b,
//    datatype: "JSON",
//    success: function (data) {
//        $('#id_nail_tel').val(data['tel']);
//        $('#id_nail_name').val(data['name']);
//    },
//    error: function (error) {
//        console.log(error);
//    }
//});

$("#id_civil").change(function () {
    a = $("#id_civil option:selected").text();
    b = $(".dropdown-toggle strong").text();
    $.ajax({
        type: "GET",
        cache: false,
        url: '/civiliagent?case_id=' + a + '&law_name=' + b,
        datatype: "JSON",
        success: function (data) {
            $('#id_nail_tel').val(data['tel']);
            $('#id_nail_name').val(data['name']);
            $('#id_nail_address').val(data['address']);
            $('#id_name').val(data['party']);
            $('#id_court').val(data['case_office']);
            $('#id_Trial_level').val(data['trial_level']);
            $('#id_case').val(data['case']);
            $('#id_nail_contacts').val(data['b_name']);
            $('#id_b_legal').val(data['f_name']);
            $('#id_law').val(data['law_name']);
            $('#id_b_tel').val(data['law_tel']);
            $('#id_b_address').val(data['law_address']);
        },
        error: function (error) {
            console.log(error);
        }
    })
});
