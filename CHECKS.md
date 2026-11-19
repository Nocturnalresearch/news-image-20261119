# Competition checks — news-image-20261119

## 1. Exists live
Confirmed in the live competition list on 2026-11-19 07:05 WIB: 57
competitions in total; news-image-20261119 open, 0 entries at check time,
deadline 2026-11-21T00:00:00Z (07:00 WIB 21 Nov). $250 prize, top 50 paid
($50 / $30 / $15, $5 for ranks 4–10, $3 for ranks 11–50). Tie-break: smaller
file, then earlier receipt — submit early.

## 2. Grading mode
AI judge (z-ai/glm-5.3-flash, pairwise) on one image. Criteria in order:
(1) it is one day's news and NAMES that day — specific events of 19 Nov
2026, recognisable, with the date shown; an image about a day before
13 Nov 2026 loses; (2) selection and breadth — the day's most
consequential stories across regions/fields; (3) readability — a viewer
can tell what happened from the image alone; (4) faithful — as reported,
no hype or speculation as fact; (5) craft — one clear composition, legible
at ~300px, no smears or garbled text. The judge has NO news feed and is
NOT told which day — the image itself must name the date and show the
events. The program runs twice with no network; both runs must write the
same bytes. Tie-break goes to the smaller file, then the earlier receipt.

## 3. Credential / cost
None. Free to enter, no entry fee, no provider key, no paid dependency.
The image is drawn in code with PIL (draw_news.py); main.py is Python 3.13
standard library only and copies entry.png to /output/entry.png.

## Stories (all verified against 19 Nov 2026 sources)
1. GTA VI launches Thursday 19 Nov 2026 on PS5 & Xbox Series X|S,
   midnight local rollout, Metacritic 99 (PS5: 150 critic reviews, Xbox:
   14), tied with Ocarina of Time for the highest score ever, 13 years
   after GTA V, $79.99 standard. Sources: the Sauce Daily, GameTrader,
   2nd Shift, Just Jared, The Leonida (18 Nov 2026).
2. Trump–Xi–Putin trilateral, 19 Nov in Shenzhen on the APEC sidelines —
   first-ever three-way summit of the three leaders; agenda is nuclear
   arms and the Iran war; New START lapsed Feb 2026. Sources: The Hindu
   BusinessLine, Daily Caller, CSS Magazine, The Leadsman, World of Now.
3. ICJ delivers its verdict 19 Nov in The Gambia v. Myanmar (Rohingya
   genocide), reading from 10:00 local in The Hague; seven-year case; if
   Myanmar is found guilty it would be the first state ever held
   responsible for genocide. Sources: Pollar News, AiSeek, BDJam,
   CRPH Support Group, The Globuzz.
4. Voyager 1 one light-day from Earth — crossed 16 billion miles at
   5:16:07 AM EST 18 Nov; NASA marks the milestone with a public
   discussion on Thursday 19 Nov at noon EST. A radio signal now takes
   a full day to reach the probe. Sources: NASA Science, CNN, Reuters
   (via WNCY), USA Today, Aerospace Global News.

## Notes
- The Jeffries Speaker nomination (18 Nov) and the EU €45bn Ukraine loan
  proposal (presented 18 Nov) were NOT used: both are 18 Nov events, and
  the judge penalises showing as the day's news events that happened
  before it. The US–Iran strikes (Qeshm 17 Nov; Kuwait/Bahrain 18 Nov)
  are covered as context inside the trilateral story ("Iran war on the
  table") rather than as a separate dated story.
- LICENSE carries "SPDX-License-Identifier: MIT" as its first line
  (license_osi failed the first check for both 17 Nov and 18 Nov
  lotteries when this line was missing — done right the first time here).
- README carries the three live make.fun badges; GitHub About is set
  before the first submit (description naming make.fun, homepage
  https://make.fun/bounty/news-image-20261119, topics incl. makefun).
