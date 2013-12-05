/**************
 * GENERAL.JS *
 *************/

$(document).on("submit", "form#login", function(e) {
	
	$.post($(this).attr("action"), $(this).serialize(), function(data) {
		try {
			var data = JSON.parse(data);
			if(data['error']) {
				$("span#login-message").text(data['error']);
			}
		} catch(ex) {
			location.reload();
		}
	});
	e.preventDefault();
});


$(document).on("click", "#login", function() {
	$("#dialogin").dialog("open");
});

