function getDocumentF5Ajax(id){
    csrftoken = $("input[name='csrfmiddlewaretoken']").val();
    //alert(id+"__"+csrftoken);
    data= {id_staff: id};
    $.ajax({
        url: "/ajax/getdocoment/f5",
        data : data,
        method : 'POST',
        headers: {
                      'X-CSRFToken': csrftoken 
                 },
        success: function (data) {
            alert(data.result)
        },
        error: function (data) {concole.log(data)}
  });
}