// Run with PLAYWRIGHT_MODULE and CHROME_PATH set when these are not on defaults.
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 try {
  const page=await browser.newPage({viewport:{width:1360,height:1000},acceptDownloads:true});
  const errors=[],sent=[];let fail=false;page.on('pageerror',e=>errors.push(e.message));
  await page.route('https://survey.test/**',r=>r.fulfill({contentType:'text/html',body:fs.readFileSync(path.join(__dirname,'survey.html'),'utf8')}));
  await page.route('https://formsubmit.co/ajax/**',r=>{sent.push(r.request().postDataJSON());return r.fulfill({status:fail?503:200,contentType:'application/json',body:JSON.stringify({success:!fail})});});
  await page.goto('https://survey.test/');
  assert.equal(await page.locator('input[type=radio]:checked').count(),0);
  assert.equal(await page.locator('.question').count(),50);
  await page.locator('header [data-page="hle"]').click();
  assert(await page.locator('#contents').isVisible());
  assert((await page.locator('#contents-links a').count())>12);
  const widths=await page.locator('#hle > .panel').evaluateAll(es=>es.map(e=>e.getBoundingClientRect().width));assert.equal(widths[0],widths[1]);
  await page.screenshot({path:'/tmp/mesa-layout-desktop.png'});
  await page.locator('#contents-links a').filter({hasText:'What the AI is asked to do'}).click();assert(new URL(page.url()).hash.includes('hle-section'));
  await page.locator('#hle-send').click();assert((await page.locator('#hle-submit-status').innerText()).includes('25 remain'));assert.equal(sent.length,0);
  for(let i=1;i<=25;i++)await page.locator('input[name="hle-'+i+'"][value="Partly"]').check();
  await page.locator('#hle-send').click();assert((await page.locator('#hle-submit-status').innerText()).includes('enter your name'));assert.equal(sent.length,0);
  await page.locator('#hle-name').fill('Test participant');await page.locator('#hle-1-comments').fill('A test note.');
  await page.locator('#hle-send').click();await page.getByText(/Submitted to the email service at/).waitFor();assert.equal(sent.length,1);assert.equal(sent[0].Name,'Test participant');assert(sent[0].Benchmark.includes('Last Exam'));assert.equal((sent[0].Responses.match(/Answer: Partly/g)||[]).length,25);assert(sent[0].Responses.includes('A test note.'));assert(!sent[0].Responses.includes('ARC-AGI-2'));assert(!Number.isNaN(Date.parse(sent[0]['Completed at (UTC)'])));assert(await page.locator('#hle-send').isDisabled());
  await page.locator('#hle-1-comments').fill('Updated note');assert(!(await page.locator('#hle-send').isDisabled()));fail=true;await page.locator('#hle-send').click();await page.getByText(/Delivery could not be confirmed/).waitFor();assert.equal(await page.locator('#hle-1-comments').inputValue(),'Updated note');assert(!(await page.locator('#hle-send').isDisabled()));
  fail=false;await page.locator('#hle-send').click();await page.getByText(/Submitted to the email service at/).waitFor();assert.equal(sent[1]['Submission ID'],sent[2]['Submission ID']);
  await page.locator('header [data-page="arc"]').click();assert.equal(await page.locator('#arc-name').inputValue(),'Test participant');
  await page.locator('header [data-page="designqa"]').click();assert.equal(await page.locator('.worked-answer').count(),25);assert(!(await page.locator('#progress').innerText()).startsWith('50'));
  await page.locator('header [data-page="finish"]').click();const waiting=page.waitForEvent('download');await page.locator('[data-export="json"]').click();const data=JSON.parse(fs.readFileSync(await (await waiting).path(),'utf8'));assert.equal(data.participant_name,'Test participant');assert(data.completions.hle.completed_at);assert.equal(data.answers.arc[1].answer,null);
  await page.reload();
  await page.evaluate(()=>window.confirm=()=>true);await page.getByRole('button',{name:'Load saved draft',exact:true}).click();assert.equal(await page.locator('#hle-name').inputValue(),'Test participant');
  await page.setViewportSize({width:390,height:844});await page.locator('header [data-page="hle"]').click();assert(!(await page.locator('#contents').isVisible()));assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.screenshot({path:'/tmp/mesa-layout-mobile.png'});
  assert.deepEqual(errors,[]);console.log('PASS: aligned panels, desktop contents links, mobile layout, 50 blank items, completion validation, per-benchmark email payload, name and time, duplicate guard, failure/retry, downloads, drafts. Email delivery was mocked.');
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
