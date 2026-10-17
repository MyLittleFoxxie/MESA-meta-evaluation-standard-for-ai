// Local, reading-only prototype checks. No participant survey is opened.
const fs=require('fs'),path=require('path'),assert=require('assert');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
(async()=>{
 const root=__dirname,html=fs.readFileSync(path.join(root,'prototype.html'),'utf8');
 assert(!/<(?:script|form|input|textarea|select|button|iframe)\b/i.test(html));
 const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1200,height:900}}),requests=[],errors=[];
  page.on('request',r=>requests.push(r.url()));page.on('pageerror',e=>errors.push(e.message));
  await page.goto('file://'+path.join(root,'prototype.html'));
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  assert.equal(await page.locator('#questions article').count(),25);
  assert.equal(await page.locator('#questions details').count(),25);
  assert.equal(await page.locator('form,input,textarea,select,button,script').count(),0);
  assert.equal(await page.locator('#questions details[open]').count(),0);
  const first=page.locator('#q1 summary');await first.focus();await page.keyboard.press('Enter');
  assert(await page.locator('#q1 details').getAttribute('open')!==null);assert(await page.locator('#q1 details p').isVisible());
  assert.equal(await page.evaluate(()=>document.activeElement.tagName),'SUMMARY');
  await page.keyboard.press('Space');assert.equal(await page.locator('#q1 details').getAttribute('open'),null);assert(!(await page.locator('#q1 details p').isVisible()));
  for(const scheme of ['light','dark']){
   await page.emulateMedia({colorScheme:scheme});await page.setViewportSize({width:390,height:844});
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
   await page.locator('#q12').scrollIntoViewIfNeeded();await page.screenshot({path:'/tmp/mesa-accessibility-'+scheme+'.png'});
  }
  await page.setViewportSize({width:680,height:700});await page.evaluate(()=>document.documentElement.style.fontSize='32px');
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.locator('#q12 summary').focus();await page.keyboard.press('Enter');assert(await page.locator('#q12 details').getAttribute('open')!==null);
  assert.equal(requests.filter(u=>!u.startsWith('file:')).length,0);assert.deepEqual(errors,[]);
  const result={passed:true,question_count:25,help_sections:25,keyboard:'Enter and Space toggle native details with focus retained',layout:'desktop, mobile 390px, light/dark, enlarged text at 680px; no horizontal overflow',network_requests:requests.filter(u=>!u.startsWith('file:')),page_errors:errors,limitations:'Interface checks do not establish human ease of use or content validity.'};
  fs.mkdirSync(path.join(root,'analysis'),{recursive:true});fs.writeFileSync(path.join(root,'analysis/prototype-verification.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
