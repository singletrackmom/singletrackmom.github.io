import json,datetime,html as H
# Each week: venue (text, script key, venue name), planner (name, key), instagram, blog, also [(text, key or None, fill)]
W=[
 (("Headwaters Center: brochures and a hello (in your Gmail Drafts)","drafts","Headwaters Center"),("Flora Moon Events","drafts"),"The late-October Evergreen Lake House wedding (collab: planner and venue)","The late-October Evergreen Lake House wedding",[("Send the Gmail drafts",'drafts',""),("Reply to Yeti or Knot with a perk","yeti",""),("Monthly check (1 Dec)",None,"")]),
 (("Evergreen Lake House: brochures, spring showcase, display album","drafts","Evergreen Lake House"),("Harper Bond Events","drafts"),"Snowy portraits from past winter weddings","",[("Blackstone Country Club: ask to be on their list","drafts","")]),
 (("Baldoria on the Water: ask for a meeting with your album","venue_meeting","Baldoria on the Water"),("Mag Events","drafts"),"A Headwaters Center wedding (collab: Mag Events)","A Boettcher Mansion wedding from this year",[("Optional: Table Mountain Meetings & Events (new)","venue_new","Table Mountain Meetings & Events")]),
 (("Holiday thank-you note to all seven venues","holiday",""),("Exquisite Events & Productions","drafts"),"Favorite moments of 2026","",[("Holiday thank-you notes to planners too","holiday","")]),
 (("The Vista at Applewood: brochures and a hello","venue_brochures","The Vista at Applewood"),("Paige Lane Designs","drafts"),"Planning tip: how much time you need for photos","",[("Monthly check (1 Jan)",None,"")]),
 (("Mount Vernon Canyon Club: “It’s Been a While” email, refresh the album","venue_while","Mount Vernon Canyon Club"),("Islagant Co. Events & Design","planner_note"),"A Boettcher Mansion wedding (collab: Harper Bond Events)","Evergreen Lake House Wedding Guide",[("Ask Baldoria for its next open house","show_ask",""),("Ask the Golden Wedding Show for its 2027 date","show_ask","")]),
 (("The Golden Hotel: “It’s Been a While” email and your Golden Hotel post","venue_while","The Golden Hotel"),("Yeti or Knot Events","planner_collab"),"Best photo spots at Evergreen Lake House, all seasons","",[("Apply for The Wedding Gathering, Denver, 28 Feb","show_ask",""),("Optional: Mighty Argo (new)","venue_new","Mighty Argo")]),
 (("Table Mountain Inn: “It’s Been a While” email and your Table Mountain Inn post","venue_while","Table Mountain Inn"),("TeeLee Floral and Events","planner_collab"),"Trial Reel: a wedding day in 30 seconds","The second Boettcher Mansion wedding from this year",[]),
 (("Headwaters Center: send your newest post and photos of their space","venue_newpost","Headwaters Center"),("Flora Moon Events","planner_collab"),"A Fossil Trace wedding (collab: TeeLee)","",[("Ask Hudson Gardens about its March showcase","show_ask",""),("Warm contact: the DJ at Quality Mobile Sound","warm","")]),
 (("Evergreen Lake House: newest post, confirm the spring showcase","venue_showcase","Evergreen Lake House"),("KM Flowers & Events","planner_note"),"A Mount Vernon wedding (collab: Exquisite Events)","Boettcher Mansion Wedding Guide",[("Monthly check (1 Feb)",None,"")]),
 (("Baldoria on the Water: ask for the next open house date","show_ask","Baldoria on the Water"),("Kaitlin Shea Weddings","planner_note"),"Florals and details from three weddings (collab: florists)","",[("Warm contact: Denver Botanic Gardens follow-up","warm",""),("Optional: The Manor House (new)","venue_new","The Manor House")]),
 (("The Vista at Applewood: newest post and brochures","venue_newpost","The Vista at Applewood"),("Mag Events","planner_collab"),"Meet the photographer: how Kevin works","Another wedding with no post yet",[("Anniversary emails to spring 2026 couples","anniversary","")]),
 (("Mount Vernon Canyon Club: brochures and a spring hello","venue_brochures","Mount Vernon Canyon Club"),("Harper Bond Events","planner_collab"),"An Evergreen Lake House wedding (collab: Flora Moon or Paige Lane)","",[("Golden Wedding Show (late Feb, confirm date)",None,""),("The Wedding Gathering, 28 Feb",None,"")]),
 (("The Golden Hotel: brochures, ask about their list","venue_brochures","The Golden Hotel"),("Paige Lane Designs","planner_collab"),"Planning tip: spring weather in Colorado","What to Ask Before You Book a Wedding Photographer",[("Monthly check (1 Mar)",None,"")]),
 (("Table Mountain Inn: brochures, ask about the Golden Wedding Show","venue_brochures","Table Mountain Inn"),("Exquisite Events & Productions","planner_collab"),"A Headwaters Center wedding (collab: Mag Events)","",[("Optional: Red Rocks Park","venue_new","Red Rocks Park")]),
 (("Headwaters Center: spring check-in and brochures","venue_brochures","Headwaters Center"),("A new planner a venue told you about","planner_new"),"Announce spring mini engagement sessions","Spring Weddings in Colorado: Weather and Light",[("Set spring mini session dates",None,"")]),
 (("Evergreen Lake House: pack for the spring showcase","venue_showcase","Evergreen Lake House"),("Islagant Co. Events & Design","planner_collab"),"Trial Reel: getting ready, behind the scenes","",[("Pack for the showcase (Clients tab checklist)",None,"")]),
 (("Baldoria on the Water: spring check-in","venue_brochures","Baldoria on the Water"),("Yeti or Knot Events","planner_note"),"Share the Headwaters guide post","Headwaters Center Wedding Guide",[("Evergreen Lake House spring showcase (late Mar or early Apr)",None,""),("Monthly check (1 Apr)",None,"")]),
 (("The Vista at Applewood: spring check-in","venue_brochures","The Vista at Applewood"),("Flora Moon Events","planner_note"),"A Red Rocks wedding","",[("Optional: Willow Ridge Manor (new)","venue_new","Willow Ridge Manor")]),
 (("Mount Vernon Canyon Club: share a new wedding","venue_newpost","Mount Vernon Canyon Club"),("TeeLee Floral and Events","planner_note"),"Why we’ve never sent a substitute","Why We’ve Never Sent a Substitute Photographer",[("Warm contacts: Denver Botanic Gardens, Blackstone, the library","warm","")]),
 (("The Golden Hotel: share a new wedding","venue_newpost","The Golden Hotel"),("Mag Events","planner_note"),"A Baldoria on the Water wedding","",[]),
 (("Table Mountain Inn: share a new wedding","venue_newpost","Table Mountain Inn"),("A new planner a venue told you about","planner_new"),"Your first spring wedding (collab: all vendors)","Your first spring 2027 wedding",[("Monthly check (1 May)",None,"")]),
 (("Headwaters Center: share a new wedding","venue_newpost","Headwaters Center"),("Paige Lane Designs","planner_note"),"Engagement session favorites (only one, then back to weddings)","",[("Anniversary emails to summer 2026 couples","anniversary",""),("Optional: Christies of Genesee open house","venue_new","Christies of Genesee")]),
 (("Evergreen Lake House: share your newest post","venue_newpost","Evergreen Lake House"),("Harper Bond Events","planner_note"),"Evergreen Lake House through the seasons","Evergreen Lake House Through the Seasons",[]),
 (("Baldoria on the Water: share a new wedding","venue_newpost","Baldoria on the Water"),("Exquisite Events & Productions","planner_note"),"A caterer collab: setups from three weddings","",[]),
 (("The Vista at Applewood: share a new wedding","venue_newpost","The Vista at Applewood"),("A new planner a venue told you about","planner_new"),"Your newest real wedding (collab)","Your newest real wedding",[]),
]
W.insert(0,(("Catch-up week: finish the Do These First list on the Start page","drafts",""),("Send the planner notes in your Gmail Drafts","drafts"),"Nothing new. Delete and repost the Baldoria post if you haven’t yet.","",[("Website edits with Claude in Squarespace",None,""),("Fix Zola and The Knot",None,"")]))
W[0][4].insert(0,("Monday: Facebook holiday card mini post in Golden Colorado Neighbors and Friends","fb_holiday",""))
start=datetime.date(2026,11,30)
def lbl(d): return f"{d.day} {d.strftime('%b')}"
def pop(key,fill="",kind="venue"):
    if not key: return ""
    attr=f' data-fill-{kind}="{H.escape(fill,quote=True)}"' if fill else ""
    return f'<span class="pop" data-script="{key}"{attr}></span>'
