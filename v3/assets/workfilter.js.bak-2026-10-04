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
    cards.forEach(function(c){ if(cat==='all'||c.getAttribute('data-cat')===cat) grid.appendChild(c); });
  });
})();
