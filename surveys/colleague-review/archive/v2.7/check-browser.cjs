// Every delivery is intercepted; this test never sends email.
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{const browser=await chromium.launch({executablePath:process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});try{
 const html=fs.readFileSync(path.join(__dirname,'survey.html'),'utf8'),page=await browser.newPage({viewport:{width:1180,height:1000},reducedMotion:'reduce'}),sent=[],errors=[];let fail=true;
 page.on('pageerror',e=>errors.push(e.message));page.on('dialog',d=>d.accept());
 await page.route('https://survey.test/**',r=>r.fulfill({contentType:'text/html',body:html}));
 await page.route('https://formsubmit.co/**',r=>{sent.push(r.request().postDataJSON());return r.fulfill({status:fail?503:200,contentType:'application/json',body:JSON.stringify({success:!fail})});});
 await page.goto('https://survey.test/');
 const state=()=>page.evaluate(()=>JSON.parse(JSON.stringify(draft)));
 const step=()=>page.evaluate(()=>draft.step);
 async function notice(expected,p=page){await p.locator('#notice-dialog').waitFor({state:'visible'});assert((await p.locator('#notice-message').innerText()).includes(expected));await p.locator('#notice-close').click();await p.waitForFunction(()=>noticeTarget===null);}
 async function restore(button='#save'){
  const before=await state(),n=sent.length;await page.locator(button).click();assert((await page.locator('#draft-status').innerText()).includes('Draft saved'));
  await page.reload();await page.locator('#load').click();assert.deepEqual(await state(),before);if(before.completion[before.step===7?'designqa':'arc']?.status==='unconfirmed')await notice('previous delivery');assert.equal(sent.length,n);return before;
 }
 async function answers(id,start=1,end=25){for(let i=start;i<=end;i++)await page.locator(`input[name="${id}-${i}"][value="Not sure"]`).check();}
 async function feedback(){for(const id of ['understanding','choices','workload','review_understanding','confidence'])await page.locator(`input[name="feedback-${id}"][value="Cannot judge"]`).check();}
 assert.equal(await step(),0);assert.equal(await page.locator('input[type=radio]:checked').count(),0);assert(await page.locator('#back').isDisabled());await restore();
 await page.locator('#next').click();await page.locator('#next').click();assert.equal(await step(),1);await notice('familiarity');assert.equal(await page.evaluate(()=>document.activeElement.name),'familiarity-ai');
 await page.locator('input[name="familiarity-ai"][value="3"]').check();await restore();
 for(const id of ['benchmarks','scores'])await page.locator(`input[name="familiarity-${id}"][value="3"]`).check();await page.locator('#next').click();assert.equal(await step(),2);await restore();
 assert.equal(await page.locator('#example input').count(),0);assert.equal(await page.locator('.worked-answer').count(),25);
 await page.locator('#next').click();assert.equal(await step(),3);await page.locator('#next').click();assert.equal(await step(),3);await notice('25 remain unanswered');
 for(const nav of ['#contents-links','#sidebar-links']){assert.equal(await page.locator(nav+' [data-question-link]').first().evaluate(e=>e.firstChild.textContent),'Question 1');assert(await page.locator(nav+' .toc-check').first().isHidden());}
 await answers('arc',1,12);
 for(const nav of ['#contents-links','#sidebar-links']){assert.equal(await page.locator(nav+' [data-question-id="1"]').getAttribute('aria-label'),'Question 1, answered');assert.equal(await page.locator(nav+' .toc-check:not([hidden])').count(),12);}
 await page.locator('#arc-1 .clear').click();assert.equal(await page.locator('#sidebar-links .toc-check:not([hidden])').count(),11);await answers('arc',1,1);await page.locator('#arc-3-comments').fill('Retained ARC note');await restore('#arc .question-tools button:not([data-theme-toggle])');
 await page.locator('#arc-13').scrollIntoViewIfNeeded();await restore('#scroll-save');await answers('arc',13);await page.locator('#next').click();assert.equal(await step(),4);
 await page.locator('#next').click();assert.equal(sent.length,0);await notice('feedback');assert.equal(await page.evaluate(()=>document.activeElement.name),'feedback-understanding');
 await page.locator('input[name="feedback-understanding"][value="Cannot judge"]').check();let partial=await restore();assert.equal(partial.feedback.arc.ratings.understanding,'Cannot judge');assert.equal(partial.feedback.arc.ratings.choices,null);
 await feedback();await page.locator('#feedback-comment').fill('ARC feedback note');await restore();
 await page.locator('#next').click();await notice('Delivery could not be confirmed.');assert.equal(sent.length,1);
 assert.equal(sent[0]['Benchmark ID'],'arc');assert.equal(sent[0].Responses.match(/Answer: /g).length,25);assert(sent[0].Responses.includes('Retained ARC note'));assert.equal(sent[0]['Feedback comment'],'ARC feedback note');assert.equal(sent[0]['Survey version'],'2.7');assert.equal(sent[0]['Feedback: confidence'],'Cannot judge');
 const first=await restore();await page.locator('#next').click();await notice('Delivery could not be confirmed.');assert.equal(sent[1]['Submission ID'],sent[0]['Submission ID']);assert.equal(sent[1]['Completed at (UTC)'],sent[0]['Completed at (UTC)']);
 await page.locator('#feedback-comment').fill('Changed ARC feedback');await page.locator('#next').click();await notice('Delivery could not be confirmed.');assert.notEqual(sent[2]['Submission ID'],sent[1]['Submission ID']);
 fail=false;await page.locator('#next').click();await page.locator('#confirmation').waitFor({state:'visible'});assert.equal(await step(),5);assert.equal(sent[3]['Submission ID'],sent[2]['Submission ID']);assert.equal(sent.length,4);let accepted=await restore();
 await page.locator('#finish-here').click();assert.equal(await step(),9);await restore();await page.locator('#back').click();assert.equal(await step(),5);
 await page.locator('#back').click();assert.equal(await step(),4);assert(await page.locator('[data-feedback]').first().isDisabled());assert(await page.locator('#feedback-comment').evaluate(e=>e.readOnly));await page.locator('#next').click();assert.equal(sent.length,4);
 await page.locator('#next').click();assert.equal(await step(),6);assert.equal(await page.locator('input[data-benchmark="designqa"]:checked').count(),0);
 await answers('designqa',1,10);await page.locator('#designqa-1-comments').fill('DesignQA only');let second=await restore();assert.equal(second.session_id,accepted.session_id);assert.deepEqual(second.completion.arc,accepted.completion.arc);assert(await page.locator('input[data-benchmark="arc"]').first().isDisabled());assert(!(await page.locator('input[data-benchmark="designqa"]').first().isDisabled()));
 await answers('designqa',11);await page.locator('#next').click();assert.equal(await step(),7);assert.equal(await page.locator('[data-feedback]:checked').count(),0);assert.equal(await page.locator('#feedback-comment').inputValue(),'');await restore();await feedback();await page.locator('#feedback-comment').fill('DesignQA feedback');
 fail=true;await page.locator('#next').click();await notice('Delivery could not be confirmed.');await restore();fail=false;await page.locator('#next').click();await page.locator('#confirmation').waitFor({state:'visible'});assert.equal(await step(),8);
 assert.equal(sent.length,6);assert.equal(sent[4]['Benchmark ID'],'designqa');assert.equal(sent[5]['Submission ID'],sent[4]['Submission ID']);assert.notEqual(sent[5]['Submission ID'],sent[3]['Submission ID']);assert.equal(sent[5]['Session ID'],sent[3]['Session ID']);assert.equal(sent[5].Responses.match(/Answer: /g).length,25);assert(!sent[5].Responses.includes('Retained ARC note'));assert.equal(sent[5]['Feedback comment'],'DesignQA feedback');await restore();assert.equal(sent.length,6);
 await page.locator('#back').click();assert.equal(await step(),7);assert(await page.locator('[data-feedback]').first().isDisabled());await page.locator('#next').click();assert.equal(sent.length,6);
 const bad=await browser.newPage();bad.on('dialog',d=>d.accept());await bad.route('**/*',r=>r.fulfill({contentType:'text/html',body:html}));await bad.goto('https://survey.test/');const baseline=await bad.evaluate(()=>JSON.parse(JSON.stringify(draft)));
 for(const variant of ['malformed','old','missing','signature']){
  const data=JSON.parse(JSON.stringify(accepted));if(variant==='old')data.survey_id='mesa-guided-arc-designqa-v2-5';if(variant==='missing')data.answers.arc[1].answer=null;if(variant==='signature')data.completion.arc.signature='bad';
  await bad.evaluate(({data,variant})=>localStorage.setItem(storageKey,variant==='malformed'?'{':JSON.stringify(data)),{data,variant});await bad.locator('#load').click();await notice('Could not load',bad);assert.deepEqual(await bad.evaluate(()=>JSON.parse(JSON.stringify(draft))),baseline);
 }
 await bad.evaluate(()=>{Storage.prototype.setItem=function(){throw Error('Storage unavailable');};});await bad.locator('#save').click();await notice('unavailable',bad);assert(!(await bad.locator('#draft-status').innerText()).includes('Draft saved'));await bad.evaluate(()=>{Storage.prototype.getItem=function(){throw Error('Storage unavailable');};});await bad.locator('#load').click();await notice('Could not load',bad);await bad.close();
 assert.deepEqual(errors,[]);console.log('PASS: separate benchmark payloads, optional finish, all-stage draft restore, save controls, malformed/version/storage failures, null vs Cannot judge, per-benchmark retries, locking and no duplicate accepted sends. Delivery mocked.');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
