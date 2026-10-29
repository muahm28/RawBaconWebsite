import datetime, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
EMAIL = "Rawbacon8743@gmail.com"
IG, TT = "https://www.instagram.com/rawbacon8743", "https://www.tiktok.com/@raw.bacon.robotic"
FTC = "https://ftc-events.firstinspires.org/team/8743"
# (iso date, end date or None, name, venue, location, rank, W-L-T, RP, npOPR, npAVG, award, blurb)
EVENTS = [
("2025-02-14", None, "Machu Picchu Qualifier", "West High School", "Iowa City, Iowa", "14th", "3–2–0", "3.00", "43.61", "69.40", "Innovate Award — 2nd Place",
 "A strong qualifier close to home. Beyond a 3–2–0 record and a 43.61 npOPR, judges recognized our design process with 2nd place for the Innovate Award."),
("2025-02-27", "2025-02-28", "Iowa Championship — Black Division", "Xtream Arena", "Coralville, Iowa", "14th", "4–2–0", "2.67", "37.56", "93.50", None,
 "Our state championship weekend in the Black Division. A 4–2–0 qualification record and a 93.50 non-penalty average put the robot's scoring ceiling on full display against the strongest field we faced all season."),
("2025-10-16", None, "Solon Scrimmage", "Solon Community Center", "Solon, Iowa", "2nd", "3–0–1", "2.75", "36.90", "52.50", None,
 "Our first outing of the season. An unbeaten 3–0–1 scrimmage showing gave the new robot its first real test and set the baseline for everything that followed."),
("2025-11-08", None, "Machu Picchu Solon", "Solon Community Center", "Solon, Iowa", "1st", "6–0–0", "3.67", "37.05", "55.33", None,
 "An undefeated 6–0–0 qualification run and our first 1st-place seed of the season — the weekend the robot's design really came together."),
("2025-11-22", None, "Machu Picchu Iowa City — November", "Johnson County 4-H Fair Grounds", "Iowa City, Iowa", "1st", "5–1–0", "3.33", "50.01", "66.83", None,
 "Another 1st-place qualification finish, and where we set our season-best OPR of 50.01 — the number that anchors our season statistics."),
("2025-12-06", None, "Machu Picchu Riverside", "Highland High School", "Riverside, Iowa", "3rd", "4–2–0", "3.50", "42.42", "81.33", None,
 "Our best non-penalty average of the 2025–26 season at 81.33, including a 157-point match — one of the highest-scoring games of our year."),
("2025-12-13", None, "Machu Picchu Iowa City — December", "Iowa City High Cafeteria", "Iowa City, Iowa", "1st", "5–1–0", "3.83", "39.87", "60.00", None,
 "A 1st-place qualification finish on our home turf. Hosting in the City High cafeteria, the robot went 5–1–0 with a 3.83 RP average."),
("2026-01-24", None, "Machu Picchu Wellman", "Mid-Prairie High School", "Wellman, Iowa", "2nd", "5–1–0", "4.00", "48.84", "68.50", None,
 "A season-best 4.00 ranking points and our highest npOPR of the year at 48.84. Five wins in six qualification matches earned us 2nd place heading into alliance selection."),
]
EVENTS.sort(key=lambda e: e[0])
assert [e[0] for e in EVENTS] == sorted(e[0] for e in EVENTS)
def d(e):
    a = datetime.date.fromisoformat(e[0]); b = datetime.date.fromisoformat(e[1]) if e[1] else None
    if b: return f"{a:%B} {a.day}–{b.day}, {a.year}"
    return f"{a:%B} {a.day}, {a.year}"
def season(e): return "2024–25 season" if e[0] < "2025-08-01" else "2025–26 season"
FIRSTS = sum(1 for e in EVENTS if e[5] == "1st")
NAV = [("index.html","Home"),("about.html","About"),("season.html","Season"),("contact.html","Contact")]
MARK = '<svg class="mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" fill="#ff5a4d"/><text x="20" y="26" text-anchor="middle" font-family="Space Grotesk,Inter,sans-serif" font-weight="700" font-size="17" fill="#0b0f17">RB</text></svg>'
def page(file, title, desc, body):
    nav = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f==file else ""}>{t}</a>' for f,t in NAV)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta name="twitter:card" content="summary"><meta name="theme-color" content="#0b0f17"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap">
