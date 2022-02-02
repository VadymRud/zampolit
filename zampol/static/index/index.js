var str = '';
let elem;
var menu= new Contextmenu({
    name:"menu",
    wrapper:".wrapper",
    trigger: ".item",
    item:[{
            "name":"Службова Картка",
            "func":"getDocumentSCAjax()",
            "link":null,
            "disable":false
          },
          {
            "name":"Аркуш Співбесід",
            "func":"getInterviewAjax()",
            "disable":false
          },
          {
            "name":"Disabled Item",
            "disable":true
          },
          {
            "name":"-"
          },
          {
            "name":"Delete Method",
            "func":"delItem()"
          },
          {
            "name":"Update Method",
            "func":"updateItem()"
          },
          {
            "name":"Add Method",
            "func":"addItem()"
          },
          {
            "name":"-"
          },
          {
            "name":"Remove Method",
            "func":"removeMenu()"
          },
          {
            "name":"Close The Menu"
          }
    ],
    target:"_blank",
    beforeFunc: function (ele) {
        // str = $(ele).text();
        elem = $(ele).children("td").children("input").val();
    }
});

	function setText() {
        alert(str);

	}

	function addItem() {
		csrftoken = $("input[name='csrfmiddlewaretoken']").val();
    //alert(id+"__"+csrftoken);
        data= {id_staff: id};
        $.ajax({
            url: "/ajax/getdocoment/sc",
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

	function delItem() {
		menu.del(4);
	}

	function removeMenu() {
		menu.destroy();
	}

	function updateItem() {
		menu.update({
			index: 5,
			name:"github",
			func:"",
			link:"https://www.jqueryscript.net",
			disable:false
		});
	}
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

function getDocumentSCAjax(){
    csrftoken = $("input[name='csrfmiddlewaretoken']").val();
    //alert(id+"__"+csrftoken);
    data= {id_staff: elem};
    $.ajax({
        url: "/ajax/getdocoment/sc",
        data : data,
        method : 'POST',
        headers: {
                      'X-CSRFToken': csrftoken
                 },
        success: function (data) {
            alert(data.result)
        },
        error: function (data) {
            console.log(data);
        }
  });
}

function getInterviewAjax(){
    csrftoken = $("input[name='csrfmiddlewaretoken']").val();
    //alert(id+"__"+csrftoken);
    data= {id_staff: elem};
    $.ajax({
        url: "/ajax/getdocoment/interview",
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