 /************ Swanalekha code ends here **********************/
var pattern=null;
var tabCount=1;
function bindSwanalekha(widget){

if(widget.aBound){ 
widget.aBound=false;
disable();
return;  
}

var A={
a:'அ',
A:'ஆ',
i:'இ',
I:'ஈ',
u:'உ',
U:'ஊ',
e:'எ',
E:'ஏ',
o:'ஒ',
O:'ஓ',
q:'ஃ',
aa:'ஆ',
ii:'ஈ',
uu:'ஊ',
ee:'ஏ',
oo:'ஓ',
ai:'ஐ',
au:'ஔ',
k:'க்',
ka:'க',
kaa:'கா',
kA:'கா',
ki:'கி',
kii:'கீ',
kI:'கீ',
ku:'கு',
kuu:'கூ',
kU:'கூ',
ke:'கெ',
kee:'கே',
kE:'கே',
kai:'கை',
ko:'கொ',
koo:'கோ',
kO:'கோ',
kau:'கௌ',
ng:'ங்',
nga:'ங',
ngaa:'ஙா',
ngA:'ஙா',
ngi:'ஙி',
ngii:'ஙீ',
ngI:'ஙீ',
ngu:'ஙு',
nguu:'ஙூ',
ngU:'ஙூ',
nge:'ஙெ',
ngee:'ஙே',
ngE:'ஙே',
ngai:'ஙை',
ngo:'ஙொ',
ngoo:'ஙோ',
ngO:'ஙோ',
ngau:'ஙௌ',
c:'ச்',
ca:'ச',
caa:'சா',
cA:'சா',
ci:'சி',
cii:'சீ',
cI:'சீ',
cu:'சு',
cuu:'சூ',
cU:'சூ',
ce:'செ',
cee:'சே',
cE:'சே',
cai:'சை',
co:'சொ',
coo:'சோ',
cO:'சோ',
cau:'சௌ',
nj:'ஞ்',
nja:'ஞ',
njaa:'ஞா',
njA:'ஞா',
nji:'ஞி',
njii:'ஞீ',
njI:'ஞீ',
nju:'ஞு',
njuu:'ஞூ',
njU:'ஞூ',
nje:'ஞெ',
njee:'ஞே',
njE:'ஞே',
njai:'ஞை',
njo:'ஞொ',
njoo:'ஞோ',
njO:'ஞோ',
njau:'ஞௌ',
t:'ட்',
ta:'ட',
taa:'டா',
tA:'டா',
ti:'டி',
tii:'டீ',
tI:'டீ',
tu:'டு',
tuu:'டூ',
tU:'டூ',
te:'டெ',
tee:'டே',
tE:'டே',
tai:'டை',
to:'டொ',
too:'டோ',
tO:'டோ',
tau:'டௌ',
d:'ட்',
da:'ட',
daa:'டா',
dA:'டா',
di:'டி',
dii:'டீ',
dI:'டீ',
du:'டு',
duu:'டூ',
dU:'டூ',
de:'டெ',
dee:'டே',
dE:'டே',
dai:'டை',
'do':'டொ',
doo:'டோ',
dO:'டோ',
dau:'டௌ',
N:'ண்',
Na:'ண',
Naa:'ணா',
NA:'ணா',
Ni:'ணி',
Nii:'ணீ',
NI:'ணீ',
Nu:'ணு',
Nuu:'ணூ',
NU:'ணூ',
Ne:'ணெ',
Nee:'ணே',
NE:'ணே',
Nai:'ணை',
No:'ணொ',
Noo:'ணோ',
NO:'ணோ',
Nau:'ணௌ',
th:'த்',
tha:'த',
thaa:'தா',
thA:'தா',
thi:'தி',
thii:'தீ',
thI:'தீ',
thu:'து',
thuu:'தூ',
thU:'தூ',
the:'தெ',
thee:'தே',
thE:'தே',
thai:'தை',
tho:'தொ',
thoo:'தோ',
thO:'தோ',
thau:'தௌ',
w:'ந்',
wa:'ந',
waa:'நா',
wA:'நா',
wi:'நி',
wii:'நீ',
wI:'நீ',
wu:'நு',
wuu:'நூ',
wU:'நூ',
we:'நெ',
wee:'நே',
wE:'நே',
wai:'நை',
wo:'நொ',
woo:'நோ',
wO:'நோ',
wau:'நௌ',
w:'ந்',
wa:'ந',
waa:'நா',
wA:'நா',
wi:'நி',
wii:'நீ',
wI:'நீ',
wu:'நு',
wuu:'நூ',
wU:'நூ',
we:'நெ',
wee:'நே',
wE:'நே',
wai:'நை',
wo:'நொ',
woo:'நோ',
wO:'நோ',
wau:'நௌ',
p:'ப்',
pa:'ப',
paa:'பா',
pA:'பா',
pi:'பி',
pii:'பீ',
pI:'பீ',
pu:'பு',
puu:'பூ',
pU:'பூ',
pe:'பெ',
pee:'பே',
pE:'பே',
pai:'பை',
po:'பொ',
poo:'போ',
pO:'போ',
pau:'பௌ',
m:'ம்',
ma:'ம',
maa:'மா',
mA:'மா',
mi:'மி',
mii:'மீ',
mI:'மீ',
mu:'மு',
muu:'மூ',
mU:'மூ',
me:'மெ',
mee:'மே',
mE:'மே',
mai:'மை',
mo:'மொ',
moo:'மோ',
mO:'மோ',
mau:'மௌ',
y:'ய்',
ya:'ய',
yaa:'யா',
yA:'யா',
yi:'யி',
yii:'யீ',
yI:'யீ',
yu:'யு',
yuu:'யூ',
yU:'யூ',
ye:'யெ',
yee:'யே',
yE:'யே',
yai:'யை',
yo:'யொ',
yoo:'யோ',
yO:'யோ',
yau:'யௌ',
r:'ர்',
ra:'ர',
raa:'ரா',
rA:'ரா',
ri:'ரி',
rii:'ரீ',
rI:'ரீ',
ru:'ரு',
ruu:'ரூ',
rU:'ரூ',
re:'ரெ',
ree:'ரே',
rE:'ரே',
rai:'ரை',
ro:'ரொ',
roo:'ரோ',
rO:'ரோ',
rau:'ரௌ',
l:'ல்',
la:'ல',
laa:'லா',
lA:'லா',
li:'லி',
lii:'லீ',
lI:'லீ',
lu:'லு',
luu:'லூ',
lU:'லூ',
le:'லெ',
lee:'லே',
lE:'லே',
lai:'லை',
lo:'லொ',
loo:'லோ',
lO:'லோ',
lau:'லௌ',
v:'வ்',
va:'வ',
vaa:'வா',
vA:'வா',
vi:'வி',
vii:'வீ',
vI:'வீ',
vu:'வு',
vuu:'வூ',
vU:'வூ',
ve:'வெ',
vee:'வே',
vE:'வே',
vai:'வை',
vo:'வொ',
voo:'வோ',
vO:'வோ',
vau:'வௌ',
z:'ழ்',
za:'ழ',
zaa:'ழா',
zA:'ழா',
zi:'ழி',
zii:'ழீ',
zI:'ழீ',
zu:'ழு',
zuu:'ழூ',
zU:'ழூ',
ze:'ழெ',
zee:'ழே',
zE:'ழே',
zai:'ழை',
zo:'ழொ',
zoo:'ழோ',
zO:'ழோ',
zau:'ழௌ',
L:'ள்',
La:'ள',
Laa:'ளா',
LA:'ளா',
Li:'ளி',
Lii:'ளீ',
LI:'ளீ',
Lu:'ளு',
Luu:'ளூ',
LU:'ளூ',
Le:'ளெ',
Lee:'ளே',
LE:'ளே',
Lai:'ளை',
Lo:'ளொ',
Loo:'ளோ',
LO:'ளோ',
Lau:'ளௌ',
R:'ற்',
Ra:'ற',
Raa:'றா',
RA:'றா',
Ri:'றி',
Rii:'றீ',
RI:'றீ',
Ru:'று',
Ruu:'றூ',
RU:'றூ',
Re:'றெ',
Ree:'றே',
RE:'றே',
Rai:'றை',
Ro:'றொ',
Roo:'றோ',
RO:'றோ',
Rau:'றௌ',
n:'ன்',
na:'ன',
naa:'னா',
nA:'னா',
ni:'னி',
nii:'னீ',
nI:'னீ',
nu:'னு',
nuu:'னூ',
nU:'னூ',
ne:'னெ',
nee:'னே',
nE:'னே',
nai:'னை',
no:'னொ',
noo:'னோ',
nO:'னோ',
nau:'னௌ',
j:'ஜ்',
ja:'ஜ',
jaa:'ஜா',
jA:'ஜா',
ji:'ஜி',
jii:'ஜீ',
jI:'ஜீ',
ju:'ஜு',
juu:'ஜூ',
jU:'ஜூ',
je:'ஜெ',
jee:'ஜே',
jE:'ஜே',
jai:'ஜை',
jo:'ஜொ',
joo:'ஜோ',
jO:'ஜோ',
jau:'ஜௌ',
sh:'ஷ்',
sha:'ஷ',
shaa:'ஷா',
shA:'ஷா',
shi:'ஷி',
shii:'ஷீ',
shI:'ஷீ',
shu:'ஷு',
shuu:'ஷூ',
shU:'ஷூ',
she:'ஷெ',
shee:'ஷே',
shE:'ஷே',
shai:'ஷை',
sho:'ஷொ',
shoo:'ஷோ',
shO:'ஷோ',
shau:'ஷௌ',
sr:'ஸ்ர்',
sri:'ஸ்ரீ',
s:'ஸ்',
sa:'ஸ',
saa:'ஸா',
sA:'ஸா',
si:'ஸி',
sii:'ஸீ',
sI:'ஸீ',
su:'ஸு',
suu:'ஸூ',
sU:'ஸூ',
se:'ஸெ',
see:'ஸே',
sE:'ஸே',
sai:'ஸை',
so:'ஸொ',
soo:'ஸோ',
sO:'ஸோ',
sau:'ஸௌ',
h:'ஹ்',
ha:'ஹ',
haa:'ஹா',
hA:'ஹா',
hi:'ஹி',
hii:'ஹீ',
hI:'ஹீ',
hu:'ஹு',
huu:'ஹூ',
hU:'ஹூ',
he:'ஹெ',
hee:'ஹே',
hE:'ஹே',
hai:'ஹை',
ho:'ஹொ',
hoo:'ஹோ',
hO:'ஹோ',
hau:'ஹௌ',
ksh:'க்ஷ்',
ksha:'க்ஷ',
kshaa:'க்ஷா',
kshA:'க்ஷா',
kshi:'க்ஷி'

};
function isToggleEvent(event){
 event = (event) ? event : window.event;
  kCode = event.keyCode || event.which; 
  return   ((event.keyCode == 13 && event.ctrlKey) || (event.which == 109 && event.ctrlKey));
};
function enable(){
/*widget.style.background='#eef';*/
widget.onkeypress=keypressEnabled;
widget.style.outline = 'dashed 1px red';
};
function disable(){
widget.style.background='white';
widget.onkeypress=keypressDisabled;
widget.style.outline = null;

};
function checkBoxListener(){
	if(widget.aBound){
		widget.aBound=false;
		disable();
	 }	
else{
		widget.aBound=true;
		enable();
	}
}
function isExplorer() {
  return (document.selection != undefined && document.selection.createRange().isEqual != undefined);
}
// compare positions
function positionIsEqual(other) {
    if (isExplorer())
        return this.position.isEqual(other.position);
    else
        return this.position == other.position;
  
}

function Position(node) {
  if (node.selectionStart != undefined)
    this.position = node.selectionStart;
  else if (document.selection && document.selection.createRange())
    this.position = document.selection.createRange();
    
  this.isEqual = positionIsEqual;
}
function keypressEnabled(event){
 
	if (event == undefined)
		event = window.event;
	if(isToggleEvent(event)){
		disable();
		document.getElementById("toggle").checked = false;
		return;
	}
	kCode = event.keyCode || event.which; 
 
	if ( kCode  == 8) {
		if(pattern.indexOf('a')>=0 || pattern.indexOf('A')>=0 || pattern.indexOf('e')>=0 || pattern.indexOf('E')>=0 || pattern.indexOf('i')>=0 || pattern.indexOf('I')>=0 || pattern.indexOf('o')>=0 || pattern.indexOf('O')>=0 || pattern.indexOf('u')>=0 || pattern.indexOf('U')>=0|| pattern.indexOf('1')>=0 || pattern.indexOf('2')>=0 || pattern.indexOf('3')>=0 || pattern.indexOf('4')>=0 || pattern.indexOf('5')>=0 || pattern.indexOf('6')>=0 || pattern.indexOf('7')>=0 || pattern.indexOf('8')>=0 || pattern.indexOf('9')>=0  ){
			pattern=pattern.replace('a','');
			pattern=pattern.replace('a',''); 
			pattern=pattern.replace('A','');
			pattern=pattern.replace('e','');
			pattern=pattern.replace('e','');
			pattern= pattern.replace('E','');
			pattern= pattern.replace('i','');
			pattern= pattern.replace('i','');
			pattern= pattern.replace('I','');
			pattern= pattern.replace('o','');
			pattern= pattern.replace('o','');
			pattern= pattern.replace('O','');
			pattern= pattern.replace('u','');
			pattern= pattern.replace('u','');
			pattern= pattern.replace('U','');
			pattern= pattern.replace('1','');
			pattern= pattern.replace('2','');
			pattern= pattern.replace('3','');
			pattern= pattern.replace('4','');
			pattern= pattern.replace('5','');
			pattern= pattern.replace('6','');
			pattern= pattern.replace('7','');
			pattern= pattern.replace('8','');
			pattern= pattern.replace('9','');
			tabCount=1;
			return;
		}
	}
	if(event.ctrlKey||event. altKey||event.metaKey){
		return true;
	}
	var char=String.fromCharCode(kCode );
	var pos=widget.selectionStart;
	if( kCode ==9){ /*Tab key*/
		tabCount++;
		if(pattern!=null || pattern!=''){
			if(tabCount==2){
				pattern=pattern+tabCount;
			}
			else{
				if(A[pattern.substring(0, pattern.length-1)+tabCount]){ 
						pattern=pattern.substring(0, pattern.length-1)+tabCount;
				}
				else{
						tabCount=1;
						pattern=pattern.substring(0, pattern.length-1);
					}
			}
		}
	}
	else{
		pattern=pattern+char; 
	}
	if(pattern.length > 5){ 
		pattern='';
		tabCount=1;
	}
	var mal=A[pattern];
	if(!mal) {
		pattern=char;
		tabCount=1;
		patternStart=widget.selectionStart;
		var mal=A[pattern];
	}
	if(mal){
			if (isExplorer()) {
				var range = document.selection.createRange();
				var stepback=  range-patternStart;
				range.moveStart("character", -stepback);
				range.text = mal;
				range.collapse(false);
				range.select();
				return false;
 		   	}
			else {
				var scrollTop = widget.scrollTop;
				var cursorLoc =  widget.selectionStart;
				var stepback=  cursorLoc-patternStart;
				widget.value=  widget.value.substr(0,patternStart)+mal+widget.value.substr(widget.selectionEnd,widget.value.length); 
				widget.scrollTop=scrollTop ;
				widget.selectionStart = cursorLoc + mal.length  - stepback  ;
				widget.selectionEnd = cursorLoc + mal.length - stepback;
				return false;
	}
	}
	if( kCode ==9){
		return false;
	}
	return true;
};
function keypressDisabled(event){
if(isToggleEvent(event)){
enable();
document.getElementById("toggle").checked = true;
return false;
}
return true;
};
widget.aBound=false;
disable();
var checkbox = document.getElementById("toggle");
if (checkbox.addEventListener) 
                checkbox.addEventListener("click", checkBoxListener,false);
else if (checkbox.attachEvent) 
                checkbox.attachEvent("onclick", checkBoxListener);
};
 function addCheckbox(textBox) {
            if(textBox==null) return;
            try
            {
			var searchBox= document.getElementById("searchInput");
            var element = document.createElement("input");
            element.setAttribute("type","checkbox");
            element.setAttribute("id","toggle");
            var labelcheckBox = document.createTextNode(' Transliterate - Use Ctrl + M to Toggle.');
            textBox.parentNode.insertBefore(element,textBox);
            if(searchBox) searchBox.parentNode.insertBefore(element,searchBox);
           /*  textBox.insertBefore(element,textBox);*/
            document.getElementById("toggle").checked = textBox.aBound;
            textBox.parentNode.insertBefore(labelcheckBox,textBox);
           if(searchBox)  searchBox.parentNode.insertBefore(labelcheckBox,searchBox);
            var p = document.createElement("p");
            p.setAttribute("style","width:100%;height:1px;");
            textBox.parentNode.insertBefore(p,textBox);
            if(searchBox) searchBox.parentNode.insertBefore(p,searchBox);
             }
             catch(ex)
             {
              alert(ex);
             }
}
function bindAllTextElements() {
	
	var ta=document.getElementsByTagName('textarea');
 
	for(var i=0;i < ta.length;++i){
		addCheckbox(ta[i]);
		bindSwanalekha(ta[i]);
	}
	var tb=document.getElementsByTagName('input');
	for(var i=0;i < tb.length;++i){	
	 type = tb[i].getAttribute('type'); 	
		if ( type == 'text' || type == null) { 
			bindSwanalekha(tb[i]);
		}
	}	
	
	var ifs = document.getElementsByTagName('iframe');	
    var len=ifs.length;
	for (var i=0;i < len; i++) {		
		bindAllTextElements(ifs[i].contentDocument.documentElement);
	}
	
 };
function addLoadEvent(func) {
	 
            if (window.addEventListener) {
            	window.addEventListener("load", func, false);
			}
            else if (window.attachEvent) {
            	window.attachEvent("onload", func);
			}
}
 
addLoadEvent(bindAllTextElements);
/************ Swanalekha code ends here **********************/
