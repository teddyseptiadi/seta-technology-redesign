const fs = require('fs');
const path = require('path');

console.log("=== Running Multi-Page QA & Validation Suite for SETA Full Redesign ===");

const baseDir = '/home/teddy/workspace/seta-redesign';
const pages = [
  { file: 'index.html', title: 'PT SETA Technology Asia', keywords: ['Vibratory Bowl Feeder', 'Automatic Sorting Machine', 'Integrated Sorting House'] },
  { file: 'about.html', title: 'Tentang Kami', keywords: ['Visi Perusahaan', 'Misi Perusahaan', 'Grand Slipi Tower'] },
  { file: 'product.html', title: 'Vibratory Bowl Feeder', keywords: ['Bowl Top', 'Drive Unit', 'Digital Control Box', 'Linear Track Feeder'] },
  { file: 'product-automatic-sorting-machine.html', title: 'Automatic Sorting Machine', keywords: ['PSG-1600', 'PSG-2600', 'Optical Vision'] },
  { file: 'product-sorting-house.html', title: 'Integrated Sorting House', keywords: ['Screw', 'Bearing', 'Flange Nut', 'Rubber Seal', 'Bottle Cap'] },
  { file: 'download.html', title: 'Pusat Unduhan', keywords: ['Product Catalogue', 'PSG Series Optical Sorter', 'triggerDownload'] },
  { file: 'contact.html', title: 'Hubungi Kami', keywords: ['GRAND SLIPI TOWER', 'contactPageRfqForm', 'submitContactRFQ'] }
];

let allPassed = true;

for (const p of pages) {
  const filePath = path.join(baseDir, p.file);
  if (!fs.existsSync(filePath)) {
    console.error(`FAIL: File missing: ${p.file}`);
    allPassed = false;
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  if (!content.includes(p.title)) {
    console.error(`FAIL: [${p.file}] Title keyword missing: ${p.title}`);
    allPassed = false;
  }
  for (const kw of p.keywords) {
    if (!content.includes(kw)) {
      console.error(`FAIL: [${p.file}] Expected keyword missing: ${kw}`);
      allPassed = false;
    }
  }
  console.log(`✓ [${p.file}] Verified structure & all keywords`);
}

if (!allPassed) {
  console.error("\nSOME QA CHECKS FAILED");
  process.exit(1);
}

console.log("\nALL 7 PAGES VALIDATED (100% PASS RATE). Ready for GitHub Push.");
