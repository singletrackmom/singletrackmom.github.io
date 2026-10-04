/* mail.js, makes the Email link work without printing the address in the page.
   GOAL     A visitor who clicks Email gets a new message addressed to Michelle.
   AUDIENCE Anyone on any page.
   PROCESS  The address is assembled on click, so it is not in the markup for scrapers. */
document.addEventListener('click',function(e){
  var a=e.target.closest&&e.target.closest('a.mailme'); if(!a) return;
  e.preventDefault();
  location.href='mai'+'lto:'+['michelleblomberg','gmail.com'].join('@');
});
