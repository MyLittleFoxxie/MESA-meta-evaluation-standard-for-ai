const fs=require('fs'),path=require('path'),assert=require('assert');
const {chromium}=require('playwright');
(async()=>{
 const B=__dirname,html=fs.readFileSync(path.join(B,'questionnaire.html'),'utf8');
 assert(!/<(?:form|input|textarea|select|button|script|iframe|details)\b/i.test(html));
 const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--no-first-run','--disable-background-networking']});
 const page=await browser.newPage();let requests=[],errors=[];page.on('request',r=>requests.push(r.url()));page.on('pageerror',e=>errors.push(String(e)));
 await page.setContent(html);assert.equal(await page.locator('article[id^="q"]').count(),25);assert.equal(await page.locator('.explanation').count(),25);
 let layouts=[];
 for(const width of [1200,390])for(const colorScheme of ['light','dark']){
  await page.setViewportSize({width,height:900});await page.emulateMedia({colorScheme});
  const m=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.getBoundingClientRect().width}));assert(m.scroll<=m.width);layouts.push({width,colorScheme,...m});
 }
 await page.setViewportSize({width:680,height:900});await page.addStyleTag({content:'html{font-size:32px}'});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 await page.keyboard.press('Tab');const focused=await page.evaluate(()=>({tag:document.activeElement.tagName,href:document.activeElement.getAttribute('href')}));assert.equal(focused.href,'#questions');await page.keyboard.press('Enter');assert.equal(await page.evaluate(()=>location.hash),'#questions');
 assert.equal(requests.length,0);assert.equal(errors.length,0);
 const result={passed:true,questionCount:25,visibleExplanations:25,expandableHelp:false,layouts,enlargedTextOverflow:false,keyboardSkipLink:true,networkRequests:requests,pageErrors:errors,note:'Mechanical reading and layout checks, not human usability evidence.'};
 fs.writeFileSync(path.join(B,'analysis/reading-verification.json'),JSON.stringify(result,null,2)+'\n');await browser.close();console.log(JSON.stringify(result));
})().catch(e=>{console.error(e);process.exit(1)});
