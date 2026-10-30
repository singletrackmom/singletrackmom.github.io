/* workfilter.js, the tab row above the work cards on the v3 home page.
   GOAL     Let a visitor narrow the cards to one section.
   AUDIENCE Anyone on the home page.
   PROCESS  Cards that do not match the chosen tab are taken out of the grid
            and put back when All is chosen. No styles are added or changed. */
(function(){
  var bar=document.getElementById('worktabs'), grid=document.getElementById('workgrid');
  if(!bar||!grid) return;
  var cards=Array.prototype.slice.call(grid.children);
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button'); if(!b) return;
    var cat=b.getAttribute('data-cat');
    Array.prototype.forEach.call(bar.querySelectorAll('button'),function(x){x.setAttribute('aria-selected',x===b?'true':'false');});
    while(grid.firstChild) grid.removeChild(grid.firstChild);
    cards.forEach(function(c){ if((' '+c.getAttribute('data-cat')+' ').indexOf(' '+cat+' ')>-1) grid.appendChild(c); });
    /* Put the tab in the address bar so the link can be shared. */
    var slug=SLUG[cat]||cat;
    if(e.isTrusted && history.replaceState) history.replaceState(null,'','#'+slug);
  });
  /* Shareable names for each tab, e.g. michelleblomberg.com/#courses */
  var SLUG={studies:'ai-strategy',tools:'ai-tools',course:'courses',adopt:'adoption',teach:'experiential-learning',personal:'personal-projects'};
  var FROM={}; Object.keys(SLUG).forEach(function(k){FROM[SLUG[k]]=k;});
  function show(cat){
    var b=bar.querySelector('button[data-cat="'+cat+'"]'); if(b) b.click();
  }
  function fromHash(){
    var h=(location.hash||'').replace('#','');
    h=FROM[h]||h;
    var b=h&&bar.querySelector('button[data-cat="'+h+'"]');
    if(b){ b.click(); var head=document.getElementById('work'); if(head) head.scrollIntoView(); }
  }
  window.addEventListener('hashchange',fromHash);
  /* No All view: the first tab shows when the page opens. */
  var first=bar.querySelector('button'); if(first) show(first.getAttribute('data-cat'));
  fromHash();
})();
