#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import childProcess from 'node:child_process';
import { createRequire } from 'node:module';

function usage() {
  console.error('Usage: trace_png_to_svg.mjs input.png output.svg [preset] [--force]');
  console.error('Preset examples: posterized2, curvy, sharp, detailed, smoothed');
  process.exit(2);
}

const args = process.argv.slice(2);
const forceIndex = args.indexOf('--force');
const force = forceIndex !== -1;
if (force) args.splice(forceIndex, 1);
const [input, output, preset = 'posterized2'] = args;
if (!input || !output) usage();

const globalRoot = childProcess.execSync('npm root -g', { encoding: 'utf8' }).trim();
const requireGlobal = createRequire(path.join(globalRoot, 'noop.js'));
let PNG, ImageTracer;
try {
  ({ PNG } = requireGlobal('pngjs'));
  ImageTracer = requireGlobal('imagetracerjs');
} catch (err) {
  console.error('Missing global deps. Install: npm install -g imagetracerjs pngjs');
  console.error(err?.message || err);
  process.exit(3);
}

const data = fs.readFileSync(input);
const png = PNG.sync.read(data);
const imageData = { width: png.width, height: png.height, data: png.data };
const svg = ImageTracer.imagedataToSVG(imageData, preset);
if (fs.existsSync(output) && !force) {
  console.error(`Refusing to overwrite ${output}; pass --force to replace it`);
  process.exit(4);
}
fs.mkdirSync(path.dirname(path.resolve(output)), { recursive: true });
fs.writeFileSync(output, svg);
console.log(`Wrote ${output}`);
