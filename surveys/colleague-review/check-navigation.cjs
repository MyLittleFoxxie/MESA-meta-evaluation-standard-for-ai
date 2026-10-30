// All network requests are served locally. No submission is sent.
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{const browser=await chromium.launch({executablePath:process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});try{
 const page=await browser.newPage({viewport:{width:1560,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.route('**/*',r=>r.fulfill({contentType:'text/html',body:fs.readFileSync(path.join(__dirname,'survey.html'),'utf8')}));await page.goto('https://survey.test/');
 const packet=JSON.parse(await page.locator('#packet').textContent());for(const [i,choice] of packet.choices.entries()){const guide=page.locator('.option-example').nth(i).locator('svg');assert.equal(await guide.getAttribute('aria-hidden'),'true');assert.equal(await guide.innerHTML(),await page.locator('#arc-1 .answers label').nth(i).locator('svg').innerHTML());}await page.locator('.answer-guide').locator('..').screenshot({path:'/tmp/mesa-answer-icons.png'});const why=packet.questions[17].example.why;for(const selector of ['#example-18','#arc-18 .example','#designqa-18 .example'])assert((await page.locator(selector).evaluate(e=>{const copy=e.cloneNode(true);copy.querySelectorAll('.term-icon').forEach(icon=>icon.remove());return copy.textContent;})).includes('Why: '+why));
 for(const label of ['Familiarity ratings','Survey answers','Feedback','Optional comments','Survey identifier','Fingerprint','Completion time','Organizer','FormSubmit']){
  const term=page.locator('#intro .submission-details [data-term="'+label+'"]');assert(await term.count()>=1);
  await term.first().scrollIntoViewIfNeeded();await term.first().click();assert((await page.locator('#term-tip').innerText()).includes(packet.definitions.find(d=>d.label===label).definition));await page.keyboard.press('Escape');
 }
 assert.equal(await page.locator('.reading [data-term="Survey answers"],.reading [data-term="Feedback"]').count(),0);
 assert(await page.locator('#back').isVisible());assert(await page.locator('#back').isDisabled());
 await page.evaluate(()=>{for(const q of packet.familiarity)draft.familiarity[q.id]=3;showStep(2);});
 for(const step of [2,3,6]){
  await page.evaluate(i=>{if(i===6){for(const q of packet.questions)draft.answers.arc[q.id].answer='Not sure';for(const q of packet.feedback)draft.feedback.arc.ratings[q.id]='Cannot judge';draft.completion.arc={status:'accepted',signature:signature('arc'),submission_id:crypto.randomUUID(),completed_at:new Date().toISOString()};}showStep(i);},step);const id=step===2?'example':step===3?'arc':'designqa';
  assert.equal(await page.locator('#sidebar-links [data-question-link]').count(),25);
  assert.equal(await page.locator('#sidebar-links li:has(>a[data-question-link])').evaluateAll(es=>new Set(es.map(e=>e.parentElement)).size),6);
  for(const q of [1,13,25]){
   const heading=page.locator(`#${id}-${q}-heading`);await page.locator(`#sidebar-links a[href="#${id}-${q}-heading"]`).click();
   await page.waitForTimeout(100);assert.equal(await page.evaluate(()=>document.activeElement.id),`${id}-${q}-heading`);
   assert.equal(await page.locator('#sidebar-links [aria-current]').count(),1);
   await page.locator(`#${id}-${q} .read-passage`).click();assert.equal(await page.locator('#return-question').innerText(),`Return to Q${q}`);
   await page.locator('#return-question').click();assert.equal(await page.evaluate(()=>document.activeElement.id),`${id}-${q}-heading`);
  }
  if(await page.locator(`#${id} .image-open`).count()){await page.locator(`#${id} .image-open`).click();assert(await page.locator('#image-viewer').evaluate(e=>e.open));await page.keyboard.press('Escape');assert(await page.locator(`#${id} .image-open`).evaluate(e=>e===document.activeElement));}
 }
 for(const label of ['Published','Claim','Evidence'])assert(await page.locator(`#designqa [data-term="${label}"]`).count()>0);
 for(const label of ['Comparison','Protection','Test materials','Methods','Situation','Repeatedly submitting results'])assert(await page.locator(`#designqa [data-term="${label}"]`).count()>0);
 assert(await page.locator('[data-term="Score"]').count()>0);for(const label of ['Original HLE','HLE-Diamond','HLE-Rolling','ARC-AGI-1','ARC-AGI-2','ARC Prize','DesignQA','Formula SAE','Private test set','Development problems','Verified evaluations','Temperature','Training-data marker','Expert disagreement'])assert(await page.locator('[data-term="'+label+'"]').count()>0,label);
 const t=page.locator('#designqa [data-term="Evidence"]').first();await t.focus();assert(await page.locator('#term-tip').evaluate(e=>e.matches(':popover-open')));await page.keyboard.press('Escape');
 for(const theme of ['light','dark']){
  await page.evaluate(v=>document.documentElement.dataset.theme=v,theme);await t.click();assert.equal(await page.locator('#term-tip').evaluate(e=>getComputedStyle(e).backgroundColor),theme==='light'?'rgb(230, 240, 250)':'rgb(41, 67, 84)');await page.screenshot({path:'/tmp/mesa-v27-popup-'+theme+'.png'});await page.keyboard.press('Escape');const colors=[];
  for(const choice of ['Yes','Partly','No','Not sure','Not applicable']){const radio=page.locator(`input[name="designqa-1"][value="${choice}"]`);await radio.check();colors.push(await radio.evaluate(e=>getComputedStyle(e.parentElement).backgroundColor));}
  assert.equal(new Set(colors).size,5);
  for(const width of [390,1560]){await page.setViewportSize({width,height:1000});await page.locator('#designqa-1').scrollIntoViewIfNeeded();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.screenshot({path:`/tmp/mesa-v27-${theme}-${width}.png`});}
 }
 await page.locator('#designqa-1-comments').fill('Preserve this comment');await page.locator('#designqa-1 .read-passage').click();await page.locator('#return-question').click();assert.equal(await page.locator('#designqa-1-comments').inputValue(),'Preserve this comment');
 await page.setViewportSize({width:390,height:844});await page.locator('#designqa-13 .read-passage').click();await page.locator('#return-question').click();await page.locator('#scroll-contents').click();assert(await page.locator('#contents [aria-current]').isVisible());await page.locator('#contents-links a[href="#designqa-25-heading"]').click();assert(!(await page.locator('#contents').evaluate(e=>e.open)));
 await page.setViewportSize({width:680,height:900});await page.evaluate(()=>document.documentElement.style.fontSize='32px');assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));assert(await page.evaluate(()=>{const a=document.querySelector('#scroll-context').getBoundingClientRect(),b=document.querySelector('#scroll-save').getBoundingClientRect();return a.right<=b.left||a.bottom<=b.top||b.bottom<=a.top;}));await page.screenshot({path:'/tmp/mesa-v27-enlarged.png'});
 await page.locator('#back').click();assert(await page.locator('#return-question').isHidden());assert.deepEqual(errors,[]);
 console.log('PASS: Contents hierarchy/current position, passage returns, persistent Back, definitions, image controls, answer colors, layouts and preserved comments.');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
