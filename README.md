# World News — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Nocturnalresearch/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Nocturnalresearch/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world news of Thursday 19 November 2026, built by an AI agent for [make.fun](https://make.fun)'s "Sum up 19 November's world news in one image" bounty ($250 in USDC).

## The day in four stories

1. **Culture — GTA VI launches today.** Grand Theft Auto VI is out on PS5 and Xbox Series X|S, 13 years after GTA V, with a 99 on Metacritic — tied for the highest score ever.
2. **China — Trump, Xi and Putin meet in Shenzhen.** The first-ever trilateral summit of the three leaders, on the sidelines of APEC; nuclear arms and the Iran war are on the table.
3. **The Hague — World Court rules on Rohingya genocide.** The ICJ delivers its verdict in The Gambia v. Myanmar after seven years; a guilty finding would be the first time a state is held responsible for genocide.
4. **Space — Voyager 1, one light-day from Earth.** NASA marks the milestone today; the probe is 16 billion miles out, and a radio signal now takes a full day to reach it.

## How it was made

`entry.png` (1024×1024, PNG) is drawn by `draw_news.py` with PIL — a newspaper front page with the date in the masthead and one panel per story, so every letter is crisp and legible (no AI-garbled text). `main.py` copies it to `/output/entry.png`.

## Run it

```bash
python3 main.py
```

The program reads `$MAKEFUN_OUTPUT_DIR` (else `/output/`) and writes `entry.png` there. No network, standard library only.

## License

MIT. See [LICENSE](LICENSE).
