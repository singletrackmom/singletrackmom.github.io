/* This Week card (Start page) and current-week highlight (Calendar). */
(function(){
  var W=window.BB_WEEKS||[]; if(!W.length)return;
  var today=new Date(); today.setHours(0,0,0,0);
  var idx=0;
  for(var i=0;i<W.length;i++){var d=new Date(W[i].start+'T00:00:00'); if(d<=today)idx=i;}
  var first=new Date(W[0].start+'T00:00:00'), last=new Date(W[W.length-1].start+'T00:00:00');
  var before=today<first, after=today>new Date(last.getTime()+6*864e5);
  var w=W[idx];
  var box=document.getElementById('thisweek');
  if(box){
    var esc=function(t){var s=document.createElement('span');s.textContent=t;return s.innerHTML;};
    var items=[['Monday','Venue',w.venue,'venues.html'],['Tuesday','Instagram',w.ig,'instagram.html'],['Wednesday','Planner',w.planner+': send the collab message or the planner note.','planners.html']];
    if(w.blog)items.push(['Thursday','Blog post',w.blog,'blog.html']);
    items.push(['Friday','Fix old posts','Three old blog posts: alt text, SEO title, SEO description.','seo.html']);
    if(w.also)items.push(['Any day','Also',w.also,'calendar.html']);
    var head=after?'<p>The six-month calendar is finished. Start again from the top of the <a href="calendar.html">Calendar tab</a>.</p>':
      '<p class="small">'+(before?'Starting Monday ':'Week of ')+esc(w.label)+'. Tap a day’s link for help with it.</p>';
    var html=head+'<ul class="todo">';
    items.forEach(function(it,n){
      var id='w'+w.start+'-'+n;
      html+='<li><label><input type="checkbox" id="'+id+'"><span><strong>'+it[0]+' · '+it[1]+':</strong> '+esc(it[2])+' <a href="'+it[3]+'">How</a></span></label></li>';
    });
    box.innerHTML=html+'</ul>';
  }
  var row=document.querySelector('tr[data-week="'+w.start+'"]');
  if(row){row.classList.add('now');var c=row.cells[0];if(c)c.innerHTML+='<br><span class="nowtag">This week</span>';}
})();
/* Berg Berg Photography Marketing Plan: copy buttons and remembered checkboxes. */
(function(){
  document.querySelectorAll('button.copy').forEach(function(btn){
    btn.addEventListener('click',function(){
      var box=document.getElementById(btn.getAttribute('data-copy'));
      if(!box)return;
      var text=box.innerText.trim();
      var done=function(){var old=btn.textContent;btn.textContent='Copied';setTimeout(function(){btn.textContent=old;},1600);};
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){});}
    });
  });
  var store=null;
  try{store=window.localStorage;store.getItem('bb');}catch(e){store=null;}
  document.querySelectorAll('.todo input[type=checkbox]').forEach(function(box){
    var key='bb-'+box.id;
    try{if(store&&store.getItem(key)==='1')box.checked=true;}catch(e){}
    box.addEventListener('change',function(){
      try{if(store){box.checked?store.setItem(key,'1'):store.removeItem(key);}}catch(e){}
    });
  });
})();