data=[];rows=[]
for i,(v,p,ig,blog,also) in enumerate(W):
    d=start+datetime.timedelta(days=7*i)
    data.append({"start":d.isoformat(),"label":lbl(d),"venue":v[0],"venueKey":v[1],"venueName":v[2],"planner":p[0],"plannerKey":p[1],"ig":ig,"blog":blog,"also":[{"text":a[0],"key":a[1],"fill":a[2]} for a in also]})
    alsocell="".join(f'<div class="also">{H.escape(a[0])}{pop(a[1],a[2])}</div>' for a in also)
    rows.append(f'<tr data-week="{d.isoformat()}"><td>{lbl(d)}</td><td>{H.escape(v[0])}{pop(v[1],v[2])}</td><td>{H.escape(p[0])}{pop(p[1],p[0] if p[1]!="planner_new" else "","planner")}</td><td>{H.escape(ig)}</td><td>{H.escape(blog)}</td><td>{alsocell}</td></tr>')
import os,pathlib
SRC=pathlib.Path(__file__).resolve().parent
OUT=pathlib.Path(os.environ.get('BB_OUT', SRC.parents[1]/'bergberg'))
open(OUT/'weeks.js','w').write("/* Generated from cal.py. One entry per week. */\nwindow.BB_WEEKS="+json.dumps(data,ensure_ascii=False,indent=0)+";\n")
open(SRC/'cal_rows.html','w').write("\n".join(rows))
# Splice the rows into calendar.html so the Calendar tab matches weeks.js
cp=SRC/'calendar.html'; ch=cp.read_text(encoding='utf-8')
a=ch.find('<tr data-week='); b=ch.rfind('</tr>',0,ch.find('</tbody>',a))+5
cp.write_text(ch[:a]+"\n".join(rows)+ch[b:],encoding='utf-8')
print(len(W))
