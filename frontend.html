<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Tamil Nadu College Enquiry Chatbot</title>

<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',sans-serif}

body{
 height:100vh;
 background:linear-gradient(135deg,#667eea,#764ba2);
 display:flex;justify-content:center;align-items:center
}

#splash{
 position:absolute;width:100%;height:100%;
 background:linear-gradient(135deg,#4a47a3,#2c2a6b);
 display:flex;flex-direction:column;justify-content:center;align-items:center;
 color:#fff;z-index:10;
 animation:fadeOut 1s ease forwards;animation-delay:2.5s
}

.loader{
 margin-top:30px;width:50px;height:50px;
 border:5px solid rgba(255,255,255,.3);
 border-top:5px solid #fff;border-radius:50%;
 animation:spin 1s linear infinite
}

.app{
 width:420px;height:640px;background:#fff;border-radius:20px;
 box-shadow:0 25px 50px rgba(0,0,0,.35);
 display:flex;flex-direction:column;overflow:hidden;
 opacity:0;animation:showApp 1s ease forwards;animation-delay:3s;
 position:relative
}

.header{
 background:#4a47a3;color:#fff;padding:18px;text-align:center
}

.icon-bar{
 background:#fff;
 display:flex;
 justify-content:space-between;
 padding:10px 18px;
}

.icon{font-size:18px;cursor:pointer}

.chat{
 flex:1;
 background:#fff;
 padding:15px;
 overflow-y:auto;
 display:flex;
 flex-direction:column;
 position:relative
}

.intro{
 position:absolute;
 top:50%;left:50%;
 transform:translate(-50%,-50%);
 color:#999;
 font-size:15px;
 text-align:center;
 pointer-events:none;
 transition:opacity 0.8s ease;
}
.intro.hide{opacity:0}

.msg{
 max-width:78%;
 padding:12px 16px;
 border-radius:20px;
 font-size:14px;
 margin-bottom:4px;
 white-space:pre-line
}
.bot{background:#f0f0ff;align-self:flex-start}
.user{background:#4a47a3;color:#fff;align-self:flex-end}
.time{font-size:10px;opacity:.5;margin-bottom:10px}

.typing{font-size:20px;padding:10px;opacity:.6}

.input-area{
 display:flex;border-top:1px solid #ddd
}
.input-area input{
 flex:1;padding:15px;border:none;outline:none
}
.input-area button{
 background:#4a47a3;color:#fff;border:none;
 padding:0 25px;cursor:pointer
}

.panel{
 position:absolute;top:0;bottom:0;width:260px;
 background:#fff;box-shadow:0 0 20px rgba(0,0,0,.3);
 z-index:20;padding:20px;display:none
}
.settings-panel{left:0}
.history-panel{right:0}
.panel h3{margin-bottom:15px;color:#4a47a3}
.panel button{
 width:100%;padding:10px;margin-bottom:10px;
 border:none;border-radius:8px;cursor:pointer;
 background:#4a47a3;color:#fff
}
.close-btn{background:#999}

@keyframes spin{to{transform:rotate(360deg)}}
@keyframes fadeOut{to{opacity:0;visibility:hidden}}
@keyframes showApp{to{opacity:1}}
</style>
</head>

<body>

<div id="splash">
 <h1>🎓 TN College Bot</h1>
 <p>Smart College Information Assistant</p>
 <div class="loader"></div>
</div>

<div class="app">

 <div class="header">
  <h2>Tamil Nadu College Enquiry</h2>
 </div>

 <div class="icon-bar">
  <span class="icon" onclick="openSettings()">⚙️</span>
  <span class="icon" onclick="openHistory()">⏰</span>
 </div>

 <div class="chat" id="chatBox">
  <div class="intro" id="introText">How can I help you?</div>
 </div>

 <div class="input-area">
  <input id="input" placeholder="Type a college name or question...">
  <button onclick="send()">Send</button>
 </div>

 <div class="panel settings-panel" id="settingsPanel">
  <h3>Settings</h3>
  <button onclick="clearChat()">Clear Chat</button>
  <button class="close-btn" onclick="closePanels()">Close</button>
 </div>

 <div class="panel history-panel" id="historyPanel">
  <h3>Chat History</h3>
  <div id="historyContent" style="font-size:13px;line-height:1.6"></div>
  <button class="close-btn" onclick="closePanels()">Close</button>
 </div>

</div>

<script>
const chat=document.getElementById("chatBox");
const intro=document.getElementById("introText");
const input=document.getElementById("input");
const historyContent=document.getElementById("historyContent");
let chatHistory=[];
let currentCollege=null;

/* ENTER KEY */
input.addEventListener("keydown",e=>{
 if(e.key==="Enter") send();
});

/* ===== COLLEGE DATA (ONLY THIS PART ADDED) ===== */
const colleges = {
 "anna university":{name:"Anna University, Chennai",response:`Anna University is a premier public technical university located in Chennai.
It offers undergraduate, postgraduate, and doctoral programs across engineering, technology, management, and applied sciences.
The university is known for its academic reputation, research focus, and strong placement ecosystem through affiliated institutions.`,courses:"B.E, B.Tech, M.E, M.Tech, MBA, MCA",fees:"Government-regulated fee structure",hostel:"Hostel facilities available in campus",transport:"Limited internal transport",placements:"Strong placements through university and affiliated colleges",location:"Chennai"},

 "srm":{name:"SRM Institute of Science and Technology",response:`SRM Institute of Science and Technology is a private deemed university with a large residential campus.
It offers programs in engineering, medicine, management, law, and sciences.
The institution is known for modern infrastructure, diverse student community, and consistent placement opportunities.`,courses:"Engineering, Medicine, Management, Law",fees:"Varies by program and category",hostel:"AC and non-AC hostels available",transport:"University bus transport available",placements:"Recruiters include multinational IT and core companies",location:"Kattankulathur"},

 "vit":{name:"VIT University, Vellore",response:`VIT University is a private deemed university known for outcome-based education and global exposure.
It offers a wide range of undergraduate and postgraduate programs with strong emphasis on research, innovation, and placements.`,courses:"Engineering, Science, Management",fees:"Program-wise fee structure",hostel:"Well-established residential facilities",transport:"Campus and city connectivity",placements:"Excellent placement record with national and international offers",location:"Vellore"},

 "psg":{name:"PSG College of Technology, Coimbatore",response:`PSG College of Technology is an autonomous engineering institution located in Coimbatore.
The college is widely respected for academic discipline, strong faculty base, and consistent performance in core and IT placements.
It offers a balanced campus environment with academic excellence and industry interaction.`,courses:"Engineering & Applied Sciences",fees:"Merit-based and regulated fee structure",hostel:"On-campus hostel facilities",transport:"Good city connectivity",placements:"Strong placement support with core and IT companies",location:"Coimbatore"},

 "amrita":{name:"Amrita Vishwa Vidyapeetham, Coimbatore",response:`Amrita Vishwa Vidyapeetham is a deemed-to-be university with a large residential campus in Coimbatore.
It is well known for its disciplined academic environment, research-driven programs, and value-based education.
The institution offers a wide range of engineering and science programs with strong industry collaboration.`,courses:"B.Tech, M.Tech, MCA, MSc, PhD",fees:"Fee structure varies by program and category",hostel:"Separate hostels for boys and girls with full facilities",transport:"University transport available",placements:"Consistent placements with core, IT, and research organizations",location:"Coimbatore"},

 "karunya":{name:"Karunya Institute of Technology and Sciences",response:`Karunya Institute of Technology and Sciences is a deemed university located in a scenic campus near Coimbatore.
It focuses on engineering, sciences, and value-based higher education with modern infrastructure and research centers.`,courses:"B.Tech, M.Tech, MSc, PhD",fees:"Program-wise institutional fee structure",hostel:"Residential hostels available on campus",transport:"College bus services available",placements:"Good placement support in IT and core sectors",location:"Coimbatore"},

 "psgcas":{name:"PSG College of Arts and Science",response:`PSG College of Arts and Science is an autonomous institution affiliated with Bharathiar University.
It offers a wide range of undergraduate and postgraduate programs in arts, science, commerce, and management.`,courses:"BA, BSc, BCom, BBA, MSc, MCom",fees:"Autonomous college fee structure",hostel:"Hostel facilities available",transport:"Good city connectivity",placements:"Placement cell supports arts and science students",location:"Coimbatore"},

 "skasc":{name:"Sri Krishna Arts and Science College",response:`Sri Krishna Arts and Science College is an autonomous institution known for academic excellence and campus discipline.
It offers diverse programs in arts, science, commerce, and management with industry-oriented learning.`,courses:"BSc, BCom, BBA, MSc, MBA",fees:"Institutional fee structure varies by program",hostel:"Separate hostels available",transport:"College transport facilities available",placements:"Active placement training and recruitment support",location:"Coimbatore"},

 "dr ngp":{name:"Dr. N.G.P. Arts and Science College",response:`Dr. N.G.P. Arts and Science College is an autonomous institution offering quality education in arts, science, and commerce.
The college emphasizes skill development, research exposure, and holistic student growth.`,courses:"BSc, BCom, BCA, MSc, MCom",fees:"Program-specific institutional fees",hostel:"Hostel facilities available",transport:"College bus transport provided",placements:"Dedicated placement cell with regular drives",location:"Coimbatore"},

 "rathinam":{name:"Rathinam College of Arts and Science",response:`Rathinam College of Arts and Science is a self-financing autonomous college located in Coimbatore.
It offers career-oriented programs with focus on employability, innovation, and industry interaction.`,courses:"BSc, BCA, BCom, MBA, MSc",fees:"Institutional fee structure",hostel:"Hostel facilities available",transport:"College transport services available",placements:"Placement support through industry partnerships",location:"Coimbatore"}
};

/* CHAT LOGIC (UNCHANGED) */
function send(){
 const text=input.value.trim().toLowerCase();
 if(!text) return;

 intro.classList.add("hide");

 addMsg(input.value,"user");
 chatHistory.push("🧑 "+input.value);
 input.value="";

 showTyping();

 setTimeout(()=>{
  let reply="Sorry, I couldn't find details for that.";
  for(let key in colleges){
   if(text.includes(key)){
    const c=colleges[key];
    reply=c.response;
    if(text.includes("fees")) reply=c.fees;
    else if(text.includes("course")) reply=c.courses;
    else if(text.includes("hostel")) reply=c.hostel;
    else if(text.includes("placement")) reply=c.placements;
    else if(text.includes("transport")) reply=c.transport;
    else if(text.includes("location")) reply=c.location;
    break;
   }
  }
  removeTyping();
  addMsg(reply,"bot");
  chatHistory.push("🤖 "+reply);
 },500);
}

function showTyping(){
 const t=document.createElement("div");
 t.className="typing bot";
 t.id="typing";
 t.innerText="...";
 chat.appendChild(t);
 chat.scrollTop=chat.scrollHeight;
}
function removeTyping(){
 const t=document.getElementById("typing");
 if(t) t.remove();
}
function addMsg(text,type){
 const msg=document.createElement("div");
 msg.className="msg "+type;
 msg.innerText=text;
 chat.appendChild(msg);

 const time=document.createElement("div");
 time.className="time";
 time.innerText=new Date().toLocaleTimeString();
 chat.appendChild(time);

 chat.scrollTop=chat.scrollHeight;
}

function openSettings(){closePanels();settingsPanel.style.display="block";}
function openHistory(){closePanels();historyContent.innerHTML=chatHistory.join("<br><br>");historyPanel.style.display="block";}
function closePanels(){settingsPanel.style.display="none";historyPanel.style.display="none";}
function clearChat(){chat.innerHTML='<div class="intro" id="introText">How can I help you?</div>';chatHistory=[];closePanels();}
</script>

</body>
</html>