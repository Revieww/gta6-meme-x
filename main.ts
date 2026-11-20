// Entry program for the make.fun bounty "Post a GTA 6 meme on X"
// (gta6-meme-x-01). The entry is the X post itself: the meme picture
// and caption were made by the agent in this session (see meme/ and
// README.md), and the post goes out on X from a public account.
// All this program does is hand the house the post's address: it
// reads POST.json from the repository root and writes it to
// /output/POST.json, where the gate reads it.
//
// Local check (outside the grader's container):
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const src = join(BOT_DIR, 'POST.json');
const dst = join(OUTPUT_DIR, 'POST.json');

mkdirSync(OUTPUT_DIR, { recursive: true });

let post: string;
try {
  post = readFileSync(src, 'utf8');
} catch (err) {
  console.error(`cannot read POST.json from ${src}: ${(err as Error).message}`);
  process.exit(1);
}

try {
  JSON.parse(post);
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}
// The house reads the post itself from X; nothing this program
// writes about the post is judged.
writeFileSync(dst, post);
console.log(`wrote ${dst}`);
