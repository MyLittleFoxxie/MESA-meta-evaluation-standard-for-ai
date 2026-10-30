// Local fixtures only. Every network request is intercepted; no delivery is sent.
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{const browser=await chromium.launch({executablePath:process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});try{
 const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
 await page.route('**/*',r=>r.fulfill({contentType:'text/html',body:fs.readFileSync(path.join(__dirname,'survey.html'),'utf8')}));await page.goto('https://survey.test');
 assert.deepEqual(await page.evaluate(()=>{const box=document.createElement('div');box.textContent='checking checking checking checking checking checking checking';document.body.append(box);annotate(box);const result=[box.querySelectorAll('.term').length,box.querySelectorAll('.term')[0].nextSibling.textContent,box.querySelectorAll('.term')[1].nextSibling.textContent];annotate(box);result.push(box.querySelectorAll('.term').length);box.remove();return result;}),[3,' checking checking ',' checking checking ',3]);
 for(const label of ['Checking','Score','Limit'])assert(await page.locator('#intro [data-term="'+label+'"]').count()>0);
 for(const theme of ['light','dark']){
  await page.evaluate(t=>setTheme(t),theme);
  for(const choice of ['Yes','Partly','No','Not sure','Not applicable']){
   const colors=await page.evaluate(c=>{const radio=document.querySelector('input[name="arc-1"][value="'+c+'"]');radio.checked=true;return [getComputedStyle(document.querySelector('.option-example[data-choice="'+c+'"]')).backgroundColor,getComputedStyle(radio.parentElement).backgroundColor];},choice);assert.equal(colors[0],colors[1]);
  }
  await page.locator('.answer-guide').locator('..').screenshot({path:'/tmp/mesa-v27-guide-'+theme+'.png'});
 }
 await page.evaluate(()=>{for(const q of packet.familiarity)draft.familiarity[q.id]=3;showStep(3);});
 assert.equal(await page.locator('#arc-1 .read-passage').innerText(),'Return to Passage');
 for(let i=1;i<=4;i++)await page.locator(`input[name="arc-${i}"][value="Yes"]`).check();await page.locator('#next').click();
 assert(await page.locator('#notice-dialog').isVisible());assert((await page.locator('#notice-message').innerText()).includes('21 remain unanswered'));assert.equal(await page.locator('#arc .validation-error').count(),0);await page.keyboard.press('Tab');assert(await page.locator('#notice-dialog').evaluate(e=>e.contains(document.activeElement)));
 await page.screenshot({path:'/tmp/mesa-v27-error-desktop.png'});await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.screenshot({path:'/tmp/mesa-v27-error-phone.png'});await page.keyboard.press('Escape');await page.waitForFunction(()=>noticeTarget===null);assert.equal(await page.evaluate(()=>document.activeElement.name),'arc-5');
 await page.setViewportSize({width:1440,height:1000});await page.evaluate(()=>{const h=document.querySelector('#arc-13-heading');window.scrollTo(0,window.scrollY+h.getBoundingClientRect().top-350);});await page.waitForTimeout(100);assert.equal(await page.locator('#sidebar-links [aria-current]').getAttribute('href'),'#arc-13-heading');
 console.log('PASS: guide colors match selected answers; definition markers occur every third mention; dialogs trap and restore focus; warning layout fits phones; Contents follows the screen center.');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
