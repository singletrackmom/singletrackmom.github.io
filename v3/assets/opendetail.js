/* opendetail.js, opens a collapsed section when a link points at it.
   GOAL     A link to one assignment opens that assignment and scrolls to it.
   AUDIENCE Anyone following a link into a page of collapsed sections.
   PROCESS  On load and whenever the address changes, find the element the
            address names. If it is a collapsed section, or sits inside one,
            open it, then bring it to the top of the screen. */
(function(){
  function go(){
    var id=decodeURIComponent((location.hash||'').slice(1)); if(!id) return;
    var el=document.getElementById(id); if(!el) return;
    var d=el.closest?el.closest('details'):null;
    while(d){ d.open=true; d=d.parentElement&&d.parentElement.closest?d.parentElement.closest('details'):null; }
    setTimeout(function(){ el.scrollIntoView({block:'start'}); },0);
  }
  window.addEventListener('hashchange',go);
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',go); else go();
})();
