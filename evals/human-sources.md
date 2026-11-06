# Human controls (pre-ChatGPT human texts)

Real texts written by people before November 2022. A good humanizer should leave them nearly untouched; edits here measure over-editing. 7 of the 10 targeted were collected (stopped on the time limit). h06-h07 use the later brief change allowing Chilean news sites with a visible article date.

| id | genre | country | written before | source domain | sha256 |
|---|---|---|---|---|---|
| h01 | forum-post (small business introducing itself) | Chile | 2020-11-10 | reddit.com/r/chile | `178b43a3ce40ea33…` |
| h02 | forum-post (question about SII for a mini pyme) | Chile | 2020-06-26 | reddit.com/r/chile | `98bbb71e73a7a720…` |
| h03 | job-post (barista, café in Ñuñoa) | Chile | 2021-06-07 | chiletrabajos.cl (Wayback 2021-06-10) | `35f7835455b4414f…` |
| h04 | job-post (barista, specialty coffee, Santiago) | Chile | 2019-08-23 | chiletrabajos.cl (Wayback 2019-09-21) | `228fbdab54db3301…` |
| h05 | about-us (family pastry shop, Frutillar) | Chile | 2022-03-16 | kuchenladen.cl (Wayback) | `c0b1dc564f0bcd11…` |
| h06 | news (pet food in neighbourhood almacenes) | Chile | 2020-06-22 | lacuarta.com | `c9a6cbca4c84eff5…` |
| h07 | news (Pymes de Barrio portal) | Chile | 2020-12-16 | lacuarta.com | `1cddeb85ab9c91d6…` |

Text is copied verbatim (news: bold markup and image captions removed) (typos kept: "onlinea", "hechar", "experiência", "perfeccionando.Hacia"). Edits made: Markdown links turned into their plain anchor text, a zero-width-space line dropped (h01), and the founding family's surname replaced with [apellido] (h05). The dates in `written_before` are the Reddit post date or the posting date shown on the archived page.

## How we searched
- Reddit: we searched the Arctic Shift archive API for r/chile titles from before October 2022 ("emprendimiento", "SII", "pyme", "negocio") and kept self-posts of 60 to 250 words. old.reddit.com returned 429 errors, and Arctic Shift began timing out after a few queries.
- Wayback: we used the CDX API to find archived chiletrabajos.cl job posts (prefix `/trabajo/barista`, etc.). archive.org blocked direct page fetches from this machine as bot traffic, so snapshots were read through firecrawl. CDX later went "Temporarily Offline" for us.
- Web search (WebSearch, firecrawl search) found only a few small-business pages, and most of those were too new to have pre-2022 snapshots.

## Rejected
- Product pages of the h01 business (Wayback 2021-12): too short (37 and about 50 words).
- chiletrabajos "vendedora tienda alimentos saludables" (2019): reads like an HR template. "maestro panadero" (2020): one sentence.
- mailchi.mp "ya-estamos-levantando-pedidos" (2021): a Mexican bakery, not Chilean.
- Reddit w8480f (2022-07, a SII question): good, but we already had 2 forum posts. Reddit bm9og1 (chilecomedia, 2019): also a forum post.
- kalgarysoap.com: Spain. panalesdelsur.cl: corporate-style honey company copy.
- azzuca.cl, rollano.cl, artesaniaschiloe.cl, mercadomapuche.cl: no snapshot from before 2022.
- TripAdvisor Valparaíso and San Pedro review pages (Wayback): the archived pages had no owner replies.

- La Tercera letters to the editor "Un año decisivo para las pymes" and "Plan nacional de rescate de las Pymes": dated 2025 and 2026, so after the cutoff.

## Candidates not reached (for the remaining 5 slots)
- Newsletter: Chilean small-business Mailchimp campaigns. The CDX filter scan over mailchi.mp timed out, and search engines don't index campaign-archive.com.
- Product copy: Yapo.cl classified ads (CDX via firecrawl works, e.g. `www.yapo.cl/region_metropolitana/...` 2021 captures). A filtered search for artisanal ads was still running when we stopped.
- Review reply: TripAdvisor owner responses for small Chilean hostales (`tripadvisor.cl/ShowUserReviews-g294306-...` Valparaíso captures exist). We needed pages that actually contain an owner reply.
- Community announcement or blog intro: no source found yet. Blogspot posts by juntas de vecinos (dated in the URL) are the best lead.

In this public copy the texts h01-h07 are link-only: each file in `dev/human/` and `locked/human/` keeps its source URLs and the full sha256 of the text we used. `python3 evals/tools/fetch_human.py` downloads the archived pages and checks any text you extract against those hashes.
