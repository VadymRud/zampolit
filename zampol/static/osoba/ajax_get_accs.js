function get_accs(btn){
    var btn_accs = "#"+btn;
    alert(btn_accs);
}
// $("#name_accs_btn").click(function () {
//     //var username = $(this).val();
//     alert('');

//     // $.ajax({
//     //     url: '/ajax/validate-username/',
//     //     // url: '{% url 'simple_ajax_validate' %}',
//     //     data: {
//     //         'username': username
//     //     },
//     //     dataType: 'json',
//     //     success: function (data) {
//     //         if (data.is_present) {
//     //             alert("A user with this username already exists.");
//     //         }
//     //     }
//     // });
//    return false;
//});

$(function() {
    $('#id_birth_date').datepicker( "option", "yearRange", "2002:2012" );
});