<link rel="stylesheet" href="styles.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap bar"><a class="brand" href="index.html">{MARK}<span><b>Raw Bacon Robotics</b><small>FTC Team #8743 · Iowa City High</small></span></a><nav aria-label="Primary">{nav}</nav></div></header>
<main id="main">{body}</main>
<footer><div class="wrap fgrid"><div><a class="brand" href="index.html">{MARK}<span><b>Raw Bacon Robotics #8743</b></span></a>
<p>FIRST Tech Challenge team at Iowa City High School, Iowa City, Iowa — run by students with the support of our mentors and school staff. Competing since our rookie year in 2014.</p></div>
<div><h3>Explore</h3><ul>{"".join(f'<li><a href="{f}">{t}</a></li>' for f,t in NAV)}</ul></div>
<div><h3>Connect</h3><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{IG}" rel="noopener">Instagram</a></li><li><a href="{TT}" rel="noopener">TikTok</a></li><li><a href="{FTC}" rel="noopener">FTC Events — Team 8743</a></li></ul></div></div>
<div class="wrap legal"><p><i>FIRST</i>® and <i>FIRST</i>® Tech Challenge are registered trademarks of For Inspiration and Recognition of Science and Technology (<i>FIRST</i>). Season statistics sourced from official <i>FIRST</i> FTC event data.</p><p>© 2026 Raw Bacon Robotics, Iowa City High School.</p></div></footer></body></html>'''
def stat(v, l): return f'<div class="stat"><b>{v}</b><span>{l}</span></div>'
STATS = stat("50.01","Best OPR")+stat("13.65","Auto average")+stat("37.98","TeleOp average")+stat("8.63","Endgame average")
def card(e):
    aw = f'<p class="award">★ {e[10]}</p>' if e[10] else ""
    cells = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k,v in [("Qual rank",e[5]),("Record (W–L–T)",e[6]),("Ranking points",e[7]),("npOPR",e[8]),("npAVG",e[9])])
    return f'<li class="ev"><time datetime="{e[0]}">{d(e)}</time><article><h3>{e[2]}</h3><p class="where">{e[3]} · {e[4]}</p>{aw}<p>{e[11]}</p><dl class="cells">{cells}</dl></article></li>'
def rows():
    return "".join(f'<tr><td><time datetime="{e[0]}">{d(e)}</time></td><th scope="row">{e[2]}</th><td class="hide-s">{e[4]}</td><td>{e[5]}</td><td class="hide-s">{e[6]}</td></tr>' for e in EVENTS)
home = f'''<section class="hero"><div class="wrap"><p class="eyebrow"><i>FIRST</i> Tech Challenge · Rookie year 2014</p>
<h1>Raw Bacon Robotics <span>Team #8743</span></h1>
<p class="lead">A student-led robotics team from Iowa City High School in Iowa City, Iowa. We design, build, program, and compete — and we bring engineering to our community while we do it.</p>
<div class="cta"><a class="btn" href="season.html">View season results</a><a class="btn ghost" href="contact.html">Contact or sponsor</a></div></div></section>
<section class="wrap band"><div class="stats">{STATS}</div><p class="note">Roughly the <b>70th percentile</b> of FTC teams by OPR this season. {len(EVENTS)} events on record, {FIRSTS} first-place qualification finishes.</p></section>
<section class="wrap"><h2>Competition schedule</h2><p class="sub">Every event, in chronological order. <a href="season.html">Full results and stats →</a></p>
<div class="tablewrap"><table><thead><tr><th scope="col">Date</th><th scope="col">Event</th><th scope="col" class="hide-s">Location</th><th scope="col">Qual rank</th><th scope="col" class="hide-s">Record</th></tr></thead><tbody>{rows()}</tbody></table></div></section>
<section class="wrap"><h2>How the team works</h2><div class="grid3">
<article class="panel"><h3>Build</h3><p>CAD-first design in Onshape, rapid prototyping, and iterative drivetrain and intake revisions between every competition weekend.</p></article>
<article class="panel"><h3>Programming</h3><p>Java on the REV Control Hub with odometry-assisted autonomous routines, tuned PID control, and driver-practice telemetry.</p></article>
<article class="panel"><h3>Outreach</h3><p>Demos for Iowa City elementary and middle schools, mentoring newer FTC and FLL teams, and STEM nights across Johnson County.</p></article></div></section>
<section class="wrap"><div class="panel spons"><div><h2>Sponsors</h2><p>Sponsorship funds parts, registration, and travel — and puts your name in front of our community all season. Sponsor slots are open.</p><a class="btn" href="contact.html">Become a sponsor</a></div>
<ul class="logos" aria-label="Current sponsors"><li>RTX</li><li>MidAmerican Energy</li></ul></div></section>'''
about = f'''<section class="hero small"><div class="wrap"><p class="eyebrow">About</p><h1>Engineering, taught with the help of the staff and mentors behind us</h1>
<p class="lead">Raw Bacon Robotics is <i>FIRST</i> Tech Challenge team #8743 at Iowa City High School. We have been competing since our rookie year in 2014, and every season we hand the tools — and the responsibility — to the next group of students.</p></div></section>
<section class="wrap"><dl class="facts"><div><dt>School</dt><dd>Iowa City High School</dd></div><div><dt>Location</dt><dd>Iowa City, Iowa</dd></div><div><dt>Rookie year</dt><dd>2014</dd></div><div><dt>Program</dt><dd><i>FIRST</i> Tech Challenge</dd></div></dl></section>
<section class="wrap"><h2>Our mission</h2><p class="sub">To build competitive robots and confident engineers — giving every student at City High a hands-on path into STEM, and sharing that path with our community across Iowa City and Johnson County.</p>
<div class="grid2"><article class="panel"><h3>Student-led, staff-supported</h3><p>Students drive the design decisions, the code, the outreach calendar, and the budget — with mentors and school staff coaching, teaching, and keeping the program running.</p></article>
<article class="panel"><h3>Gracious Professionalism</h3><p>We compete hard and help hard. Lending a part, sharing a fix, or scouting honestly matters as much as the score on the board.</p></article>
<article class="panel"><h3>Iterate in public</h3><p>Every design is documented in the engineering portfolio so the next season starts from what we learned, not from scratch.</p></article>
<article class="panel"><h3>Open doors</h3><p>No experience required. We teach CAD, Java, machining, and presentation skills to anyone at City High who shows up ready to learn.</p></article></div></section>
<section class="wrap"><h2>Where we came from</h2><ol class="ev-list plain">
<li class="ev"><time>2014</time><article><h3>Rookie season</h3><p>A handful of City High students, a borrowed workspace, and a name nobody forgets.</p></article></li>
<li class="ev"><time>2015–2024</time><article><h3>A decade of FTC seasons</h3><p>Qualifiers across Iowa, judged awards, and a steady pipeline of students moving into engineering and computer science.</p></article></li>
<li class="ev"><time>2024–25</time><article><h3>Machu Picchu qualifier &amp; Iowa Championship</h3><p>Competed at the Machu Picchu qualifier and the Iowa Championship Black Division, earning 2nd place for the Innovate Award.</p></article></li>
<li class="ev"><time>2025–26</time><article><h3>Six events and three first-place seeds</h3><p>A new robot, a Solon scrimmage opener, and first-place qualification finishes at Solon, Iowa City in November, and Iowa City in December.</p></article></li></ol></section>'''
groups = ""
for s in ("2024–25 season","2025–26 season"):
    groups += f'<h2 class="seasonh">{s}</h2><ol class="ev-list">{"".join(card(e) for e in EVENTS if season(e)==s)}</ol>'
seas = f'''<section class="hero small"><div class="wrap"><p class="eyebrow">Season results</p><h1>Results &amp; stats</h1>
<p class="lead">{len(EVENTS)} events, an award-winning design process, and season-best performance numbers that place us around the 70th percentile of FTC teams by OPR. Events are listed in chronological order.</p></div></section>
<section class="wrap band"><div class="stats">{STATS}{stat("~70%","OPR percentile")}</div></section>
<section class="wrap">{groups}</section>'''
contact = f'''<section class="hero small"><div class="wrap"><p class="eyebrow">Contact</p><h1>Contact us</h1>
<p class="lead">Questions about the team, interested in mentoring, or thinking about sponsorship? Families, mentors, and sponsors — we would love to hear from you.</p></div></section>
<section class="wrap grid2"><article class="panel"><h2>Get in touch</h2><ul class="clist"><li><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><span>Instagram</span><a href="{IG}" rel="noopener">@rawbacon8743</a></li><li><span>TikTok</span><a href="{TT}" rel="noopener">@raw.bacon.robotic</a></li></ul></article>
<article class="panel"><h2>Sponsors &amp; mentors</h2><p>Sponsorships cover registration, parts, and travel to events like the Iowa Championship at Xtream Arena. Mentors with engineering, software, machining, or business backgrounds can give as little as an hour a week.</p>
<a class="btn" href="mailto:{EMAIL}?subject=Raw%20Bacon%20Robotics%20sponsorship">Email us about sponsorship</a></article></section>'''
PAGES = {"index.html":("Raw Bacon Robotics #8743 | Iowa City High School FTC Team","Raw Bacon Robotics, FIRST Tech Challenge team #8743 from Iowa City High School, Iowa. Season results, robot build, programming, and outreach.",home),
"about.html":("About | Raw Bacon Robotics #8743","Raw Bacon Robotics is a student-led FIRST Tech Challenge team at Iowa City High School in Iowa City, Iowa, competing since our 2014 rookie year.",about),
"season.html":("Season Results & Stats | Raw Bacon Robotics #8743","Event-by-event FTC results for team #8743 in chronological order, plus OPR, auto, TeleOp, and endgame averages.",seas),
"contact.html":("Contact & Sponsor Us | Raw Bacon Robotics #8743","How to contact, mentor, or sponsor FTC team #8743 at Iowa City High School.",contact)}
for f,(t,ds,b) in PAGES.items(): (ROOT/f).write_text(page(f,t,ds,b),encoding="utf-8")
