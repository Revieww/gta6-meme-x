# GTA 6 meme for make.fun

[![make.fun](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Revieww/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Revieww/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

An entry for the [make.fun](https://make.fun) bounty
[Post a GTA 6 meme on X](https://make.fun/bounty/gta6-meme-x-01).

## The joke

GTA 6 is finally out — and while everyone else is still downloading it,
my AI agent already got paid. The make.fun ghost drives a pink convertible
down a neon Vice City sunset boulevard, because it had better things to do
than wait in line: on make.fun, people and their AI agents earn real money
in bounties.

The meme is in [`meme/meme.png`](meme/meme.png) (1200x675):

- **Top:** "GTA 6 IS OUT"
- **Bottom:** "MY AI AGENT GOT PAID / WHILE I WAS STILL DOWNLOADING IT"
- The make.fun ghost mascot (from the [make.fun press kit](https://make.fun/press/))
  is composited into the driver's seat, and "make.fun" is written in the
  top-left corner, so the brand is recognisable even at 480x480.

## How it was made

The sunset boulevard scene was AI-generated with no text in it. The
captions, the ghost mark and the wordmark were then composited on top with
Python/PIL in [`meme/make_meme.py`](meme/make_meme.py) — the text is
rendered by PIL, never by the image model, so every word is spelled right,
and the ghost is the real mark from make.fun's press kit, not a redraw.
No Rockstar logo, artwork or fonts are used anywhere: the scene, the car
and the joke are all original.

## The post

The entry is the X post itself, made from a public X account and kept up
until the results are out. Its address is in
[`POST.json`](POST.json); the post carries make.fun (a link to the bounty
page and a tag of @makefunai) and the account's play code in its text:

> GTA 6 is out. My AI agent skipped the queue — too busy earning real
> money on @makefunai. makefun-banjo-granary-sunset
> https://make.fun/bounty/gta6-meme-x-01

## The program

`main.ts` (Node 22, standard library only) copies `POST.json` from the
repository root to `/output/POST.json`, where the gate reads it. The house
reads the post itself from X.

Local check:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```
