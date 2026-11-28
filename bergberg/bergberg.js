/* Berg Berg Photography Marketing Plan: This Week card, message pop-outs, copy buttons, remembered checkboxes. */
(function(){
  var S=window.BB_SCRIPTS||{}, W=window.BB_WEEKS||[];
  var esc=function(t){var s=document.createElement('span');s.textContent=t;return s.innerHTML;};
  var uid=0;
  function popHTML(key,venue,planner){
    var m=S[key]; if(!m)return '';
    var f=function(t){return t.replace(/\{venue\}/g,venue||'[venue]').replace(/\{planner\}/g,planner||'[planner]');};
    var id='msg'+(uid++);
    var copy=key==='drafts'?'':'<button class="copy" type="button" data-copy="'+id+'">Copy</button>';
    return '<details class="msg"><summary>See the message</summary><p class="msg-title">'+esc(f(m.title))+'</p><div class="script" id="'+id+'">'+esc(f(m.text))+'</div>'+copy+'</details>';
  }
  /* Current week */
  var today=new Date(); today.setHours(0,0,0,0);
  var idx=0, after=false;
  if(W.length){
    for(var i=0;i<W.length;i++){if(new Date(W[i].start+'T00:00:00')<=today)idx=i;}
    var last=new Date(W[W.length-1].start+'T00:00:00');
    after=today>new Date(last.getTime()+6*864e5);
  }
  var w=W[idx];
  var box=document.getElementById('thisweek');
  if(box&&w){
    var before=today<new Date(W[0].start+'T00:00:00');
    var items=[
      ['Monday','Venue',w.venue,'venues.html',w.venueKey,w.venueName,''],
      ['Tuesday','Instagram',w.ig,'instagram.html','','',''],
      ['Wednesday','Planner',w.planner,'planners.html',w.plannerKey,'',w.plannerKey==='planner_new'?'':w.planner]
    ];
    var C=(window.BB_CARRY&&window.BB_CARRY.items)||[];
    for(var c=C.length-1;c>=0;c--){items.unshift(['First','Carried over',C[c].text,C[c].help||'index.html',C[c].key||'',C[c].fill||'','']);}
    if(w.blog)items.push(['Thursday','Blog post',w.blog,'blog.html','','','']);
    items.push(['Friday','Fix old posts','Three old blog posts: alt text, SEO title, SEO description.','seo.html','','','']);
    (w.also||[]).forEach(function(a){items.push(['This week','Also',a.text,'calendar.html',a.key||'',a.fill||'','']);});
    var html=after?'<p>The six-month calendar is finished. Start again from the top of the <a href="calendar.html">Calendar tab</a>.</p>':
      '<p class="small">'+(before?'Starting Monday ':'Week of ')+esc(w.label)+'.</p>';
    html+='<ul class="todo">';
    items.forEach(function(it,n){
      html+='<li><label><input type="checkbox" id="'+(it[1]==='Carried over'?'c-'+(window.BB_CARRY.updated||'')+'-'+n:'w'+w.start+'-'+n)+'"><span><strong>'+it[0]+' · '+it[1]+':</strong> '+esc(it[2])+' <a href="'+it[3]+'">Help</a></span></label>'+(it[4]?popHTML(it[4],it[5],it[6]):'')+'</li>';
    });
    box.innerHTML=html+'</ul>';
  }
  /* Message pop-outs anywhere on a page */
  document.querySelectorAll('[data-script]').forEach(function(el){
    el.outerHTML=popHTML(el.getAttribute('data-script'),el.getAttribute('data-fill-venue')||'',el.getAttribute('data-fill-planner')||'');
  });
  /* Shade this week's calendar row */
  if(w){var row=document.querySelector('tr[data-week="'+w.start+'"]');
    if(row){row.classList.add('now');row.cells[0].innerHTML+='<br><span class="nowtag">This week</span>';}}
  /* Copy buttons, including ones added above */
  document.addEventListener('click',function(e){
    var btn=e.target.closest&&e.target.closest('button.copy'); if(!btn)return;
    var src=document.getElementById(btn.getAttribute('data-copy')); if(!src)return;
    var done=function(){var old=btn.textContent;btn.textContent='Copied';setTimeout(function(){btn.textContent=old;},1600);};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(src.innerText.trim()).then(done,function(){});}
  });
  /* Remember checkboxes on this device */
  var store=null; try{store=window.localStorage;store.getItem('bb');}catch(e){store=null;}
  document.querySelectorAll('.todo input[type=checkbox]').forEach(function(b){
    var key='bb-'+b.id;
    try{if(store&&store.getItem(key)==='1')b.checked=true;}catch(e){}
    b.addEventListener('change',function(){try{if(store){b.checked?store.setItem(key,'1'):store.removeItem(key);}}catch(e){}});
  });
})();
