function android(){
  $.ajax({
    type: "GET",
    url: "/android/js",
    data: "",
    success: function(data) {
      var arr = data.split('|');
//	  console.log('yes')
      if(arr[1] == 'new'){
        var current_uri = window.location.pathname;
		if(current_uri == '/froze/new/' && window.location.search.indexOf(arr[0])+1){
		  //do nothing
		}
		else{
		  var uri = '/froze/new/?phone_client=' + arr[0] + '&from_android';
          window.open(uri, '_blank');
		}
      }

      else if(arr[1] == 'existing'){
        var current_uri = window.location.pathname;
		if(current_uri == '/search/new' && window.location.search.indexOf(arr[0])+1){
		  window.location.reload();
		}
		else{
		  var uri = '/search/new?po_telefonu=' + arr[0] + '&from_android';
          window.open(uri, '_blank');
		}
      }
    }
  });
}
$(document).ready(function() {
  setInterval(function() {
    android();
  }, 3000);
});