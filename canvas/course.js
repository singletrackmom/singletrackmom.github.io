/* Shared course page script: open the module that holds a linked anchor; copy-email footer link. */
(function(){
  function openTo(t){var d=t&&t.closest('details');while(d){d.open=true;d=d.parentElement&&d.parentElement.closest('details');}}
  function openHash(){var h=location.hash&&document.getElementById(location.hash.slice(1));if(!h)return;if(h.tagName==='DETAILS')h.open=true;openTo(h);}
  window.addEventListener('hashchange',openHash);openHash();
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a)return;var t=document.getElementById(a.getAttribute('href').slice(1));if(t){if(t.tagName==='DETAILS')t.open=true;openTo(t);}});
})();
(function(){
  var u=['michelleblomberg','gmail','com'];
  function mmToast(el,msg){var t=document.createElement('span');t.textContent=msg;t.setAttribute('role','status');t.style.cssText='margin-left:.5rem;font-size:.875rem;color:#456546;font-weight:600;white-space:nowrap';el.insertAdjacentElement('afterend',t);setTimeout(function(){if(t.parentNode)t.parentNode.removeChild(t);},2600);}
  document.addEventListener('click',function(e){
    var a=e.target.closest && e.target.closest('.mailme');
    if(!a) return; e.preventDefault();
    var email=u[0]+String.fromCharCode(64)+u[1]+'.'+u[2];
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(email).then(function(){mmToast(a,'Copied '+email);},function(){});}
    var gm='https://mail.google.com/mail/?view=cm&fs=1&tf=1&to='+encodeURIComponent(email);
    var w=window.open(gm,'_blank','noopener'); if(!w){ try{window.location.href='mai'+'lto:'+email;}catch(_){}}
  });
})();
