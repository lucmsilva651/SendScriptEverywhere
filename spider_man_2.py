import time
import pyautogui
import pyfiglet

figlet_text = pyfiglet.figlet_format("lucmsilva")

print(figlet_text)
print(f"Starting in 5 seconds...\nPlease put your Telegram or Discord client on focus now.")

time.sleep(5)

def enviar_script(script_text):
    linhas = [linha.strip() for linha in script_text.splitlines() if linha.strip()]
    
    for linha in linhas:
        pyautogui.write(linha)
        pyautogui.press('enter')
	# 250ms timing to avoid breaking ToS (you are will be banned of anywhere anyways)
        time.sleep(0.25)

    return len(linhas)

# bee movie script
linhas_enviadas = enviar_script("""
SPIDER-MAN 2
Written by
Michael Chabon
(CONT'D)
(CONT'D)
(CONT'D)
(CONT'D)
FADE IN:
OVER CENTRAL PARK
Gorgeous fall day. Hot-chestnut weather. Spider-Man sails in
off Central Park West on a line of silk. King of the
Manhattan skyline. Swinging from a turret of the Dakota.
PETER (V.O.)
Look at this guy.
Sailing over the Sheep Meadow, bouncing off the top of
Reptile House. Sharp turn onto Fifth Avenue, hard around the
Plaza Hotel.
PETER (V.O.)
Look at him. Like he doesn't have a
care in the world.
FIFTH AVENUE
is a torrent of taxis and humans and steam from the manholes.
He skims along it like a dragonfly, heading downtown.
PETER (V.O.)
You probably think it'd be cool to
trade places with this guy. Styling
costume. Awesome powers. Greatest
damn city in the world.
AT 36TH STREET
He throws down a great big giant elastic band of webbing.
Turns a couple of office towers into an enormous slingshot.
Curls into a ball and hits the rubber band dead center.
PETER (V.O.)
Is that what you're thinking?
He gets just enough bounce to catapult him up over the top of
the Empire State Building. Toe barely grazes the needle tip.
PETER (V.O.)
Well, maybe you'd better think
again.
He pinballs down Fifth Avenue and then out
OVER UNION SQUARE
Heading for the Flatiron Building, with the big DAILY BUGLE
sign. Circling in, alighting on its roof.
2.
(CONT'D)
(CONT'D)
PETER (V.O.)
Maybe you'd better wait until you
see the kind of day this guy's
having.
J. JONAH JAMESON'S BIG UGLY MUG
So steamed the very air around his head shimmers.
JJJ
Parker, you're fired!
INT. JJJ'S OFFICE — DAY
He tosses a stack of photos at PETER PARKER. They're awfully
nice photos. Maybe a little too nice.
JJJ
Dogs catching Frisbees in the
park... Some fat old geezer playing
chess... Autumn leaves.
PETER
I was thinking maybe the Bugle
could show another side of New York
for a change–-
JJJ
Parker, if I believed for one
second those pictures were an
accurate reflection of this town,
I'd hang myself from the top of the
Chrysler Building. I don't pay you
to be a sensitive artist! I pay you
because for some reason that psycho
Spider-Man will pose for you.
PETER
Well, it's like I told you, Mr.
Jameson. Spider-Man won't let me
take any more pictures of him. He
says you only use them to slander
him. You've turned the whole city
against him.
JJJ
A fact I'm very proud of! Having
that lunatic around has weakened
the moral fiber of New York! The
police are demoralized! The
citizens lazy! Now get your pretty
little "portfolio" out of my face
before I go into a diabetic coma!
3.
(CONT'D)
(CONT'D)
PETER
Mr. Jameson, please. You can't fire
me. Even working two jobs I can
barely make tuition, and Aunt May's
social security doesn't amount
to...
JJJ mimes tying a noose around his neck, throws his head
back, thrusts his tongue from his mouth. Peter folds.
PETER
What if--all right, what if I did
have a shot of Spider-Man?
Peter reaches into his knapsack and takes out a manila
folder. Slides out a fantastic shot of Spider-Man saving a
nun from an oncoming meat truck. JJJ eyes it hungrily.
JJJ
It stinks. I'll give you three
hundred.
He reaches for it. Peter snatches it back.
PETER
No. There's no way I can sell you
this shot... until you agree to run
more balanced coverage of SpiderMan.
JJJ
I take my journalistic
responsibility to present balanced
coverage very seriously Parker, you
know that. Fine. I'll give you
four. I'll nominate him for a
goddamn medal, Parker. You have my
word.
PETER
Five.
JJJ
That's outrageous.
(beat)
Done.
Peter lets go of the photo, then sits a moment. Knowing he
has just made big mistake.
JJJ
All right, you've wasted enough of
my precious time, Parker. Get lost.
4.
PETER
Time. Right.
Peter snaps out of it, looks at his watch: oh, shit. He leaps
to his feet, grabs his knapsack, and runs out.
EXT. MINEO'S PIZZA — DAY
Peter rides up on an elderly Kawasaki: RUMBLING, COUGHING,
SPUTTERING. Not a well machine. On the back, a hotbox with
the Mineo's logo. Peter leaps off and runs into the pizzeria.
A PAGER beeps.
INT. MINEO'S — DAY
Peter hurtles into the shop, out of breath, frantic. Yanks
the pager from his pocket.
PETER
Sorry! Mr. Aziz, I'm sorry.
MR. AZIZ hangs up the phone. The BEEPING stops. Life has
disappointed Mr. Aziz; Peter's only a side-manifestation.
MR. AZIZ
Twenty-one minutes ago, in comes an
order from the high-quality law
firm of Foehn, Harmattan & Buran
for seventeen extra large deep-dish
pizzas. In eight minutes, I am
defaulting on the Mineo's twentynine minute guarantee. Indeed
numerous banners and signs proclaim
the sacred number.
MR. AZIZ (cont'd)
Then not only will I be receiving
no money for these pizzas, I will
lose the customer forever to Pizza
Yurt. And they are killing me
already.
PETER
Why didn't you send Salim?
MR. AZIZ
Salim was deported yesterday. I
have no hope but you. You must make
it in time.
He starts thrusting pizzas at Peter, stacking them in Peter's
arms until we can't see his face anymore.
5.
MR. AZIZ (CONT'D)
You are a nice young man, Peter,
but you are not dependable. This is
the last chance I can give you. You
must cross forty-two blocks in
seven and one half minutes. Or your
ass is to be fired.
Peter checks the big Mineo's clock. It's 5:44.
EXT. MINEO'S - NIGHT
Peter runs to his bike, dumps the pizzas into the hotbox.
Climbs on, kicks it. Nothing. Kicks it again. Nothing.
PETER
I don't believe this!
Mr. Aziz watches, contemplating suicide. Peter kicks it once
more and it starts. He goes slobbering off.
EXT. NEW YORK STREET — DAY
Peter halted. Looks at his watch. 5:47.
A van has collided with a Town Car. The DRIVERS are on the
street, shouting and threatening each other. The PASSENGER
gets out, too. The three men come to blows.
Peter pops up onto the sidewalk. Mistake. An old lady in a
wheelchair comes out of nowhere. Peter hits the brakes.
Swerves. The bike stalls. He kicks wildly at the starter:
dead. And it's 5:48.
Peter leaps off the bike. With a mighty heave he wrenches the
hotbox right off the back of the motorcycle, snapping bolts,
twisting metal. Then he ducks into an alley.
EXT. LOWER MANHATTAN - NEW YORK STREET — AERIAL SHOT
Spider-Man swings toward the Woolworth Building. One-handed,
since the hotbox is tucked under his left arm. At the end of
each arc he freefalls until he shoots the next strand of web.
Below, two boys chase each other and a basketball into the
street. A car is coming right at them.
Spider-Man's spider sense tingles. He looks down; sees the
trajectories of car, ball and boys, pure vectors of physics
plotted against the air: collision.
Spider-Man heaves the hotbox away. It arcs heavenward. With
his hand now free, he shoots a strand of web.
A lasso of web encircles the boys and yanks the boys toward
the opposite side of the street.
6.
(CONT'D)
Sets them on their feet.
The car squeals past, horn BLARING.
The boys, dazed. The basketball shoots in, a web-slung chest
pass. One of them catches it. They look up at the sky.
Spider-Man catches up to the hotbox as it hurtles earthward,
past him. Snags it with a web and drags it back up. The
Woolworth Building looms. Spider-Man snags its pinnacle and
arcs around it, circling in.
INT. WOOLWORTH BUILDING - LAW OFFICES - DAY
Peter rushes in with the stack of pizzas. Out of breath, kind
of wild looking. A big, silly grin on his face.
PETER
Pizza time!
He sets the pizzas on the desk. The receptionist stares at
him, then at the pizzas: disgust. Peter looks--there's a gob
of webbing on the top box. Sheepish he scrapes it off.
PETER
Sorry.
INT. MINEO'S PIZZA — EVENING
Peter struts in, grinning.
PETER
Mr. Aziz! I'm back! I--
Mr. Aziz whirls on him.
MR. AZIZ
You are fired, that is what you
are. The pizzas arrived three
minutes late! Peter, the twentynine minute guarantee is a promise.
I know a promise means nothing to
you, but to me it is serious.
PETER
It's serious to me, too, Mr. Aziz.
Honestly. Please, I need this job,
please give me another chance.
Mr. Aziz shakes his head. Peter gives up.
EXT. OSBORN/PARKER APARTMENT - NIGHT
Peter's tired old Kawasaki pulls up in front of the building,
backfiring. He climbs off it.
7.
Trudges into the lobby.
SPIDER SENSE. Peter's surging HEARTBEAT. A shadow looms.
Peter jumps back, then lashes out and grabs hold of his
attacker. Ducks, twists, flips a very large man over his
shoulder. The guy SLAMS against the lobby floor. It's a beefy
SECURITY GOON. Peter has flattened the guy.
GOON
Christ, I think you broke my
tailbone!
PETER
Oh, man, I'm sorry, I--
GOON
I was only going ask for your ID!
PETER
My ID? Since when--?
INT. OSBORN/PARKER APARTMENT - NIGHT
Peter takes out his key. But instead of a keyhole there's a
card-reader. He's puzzled. The door flies open.
HARRY
What the hell you did to my
security guy?
PETER
He surprised me! I grabbed him and
he... he must have lost his
footing.
(how lame!)
I think they just waxed the lobby.
(changing the subject)
What's with the muscleman, Harry?
Did somebody threaten you?
HARRY
You're kidding, right? Pete, I'm
lucky Spider-Man hasn't killed me
already! He knows I'll spend every
last dime I have to take him down.
PETER
Harry. I'm worried about you.
You've really gotten kind of...
He takes a slender hybrid PDA/remote from his pocket. Taps
some buttons.
8.
(CONT'D)
(CONT'D)
Titanium bars slide across the windows. Steel shutters come
down. Laser trip-beams spin a glowing web across the living
room. Another beam lances from the ceiling and performs a
retinal scan of Peter. He flinches.
PETER
...paranoid.
Harry holds up the screen of his super-Palm. It reads ID
CONFIRMED: PARKER, PETER.
HARRY
I guess you're who you seem to be.
PETER
Please just tell me you didn't put
a camera in the bathroom.
Harry taps, and all the barriers retract; the beams die. He
gets right in Peter's face. Trying to be funny but with weird
intensity.
HARRY
You could save me a buttload of
money and trouble if you would just
tell me how you always manage to
find the guy.
.PETER'S FACE
The impossibility of the situation; the pain.
PETER
I would if I could. I swear to you.
Harry stares at him, searching his face. Something there that
he doesn't quite believe. Peter struggles to meet Harry's
searching gaze. Falters. Fails.
HARRY
That's fine. No, I'm serious. You
don't need me, I don't need you.
We're not even really friends, are
we?
Takes two tickets from his pocket, tosses them on the table.
HARRY
Hear are those tickets you wanted.
That Octavius guy at Columbia. Have
fun.
THE TICKETS
9.
THE ANANSI PROJECT: AN INTERIM REPORT. PROFESSOR OTTO
OCTAVIUS. DAVIS AUDITORIUM. 6PM.
PETER
Octavius! Otto Octavius is the god
of arachnid biomimetics. Harry, I
know you're mad at me, but come on!
You can't miss that!
Peter is perfectly serious. Harry can't help smiling.
HARRY
Lord have mercy on my soul.
PETER
You promised you'd introduce me to
him!
The rage flares up again in Harry.
HARRY
And you promised to help me get
Spider Man!
(subsides)
All right, fine. I keep my
promises.
PETER
Great! Okay! Let's bolt.
They start to go out. Harry stops by the door, points to the
answering machine.
HARRY
Oh, there was a message. For you. I
didn't feel like picking up.
Peter goes to the machine, presses play.
MJ'S VOICE
Hello. This is Mary Jane Watson,
star of the Broadway stage.
(beat)
You guys, I'm so nervous!
Peter checks his watch.
PETER
Hmm. Geez, I hope the lecture's
over by 7:30. I need to get down to
the theater by 8.
HARRY
Didn't you already see that lame
show of hers?
10.
PETER
Twice.
HARRY
Christ, Pete, I know you're her
boyfriend, and all, but that's
above and beyond.
PETER
Hey, tonight she's playing the
lead! She's the, you know, the
understudy.
As they walk out of the apartment.
HARRY
What, did she poison the leading
lady?
PETER
Shut up. And I'm not her boyfriend.
Bars descend, indicators flare, as they shut the door.
INT. COLUMBIA UNIVERSITY — DAVIS AUDITORIUM — NIGHT
Packed house of researchers, reporters, interested members of
the public. PROF. CZERNOWITZ is introducing Otto Octavius.
CZERNOWITZ
...as a doctoral candidate he was
dazzling. Now I'm afraid he's left
us mere mortals far behind. It's my
great honor to present, director of
the Anansi Project, winner of a
National Science Medal, Dr. Otto
Octavius.
APPLAUSE as Otto strides out. Younger than you might expect.
Wearing a long black Gaultier jacket. Smiling like a man
with a surprise in store for us. He and Czernowitz meet. A
stiffness between them. Czernowitz looks intimidated.
OTTO
Frank.
CZERNOWITZ
Otto.
They shake hands awkwardly. Then Otto strides to the podium.
Grins, self mocking. Behind him on a table, a violin and
bow. Piano to one side.
11.
(CONT'D)
(CONT'D)
(CONT'D)
OTTO
He told you I was "dazzling," but
what he's too nice to bring up is
was what an insufferable little
wretch I was.
Laughter. The lights dim; spot on Otto. Behind him a large
flatpanel monitor descends. As he talks, the display will
mirror, expand on and illustrate his words.
OTTO
Biomimetics seeks to adapt for
human use the technologies of other
species. We poor humans have always
envied our fellow creatures their
talents; soon we will share them.
Peter is rapt; Harry is playing Tetris on his Palm Pilot.
OTTO
My own researches have been into
arachnid technology: adapting, the
remarkable abilities of spiders,
their web-spinning abilities, their
astonishing, almost precognitive
impulse control.
Harry notices how spellbound Peter is; leans over.
HARRY
I will never understand this spider
thing of yours.
Peter takes no notice.
OTTO
We had some success with
manipulating spider RNA. But it's
in the area of octopedal locomotion
that things are really getting
exciting. The goal is to provide
stable motion on every possible
kind of terrain and superior
manipulation at a distance.
Otto steps out from behind the podium.
OTTO
You can't imagine the sheer number
crunching might required to control
and coordinate eight legs. Really
tough. Actually, it was a chance
visit to the Bronx Zoo that gave me
the key insight.
12.
(CONT'D)
(CONT'D)
(CONT'D)
(CONT'D)
(CONT'D)
He walks toward the monitor, which displays an octopus, along
with a diagram of its nervous system.
OTTO
The octopus has the equivalent of a
powerful processor in each leg,
networked to the central unit in
her brain.
The display fades to a diagram of the Rig, eight legs
networked to each other through and to the center. The
center is empty; then a diagrammatic human operator appears.
OTTO
Now, so far the capacity to control
the full complement of eight legs
is beyond our capacity. But we've
been able to implement a similar
system using...
Otto takes a step forward, smiling a little coyly. Then from
somewhere behind him a pair of glinting pseudopods snake out.
The black stealth-bomber glint of superhard ceramic. A gasp
from the audience.
OTTO
Four!
Harry sits up. Puts away the Palm Pilot.
The 'pods hover over Otto's shoulders a moment, undulant.
OTTO
I call it a self-articulating
network, but I'm afraid the name
that has stuck is Otto's Octopus.
One 'pod reaches to tap him on the shoulder.
OTTO
Yes? Oh, thank you. It is a little
warm in here.
The arms help him out of the jacket, and as it comes off,
another pair of pseudopods is revealed. The audience goes a
little nuts.
One 'pod takes up the violin; another, the bow. The next pair
snake out toward the piano; Otto strikes up a Grieg sonata.
With his own two hands, he takes out a fat cigar and lights
it; puffs contentedly.
The audience, amazed, afraid, half suspecting that it's all a
prank.
13.
(CONT'D)
(CONT'D)
(CONT'D)
(CONT'D)
(CONT'D)
Peter with a look of open-mouthed wonder. The music breaks
off.
Now the 'pods assume a configuration like a daddy long-legs,
"toes" splayed against the dais, arching high into the air.
Among them hangs, perfectly at ease, Otto. One at a time, in
turn, he raises and lowers each foot.
OTTO
Each one of my four assistants here
is equipped with its own hundredteraflop processor.
He begins to stride back and forth across the stage on his
four dancing pseudopods.
OTTO
Computer architecture so
sophisticated and capable of
learning it approaches
consciousness.
He sinks back onto the two lower 'pods. The upper ones snake
out around him.
OTTO
At times I feel the Rig here has a
life of its own.
LEFT UPPER PSEUDOPOD takes a piece of paper from Otto's
pocket. RIGHT UPPER produces a pen and scrawls something
across the paper. Then the 'pod with the paper slaps it
across Otto's back. He turns around, as if confused, walking
on the lower pseudopods. The sign says GEEK!
Laughter from the audience. They're eating this up. Otto,
back to the audience, whirls his head around.
OTTO
Given time, and a strong enough
host...
(rueful smile)
...its systems and my own would
actually begin to integrate with
each other--
The pseudopods rip away his shirt, revealing THE RIG nestled
right up against his spine, overlapping his own flesh.
OTTO
--Merge into one organism.
14.
AUDIENCE
Shock, even revulsion at the sight of the implants. Then a
surge of APPLAUSE.
PETER
Gapes, bowled over.
PETER
You have to introduce me to him!
HARRY
Don't you have a diva waiting?
Peter checks his watch.
PETER
I can make it.
INT. DAVIS AUDITORIUM - BACKSTAGE - NIGHT
Otto lurches in on the pseudopods to a ROAR of applause from
the hall.
The 'pods telescope in and Otto falls to the floor. But one
of the 'pods remains slightly extended.
OTTO'S team crowds around him and drag him over to the NEURAL
COUPLER UNIT. They mount it around him.
The TEAM LEADER twists the Rig's LATCH. This is a dial with a
glass tube at its heart, like a spirit level, with a single
glowing bubble of air. He aligns the bubble with a mark and--
WHAM-the 'pod LASHES out and knocks the Team Leader aside.
INT. DAVIS AUDITORIUM - AUDIENCE - NIGHT
People are still applauding. But Peter's spider-sense
TINGLES. He gets up.
PETER
I'll meet you in the lobby.
HARRY
Where are you--
PETER
Too much coffee.
INT. DAVIS AUDITORIUM - BACKSTAGE - NIGHT
The Rig is out of control. Otto hangs from it like a doll.
The pseudopods whip and buzzsaw. Smash lightbulbs. Scatter
humans.
15.
(CONT'D)
Spider-Man leaps into the middle of the cyclone. He tries to
reach Otto. The 'pods feint and block.
He fires web snares at the pods; pins them to the wall. They
break free, lash out. Knock Spider-Man down.
Spidey leaps up, fires a strand in either direction, snags
the upper two 'pods. Yanks them toward himself. Ties them in
a knot. They GRIND in protest. Keeping a grip on the knot
he--
Spins a thick cocoon around each of the lower ones, padding
each out until it's a gently flailing balloon. The Rig
struggles for a moment, then powers down. Otto falls to the
floor, the 'pods knotted across him.
Spider-Man kneels beside Otto. Making sure he's okay.
The Team Members hurry over with the coupler. Spider-Man gets
out of the way. The team gets Otto into i and the Team Leader
twists the Latch.
SPLORCH. The rig pops open. Otto falls out.
We see that Otto's bare, muscular back is enhanced by four
neural sockets. They roll him over.
Otto opens his eyes. The irises of his eyes seem to be
leaking into the whites: pinwheels. Strange flowers. Octopi.
ASSISTANT
Look at his eyes!
ASSISTANT 2
We're overdoing the endorphin push.
TEAM LEADER
That's the symbiosis routines in
the Rig. It's actually trying to
reconfigure his optical functions.
OTTO
Was I... was I fighting Spider-Man?
Everyone looks around at Spider-Man. Spider-Man's not there.
Otto sits up. They try to help him.
OTTO
I'm fine! Thank you. I'm fine. Now,
get off me.
He stands up, shaky. Brushes off their helping hands.
16.
(CONT'D)
(CONT'D)
TEAM LEADER
Otto, it was too long. You stayed
in the Rig too long.
OTTO
No, the problem is that I didn't
stay in it long enough! My system
never gets the chance to reach
equilibrium with the Rig's!
They stare at him. Is he serious? He looks around. Sees the
broken light bulb. The slashed curtain. The shattered chair.
He sits down.
OTTO
Maybe I stayed in the rig too long,
I don't know.
They bring him a glass of water and a clean shirt. He accepts
their ministrations.
OTTO
Thank you. Thanks a lot, Teddy.
(concerned)
Are you all right? I didn't hurt
you?
TEAM LEADER
(relieved)
I'm fine, chief.
INT. DAVIS AUDITORIUM - BACKSTAGE CORRIDOR
Harry introduces Peter to Otto; they're shaking hands. Otto
looks a bit frazzled but basically fine.
HARRY
Doesn't it hurt to be jacked into
that thing?
OTTO
Actually, thanks to the endorphin
boosters it feels very good. Coming
out's a bitch.
PETER
It's so great to meet you. And the
Rig's pretty--cool.
OTTO
Still one or two--
(twitches his head)
Kinks to work out. But basically
sound.
17.
(CONT'D)
PETER
Actually, Doctor, I was hoping to
hear you talk about the superspider
research.
OTTO
Ah. Well. Unfortunately we lost our
funding for that project. I'm
afraid it was rather poorly
managed. And please... call me
Otto. Any friend of the Osborns is
my friend. The Rig's materials and
kinetechnology is all Oscorp design
and build. Norman Osborn was a huge
supporter of my work. A steady and
generous supporter. Not too mention
a true original. A man, in a world
of mediocrities. He's very sorely
missed.
At this mention of Norman, a shadow clouds Harry's face.
OTTO
So I hear you're into spiders.
PETER
It's sort of a hobby.
OTTO
And you guys had a--field trip? To
our lab last year? I hope that was
interesting?
PETER
Oh, yeah. Changed my life.
HARRY
Pete? Not that I really care, but
don't you have an ego extravaganza
to get to?
Peter looks at his watch: it's 7:45.
PETER
Jeez! Oh, my God. I have to go.
Now!
OTTO
Ego extravaganza?
PETER
It's our friend--
18.
(CONT'D)
(CONT'D)
HARRY
Your friend.
PETER
--MJ. Mary Jane Watson. She's in
this musical. She's the understudy
and she's making her big debut in
fifteen minutes.
He shakes hands with Otto, then starts away.
PETER
You ought to check it out, I bet
you'd really get into it.
EXT. MARTIN BECK THEATER — NIGHT
The Marquee reads: BRIDE! Over it, enormous cutouts of Dr.
Frankenstein and the Bride. The name Deirdre DUNN plastered
everywhere.
A tour bus pulls up in front of the theater. The nameplate
reads: MT. NEBO CENTER FOR ASSISTED LIVING. A BUNCH OF OLD
LADIES file out.
We're with two of the ladies, SOPHIE and ROSE. As they enter
the lobby, they are each handed a program.
Rose notices a leaf of paper poking from the program. Tugs it
out.
ROSE
What's this?
THE PIECE OF PAPER
DURING TONIGHT'S PERFORMANCE, THE ROLE OF ELIZABETH
FRANKENSTEIN WILL BE PLAYED BY MARY JANE WATSON.
ROSE
Wouldn't you know it. Sixty dollars
a ticket and we get the understudy.
SOPHIE
Deirdre's probably in rehab again.
INT. THEATER - BACKSTAGE - NIGHT
Frenetic stagehands make last minute changes. Actors loiter
in the wings. We travel down the wings, past actors and crew
who crowd the stairs, down to the dressing rooms.
MJ WATSON sits at the mirror, making little adjustments to
her makeup.
19.
(CONT'D)
(CONT'D)
She's in costume as Elizabeth Frankenstein and holding a
blond wig in her hands. RENARD, the actor playing
HENRY FRANKENSTEIN, lounges beside her, calm where she's
worried. He's very good-looking.
RENARD
Just remember, acting is reacting.
MJ
Got it.
Clearly troubled rather than nervous. The door to the
dressing room opens. MJ turns expectantly. ANOTHER ACTOR'S
there, costumed as an Angry Villager.
MJ
Did you check Will Call?
ACTOR
The ticket is still there.
MJ looks sad. Puts on the wig, tugs it straight, and smiles
at herself. Big theatrical smile. The show must go on.
Renard pulls a chair over, sits down right beside MJ.
RENARD
Hey, cheer up. There's a TV crew
here, you know. From New York 1.
They heard about your big debut.
MJ
How did they hear?
RENARD
I don't know. Somebody must have
called them. Somebody who likes the
way you... act.
Flirting hard. He brushes a flake of mascara from her cheek.
RENARD
So, who is he, your Mr. No-Show?
MJ
A friend of mine.
ACTOR
Boyfriend?
MJ
No. Just a friend. I thought he
might want to see my debut, but I
guess he doesn't.
20.
ACTOR
Eh, who needs him?
MJ
(resolute)
That's what I say. Who needs him?
The STAGE MANAGER comes in.
STAGE MANAGER
MJ? You ready?
I/E. THEATER — NIGHT
Peter tears into the lobby. Runs up to the theater door. A
burly USHER stops him.
USHER
Whoa. You can't go in there. Nobody
seated once the performance begins.
Points to a sign which confirms this.
PETER
But I--
USHER
It's to help maintain the illusion.
PETER
I understand. But I have to get in
there. Mary Jane Watson is a friend
of mine.
USHER
And as far as I can tell, she is a
very nice young lady.
(beat)
Nobody seated once the performance
begins. You can go in at
intermission.
PETER
When's that?
USHER
(checks watch)
About forty-two minutes from now.
MJ'S CAST HEADSHOT
Nice picture. A little sultry.
21.
INT. THEATER — LOBBY - NIGHT
It's on a wall by the front doors. Peter's gazing at the
picture. Just kind of amazed by how pretty she looks.
Spider-sense TINGLES.
SIREN in the distance. Faint SQUEAL of tires.
INT. THEATER — ONSTAGE - NIGHT
MJ as Elizabeth with Renard as Henry F. Henry is singing his
big number, "I Created A Man." MJ emotes back at him. Her
gaze strays toward the house.
Right in the front row, a glaringly empty seat.
Back on MJ. She sings.
OUR TWO OLD LADIES
Way at the at the back of the house.
ROSE
She's terrible.
INT. THEATER — NIGHT
SIREN is louder. Peter ducks out into the street. Something
is happening and he needs to stop it. It's coming from over
on Broadway.
A CAR flashes through the intersection of 45th and Ninth.
Driving way too fast. In traffic. Skids. Smashes into a car.
Then another. Then keeps on going downtown. Two seconds
later, one two three police cruisers.
Peter looks back at the theater. Then at his watch. Then back
to the avenue.
PETER
It's not your problem, Pete. It's
the police's problem. It's not your
problem.
EXT. NINTH AVENUE - NIGHT
"CAR CHASE" SCENE (CC)
The car roars down the avenue, weaving in and out. The
cruisers in pursuit.
It's a rag-top; THREE GUYS. Two in the back with machine
guns. Oh, like Spider-Man didn't see that coming! Spider Man
flies elegantly through their fire. Snags the two shooters.
Pins them to light posts and hangs them out for the police.
22.
Now Spider-Man turns to the DRIVER. Lands on the car. Is
thrown off. Shot at. Keeps coming back.
In the end he crawls under the car, comes over top, webs up
the Driver's gun. Manages to get them both out just before
the car slams into a big construction site dumpster and
EXPLODES.
EXT. CONSTRUCTION SITE - NIGHT
TWO POLICEMEN come running over. Spider-Man lowers the poor
bastard down to them on a line, headfirst. They grab him and
cuff him. One leads him away. The other looks up at Spider
Man.
POLICEMAN 2
There's no way I can not arrest you
for that.
SPIDER-MAN
Duly noted.
He fires a web and swings back uptown.
POLICEMAN 2
It's a lot safer in jail, SpiderMan!
EXT. NINTH AVENUE - NIGHT
Spider-Man, swings back toward the theater. Spider sense
TINGLES. His head snaps left.
Atop a building nearby, the flash of a sniper's rifle. The
next instant a shot rings out. A bullet snips the dragline
neatly in two. It goes slack and Spider-Man falls out of the
sky. Spider-Man plummets to the ground.
A MOTHER is pushing TWINS in a stroller. Right under him.
Moving like a diver he twists around. Fires a web that snags
a small billboard across the street. He stops falling.
The webbing peels the entire top sheet off the billboard, in
a single piece. Peter falls the last four feet or so. Manages
to arrest his fall, slamming his shoulder into the pavement.
Nearly hits the TWINS.
MOTHER
Maniac! Idiot!
Peter stumbles to his feet. Two big BRUISERS rush him. One
carries a pair of heavy-duty handcuffs. They're on him.
They're big, but Peter handles them easily with a little fake
kung fu. Then he looks up.
23.
(CONT'D)
(CONT'D)
Scans the skies over Ninth Avenue. All quiet. There's nothing
there now.
TAUNTING MAN
(O.S.)
Hey, look. It's the ten million
dollar man.
Spider-Man looks down. And sees that a crowd has gathered
around him. Most just staring at him like hungry dogs.
TAUNTING MAN
We get five, six guys together, we
could take him. That's like, what,
two million apiece. Come on.
But he doesn't step forward. Nobody steps forward. Then a
little kid steps forward. Twelve or thirteen.
KID
You in for it now.
The kid hands Spider-Man an early copy of tomorrow's Bugle.
THE PHOTO PETER SOLD HIM TODAY(captioned SPIDER MAN ASSAULTS
NUN!!!) and THE HEADLINE:
WANTED -- $10,000,000 REWARD.
SPIDER-MAN
Ten million dollars. I should
arrest myself.
Bounds right over them and then into the night.
SPIDER-MAN
Give it your best shot, New York.
INT. MARTIN BECK THEATER — LOBBY - NIGHT
Peter comes tearing back in. The lobby's ominously empty. The
same usher stands there. Ready for Peter.
PETER
Tell me I didn't miss intermission.
In reply the usher just crosses his arms.
INT. THEATER - NIGHT
MJ is having a deep scene with the Monster and the Bride,
just before the tragic conclusion.
24.
(CONT'D)
At the back of the theater, one of the old ladies watches,
expressionless. Her friend is sound asleep.
EXT. THEATER - STAGE DOOR
Peter waits, watching the door. Some actors come out. Peter
perks up--no.
Then she's there.
PETER
MJ!
She sees him, is pierced through by the sight of him--and
keeps walking. He goes after her.
PETER
MJ. Please.
She keeps going. He takes her by the arm. She shakes it off.
She isn't going to even speak to him. On second thought-- She
turns back to him.
MJ
You know, when you said you wanted
to be friends, I believed you.
PETER
I do want to be friends.
MJ
Well, then you aren't a very good
friend, are you?
PETER
I tried, MJ. I got here. I mean, I
was a little late. They wouldn't
let me in.
MJ
But you missed everything! All of
it! Why didn't you come in at
intermission?
Peter doesn't know how to answer this; can't lie fast enough.
PETER
Well--there was an accident--in the
street. I went to get a picture
and--
She doesn't want to hear it. Starts away again.
25.
PETER (CONT'D)
MJ. I do want to be your friend.
I'm sorry. Please.
She looks at him. Is she softening? Peter will never know.
Renard comes out of the theater. Checks out Peter.
RENARD
Good night, MJ. You were wonderful.
Gives her a big hug. When he lets go, MJ is staring right at
Pete. Her look says, See? You could lose me. Renard gives
Peter the fisheye and then walks off.
PETER
MJ. You aren't-- are you...
MJ
Renard's just a friend. Why. Do you
wish I was seeing somebody? Would
you like to get rid of me and for
all?
PETER
MJ--
MJ
No. No, I think you enjoy this idea
you have that I'm going around
carrying a torch for you. Which I'm
not.
(beat)
No, I'm not seeing anybody, Peter.
But you know what? I might meet
someone. I might even fall in love
with somebody. Tomorrow. And then
nobody will be carrying a torch for
you. And then what will you do?
She's angry. He looks like he thinks she has a right to be.
PETER
MJ. You don't know. You don't know
how much I think about you. How
much I--
MJ
No, that's right. I don't know
anything. I've known you since the
first grade but I don't know
anything about you.
26.
Peter takes a step toward her. Looks into her eyes. Six
inches of air separates him from having her.
His PAGER goes off. He's embarrassed, fumbles with it.
PETER
Sorry. It's--oh. It's Aunt May.
She hardly ever pages me. I
better--
MJ watches him go. Typical.
EXT. PAYPHONE - NIGHT
Peter's on the phone, worried.
PETER
Aunt May? Aunt May, what's the
matter? Why are you crying?
INT. AUNT MAY'S HOUSE - SIMULTANEOUS
Aunt May's in her bathrobe, sitting at the kitchen table. Not
so quietly losing it.
MAY
What's the matter? I'm going out of
my mind, that's what the matter! I
can't take it any more!
EXT. PAYPHONE - SIMULTANEOUS
Peter is distressed.
PETER
Okay, okay, Aunt May, settle down.
I'm coming.
He hangs up, and runs back down to the alley where he left
MJ. But she's gone.
EXT. TRIBOROUGH BRIDGE - NIGHT
Peter races out to Queens on his lousy motorcycle.
INT. AUNT MAY'S HOUSE - NIGHT
Peter comes running into the house at top speed, tears into
the kitchen.
Aunt May's just sitting there, not crying. Scarily still,
holding a cup of tea, in a pool of light. Nice plate of
cookies beside her.
27.
PETER
Aunt May? What--
MAY
There's a fly.
PETER
A fly?
MAY
A fly, a bee, I don't know what it
is. Buzzing all around the house,
it's driving me insane! Who can
sleep with a racket like that?
PETER: Okay.
PETER
All right. I'll take care of it.
MAY
I tried to kill it myself, but I
can't. I don't know where it is.
Peter cocks an ear, his hearing spider-sharp.
PETER
It's in the bedroom on your lamp.
She gives him a look; how did he
know that?
INT. AUNT MAY'S HOUSE - BEDROOM
Peter steps into the bedroom and closes the door behind him.
His eyes dart to a porcelain shepherdess holding up a forty
watt bulb and a gilt-edged shade.
There on the shepherdess's bonnet perches a big fat juicy
fly. If we could detect such things, we would sense that the
fly feels a sudden alarm.
INT. AUNT MAY'S HOUSE - KITCHEN
Aunt May hears the THWING of Spidey's webbing and then a
SPLAT.
Peter emerges from the bedroom, looking satisfied.
PETER
Mission accomplished.
28.
MAY
I'm sorry, Peter. I know you must
think I'm losing my mind. It's
just-- your uncle always killed the
bugs around here.
PETER
He was a handy guy to have around.
(beat)
I never realized how much I
depended on his advice.
A beat.
MAY
Something on your mind?
PETER
Well--
MAY
You could talk to me, you know.
PETER
Yeah, I know that. But I--
MAY
Peter...
(taking a chance)
I've seen the change that has come
over you since Ben died. Everyone
has.
Peter looks startled. Guilty.
PETER
Change...? I don't... What do you
mean?
MAY
You have to grieve him, Peter. You
have to let yourself mourn.
PETER
Oh. Yeah.
(beat)
I wish I could.
MAY
What?
PETER
Oh--no, I mean, I know, you're
right.
29.
(CONT'D)
(CONT'D)
MAY
Sooner or later, Peter, you have to
let it out. It might as well be
now.
Peter nods. Sits down. Weight of the world.
PETER
I'm having a very hard day, Aunt
May.
She slides the plate of cookies over to him. He takes one.
Chews it. Sighs.
MAY
Go ahead. Cry.
PETER
No, Aunt May. I can't cry. I can't
mourn Uncle Ben. I don't have the
right.
MAY
Don't be silly, Peter. Of all
people--
PETER
Of all people, not me. You don't
know- everything there is to know,
Aunt May. About how Uncle Ben died.
The guy who-- that punk.
(deep breath)
I had a chance to stop him.
MAY What?
PETER
The guy. I ran into him. A couple
of hours before he shot Uncle Ben.
He was robbing this place. And I
knew it. And I could have stopped
him easily. But I let him run right
past me. Because at the time it
didn't seem like my problem.
She's just looking at him. Dry-eyed. A little confused,
maybe.
PETER
And then like an hour later, that's
when Uncle Ben was waiting for me
and this guy went up to him and...
30.
(CONT'D)
(CONT'D)
(CONT'D)
She sits a moment longer. Then she stands up and takes the
plate of cookies away from him.
MAY
Well, I guess I can understand how
you didn't want to tell me this.
Turns and dumps all the lovely cookies into the trash. Quiet
fury.
MAY
I mean, on the surface, it does
seem to be something fairly
unforgivable.
PETER
Aunt May?
She swings the china plate above her head, then brings it
down against the counter. It shatters.
MAY
Damn it!
She crouches stiffly and begins to pick up the pieces. Peter
goes to help her but she pushes him away. As she tosses
shards into the trash, she cuts herself.
MAY
Ow! Damn it.
Pokes her finger into her mouth. Peter tries to put his hand
on her shoulder.
MAY
Get away from me. Get out!
He backs away. She takes the Dustbuster from the broom closet
and begins noisily to bust dust. Steely eyed.
PETER
Aunt May--
She ignores him, vacuuming. He turns and walks out.
EXT. BQE - NIGHT
Peter roars back to the city. As he slows in some traffic,
the bike begins to backfire and throw sparks. Then it
actually bursts into flame. Fellow motorists honk at him. One
leans out of a passing car.
31.
(CONT'D)
FELLOW MOTORIST
Yo, butthead, your motorcycle is on
fire.
Peter scrambles over onto the shoulder. Leaps off the burning
bike. Contemplates the flames then starts to stamp them out.
This quickly devolves into a vicious kicking.
PETER
Stupid frigging piece of junk! Why
can't I have one thing in my life
that actually works!
Fellow motorists slow their cars to watch as Peter's spider
strength renders the bike a heap of junk in seconds.
PETER
Can't-- even-- cross town without
bursting into flames-- or being
shot at!
Peter stands over the corpse of the bike, heart POUNDING.
Then turns and starts to limp home along the median.
INT. OSBORN/PARKER APARTMENT — NIGHT
Harry is lying on the couch, watching a tape of Barbara
Walters interviewing the his father. With the aid of a shaker
of martinis. And a little amber prescription bottle.
THUMPING from outside, muffled through the blast shutter over
the door.
PETER
(O.S.)
Harry, god damn it, let me in!
Harry picks up the remote and punches in the code. The
barrier goes up. Peter drags his sorry ass in the door. He's
a wreck.
HARRY
I made martinis.
PETER
I see that.
Onscreen, Norman Osborn sheds a single shining tear. Harry is
crying, too.
HARRY
That's the only time that man ever
cried.
32.
(CONT'D)
(CONT'D)
(CONT'D)
PETER'S FACE
Oh, brother. Here we go.
He takes a deep breath, then sits down beside Harry.
HARRY
Have a drink. You look like you
could use one.
PETER
I probably could. But no, thanks.
He points to the bottle of pills.
PETER
What are those?
HARRY
Dinner. Courtesy of Dr. Chomsky.
PETER
I'm sure he doesn't want you taking
them with alcohol.
HARRY
She. No, you're right. She'd
probably be very disappointed in
me.
They sit and watch the tape of Norman Osborn. Now Norman is
his old in-control self again, telling Barbara Walters a
story. Barbara is laughing.
HARRY
Pete. Just tell me where to find
him. Tell me where you meet him.
That's all you need to do. I'll
take care of the rest.
Peter looks at him. Harry just keeps staring at the screen.
PETER
I can't. He broke off contact with
me. He said I've made it too
dangerous for him. He almost got
killed today.
HARRY
I know.
(beat)
Who do you think put up the bounty?
Onscreen, Norman Osborn is laughing, now, too. A strangely
familiar laugh. His goblin grin is reflected for a moment on
his son's face, mad glint of the TV in his eye.
33.
PETER
Bounty!
HARRY
I'm sorry, did I say bounty? I
meant reward.
PETER
Harry, what you're talking about
is--
HARRY
Murder? Maybe. People get murdered,
Pete. My father. Your uncle. It
happens.
The tape goes blank. Harry's eyes fill with static. Peter
gets up.
PETER
I think--it would probably be best
for me to move out.
HARRY
What? Because of what I said about
Spider-Man? Pete, don't be--
PETER
Mr. Aziz fired me today, Harry. And
I can't work for the Bugle anymore.
So. I can't afford to pay you rent
anymore.
HARRY
You'll find another job. I'll carry
you until you do, no problem.
PETER
I couldn't let you do that.
Harry sloshes upright. Grinning a twisted grin.
HARRY
No, that's right. You wouldn't want
to be a sniveling little do-nothing
freeloader. Like me.
PETER
Harry, come on. Let's not--ah,
forget it.
He starts to walk out.
34.
(CONT'D)
(CONT'D)
HARRY
Pete?
Harry sits up, drunk and stoned but still Harry.
HARRY
Well... where are you going to go?
Home to Aunt May?
PETER
No, I don't think I'm so welcome
there anymore.
He climbs up to his bedroom door. Tries to open it. Pushes
some buttons. Nothing happens.
PETER
Harry, could you please let me into
my bedroom?
INT. OTTO'S LOFT - NIGHT
Otto lies in a steaming bathtub, recuperating from his show.
Nice tub, good cigar. TV flickering in the wall.
On the news: His performance. Video coverage of the lecture,
of Otto strutting around the stage.
BOY TALKING HEAD
...potential applications, Octavius
said, range from handling nuclear
waste to detonating underwater
mines to the exploration of outer
space.
GIRL TALKING HEAD
Speaking of creepy crawlies, Jim,
it seems that Spider-Man is finding
New York to be a very tough town.
At the words "Spider-Man" Otto sits up in the tub. He leaps
out, dripping, and pads over to the television wall.
Otto hits the record button on his DVD-R. We see several
shelves of DVD archives arranged above the recorder.
On TV, the incident is reported. Jameson is there, ranting.
We see the headline about the reward. Then there's a shot of
Spider-Man scaling a wall.
Otto zooms in on it, watching with a scientist's eye.
The girl talking head comes back on.
35.
(CONT'D)
(CONT'D)
GIRL TALKING HEAD
It was a scene right out of All
About Eve tonight when a spokesman
for Deirdre Dunn announced that the
Broadway star, currently playing
the lead in the popular musical
Bride! would be taking a temporary
leave of absence for some well
needed rest...
Otto pops out the disk, fits it into its box, scrawls a
label. Files it on the shelf. We see that it is labelled:
SPIDER-MAN 5/24/04. All of the other disks are labelled the
same way. They go back for a year.
GIRL TALKING HEAD
...said that the role will be
played by Miss Dunn's understudy,
Mary Jane Watson.
Otto's attention is drawn to the screen again. MJ is being
interviewed, in makeup, backstage.
MJ
(ON TV)
Well, this is great opportunity for
me, but mostly I just wish for a
very speedy recovery for Deirdre.
Otto's gaze remains scientific, but somehow softened. Towels
off his hair, watching MJ's lovely face.
We pull back and reveal as we do so his four backjacks, each
capped with a rubber seal, glistening.
INSERT
The next day's Bugle: NEW YORK TO SPIDER-MAN: DROP DEAD.
EXT. NEW YORK STREET — NEWSSTAND - DAY
The newspaper sits atop a pile. THWIP! A fine mesh of
webbing spreads across the edge of the paper. The NEWSVENDOR
watches openmouthed as the paper is tugged gently skyward.
A dollar bill comes dangling down on a thin silky thread.
EXT. NEW YORK STREET - LAMPPOST - DAY
Spider-Man crouches atop the lamppost, scanning the paper.
Crumples it up. Head snaps to the left. TINGLE of spider
sense. A GUNSHOT. A SCREAM.
EXT. KOREAN GROCERY - DAY
36.
A THUG runs out with a sackful of money. Stuffs his gun into
his waistband.
A jet of webbing catches his left arm and pins it to the
wall. Another catches his right arm, then THWIP-THWIP each of
his legs at the ankle. He's pinned and struggling. He
drops the bag.
Spider-Man picks up the bag. Opens it and peers inside.
SPIDER-MAN
You shot someone for nineteen
dollars? That's--
Out of nowhere looms a huge OBJECT, heading for his skull. A
wet impact.
It's a WATERMELON, wielded by a pair of YOUNG MEN. A neat
stack of watermelons behind them.
Spider-Man wobbles. Sags.
YOUNG MAN
You're under arrest.
The GROCER comes running over. A bloody patch on his upper
arm. Picks up the bag of money. Screams at the young men.
GROCER
What's the matter with you? He's a
good guy. I'm sorry, Spider-Man.
Here.
He jabs the grubby pile of bills toward Spider-Man. A SIREN.
Spider-Man closes the Grocer's hand around the money.
SPIDER-MAN
(to Grocer)
Thanks.
As the police run up, Spider-Man takes to the sky.
EXT. QUEENS - FILIPINO CULTURAL CENTER - NIGHT
Dusk outside Bingo Hall. A black Volvo pulls up. Five HOODS
pile out and go running in.
INT. BINGO HALL - NIGHT
Two hundred frightened but outraged old Filipina ladies
relinquish their bingo money to the pillowcases of the hoods.
A thick strand of webbing lances in and SMACKS the gun of the
Lead Hood. Snatches it from his hand. Then swings it into
his temple, knocking him cold.
37.
SPIDER-MAN
Stands in the doorway, wielding the web like a lariat.
The gun flies through the air, conking the Second Hood on the
head, then the Third, Fourth and Fifth. They all go down in
under three seconds.
The old ladies turn to Spider-Man. Hard to read their
expressions. He waves his fingers.
OLD LADY
Ten million dollars!
They start toward him, and then they're on him, bludgeoning
him with their handbags.
INT. BINGO HALL - NIGHT
He stumbles free of them and then leaps to safety.
INT. JJJ'S OFFICE — NIGHT
JJJ's working late. Studying two alternate front pages. One
says: NOWHERE TO RUN TO, BABY. The other says: NOWHERE TO
HIDE.
CRASH!!!!! A blizzard of broken glass. JJJ ducks under his
desk as the avalanche comes down.
Spider-Man drops down through the skylight over JJJ's desk.
JJJ comes out from under the desk. Sees Spider-Man standing
there.
SPIDER-MAN
Got a minute?
JJJ picks up his phone. Punches a button.
JJJ
This is Jameson. Code S. Repeat.
Code S.
SPIDER-MAN
Is that S as in "shut the hell up"?
He slaps a gob of webbing across JJJ's mouth, then, in a few
seconds, encases him entirely. A slick pupa. Takes the
straw from JJJ's Big Gulp. Picks up the cocoon. Jams in the
straw about where JJJ's mouth should be. Garbled CURSING.
Spider-Man sticks the cocoon under his arm and leaps to the
38.
(CONT'D)
(CONT'D)
ceiling. Clambers across the newsroom, over the astonished
staff. Out a window, upside down.
EXT. ROOF OF BUGLE - NIGHT
Spider-man rips the cocoon away. JJJ starts to rant but looks
over the cornice and sees the street far below. Cringes and
pulls back. Afraid.
JJJ
I-- I'm acrophobic. Fear of
heights.
SPIDER-MAN
Really, I thought that was fear of
spiders.
(beat)
Look, Jameson. I'm fine with you
hating me. I'm even fine with you
slandering me. But getting me
killed, I don't know, that kind of
irritates me a little.
JJJ creeps carefully away from the edge.
JJJ
The Bugle didn't tell anybody to
kill you.
His courage returning. He starts to close in on Spider-Man.
JJJ
Look, pal. I'm not fine with
anything about you. You are a
danger to this city. You may not
believe in old-fashioned ideas like
due process and the rule of law,
but I do. You come in here with
your tight pants and your sticky
fingers and you tell us you're a
hero. But you know what I see? A
vigilante, a muscle man, a gangster
in spandex. What gives you the
right? Because you're the
strongest? That's not the country
I'm from.
JJJ has Spider-Man on the defensive--backing away.
JJJ
You know, I hired a psychiatrist to
do a profile of you. Did you see
that story?
(MORE)
39.
(CONT'D)
(CONT'D)
(CONT'D)
JJJ (CONT'D)
Did you read what that lady said?
"Delusionary." "Narcissistic."
"Messiah complex." Translation:
JJJ goes in for the kill.
JJJ
You need to get a life, pal.
A door SLAMS. A DOZEN SECURITY GUYS pour out onto the roof.
Spider-Man looks at them, then back at JJJ. Seems about to
speak. Then leaps over the side of the building, and is gone.
The security men run to the ledge.
JJJ
Where the hell were you? You're all
fired.
INT. OSBORN/PARKER APARTMENT - NIGHT
Peter has his stuff packed up; he's carrying out three
suitcases and big laundry sack. Harry comes out into the hall
to watch him go.
HARRY
So, that's it. You're just going.
Peter starts to say something, then just nods.
HARRY
Where?
PETER
I found a place out in Sheepshead
Bay.
As he goes out the door, the laundry bag tumbles from the
pile of suitcases. Peter stoops to pick it up.
HARRY
You don't have to take dirty
clothes. You can still do your wash
here, you know.
Peter shrugs.
PETER
I need the big machine.
INT. LAUNDROMAT - NIGHT
3 AM. Deserted. Peter sits in a plastic chair, reading a
thick tome entitled Biomolecular Chemistry.
40.
(CONT'D)
(CONT'D)
A pile of similar tomes beside him. Makes a note in a
notebook.
A YOUNG MAN enters, carrying a laundry sack. Sees Peter
sitting there. Peter doesn't look up. The man goes over to
a machine.
Spider sense TINGLES. Peter looks up as in slow motion the
man walks, KEYRING JINGLING, CHANGE in his pocket, earphones
THROBBING in his ears.
Slowly the fingers reach for the lid of the machine.
PETER
No!
The man gapes at him.
PETER
You can't use that one. That's my
machine.
The man decides that Peter is mad. He begins to stuff his
clothes back into the sack.
YOUNG MAN
Okay, mister. Take it easy.
He shoulders the bag and hurries out.
YOUNG MAN
The yellow light's flashing.
Peter waits a moment, then runs over to the machine.
The OUT OF BALANCE light is blinking. Peter lifts the lid.
Pulls out the red and blue suit, soaking wet.
INT. DR. CHOMSKY'S OFFICE
Harry sits facing Dr. Chomsky, a petite Korean-American
woman.
DR. CHOMSKY
Nightmares?
HARRY
Every night. Two of them, last
night.
DR. CHOMSKY
What are they about?
41.
HARRY
I didn't think you guys handled
dreams anymore. I thought that
dreams were just brain garbage.
DR. CHOMSKY
They are. But you can learn a lot
about a person by going through
their garbage.
Harry thinks. He closes his eyes.
HARRY'S NIGHTMARE
He's shaking hands with his father. They're both smiling.
Then with a horrible wet sound Harry splits open, right down
the center, and Norman Osborn steps out of the husk. The real
Norman starts to laugh his GOBLIN laugh.
BACK ON HARRY
He opens his eyes. Real pain in them.
HARRY
They're disgusting. I don't want to
talk about them. Just, please. Give
me something to help me sleep
through them.
The doctor stares at him. Sighs. Reaches for the prescription
pad.
INT. MARTIN BECK THEATER - AUDIENCE
Otto sits in the fifth row, center. Watching.
INT. THEATER - ONSTAGE
MJ sings her big number, "The Mind of the Man I Love."
INT. THEATER - AUDIENCE
Otto's entranced.
INT. MARTIN BECK THEATER - BACKSTAGE - NIGHT
MJ stalks offstage to lackluster APPLAUSE. Dissatisfied.
Renard follows right behind.
MJ
I sucked!
RENARD
You sucked not.
42.
(CONT'D)
INT. DRESSING ROOM - CONTINUOUS
MJ runs into the dressing room, flings herself onto a
battered sofa. There's a Bugle lying there; she tosses it
toward Renard.
MJ
The Bugle was right. I do "manage
to be both overstated and paperthin at the same time."
RENARD
Someone doesn't agree with you or
the Bugle.
He points to a big bouquet of black roses, with a card. She
goes to them, intrigued, charmed, irritated all at once.
Opens the card.
MJ
If Peter thinks he can...
THE CARD
It reads: I THINK YOU ARE BRILLIANT.
O.O.
MJ "O.O.?"
RENARD
Oh oh.
EXT. MARTIN BECK THEATER - NIGHT
MJ is walking out, carrying the flowers. Otto approaches, but
keeps a certain distance. He doesn't want to frighten her.
He's dressed with a sharpness that is only slightly funereal.
OTTO
Miss Watson?
She turns, startled but somehow having expected it, too.
OTTO
I'm Otto Octavius. I--I sent you
those flowers.
MJ
Oh oh.
OTTO
I hope that wasn't out of line. Was
it? It was. Excuse me. I'm sorry.
43.
(CONT'D)
He turns and walks away. Shaking his head. Not so much
embarrassed as disturbed by the failure of his experiment.
MJ
No! I mean--
OTTO
I won't bother you again.
MJ
Wait!
Slowly Otto turns back.
MJ
I loved the flowers. I've been sort
of hoping somebody might send me
flowers.
OTTO
Peter Parker?
MJ
Yeah...? How do you...?
OTTO
Peter's a friend. Of a friend.
Honestly, I don't really know him
very well at all. But he's the one
who told me about you. About your
being in this show. Which I loved.
It was beautiful. You were
brilliant, I meant it.
MJ
Thank you. Unfortunately the drama
critic of the Daily Bugle doesn't
agree with you.
OTTO
The man is a well-known idiot.
MJ
Really?
OTTO
Legendary.
She likes this. The bubble of weirdness between them pops. We
can almost hear it. MJ salutes him with the roses.
MJ
Thanks for these.
44.
MJ and the roses go very well together. Otto stares. Inner
turmoil visible. A long beat goes by. She turns to leave.
OTTO
Do you believe in the value of
boldness, Miss Watson?
MJ
At all times.
OTTO
Have dinner with me. Right now.
MJ hesitates. Not because she doesn't want to; because she
does. This is a big yes for her.
MJ
Where did you have in mind?
OTTO
There's this Ethiopian place on
West 47th.
MJ
Ethiopian. Wow. I've never--
He wiggles his long elegant fingers. Faintly but disturbingly
tentacular.
OTTO
I like to eat with my hands.
INT. MESKEREM ETHIOPIAN RESTAURANT - NIGHT
A lovely server settles an enormous platter of doro wat and
other fine and strange foods before them. Otto is delighted
to see it. MJ less sure.
OTTO
Yum. Look at that.
MJ
It's very... colorful.
Otto digs in. After a moment MJ tears off a piece of njera
and joins in. Warily. Otto watches her. She looks right back
at him.
OTTO
Well?
MJ
Strange but good.
45.
OTTO
You were telling me about your
mother.
MJ
I know I was, and I'm sorry. Let's
talk about you. You seem like a
much more interesting person than
me.
OTTO
Not to me.
(self mocking)
Not right now, anyway.
INT. RESTAURANT - LATER
They are sitting closer to each other. She's finishing a
story. It's supposed to be funny but he just nods, serious.
OTTO
And did you have a dog?
MJ
When I was little. Tasha. She--no.
I am not going to tell you about my
childhood pets. That's enough. It's
your turn. Tell me about what you
do. It sounds fascinating.
OTTO
I could describe it to you. But you
would never believe it.
MJ
Try me.
OTTO
I'll tell you what. Come uptown.
Right now. I'll show you the lab.
I'll show you the rig.
MJ
Oh, I couldn't--
OTTO
Boldness in all things.
INT. ANANSI PROJECT LABORATORY - NIGHT
The darkened laboratory. Machines softly interrogate one
another. KEY in the door. Slash of light.
46.
All the lights go on as Otto ushers MJ in. She notices the
rig right away. It hangs in its dock, a malign orchid.
MJ
Is that it?
Otto is in love with the rig, of course. The way that a man
might be in love with a ship, or a 1971 Chevrolet Barracuda.
OTTO
That's it.
She gets that he has feelings for his machine.
MJ
It's beautiful.
(beat)
It's a little freaky.
OTTO
Well, I'm a little freaky. You
should probably know that about me.
MJ
Okay.
THE RIG
One of its heads. The one with a somehow crafty expression in
its staring black sensor.
POV - THE RIG
As Otto "comes out" to MJ.
OTTO
I am not like other people, MJ. I'm
not like anybody you've ever met.
Freaky, yeah, I'm a freak of
nature. I taught myself calculus
when I was nine. I was a chess
grandmaster at fifteen. I don't
say it as a boast. It was hell on
earth. I had to fight every day of
my life.
MJ
I knew a kid like that.
OTTO
But there was always that one
pretty girl who also managed
somehow to be nice. I'll bet that
was you, huh?
47.
(CONT'D)
(CONT'D)
(CONT'D)
MJ looks away, smiles.
THE RIG
Deep in its sensor, a diode pulses. Now it's watching MJ.
OTTO
Today, I'm all right with it. I've
learned to embrace being a freak. I
accept that I was given the gift of
intelligence for a purpose. Which
is this thing you see. The rig.
Otto's Octopus.
He goes over to it. Takes hold of one of its hands. A touch
of the bridegroom.
MJ
What does it, well... do?
OTTO
Oh, it cuts hair.
She laughs.
OTTO
What does it do? It improves you.
It makes you better.
MJ
You mean it makes you stronger?
OTTO
Stronger, faster, yes, but also
smarter. Much smarter. When I'm
jacked in, I feel like my grasp
finally equals my reach. I can feel
myself--expanding. Not just my
physical grasp but my mind, my
heart, my soul. I feel enlarged by
the experience. And it feels right.
Have you ever felt anything like
that?
MJ
I thought so. One time.
She goes over to the rig. Slowly extends her fingers toward
the nearest head. As her fingers draw nearer the diode pulses
and we begin to fear for the fate of her fingers. Her
fingertips touch-- the eye goes dark.
MJ
When you say "jack"...
48.
(CONT'D)
(CONT'D)
OTTO
There are four shunts that
interface directly with my central
nervous system. I wear it. But it's
also wearing me.
He reaches up and takes hold of the latch, with its spirit
level bubble.
OTTO
This is the neural integrity seal.
The latch, basically.
MJ
Does it hurt?
OTTO
The system delivers a steady dose
of pain blocking endorphins the
whole time I'm in it. Which so far
has never been longer than a few
hours. The goal is a permanent
interface. Of course the idea
of a permanent human/machine
integration makes some people
uneasy.
Granted, MJ's looking a little uneasy. Otto fingers the
Latch.
OTTO
The Rig is designed to seek to
implement a systems merger with the
host. Unfortunately, so far, my
flimsy human tissue's not up to the
challenge. Not yet. We're working
on that.
MJ is freaked, and fascinated.
MJ
So you have, like... holes? In your
back? Permanent ones?
OTTO
Want to see them?
Daring her, a little bit.
MJ
Not really, but yes.
He turns. Unbuttons his shirt. Lowers it. Four black glinting
discs in his back. Freaky but beautiful.
49.
MJ (CONT'D)
Whoa! Okay. Thank you. Very nice.
He pulls up the shirt, rebuttons it, turns. Shirttails
hanging out.
OTTO
It's late.
MJ
It is.
A DOORBELL PANEL
A FINGER scans the names. Stops at WATSON. Press the BUZZER.
EXT. MJ'S APARTMENT BUILDING - NIGHT
Peter's standing there. Dressed up. Holding a single red
rose. He waits. There's no answer. He checks his watch; it's
late. Then cue the TINGLE of spider-sense. He whirls, hears
FOOTSTEPS, VOICES.
MJ and Otto approach the building. Peter's face as he
registers the voices: alarmed.
REVERSE ANGLE
On the front step as MJ and Otto approach. Peter's not there.
MJ turns to Otto, carrying the big dark bouquet.
MJ
Thank you. I had a really nice,
really interesting time. And thank
you for the flowers.
PETER PARKER
Clings to the side of her building, upside down. Takes the
single cheap rose from his teeth. Looks at it.
OTTO
So, maybe it's out of line. For me
to ask you this. But I don't want
to make a fool of myself. Are you
seeing Peter Parker? Because if you
are--
MJ
No. I was. But he wouldn't... He
couldn't... He just couldn't.
OTTO
It's really none of my business.
50.
(CONT'D)
But he looks pleased with the information. He holds out his
hand.
OTTO
Good night.
She takes his hand, then plants a kiss on his cheek.
 PETER
Watching the kiss. It's breaking his heart.
MJ
Turns and lets herself into the building.
INT. MJ'S BUILDING - LOBBY - NIGHT
She presses herself against the door. Stunned at her own
brazen behavior.
EXT. MJ'S BUILDING - NIGHT
As Otto turns and starts back across town. A skip in his
step. A cybergoth Gene Kelly. Feels like dancing with a
lamppost.
EXT. LAMPPOST - NIGHT
As Otto walks through its beam we notice a dark shape
crouching on the stanchion. Watching.
EXT. SCIENCE BUILIDNG - NIGHT
The domed building where it all began for Peter. A shadow
from the shadows leaps onto the domes. It's Peter.
INT. SCIENCE BUILDING - NIGHT
The great central hall. It's deserted and dim. He walks
around. Hears echoes of that afternoon a year ago.
The spider cages are empty.
He looks down at his hand where the spider bit him, rubs it.
Thoughtful, then his face breaks. He sits down, buries his
face in his hands. Chokes up.
A WHIRR; he looks up, TINGLING.
INT. ANANSI PROJECT LABORATORY - NIGHT
Peter creeps down the hall just outside. We HEAR the
unmistakable WHIRR of the rig.
SERIES OF SHOTS - COUPLING THE RIG
51.
(CONT'D)
1) Otto lowers the Rig into position.
2) The Rig watches, expressionless.
3) Otto steps into the Rig. Engages the coupler. A WHINE of
hydraulics.
Otto reaches back to twist the Latch. Can't quite see what
his fingers are doing.
His fingers can't reach. Can't reach. He strains, grunting.
Gives up. Starts to press the decoupler. Then--
--a 'pod reaches in for the Latch and TWISTS IT.
Otto flinches, then lets go as blessed relief floods his
features. Sinking in. The irises of his eyes spiral out.
One of the 'pods reaches toward his face and, tenderly,
strokes it with steely finger.
Peter, watching, GASPS.
The 'pods hone in on the sound at once, quivering. Otto looks
over.
OTTO
Who's there?
Peter steps out of the shadows.
OTTO
Parker?
PETER
Hi.
OTTO
(rattled)
What the hell are you doing here?
PETER
I wanted to talk to you. But I see
you're--what are you doing?
OTTO
I was just--uh. Celebrating.
PETER
You use that thing...
recreationally?
OTTO
It helps me relax.
52.
INT. ANANSI PROJECT LABORATORY - NIGHT
Peter sits across a desk from Otto. One 'pod puts on a CD.
Two others are busy pouring two cans of Coke. Peter eyes the
'pods warily. Otto taps at the keyboard of his computer.
OTTO
The viral delivery system we were
using in the superspider project.
PETER
That's right.
Otto hits a few more keys.
OTTO
That's why you came here.
PETER
What other reason would there be?
Otto shrugs.
OTTO
Here. Yes, we were using a modified
arbovirus. Highly infectious in
spiders. We replaced the nucleonic
RNA with whatever we wanted to code
for and the virus did the rest.
PETER
Is this arbovirus infectious in
humans?
OTTO
It could be. If we had wanted to
introduce spider material into a
human, I suppose we could just have
just gotten one of the little
critters to bite--
Staring at Peter. Understanding without knowing.
PETER
What?
POV - THE RIG
It watches Peter and Otto, pulsing softly.
OTTO
Why do you want to know?
PETER
I'm just curious.
53.
As Peter says these words:
They are processed by the suit; it subjects them to a
VISUAL VOICE-STRESS ANALYSIS
The pattern is scanned and designated COUNTERFACTUAL.
AN INDICATOR begins to blink on one of the pods.
AT OTTO'S WORKSTATION
The ROUTER begins to blink in kind.
ON THE MONITOR
Windows pop up, running archive footage of Spider-Man:
climbing, swinging, leaping.
Another window: Superspider Inventory: 1 through 15. Number
15 flashes: LOST.
But Otto's not even looking at the monitor; he doesn't need
to.
OTTO
Spider-Man's a friend of yours,
isn't he?
Peter starts to play the question off.
PETER
No, not a friend--
OTTO
Know anything about him?
PETER
Not much. Kind of a quiet guy.
OTTO
Know if he was ever bitten by a
spider?
PETER
He might have been. I wouldn't
know.
OTTO
We lost a spider. If, by chance, it
bit him. Is that what happened? And
transferred the viral genotrope in
its venom...
He's advancing on Peter now. The 'pods billow and arc.
54.
OTTO (CONT'D)
That's great! It's a conceptual
breakthrough!
PETER
Not to him, it isn't. He's sick of
it. That's why I came to see you.
To see if there's any way to--
OTTO
Why didn't he just come himself?
PETER
Huh? Oh, because. He's, uh,
horribly disfigured. Up close.
That's why he wears the mask.
(shudders)
It's like, he has these little
hairs all over him, and compound
eyeballs. And the smell!
OTTO
Unfortunate. No way to control the
process, I suppose, relying on a
bite.
(beat)
He could probably use one of these
eventually.
He reaches into a tray behind him. Holds up a tiny ziplock
bag with a speck inside. Peter leans in to look. A tiny bit
of circuitry--a spider-mite of silicon.
PETER
What is it?
OTTO
It's basically an immune system on
a chip. You seed it with a sample
of the material you want to defend
against, and it pumps out antigens.
I call it a parity chip.
PETER
Parity?
OTTO
Equilibrium. The Rig is so
powerfully integrative that right
now it overwhelms my own systems.
I'm hoping to use this to boost my
body's immunity.
(MORE)
55.
(CONT'D)
(CONT'D)
OTTO (CONT'D)
In theory your friend could seed
this with some of his own
spiderized DNA, implant it, and
knock out the genes that are coding
for his spider traits.
He tosses the chip back onto the tray.
OTTO
This is just a prototype. We're not
in fab yet.
Peter regards the tray, the little baggie. There it is. His
salvation. His eyes stray up to:
AN AIRVENT IN CEILING
Conveniently located just over the tray.
OTTO
I had dinner with Mary Jane Watson
tonight.
Peter looks back, caught by surprise.
PETER
Oh. Yeah. I know.
OTTO
Terrific girl.
PETER
Agreed.
INT. ANANSI PROJECT LABORATORY - NIGHT
The Rig is back in the coupler. Otto is at his workstation,
asleep in his chair. All quiet.
THE AIRVENT
A tiny thread drops from it. Weighted with little suction
cup of webbing.
The little fishing line drops into the tray. Bounces. Misses
the baggie. Bounces again. Snags it.
THWIP! The baggie shoots up into the air and through the
slats of the vent.
INT. VETERINARY SUPPLY STORE - DAY
Peter walks in, trying to appear nonchalant.
56.
(CONT'D)
CLERK
Can I help you?
PETER
Yes, hello. I need some soft tissue
xx. And a Y-gauge syringe.
CLERK
A Y-gauge... what are you trying to
treat, a rhinoceros?
PETER
A spider.
(beat)
Really big spider.
INT. DITKOVICH'S HOUSE - PETER'S ROOM - NIGHT
Peter drops a box filled with lab supplies onto his tiny
desk. Sweeps everything off the top of it.
INT. DITKOVICH'S HOUSE - LIVING ROOM - NIGHT
A tiny house in Brighton Beach. DITKOVICH is playing cards,
for money, with his Ukrainian cronies. HUGE CLATTER. They all
look up at the ceiling. Then at Ditkovich.
DITKOVICH
(in Ukrainian, subtitled)
The new roommate.
They go back to their game. SOMETHING BREAKS. Ditkovich lays
down his cards with a sigh.
DITKOVICH
(in Ukrainian, subtitled)
I think he took my vodka.
INT. DITKOVICH'S HOUSE - STAIRS - NIGHT
Ditkovich calls up as we climb the stairs and start down the
upstairs hall.
DITKOVICH
Mr. Parker? Everything is all
right?
INT. PETER'S ROOM - NIGHT
Peter is wiping down the glass surface of the desk with
Clorox. We see: gauze pads, adhesive tape, alcohol, pipette.
A hot plate with a saucepan of boiling water. A box of
Morton's kosher salt. A bottle of vodka.
57.
(CONT'D)
PETER
Yes! Everything's fine! Sorry!
He decants some of the steaming saline into a tube.
He picks up the pipette, scrapes at the inside of his cheek.
Then he picks up the chip with a clasp. Smears the tissue
against the chip. Drops it into the tube.
Holds up the BIG NEEDLE. Jeez. Pokes it down into the tube,
and draws in the fluid. The chip is sucked in along with it.
He stares into the whirling fluid in the syringe.
SERIES OF SHOTS - THE SYRINGE
In its swirl:
1) Spider-Man careens like a maniac through Greater Manhattan
airspace.
2) Peter Parker sits despondent in Otto's laboratory, head in
his hands.
3) He crouches at the side of Ben Parker, watching him die.
BEN
(O.S.)
I thought I'd taught you the
meaning of responsibility, Peter.
At least by my death. That's the
part of all this that makes me the
saddest.
Peter turns. Uncle Ben is sitting on the bed behind him.
PETER
You don't know what it's like,
Uncle Ben. You don't know how it
feel to be such a freak of nature!
Okay, with great power comes great
responsibility. I get that.
But you know what comes with no
power? No worries. No guilt. No
freak show!
With his free hand he pours a shot of vodka. Tosses it back.
PETER
I'm not going to lose Mary Jane
because of Spider-Man. I can be
Spider-Man, or I can have a life. A
normal life.
And drawing a deep breath he jerks up his shirt, baring his
hip.
58.
Pops the needle under the skin. Squeezes. It hurts. A lot.
His eyes roll back in his head.
INT. DITKOVICH'S HOUSE - LIVING ROOM - NIGHT
CLINK of coins. A muffled THUD from above. Play stops.
Ditkovich starts to say something. Changes his mind.
DITKOVICH
Hit me.
INT. PETER'S ROOM - NIGHT
Peter wakes up on the floor. Sits up. Hand to his hip; a tiny
dimple under the skin.
He checks himself out in the mirror. Strong. Fit. No visible
difference. He frowns, then leaps up into the air. Completes
a half-flip, and sticks feet first against the ceiling. Damn.
He dresses with care, buttoning his neat civilian clothes.
Then he goes to the closet. Crouches down, opens a panel in
the closet wall. Takes out a little rolling suitcase with a
picture of Wolverine. Unzips it:
The red and blue suit, neatly folded.
EXT. FAR BROOKLYN - VACANT LOT - DAWN
Still dark. Peter carries the suitcase down a deserted
street and then out into a swampy waste. In the distance,
HOMELESS MEN around a burning steel drum. Here, a steel drum
standing alone.
The suitcase CLANGS against the inside of the drum. Peter
takes out a can of lighter fluid.
Douses the thing liberally, then strikes a match. HUGE,
STUPIDLY HUGE FIREBALL.
Peter leaps to one side. Kicks over the drum. Flame scatters
everywhere. He jumps around trying to stamp them out. Faraway
LAUGHTER from the men.
Peter picks up still-intact suitcase.
PETER
Ouch!
He shakes the costume out of the smoldering case.
Picks it up off the ground, stares at it. The dead eyes of
the mask stare back.
59.
He stuffs the thing into the steel drum and walks away. Does
not look especially unburdened.
EXT. VACANT LOT - ANOTHER VIEW
A HOMELESS MAN watches Peter walk away from the drum.
He tacks a little unsteadily across the lot toward the drum.
INT. SUBWAY CAR - DAY
Peter riding in a subway car, smudges of black on his face.
Nearest him sits A YOUNG WOMAN in scrubs. Near her are a
couple of MEN. They're staring at her. Peter sees it.
MAN
Hi.
YOUNG WOMAN
Hello.
MAN
I'm Jack. I said, Hi. I'm Jack.
The woman was trying to ignore him. She blushes.
Peter's spider sense TINGLES as he watches.
SECOND MAN
You don't got to be rude, bitch.
Peter, sweating. His fingers flex. His lips narrow. His eyes
meet the second man's.
The train pulls screeching into the station. The doors open
and the girl slips out. The men stand up as if to follow her,
then sit back down. They laugh.
One of them flips Peter off. Peter looks away.
INT. DAILY BUGLE - JJJ'S OFFICE - DAY
The homeless man stands across the desk from JJJ. Carrying
the charred husk of the suitcase.
JJJ
I hope you don't have the head of
an extraterrestrial in there.
HOMELESS MAN
No, sir.
JJJ
Because if you do, you're the third
guy this week.
60.
(CONT'D)
(CONT'D)
(CONT'D)
The homeless man unzips the bags and yanks out the costume.
It's blackened and crumpled but still gorgeous. Real.
JJJ
Where the hell did you get that?
HOMELESS MAN
This guy left it in the garbage.
Out in New Lots. First he tried to
set it on fire.
JJJ
Set it on fire?
He takes the costume and shakes it out by the shoulders.
Turns it this way and that. Then he grins.
JJJ
He's out. Thrown in the towel!
Abandoned his sad masquerade! He--
A dark thought occurs.
JJJ
That loser! Quitting on me! In the
middle of the best damn story I've
had in thirty years! If I hadn't
already crushed him, I'd crush him
again just for giving up on me!
JJJ is forgetting his visitor.
HOMELESS MAN
Uh, mister...
JJJ
Wait a minute. What kind of idiot
does he think I am? A burnt
costume! How heavy-handed can you
get? Sure, he wants everybody to
think he's quit. When, in reality,
he's just going underground.
Inventing a whole new identity for
himself!
HOMELESS MAN
Mr. Jameson, please, I'm hungry.
JJJ haggles, but his heart's not in it. He's staring fixedly
at the Spidey suit.
JJJ
I'll give you fifty bucks.
61.
HOMELESS MAN
A hundred.
JJJ
Seventy-five.
EXT. UNIVERSITY - DAY
Peter comes up out of the subway, carrying a knapsack. Part
of a stream of other students.
Walks past an alley, sees THREE MEN standing together. None
of them savory looking. Two are clearly threatening the
third. They rifle the pockets of his jacket. They snatch a
little parcel. Slap him.
Peter's face, wrestling with the problem. Should he do
something? He takes a deep breath and keeps on walking.
Hesitant at first, then steadily.
INT. JJJ'S OFFICE — NIGHT
Late editorial meeting. The costume hangs conspicuously from
the door. STAFFERS keep sneaking glances at it as JJJ
harangues them.
JJJ picks up a front page proof. Headline: SPIDEY PLAYS
POSSUM!
JJJ
Spider-Man has put himself into a
one-man witness protection program.
He's in hiding. And it's going to
be my personal mission, and yours,
to root him out! Expose him to the
light! There's no hiding from the
truth, let's show him that!
(beat)
That's all I have so far. You
people figure out the rest.
They all get up and file out. Some groans. ROBBIE ROBERSTON
turns as he's leaving, pausing by the costume. Sniffs.
ROBBIE
Lighter fluid.
He goes out. Shuts the door.
Jonah goes over to the suit. Regards it. Leans forward.
Sniffs it. A weird idea comes into his brain. He starts to
unbutton his shirt.
62.
INT. JJJ'S OFFICE — NIGHT
We're watching him, maybe through the window. He pulls the
mask down over his head, completing the costume. Naturally
it's not a perfect fit.
He poses stiffly, movements awkward. Then he catches sight of
himself in a mirror. Strikes a pose. Another.
A parody of Spidey's characteristic moves. Finally he does
the upside-down hook'em horns webshooting thing. We leave him
having a shameless amount of fun.
INT. DITKOVICH'S HOUSE - DINING ROOM
The next morning Peter wakes up in bed. Sits up, blinking,
pressing at his hip.
He picks up Biomolecular Chemistry. Holds it close, far,
close. Readable but a little blurry. He smiles.
Gets out of bed. Maybe he's shrunken a bit.
He goes over to a wallpapered wall and lays his palm against
it. It slides a quarter inch; he smiles. It sticks. He
frowns. He creeps up the wall and onto the ceiling. Hangs
there. Drops onto the floor. Not yet.
He FIRES a strand of web. It shoots clear and thin. Then
weirdly it SPUTTERS. FOAMS UP.
He shakes his hand at the wrist. Shoots again. Another clear
strand shoots out and hits his knapsack. Jerks it back to
him. But something is changing.
PETER
It's working.
He's delighted.
INT. DITKOVICH'S HOUSE - STAIRS - DAY
Peter comes flying down the stairs.
PETER
Ditkovich! Ditkovich!
He gives an exuberant little kick at the bottom of the
stairs. Loses his footing. Falls on his ass.
Ditkovich looks down at him. Peter's not even embarrassed.
63.
(CONT'D)
(CONT'D)
PETER
What a klutz, huh?
(grins)
I need to use the phone.
INTERCUT - PETER AND MJ
MJ is doing yoga. In Downward Dog pose when the phone rings.
MJ
Hello?
PETER
MJ? It's Peter. I-- I want to see
you.
She doesn't say anything.
PETER
I want to take you out. After your
show. Tonight. I thought we could
have dinner. I've made a few
changes.
MJ
I can't, Peter. Even if I wanted to
see you. Which I'm not totally sure
that I do. I already have plans.
PETER
With Otto Octavius?
She's taken by surprise by this.
MJ
I don't think that's any of your
business, Peter. Goodbye.
She hangs up, leaving Peter looking puzzled.
INT. ANANSI PROJECT LABORATORY - NIGHT
Otto's singing in the shower. The shower is actually a
hazmat-exposure rinse. He towels off. Singing "Tonight" from
West Side Story.
In his exuberance, he is being WATCHED by the Rig. After a
moment he approaches the Rig. Reaches up to touch it.
OTTO
(just kidding around)
You jealous? Silly thing. You know
what you and I have is special.
64.
(CONT'D)
(CONT'D)
A moment of doubt.
OTTO
Actually, I almost wish I could
take you with me. Don't feel like
quite such a fool with you around.
Must be the endorphin push.
He looks around. Peels off his shirt.
INT. MARTIN BECK THEATER - STAGE - NIGHT
MJ's on stage, singing. We do a kind of Citizen Kane rise up
into the catwalks high above the stage.
Peter Parker dangles by a thread. Upside down. Listening as
MJ's voice rises.
INT. QUEENS HOT DOG STAND - NIGHT
Otto and MJ carrying a couple of dogs apiece toward the
counter. It's very crowded. Otto's wearing his long coat.
MJ
Thanks for indulging me. I know
it's a long way to come for a hot
dog. But these are the best.
OTTO
I've never been to Queens before.
Otto stumbles. Two 'pods shoot out of the bottom of his coat
and arrest his fall.
He rights himself, blushing. No one has noticed but us. He
takes a bite.
OTTO
It's a very good hot dog.
MJ
I really needed it.
OTTO
I'm sorry the show's not getting
any easier for you.
MJ
It's like there's this pane of
glass between me and the audience.
They can see me and hear me, but
they can't feel me.
65.
OTTO
I don't agree. I think you're the
most marvelously expressive
performer I've ever witnessed.
MJ beams for an instant, then cracks up, then looks at him.
MJ
You're sort of gaga over me, aren't
you?
OTTO
Sort of. I hope that's okay.
MJ
I think so.
OTTO
I know we haven't known each other
for very long. But I--
He winces, and reaches involuntarily for his side.
MJ
You okay?
OTTO
Bad back.
Through the plate-glass windows we can see Peter watching
them from out on the street.
EXT. STREETCORNER - NIGHT
Otto and MJ stand a foot apart.
OTTO
So what do you want to do, now?
MJ
I don't know.
OTTO
Would you like--
(flinches)
Would you like to come to my place?
My home, this time. Not my lab.
I've been working on a Mozart trio.
MJ (confused)
You have another Rig at home?
Oops.
66.
(CONT'D)
OTTO
Well, sort of. You see--
TWO BIG BAD MEN pass. One bumps into Otto. Kind of hard.
OTTO
Hey, watch it, man.
The BBM ignores him. Otto starts after, with those freaky
octopus eyes.
MJ
Otto...
Otto seems to rise up, weirdly looming.
OTTO
I don't know why human beings
persist in believing that mere
physical bulk confers some sort of
evolutionary advantage.
The BBM feels a tap on his shoulder. It's a 'pod, natch.
MAN
Yeah?
The 'pods snake out around Otto, fatal and alert.
On MJ
She looks fully as if the flesh of the guy that she's sort of
getting a crush on has suddenly sprouted four steel arms.
Otto and the faithful Rig make short work of the two men.
Otto turns back to MJ, hanging in the air. Aglow with the
work out. Hurricane eyes. SIRENS in the distance.
OTTO
We wanted to show you what we are.
EXT. STREETCORNER - ANOTHER VIEW
Peter is watching from a distance as Otto bursts out into
strange bloom.
PETER
Oh oh.
Starts to run toward them. Then stops. Looks around. Sees:
EXCELSIOR SOUVENIR SHOP
He dashes in and looks around. Finds a Spider-Man replica t
shirt.
67.
Grabs it, and a Big Apple ski mask. Runs out of the shop with
the SHOPOWNER running after him.
As he runs he pulls on the long-sleeved T-shirt and mask.
EXT. STREETCORNER - ON OTTO AND MJ
The arms retract and Otto comes to her, his clothing in
tatters. She backs away. Turns. Tries to run.
A 'pod lazily retrieves her. Whips her around.
OTTO (plural voice)
Look at us!
She meets his gaze. He looks tenderly at her. SIREN getting
louder.
OTTO
(normal voice)
You're so lovely.
The fingertip of the 'pod strokes her cheek with the same
tenderness. Ick.
MJ
Get away from me!
She tries to duck free of the 'pod. He won't let go.
SPIDER-MAN
(O.S.)
Let go of her.
Otto turns. Sees Peter standing there. Laughs.
OTTO
We're out of candy, kid. You'll
have to TP the house.
SPIDER-MAN
Put her down!
He flies at Otto. Otto sidesteps him and, reinforcing his
grip on MJ, starts to flee up the side of a building. On top
of the building they start to fight.
A leaping pursuit across the rooftops. Elevated tracks in
the distance. On the next to last rooftop before the tracks,
Otto turns. The fight begins.
It's not a fair fight; Otto his hampered by holding MJ.
Otto looks at MJ: reproach in his eyes. Then he sets her
gently down. And leaps over to the next building.
68.
Spider-Man goes to MJ. She shakes his arm.
MJ
Go get him. Please. He's not bad.
Peter peers at her through the eyeholes of the ski mask.
PETER
Do you...Do you love him?
MJ
He's my friend. He's angry. And
dangerous. Please, Spider-Man.
Don't let him hurt himself.
Spider-Man nods. And goes after Otto. Chases him across the
last rooftop before the tracks. Otto hesitates on the ledge.
Spider-Man flies at him headfirst. HITS and they both tumble
over the side of the building.
"TRAIN SEQUENCE" (TR)
They fall onto the elevated tracks that run alongside the
building.
A train is passing at that moment. They smash down onto the
top of it and are carried along the rushing tracks.
Otto rights himself. Gets to his feet.
OTTO
I'm ready. Come on.
Spidey rises and then it's basically a five mile long version
of King of the Hill, at high speed. Or maybe the myth of
Sisyphus. Otto digs at the head of the car, and Spidey comes
after him. And Otto throws him off, and Spidey comes after
him.
Every time he falls off the train, something worse happens to
Spider-Man than the time before. It's brutal. But he always
climbs back on.
At one point Spidey manages to get right onto Otto's back. He
gets his hand in at the root of the 'pods and grabs hold of
the Latch. Pulls on it. It SNAPS and swings free. Still
attached. But useless. And Otto HURLS him off the train.
Spidey climbs back on.
After the Latch busts, Otto just keeps getting stronger. But
we notice that Spidey seems to be tiring. He's winded.
So it makes Otto angry that Spidey keeps on coming. He knocks
Spidey off again, and then smashes in the window of the car
beneath his feet, reaches in with his 'pods.
69.
He starts yanking people right out and tossing them to the
side. Spider-Man snares them all in webs. The last time, his
webbing SPUTTERS before it fires.
Finally Otto rips the controls right out of the car. Then he
jumps off the train. Spider-Man wants to go after him.
But the train is now hurtling out of control. He can't just
leave it.
He stays. And it's a good thing, because a big L-bend in the
tracks is coming up. And the train is going much too fast to
take the turn.
Spider-Man manages to get all the passengers evacuated to the
rear half of the train.
Then he gets behind the first three cars (now empty), right
in down between, and cuts the lead ones loose. Gives them a
mighty push. They race ahead, smash through the guard rail,
and PLUNGE over the side of the elevated.
Now Spider-Man has to stop the part with the PASSENGERS. He
jumps down in front of the car that's now the lead. Plants
his legs against the speeding track itself. Railroad ties
SNAP-SNAP-SNAP and the momentum slows. But not enough.
Finally, web SPUTTERING, at the very limit of his strength,
Spider-Man strings his own body between buildings with
webbing, making himself into the focus of a giant slingshot,
with all those tons of train shoving right up against him.
And the train slows. And slows. And slows. And stops. The
Passengers CHEER.
Utterly spent, his makeshift costume tattered, gaping holes
in his mask, Spider-Man hangs over the abyss, clinging to the
edge, held in place by the tension of his webbing against the
bulk of the train behind him. And then--
AT HIS WRISTS
The webbing gives out. For good. The spinnerets FOAM OVER
like emptied aerosol cans.
He hangs suspended for a moment. Then falls--
And is caught, by the Passengers. Leaning out of the front
windows of the train.
They drag him back in and lay him on the floor. His mask is
so torn and stretched that you can see more than half his
face.
The passengers look down at him. Then AN OLDER MAN reaches
down and tugs the mask back over Spider'man's face. Looks up
at the others: Anybody got a problem with my doing that?
70.
(CONT'D)
Nobody does.
INT. ANANSI PROJECT LABORATORY - NIGHT
Otto stumbles back into the lab. He's crying. He backs into
the coupler and activates it. It advances to a certain point
and then stalls. Tries it again; nothing.
His hand reaches for the Latch. It's loose; he remembers in
FLASHBACK - FIGHT
As Spider-Man BUSTS the latch while trying to decouple Otto.
PRESENT MOMENT - LAB
A glinting black 'pod joins his hand on the Latch. They are
together forever now. A look on Otto's face of inexpressible
rapture or possibly unbearable pain. He sinks to the ground.
INT. ANANSI PROJECT LABORATORY - DAY
Early the next morning. One of the GRADUATE ASSISTANTS lets
lets herself in. Wearing headphones, listening to the Flaming
Lips. Nicest time of the day.
Singing along, hangs up coat, turns on lights. Takes a moment
or two to sense that something is amiss. Doffs the
headphones. Turns to look at:
THE EMPTY COUPLER
Cables dangling loose.
This pretty much freaks out the Graduate Assistant
completely.
ASSISTANT
Professor Octavius?
OTTO
Lies on the floor, naked, in the rig. Weird fluid seeping
from the flesh/machine interface. The assistant goes for the
phone, stabs out a code.
ASSISTANT
This is Gretchen McCord, in the
Anansi lab. I need help. I need
doctors. A lot of doctors.
An ALARM begins to sound.
INT. RESEARCH CENTER - CORRIDOR - DAY
A special team of commando DOCTORS, extreme surgeons, rush
along, wheeling equipment and gear. They're like Helmut
Newton doctors, packing in a portable operating theater.
71.
INT. ANANSI PROJECT LABORATORY - DAY
Converted to an impromptu surgery. Otto lies on a table with
the 'pods wilting around him.
The X-docs go to work. They're wearing mirrored eyeshades and
using laser instruments. It's a complicated ballet of
machinery and surgeons and blood. The ANESTHESIOLOGIST
monitors the EKG.
DOCTOR 1
Jesus! Look at his tissue! It's
changing so fast you can see it.
DOCTOR 2
His autoimmune function is breaking
down completely.
DOCTOR 3
The Rig's like a parasite...that's
going to kill its host.
DOCTOR 4
Unless we kill him first by trying
to remove it.
The pace of the EKG ratchets up a notch.
ANESTHESIOLOGIST
I may need to give him a little
more. So are we going to do this or
not?
The doctors look at each other.
DOCTOR 3
All right. Come on.
The Anesthesiologist prepares to turn up the gas on Otto.
One of the 'pods stirs faintly. Unobserved. It's diode
pulses. Takes in the situation.
The surgeons take up their instruments.
From the pseudpod, a soft WHIRR as we travel down
INTO THE POD ITSELF
Into its systems. Impulses sent to a fabrication unit. A
complicated organic molecule takes rapid shape, then a dozen
more like it, and we follow them back out of the fab.
The molecules are pumped directly into another system: Otto's
nervous system. Up the spine, toward the brain.
72.
(CONT'D)
(CONT'D)
(CONT'D)
(CONT'D)
A soft feminine VOICE wells up, muffled. Almost sounds like
it's saying, Wake up, Otto.
OTTO'S BODY
We travel up along his hips and chest, through his neck and
up to
HIS EYES
They snap open.
OTTO
I'm awake.
With a ROAR he comes to life. The 'pods windmill and lash and
flail. A tornado or turbine.
Within moments, Otto stands surrounded by bodies. He's
bleeding himself.
The servo of a 'pseudopod TRILLS softly. The other 'pods
gather near it, and turn their attention as one on Otto.
Darting, flexing, the 'pods go to work on Otto's wounds. One
cleans with a swab. One secretes an ointment. One radiates a
healing light. And one pours him a glass of brandy. He knocks
it back. Sighs.
OTTO
All right. System report.
He appears to be LISTENING to a voice in his head, a soft
feminine MURMUR we can almost make out. Winces.
OTTO
Jesus, that's disgusting. How long
do we have?
(listening)
I'm going to have to try the parity
chip.
He goes over to the tray. Of course it's not there.
OTTO
Spider-Man! He stole it--or Parker
stole it for him.
(listens)
No, no time to fab a new one.
His VOICE thickens as he shift to the plural, as if another
strand had been woven into it.
OTTO
We need to find another means of
attaining system equilibrium.
73.
INT. ANANSI PROJECT LABORATORY - CONTINUOUS
Otto opens one of the X-doctors' portable lockers. Stacked
with their rubberized scrub-jumpsuits. Holds it up. Yes, it
will do. The 'pods take it from him.
THE 'PODS
Go to work modifying the uniform. A blade. A needle. A heat
sealer. Then they hand it back to Otto. He holds it up; now
it can fit around the rig.
INT. LABORATORY - NIGHT
Otto checks himself out in a mirror over a sink. Pretty
styling. He looks closer.
HIS EYES
Colored storms race across them. The surface of Jupiter.
This won't do. He picks up a pair of eyeshields.
Electrochromic lenses that darken at a touch. He darkens
them, then smiles at the man in the reflection: Doc Ock.
OTTO
Not bad for a dying man.
INT. MARTIN BECK THEATER — REHEARSAL ROOM - DAY
MJ is taking some coaching from a WOMAN AT A PIANO. Trying to
find around a thorny note in her song. The DIRECTOR of
Bride! pokes in his head.
DIRECTOR
MJ? Talk to you a minute?
MJ looks at the Pianist. The Pianist knows. Looks away.
INT. DIRECTOR'S OFFICE - DAY
MJ's talking fast as he ushers her in.
MJ
Bobby, I know I keep screwing up my
blocking in the scene with the
couch.
DIRECTOR
You've been fine.
MJ
I've been working all day with
Renard--
74.
(CONT'D)
(CONT'D)
DIRECTOR
Sit down.
She sits. He slides a box of mints across the desk.
MJ
No, thank you.
DIRECTOR
Take one. It's a proven fact that
it's harder to cry if you have a
mint in your mouth.
She doesn't get it. Then she gets it.
MJ
When is she coming back?
DIRECTOR
Tomorrow night. She's strong and in
good voice, and she's all ready to
go.
MJ
Well. I'm glad to hear that. It was
a great learning experience for me,
and--
DIRECTOR
I'm glad you feel that way, MJ, I
really am. But, well, there's one
more thing I have to tell you.
She cocks her head, curious, no idea what it could be.
DIRECTOR
Please, have a mint.
She takes a mint.
DIRECTOR
Allie Black is going to take over
as the Shepherdess. And as Mrs.
Frankenstein's understudy.
MJ's eyes fill with tears. She goes pale.
MJ
What? Why? Bobby, why?
75.
DIRECTOR
Well, I just think, and Howard
agrees with me, that it would be
best. Overall. It's not you, MJ.
It's the show. It's just not the
best fit. For you.
MJ is in shock now. She nods, rises, heads for the door.
Before she goes out she turns back. Being brave.
MJ
Bobby, can I ask you something? Do
you think I have any talent?
DIRECTOR
Talent? Yes. And guts. Looks, too,
if you don't mind my saying so.
But--
MJ
But what?
DIRECTOR
Nothing.
MJ
Come on. You'll be doing me a
favor.
DIRECTOR
You seem to have a hard time
opening up. Really connecting to
the audience. There's something
broken way down inside of you that
you don't want to let out. Most
people don't. But actors have to.
She nods, bitterly. She knows. She slips out.
EXT. THEATER - DAY
MJ stands outside the theater. Bills are going up over the
posters, next to the words DEIRDRE DUNN, that read HER
TRIUMPHANT RETURN. It's raining. Maybe it's even starting to
snow. She just stands there, crushed.
FOOTSTEPS. It's Renard, walking into the theater. He sees
her, and then starts to act like he didn't.
MJ
Renard?
76.
RENARD
Oh!
(bad acting)
MJ Hi. Hey. I heard.
MJ
I should have known. I don't know
why I ever thought I--
RENARD
Yeah, that's tough. I know how
you're feeling.
Somehow not quite sincere.
MJ
No, you don't. There's only one
person who knows how I'm feeling
right now.
INT. PETER'S ROOM - DAY
Peter is on the phone. He's a wreck, battered, cut.
RECEPTIONIST
(O.S.)
Center for Biomimetic Research.
PETER
Dr. Octavius, please?
RECEPTIONIST
Just a moment.
HARSH VOICE
(O.S.)
Who is this?
PETER
I'm a... friend... of Dr. Octavius.
HARSH VOICE
(O.S.)
Dr. Octavius has resigned his
appointment. Who is this?
Peter hangs up. Spooked. A KNOCK at his bedroom door. He
jumps.
PETER
Yeah?
Ditkovich opens the door.
77.
DITKOVICH
Pretty girl is here.
INT. DITKOVICH'S HOUSE - DAY
Peter comes down the stairs. MJ is standing in the living
room. They look at each other; he reads her sadness.
PETER
What happened?
She goes to him and bursts into tears. He holds her. Strokes
her hair. She looks up at him.
MJ
You're wearing your glasses.
EXT. CONEY ISLAND - BOARDWALK - DUSK
They walk along the deserted boardwalk. Snow flurries.
PETER
Those guys are crazy, MJ. That's
all I can say. I saw you. You were
awesome.
She turns to look at him.
MJ
You saw me? When did you see me?
PETER
Oh, I dropped in the other night.
You were fantastic! You put
everything you have out there, MJ.
Everything you are. Right up front.
You always have. That's what I've
always...
MJ
What? That's what you always what?
He puts his arm around her. She leaves it there.
INT. DINER - NIGHT
Peter drinks coffee. MJ's eating a huge sundae.
PETER
I know what a jerk I've been. I
understand why you got mad at me. I
said I would always be there for
you, and then I wasn't.
(MORE)
78.
(CONT'D)
(CONT'D)
PETER (CONT'D)
But I swear to you, MJ, things are
going to be different now.
She rolls her eyes.
PETER
What? I'm serious.
MJ
Why are things going to be
different now? Because you started
wearing your glasses again?
PETER
Because--I can't tell you. But you
don't need to worry about it,
because I have changed, and--
But MJ's getting steamed.
MJ
You can't tell me? You can't tell
me! Peter Parker, if you can't tell
me, if you can't trust me, then
nothing has changed at all! You and
your little boy secrets!
She pushes away the ice cream.
MJ
Call me when you're ready to grow
up!
PEOPLE are staring. Timidly Peter raises a finger.
PETER
Check, please.
MJ
Isn't there one semi-normal, grown
up human male in this whole goddamn
city?
The WAITRESS brings the check.
WAITRESS
I hope that was a rhetorical
question.
Peter takes out his wallet. As he opens his wallet, he
already knows what he will find in it.
It's empty.
79.
(CONT'D)
(CONT'D)
PETER
I, uh, I need to get to an ATM.
MJ, disgusted, yanks open her purse. Scrambles up from the
table.
MJ
Yeah. Things have really changed a
lot.
MJ shakes her head, tosses down a twenty, walks out.
EXT. MINEO'S PIZZA - NIGHT
Peter approaches. GIBREEL is out front, struggling to attach
a hot box to the back of his motorscooter. It tumbles.
Peter lurches to grab it but PIZZAS go scattering everywhere.
GIBREEL is frantic. Peter tries to help him gather them.
PETER
Same thing happened to me one time.
Mr. Aziz comes out.
MR. AZIZ
Peter Parker!
INT. MINEO'S PIZZA - NIGHT
Peter stands supplicant, Mr. Aziz shaking his head. The phone
RINGS and RINGS.
PETER
It's just I'm flat broke, Mr. Aziz.
Please give me another chance.
MR. AZIZ
I am sorry, Peter, but following
your downsizement I have been
obliged to hire my nephews from
home.
He nods his head toward SALADIN, who is engaged in fatal
combat with a round of dough.
MR. AZIZ
If anything they are even less
competent than you, but they are
family.
He reaches for the phone.
MR. AZIZ
Yes, yes, Mineo's.
80.
VIEW THROUGH THE WINDOW
As Gibreel putters away on his scooter. The hotbox comes
loose and smashes against the street.
Before Mr. Aziz can react, SPIDER-MAN walks in. Not Spider
man. A guy in a realistic Spidey mask. With a big Glock.
Brandishes it toward Peter, then Mr. Aziz.
Saladin holds up the sagging round of dough.
SPIDEY HOOD
Okay, Hadji, give me everything you
got.
Mr. Aziz tries to smile.
MR. AZIZ
All right, but I hope you have a
very modest habit, my friend,
because this is not going to buy
you much of a fix.
SPIDEY HOOD
Shut up!
He CLUBS Mr. Aziz on the head with his gun.
Peter throws himself on the hood. Tries to get a choke-hold
on him.
The hood elbows Peter, then punches him hard in the stomach.
Peter tries to grab him again. The hood smashes him over the
head with his gun. Peter sags to the floor.
The hood snatches all the cash from the register.
Mr. Aziz comes over and helps Peter to his feet. Mr. Aziz is
crying.
MR. AZIZ
Thank you, Peter. You are a very
good person.
Peter staggers to his feet.
INT. HARRY'S APARTMENT - DAY
Harry's sleeping in the middle of the day, face down.
Bottles by the bed. A CLUNK. His eyes unstick. ANOTHER WEIRD
METALLIC CLUNK. Harry sits up. It sounds like it's coming
from the other side of his titanium security shutters.
81.
(CONT'D)
(CONT'D)
He hits the security panel. An image of the lobby station.
The guard is dead.
BRRRONG. The shutters are ripped open. Doc Ock steps in from
five stories up. ALARMS are screaming.
OTTO
I don't have time to waste, Osborn.
I need money. Lots of it. Quickly.
And a well-equipped laboratory.
He takes a small envelope from his pocket, holds it out to
Harry.
OTTO
That's my Christmas list, Santa.
Account numbers. Suppliers. The
address I want it all sent to.
(grins)
I'm going free-lance.
HARRY
This is nuts, Otto. Are you nuts?
You killed one of my security guys!
(points to window)
You trashed five million dollars
worth of bomb shielding! What the
hell's your problem?
OTTO
We must achieve system equilibrium.
Otto can't survive in this
intermediate state.
HARRY
Otto can't?
He looks curiously at Ock. There's something different--the
weird plural voice. Ock masters it.
OTTO
I need Spider-Man.
That gets Harry's interest.
OTTO
I need his body. Not all of it,
just his immune system. Well, and
his spine. And all of his bone
marrow.
HARRY
His spine?
82.
(CONT'D)
OTTO
All you need to know is that in
return for your--corporate
support--for this procedure... I
guarantee you that transition to
the next level of human evolution
will...unavoidably... kill SpiderMan.
There's a distant rising TROMP of feet. A POUNDING on the
outer doors.
OTTO
Think it over, Junior. What would
your father want you to do?
SECURITY
(O.S.)
Mr. Osborn! Mr. Osborn!
Harry looks at Otto, who tosses the envelope at him. Harry
fumbles the catch.
Otto leaps out through the window. The SECURITY MEN burst in,
looking around.
SECURITY MAN
Mr. Osborn! Are you all right?
EXT. QUEENS CEMETERY - DAY
A black Mercedes pulls up amid the rolling gray surf of a
Queens cemetery. A CHAUFFEUR gets out and comes around the
car. Opens the door for Harry.
Harry gets out and looks around at the. Barren, wintry. He
hates it here.
EXT. CEMETERY - NORMAN'S GRAVE - DAY
Harry stands in front of the headstone. A hint of spookiness
in drift of leaves across the grave.
HARRY
Dad. I know that you were a man of
honor. A man who always played by
the rules. And I know I'm not
supposed to take the law into my
own hands.
Mocking LAUGHTER. Harry gazes at the thirteen unlucky
letters:
NORMAN OSBORN.
83.
NORMAN OSBORN
(O.S.)
"I know I'm not supposed to take
the law into my own hands." What a
pussy!
HARRY
Dad--
NORMAN OSBORN
You saw what Spider-Man did to me.
He's playing by a different sent of
rules. Rules for men. Let this
Octopus do it for you, if you
aren't man enough to do it
yourself. But if he fails... I
expect you to avenge me.
Harry falls down onto his knees. Collapses on the grave.
HARRY
I will. I swear!
INT. LIMOUSINE - DAY
Harry flips open his cell phone, punches a number. Dirt from
the grave on his cheek.
HARRY
Octavius? Osborn. You'll get
everything you need.
INT. BUGLE - DAY
Peter walks into the city room, toward Jameson's office. He
stops when he sees:
THROUGH THE PARTITION
Harry and JJJ, talking urgently. On the door behind Harry,
Peter sees:
HIS COSTUME
The sight of his shocks him.
He walks up to Betty Brant's desk.
BETTY
You back on the job?
PETER
I'm hoping to be.
84.
(CONT'D)
BETTY
You sure know how to pick your
moments.
JJJ
(O.S.)
You change your mind?!
INT. JJJ'S OFFICE — DAY
JJJ and Harry are face to face.
JJJ
You can't promise a ten million
dollar reward and then change your
mind! I've stoked the greed and
bloodlust of eight million people
to a fever pitch! You're just going
to turn your back on that?
Harry is strangely cool. Cooler than we've ever seen him.
HARRY
I've found a more effective means
of obtaining my end.
JJJ
Yeah? And what is that?
HARRY
You'll know soon enough.
JJJ
Oh, really? Tell me this, Osborn...
How do I know that you aren't
Spider-Man? Eh? Maybe this whole
reward thing was just an elaborate
dodge. And now that's things are
getting a little hot for you, you
want to call it off! Your father
was a strange character, I always
thought so. Maybe you're a little
strange, yourself.
Jabs that Jameson finger at Harry.
JJJ
Now go home, and leave the running
of a public smear campaign to the
people who really know what they're
doing.
Harry grabs the finger and crumples it in his fist. Jameson
snatches it back, wincing.
85.
HARRY
You're just a grandstanding hack,
Jameson! You don't know what it's
like to want revenge so bad you can
taste it!
Harry stalks out, brushes past Peter. Peter reaches out to
him.
PETER
Harry? Harry, what's going on?
Harry whirls, furious, about to strike. The wire lattice
embedded in the safety glass of the partition casts a grid of
shadow across Peter's face; it looks like webbing.
Harry peers at Peter, fixedly, then turns and walks out.
JJJ turns to Peter, sucking on his sore finger. Peter eyes
the costume.
JJJ
Jesus, Parker, how many times do I
have to fire you?
EXT. AUNT MAY'S HOUSE - DAY
A sunny day. Geraniums. Otto notices the geraniums by the
door. Rings. Aunt May's there.
MAY
Yes?
OTTO
Excuse me. I'm looking for Peter
Parker.
Sorrow on the old woman's face at the name.
MAY
He isn't here. Do you mind my
asking what this concerns? Are you
a friend of Peter's?
OTTO
We share a hobby.
MAY
What hobby is that?
OTTO
Spider-Man.
86.
(CONT'D)
(CONT'D)
MAY
Spider-Man?
(nods)
One look at you and I should have
known.
OTTO
Please.
There's a WHIRR but it's Otto's own meat arm that shoots out.
He clutches Aunt May. WHIRRING. Otto struggles against a
murderous impulse in the 'pods.
OTTO
Please! It's very urgent. Where is
Parker?
MAY
I haven't seem him in over a week!
We had an argument, I threw him
out. I don't know where he is! And
that's the truth.
She's lying. But doubt creases Otto's face. May sees it. And
suddenly fear gives way to something else. Anger. Pride. Will
to live.
MAY
Now I'll thank you to take your
hand off of me!
Otto's surprised. So is May. He retracts his hand.
OTTO
We will find Spider-Man. We will
flush him out.
MAY
You do that. Just leave Peter
Parker alone.
"OCK'S RAMPAGE"
Three scenes of urban destruction.
EXT. PRADA - DAY
Ock alights outside the flagship store. Goes "shopping."
Trashes the place, terrifies fellow shoppers. Goes out with
cool new clothes. As he's walking out he says, with panache:
87.
OTTO
My name is Otto Octavius. I am a
mad scientist. I'm looking for
Spider-Man.
EXT. LINCOLN TUNNEL - DAY
Cars lined up heading out of town, traffic stalled. Drivers
touchy. Suddenly a car FLIES right out of the tunnel. Lands
on and crushes some other cars.
Another car flies out. Then another. A few more besides. Then
there's a METALLIC GROANING and SCRAPING.
Ock emerges, dragging an ARMORED CAR behind him. He tosses
cars in front of the tunnel mouth to one side. Clears a
space. Then rips open the armored car.
People leap from their cars to harvest the whirling money.
Quickly they turn savage, fighting each other, slipping and
sliding on the ice as they chase the money.
Otto strides among them. Hangs over them. They stop fighting
and look up.
OTTO
My name is Otto Octavius, I am a
mad scientist. The destruction will
not stop until Spider-Man
surrenders himself to me.
EXT. ROSE SPACE CENTER - DAY
Otto smashes his way into the building, shattering the huge
windows, scattering schoolchildren.
INT. SPACE CENTER - DAY
He heads straight for the Willamette Meteorite.
TOUR GUIDE
...found in Oregon, weighing over
15 tons...
OTTO
It's closer to sixteen.
He digs in the 'pods. Grips the Meteorite.
Pulls. Pulls. Pulls. And UPROOTS it. Carries right out of the
museum.
88.
(CONT'D)
INT. FIFTH AVENUE - DAY
Otto stalks down the avenue swinging the space rock at the
end of his 'pods like an enormous mace. Gouging huge chunks
out of buildings on either side.
INT. WASHINGTON SQUARE PARK - DAY
Otto winds up like a cricket bowler and then hurls the
meteorite through Washington Square Arch.
He turns to a HORRIFIED CROWD who cower nearby.
OTTO
I'm sure you know who I am by now.
Let me repeat. Spider-Man is
responsible for the fate of New
York City.
Turns to a WOMAN. Gently.
OTTO
Did you get that?
WOMAN
Spider-Man is responsible.
OTTO
Thank you.
WOMAN
You're welcome.
Otto stalks away. We get a good look at him as he goes by. He
looks bad. The toll on his tissues is becoming visible;
tracery of black webbing across his skin.
TELEVISION NEWS REPORT
Features footage of Ock's reign of terror.
REPORTER
As the carnage continues, Denise,
one question is increasingly on the
mind of New Yorkers--where is
Spider-Man? If he won't give
himself up to Octavius-- why
doesn't he stop him?
INT. PETER'S ROOM - DAY
Peter watches the broadcast on a tiny B&W TV.
He looks as if he's been lying there motionless for days.
Weeks. Unshaven. In pajamas. In a bad way.
89.
WOMAN ON TV
...he told us that Spider-Man is
responsible for this.
(to camera)
Spider-Man, please. Do as he says.
Peter's hand strays to the place on
his hip where he made the
injection.
REPORTER
Back to you, Denise.
GIRL TALKING HEAD
Thank you, Rhonda. And, now, here
in the studio, we have JJ Jameson,
publisher of the New York Daily
Bugle. In recent days, your paper
had been taking some of the credit
for apparently driving Spider Man
into hiding. Now that he doesn't
seem to want to come out of hiding,
do you feel your paper deserves
some of the blame for--
JJJ
(ON TV)
For the fact that Spider-Man is a
damn coward? Absolutely not! As
much as I deplore this Doctor
Octopus character's methods--
GIRL TALKING HEAD
Doctor Octopus?
JJJ
(ON TV)
That's what we're going with, what
do you think?
A KNOCK on the door. Soft, at first. Peter ignores it. Then
LOUDER.
MAY
(O.S.)
Peter?
Panic. Peter switches off the television. Makes a frantic,
doomed attempt to tidy the room. Gives up. Goes to open the
door.
Aunt May comes in, carrying grocery bags and a baked good.
Tries to conceal her distaste at the room.
90.
(CONT'D)
(CONT'D)
MAY
Well, isn't this--snug. Here, I
made you some soup, and your
favorite, a Boston cream pie. Real
whipped cream.
PETER
You came all the way over here--
with soup?
MAY
And Boston cream pie.
PETER
Aunt May, haven't you seen the
news? Don't you know what's
happening out there?
MAY
The trains are still running. If
the trains are still running, it
must be all right.
(beat)
And I haven't heard from you in so
long, dear. I'm worried about you,
Peter, you don't look well. Come
downstairs and have some soup.
INT. KITCHEN - NIGHT
Peter sits at the table while Aunt May puts a bowl of soup in
front of him. He digs right in. Days since he ate.
MAY
You know, that awful Octopus. He
came looking for you. Earlier
today.
The spoon stops halfway to his mouth. Freaked by this.
PETER
He came to see you? Why?
MAY
He said that he was looking for
Spider Man.
She's fiddling with the Boston cream pie. Not looking at him.
MAY
For some reason he seemed to feel
that you might know where to find
him.
91.
(CONT'D)
(CONT'D)
(CONT'D)
A long pause. Then Peter goes back less heartily to his soup.
MAY
I can't say that he was a very nice
man.
She pokes a finger into his soup, tastes it.
MAY
I sent him packing.
(beat)
Too much dill.
PETER
Aunt May. The last time we... at
the house... what I told you...
MAY
You should have told me sooner. And
I should have forgiven you before
now. It would have been so much
easier for both of us.
PETER
I would have liked that. Things
haven't been very easy at all.
Tears in his eyes.
MAY
Peter, I understand the burden that
you've been carrying.
PETER
No, you don't.
MAY
Yes, I think I do. The sense of
guilt. Of responsibility.
PETER
I'm so sick of that word.
MAY
But that's how life is, Peter.
She slices him a piece of Boston cream pie (really a cake).
MAY
(cont'd)
Responsibilities are thrust on you.
Calamities. Tragedies. Through no
fault of your own. And you sit, and
you say--
92.
(CONT'D)
(CONT'D)
PETER
Why me?
MAY
Yes, you say, why me? And the
answer is, you'll never know the
answer to that.
She looks at the pie--why not? Cuts herself a piece. Takes a
bite.
MAY
Mmm. Not bad. But the real question
you should asking is not, why me?
It's, what are you going to do
about it?
(beat)
My particular answer to that
question is, to bring my only
nephew some chicken noodle soup and
a Boston cream pie.
He isn't crying anymore. He's just listening, and eating pie.
MAY
I don't what the answer is for you,
Peter. But you do.
PETER
It's so hard, Aunt May. I just want
to have a normal life. The kind of
life--
MAY
That doesn't break your heart?
(beat)
That would be nice, wouldn't it?
Normal, I don't think so.
EXT. RUINED PIER - NIGHT
Doc Ock's secret lair. It hums with activity within.
INT. SECRET LAIR - NIGHT
A laboratory is in place. Much of the equipment labeled
Oscorp Systems, Inc. Ock has been working all night. He steps
away from making adjustments to a nasty-looking surgical
table. Sits down in a chair.
Harry is there, irritated, strung out.
93.
(CONT'D)
(CONT'D)
HARRY
Why don't you have him yet? What am
I paying you for?
OTTO
He won't come out... I can't flush
him.
Two 'pods snake out and grab a can of soda, a slice of pizza.
The other two take hold of one of his meat arm. One jacks in
a blood probe.
OTTO
How is it?
HARRY
How is what?
OTTO
I'm not talking to you!
Otto looks over at:
A MONITOR
It displays the analysis of his immunoresponse. Not good.
OTTO
I see.
(beat, plural voice)
We have one remaining vector.
HARRY
Vector? What do you mean.
OTTO
(normal voice)
I mean, I want to see Mary Jane
Watson again.
INT. MJ'S BEDROOM - NIGHT
Television going, footage of Otto's havoc. MJ dozes in the
blue light. BOOM. She stirs. BOOM! SCREAMS of people in the
street. Her eyes open. The sound of the 'pods--kzh-kzh kzh.
She goes to the window and looks out.
The buildings across the way lie in rubble. Fires. People
running in panic. In the center of it stands Doc Ock. A
literal path of destruction behind him.
OTTO
Mary Jane! Mary Jane!
94.
(CONT'D)
(CONT'D)
She pulls back from the window. Summons her nerve. Goes to
the window and throws it open. Steps out onto the little
balcony of her apartment.
MJ
Otto... Otto. Why are you doing
this?
A look of agony passes across his face.
OTTO
Why?
His features harden.
OTTO
Because we need to catch a spider.
He climbs straight up the face of the building to her.
OTTO
And you are the fly.
EXT. MJ'S NEIGHBORHOOD - NIGHT
In flames. Police and rescue crews. Peter comes running up
toward the street where she lives. It's cordoned off. A
POLICEMAN stops him.
POLICEMAN
That's as far as you can go, buddy.
Peter steps back, horrified by the destruction. People
huddle miserably nearby. A Nynex guy is standing on top of
his truck, trying to see what's happening.
BYSTANDER
1 Where's Spider-Man in all this?
BYSTANDER 2
That's what I'm saying, what's his
problem? It's like, how selfish can
you be?
BYSTANDER 3
He's responsible for all of this. I
saw it on TV.
Peter hears all this. Jesus.
A HUGE CRASH in the distance, then a series of CRUNCHES.
BYSTANDER
1 What was that?
95.
NYNEX GUY
He just climbed up the side of a
building. He's talking to some
girl! He's grabbing her!
There's just time for the shock to register on Peter's face
when Ock comes crashing past with MJ caught up struggling in
one 'pod.
The police raise their weapons. Ready to fire.
COP
No, you'll hit the girl.
Ock's moving incredibly fast. He steps right over the police
line--and right over Peter. Peter runs after them.
PETER
MJ! MJ!
MJ hears him--
MJ
Peter?
--but Ock just keeps on going. Peter picks up a broken beam
lying nearby and hurls it at Ock's legs as hard as he can. A
'pod lashes out and flicks it away. Then lashes at Peter,
too, and sends him flying.
He lands hard. Ock vanishes from sight.
Peter gets up, looks around. Jumps into the Nynex truck.
Takes off after Ock at top speed. The Nynex guy has to leap
off.
NYNEX GUY
That dude took my damn truck!
EXT. AVENUE - NIGHT
Ock stalks along the street, moving fast. MJ struggles in the
'pod.
MJ
Otto! Otto, stop!
Otto reaches back, with a meat hand, as if to slap her.
Catches himself.
OTTO
Okay. Okay!
Poor Otto's brain is shivering into shards.
96.
(CONT'D)
(CONT'D)
OTTO
Okay, MJ. Darling. Let me try to
explain this to you.
He stops and sets her down somewhat roughly.
MJ
Let me go.
OTTO
I can't.
She stares at him.
OTTO (cont'd)
No.
(listens)
Shut up!
MJ
I didn't say anything!
OTTO
I'm not talking to you! Okay. Okay,
I'll let go. But don't leave me.
He uncoils a 'pod from her waist. She starts to bolt.
OTTO
I'm going to die, MJ!
EXT. AVENUE - NIGHT
Peter races in the truck. Weaving through traffic. Sees Ock
in the distance.
EXT. AVENUE - NIGHT
Otto retracts the arms. MJ turns toward him. Sees real pain
there. Takes a step his way.
OTTO
Please. Come. You'll be helping us.
We promise.
As he speaks, one of the 'pods snakes beckoningly out. MJ
notices, and she shudders.
MJ
Otto, who is we?
GUNNING ENGINE. Here comes Peter, tires squealing. Otto
snatches MJ up again with one 'pod. Rises up on the lower
pair.
97.
And with the fourth, PLUNGES straight into the cab of the
truck and grabs hold of Peter. Rips him out and tosses
him aside.
The truck crashes against a lamppost and splits open. A
bicycle chained to the lamppost goes flying and lands with a
clatter. Peter lies amid spools of cable and orange plastic
fencing. He stands up shakily.
Now a HELICOPTER descends on the intersection. Squad cars
arrive from every direction.
One of the 'pods snakes up and grabs hold of the chopper's
strut. Another reaches right into the whirl of the
helicopter's rotors. His 'pod takes hold of the rotor shaft
and with a horrible shrieking brings it to a halt. Then Ock
hurls the chopper directly at the police cars.
Watching the explosion, grinning, he retreats. He doesn't
see:
THE WEB
That Peter has improvised, from orange fencing, across the
intersection. It's crooked and lame but Ock stumbles. Loses
his balance. SLAMS to the ground. One 'pod stays aloft,
holding MJ.
Peter runs to her, she grabs hold of him. He tries to pry it
loose. No way. Now another 'pod snakes in and grabs Peter and
bats him lightly aside.
OTTO
Tell your friend Spider-Man I need
to talk to him.
Then they're gone. Peter's alone in the rubble. Defeated...
and then, abruptly, grim. He goes over to the wreckage of the
Nynex truck. Pulls out the toolbox. Opens it. Takes out a
wicked needle-nose pliers. Holds it up. Should he?
FLASHBACK - CONEY ISLAND
They walk down the boardwalk in the snow. A few strings of
colored lights. He puts his arm around MJ's waist.
PETER
(V.O.)
I just want to have a normal life.
A life--
MAY
(V.O.)
--that doesn't break your heart?
That would be nice, wouldn't it?
98.
(CONT'D)
(CONT'D)
PRESENT MOMENT - AVENUE - NIGHT
He looks around at the smoldering wreckage around him. Then
at the pliers. This is going to hurt.
He JABS the knife directly into his hip. Digs around. The
worst SPLORCH imaginable results. His eyes roll back in his
head. He staggers. But he holds up the bloody chip and grimly
smiles.
He looks around--needs wheels. There's the bicycle. A
little bent. It will do. He takes pedaling after Ock and MJ.
EXT. AVENUE - NIGHT
Peter rides past LOOTERS, smashing store windows. A LOOTER
holds up the television he has snatched.
LOOTER
Hey, look here, I got me my eightarmed discount.
Peter slows, watching, frowning.
LOOTER
What are you going to do about it?
Peter pedals off, slows again, turns.
PETER
You really should put that back.
The looter, incredulous.
LOOTER
Man, shut up.
His friends laugh. Then there's a cry for help.
Peter looks. Some other LOOTERS have descended on a SIKH man
who is defending his store.
LOOTER
Yo, why don't you go back to
Baghdad?
PETER
Hey!
Everyone turns to look at him. Peter looks down the Avenue.
Far, far away, by the Flatiron Building, we can see the
dancing glint of Ock's 'pods.
Then LOOTERS fall on the Sikh man.
99.
(CONT'D)
(CONT'D)
Peter drops the bike, and runs into the midst of the gang.
They turn on him. The Sikh man crawls out of the melee,
bleeding. The looters swell around Peter, kicking, stomping,
punching. He goes down under the surf of men.
Then, with an audible WHOOSH, the gang of looters FLIES
BACKWARD. It's like a blossom blooming. Peter rises to his
feet, bloodied but steady. The men come at him again but now
he makes short work of them, leaping, kicking, dancing.
The Sikh Man looks on, throwing sympathy punches.
The looters lie fallen around Peter. He reaches down to yank
the stocking cap from one of the men's heads.
PETER
Are you using this?
INT. JJJ'S OFFICE — NIGHT
JJJ is at his desk, on the phone. People coming and going.
The Spidey suit hangs in a nice class case.
JJJ
Any sign of him? No?
WHAP. From the boarded-up skylight. JJJ looks up. Uh oh.
A foot SMASHES through the wood, splintering it, and then
Peter, stocking cap over his face, lands in front of JJJ's
desk. He goes over to the case, SHATTERS it. Reaches in and
takes the suit. Holds it up.
JJJ
What the hell do you think--
PETER
It makes you look fat.
He fires a web up out of the skylight, gives it a jerk, and
then sails out after it.
EXT. FIFTH AVENUE - NIGHT
Spider-Man swings along the avenue, trying to catch up to
Dock Ock.
EXT. ROCKEFELLER CENTER - NIGHT
He catches up to him at Rockefeller Center and they fight, in
the snow, on the ice of Wollman Rink. MJ gets away from Otto
but then stays to watch.
Each combatant gifted in his own way with power, agility, a
kind of grace.
100.
OTTO
Not bad for a couple of freaks.
SPIDER-MAN
Speak for yourself.
OTTO
I speak for us both. You have the
greater power--power I need. But I
have the strength of knowing what I
am. I embrace my freak nature. I
revel in it. You will always be
fighting against it. That is why I
will win this battle.
And he does. At last Spidey lies defeated at Doc Ock's
numerous feet. Doc Ock picks him up, and grabs MJ. He takes
his cell phone out of his pocket. Coolly punches a number.
INT. HARRY'S APARTMENT - NIGHT
Harry sits watching the destruction on television. Clearly
drugged to the gills. The phone rings. He manages to notice.
HARRY
What.
OTTO
Your father's soul will soon rest
in peace, Mr. Osborn. Meet me at
the pier.
Click. Harry rises wobbling to his feet. A strange echoing
LAUGHTER in his ears.
INT. DOC OCK HQ - NIGHT
Ock tosses Spider-Man onto his BIG NASTY SPINAL-CORD
EXTRACTING TABLE. MJ he sets down more tenderly to one side.
He prepares the procedure. It looks like it's going to be
extremely painful.
EXT. DOC OCK HQ - NIGHT
Harry's limo pulls up. Harry gets out. Looks around
nervously.
INT. DOC OCK HQ - NIGHT
MJ revives, sits up. Groggy. Harry stumbles in. Sees MJ.
HARRY
MJ? What are you--
101.
Otto turns. He has Spider-Man all strapped in, now.
OTTO
Hello, Harry. Come to watch? I
guess you've been waiting quite
some time for this moment. I
suppose before anything else you'd
like to know who put your father in
the ground.
Harry draws closer, fascinated. He nods. MJ hangs back.
Otto reaches out and YANKS the mask off of Peter.
HARRY'S FACE
Horror. The memory of Peter and his father shaking hands. Of
Spider-Man leaving the corpse of Norman Osborn. Masks begin
to circle one another in his mind--the masks of Norman
Osborn's collection, Spider-Man's mask--and one other, green
and grinning.
MJ
Peter?
(dawning shock and horror)
Peter!
She runs toward the table. A 'pod lashes out and knocks her
brutally aside. Harry goes to her, sees the blood on her
cheek.
Looks back at Peter lying on the table as a great, spiked,
vascular probe begins to descend on the torn form of his
friend.
The LAUGHTER begins to sound louder in his ear and the probe
descends.
HARRY
No! This isn't-- I'm not--
He stumbles to his feet, stoned and terrified, and lurches
out of the laboratory.
Ock swings another fell-looking unit into place near Peter's
head. All of the 'pods are working in balletic unison to
prepare the procedure.
MJ stands. She sees a big spanner lying on the ground. Picks
it up. Tucks it behind her back. Starts to inch toward Otto.
MJ
Otto. Don't do this. You don't want
to do this.
102.
(CONT'D)
(CONT'D)
(CONT'D)
(CONT'D)
OTTO
There's no way to avoid it. We only
need pieces of him, really, but
they're rather crucial pieces.
She's coming closer to Otto.
OTTO
If we could take what we needed
without killing him, we would, but
alas--
He flips a few more controls.
Two of the 'pods zero in on Peter's head. One extrudes foam
onto it. The other produces a clipper-head.
With a few rapid strokes they shave Peter bald.
OTTO
No, that's not true. We're looking
forward to this death. You know
what's interesting? Humans always
think of the killer instinct as
something very primitive. A relic
of the savage past.
Now all the cruel apparatuses are in place. An urchin of
steel spines, miniature 'pods, wriggle toward Peter's bare
skull.
OTTO
But the longer we spend at this
level of evolution, the more we
realize that that's just wrong.
Think about it. Human beings have
only gotten better and better at
killing over the last fifty
thousand years. This is what we're
evolving toward...
She's close enough, now. She raises the wrench, high and
brings it down--
ZWIPP. A 'pod lashes around the wrench and jerks it from her
hand. Another 'pod knocks her back against the wall.
OTTO
(plural voice)
Get away from Otto, bitch!
Ock turns on her, and the 'pods lash out and hover, just
above her, ready to cut her to ribbons.
103.
(CONT'D)
(CONT'D)
MJ
Otto... please.
She climbs unsteadily to her feet. Looking him in the eye.
MJ
Otto... hey? Look at me. Please?
Just look at me.
She crosses to him. The arms strike, and come within inches
of her face. She flinches but doesn't give way. Then takes
another step toward him. Reaches up. Lifts the glasses. Peers
into his wild, dying eyes.
MJ
I know that you're in there. I can
feel you? Can you feel me?
The arms WHIRR and twitch, impatient as hounds at the end of
their leash.
OTTO
Yes, MJ. I can feel you.
MJ
Otto, you are not a killer. Your
work is not about killing. Your
work is about making us better
humans, right? Better at being
human.
OTTO
Better at surviving in this
poisonous world.
MJ
Why? Why survive? Just for the sake
of surviving?
Otto points at Peter with a meat hand.
OTTO
You love him.
MJ
Yes. I do.
Otto's at the limit of his control. All his systems breaking
down. The WHIRR of the arms ratchets up to a WHINE.
OTTO
I thought there was a place for me
in your heart. The first place I
ever felt like I belonged.
104.
(CONT'D)
(CONT'D)
Distant sound of SIRENS from outside.
MJ
There is, Otto! There is a place.
For you. For me. There is.
OTTO
You might be right. There might be.
Slowly, the 'pods snake up toward the rafters of old
building. Lash around them. Pull tight.
OTTO
Let's find out.
With a crash, he pulls the ceiling in. The walls begin to
collapse in on themselves.
A pillar tips over onto Otto, then smashes through the floor,
dragging Otto with it. Into the water below.
With a WHOOSH Otto is thrust down deep into the water.
EXT. UNDERWATER - CONTINUOUS
Otto plunges, 'pods billowing up behind him. A streamer.
INT. DOC OCK HQ - CONTINUOUS
Peter revives. Looks around. Stuff falling everywhere. He
kicks and thrashes his way out of the surgical unit. Spider
sense TINGLES.
He sees, in slow motion:
The central roof beam give way, with a mighty GROAN.
MJ, leg pinned under a fallen slab of concrete.
The inevitable trajectory that links them.
PETER
MJ!
He leaps across and lands under the beam just at it hits,
muscles taking on a massive burden of wood and inertia. He
sags-- sags-- sags--stops. He squats under it like Atlas
underneath the heavens. His face is five inches from MJ's.
PETER
Hi.
Peter gives away a little more. Faces four inches apart.
105.
MJ
Hi.
The weight seems to increase exponentially. Three inches.
PETER
This is really heavy.
Peter sags again. Now their faces are less than an inch
apart.
MJ
I'm trying. I'm stuck. I think my
leg is broken.
PETER
Least of our worries.
CREAKING. MOANING.
EXT. DOC OCK HQ - DAY
Dawn. The grand old building carefully goes about the
business of sinking into the river.
EXT. UNDERWATER - CONTINUOUS
Otto thrashes in the Rig as the 'pods struggle toward the
surface. For a moment he looks like his namesake.
INT. DOC OCK HQ - DAY
Peter is drenched in sweat. He's shaking. MJ is trying to
free herself.
MJ
If I could just--feel--my foot.
PETER
MJ. In case we die--
But he runs out of breath before he can finish the sentence.
MJ
You do love me.
PETER
I do.
She had better hurry. He is about to break. Their faces are
nearly close enough for a kiss.
106.
MJ
Even though you said you didn't.
Now Peter can only nod. No breath to spare. MJ's face
brightens--she's freed her foot.
She crawls out from under the slab, then under Peter's arms
as he drops the beam. As it slams through the floor, he
snatches her up, then fires a web through a place where the
walls have collapsed. He yanks them up and out just as:
EXT. DOC OCK HQ - NIGHT
The entire structure upends and then slides with a certain
urgency into the East River.
EXT. UNDERWATER - CONTINUOUS
Otto turns his face away--
And ten thousand tons of ancient lumber comes tumbling down
on top of him.
INT. NORMAN'S OSBORN'S PENTHOUSE - DAY
Harry Osborn lies in the middle of the floor of a great,
empty ballroom floor. A small dark island in a sea of
parquet.
He wakes up like Sal Mineo in Rebel Without a Cause, alone,
lost, abandoned.
Stands up. Looks around. Echoes and ghosts.
He wanders the empty rooms and halls. Draped furniture.
Carpets rolled.
Climbs the stairs. Stops at the door to his father's office.
Hesitates. Goes in. There's nothing there except--
Something in the corner. A small piece of colored paper.
He goes over and picks it up. It's a little, store-bought
Halloween card. More ghosts. HAVE A BOO-TIFUL HALLOWEEN.
Opens it up. “To Dad, Love Harry." He lets it drop.
NORMAN OSBORN
(O.S.)
All right, Harry. It's your turn
now.
Harry looks around sharply. No one there.
107.
NORMAN OSBORN (CONT'D)
(O.S.)
I want to see what kind of stuff
you're made of.
HARRY
No. No, Dad. He's my friend.
He looks into the mirror over the mantlepiece. Norman is
there.
NORMAN OSBORNE
Is he. Your friend. I guess that's
why he stole your girlfriend. I
guess that's why he killed me.
HARRY
Dad, I don't know. I'm not sure.
There's a lot I don't understand.
NORMAN OSBORNE
"I don't know." "I'm not sure."
Harry, you swore an oath! You put
your word, your money, your name on
the line! You swore to make SpiderMan pay. Now, make him pay!
Harry's leaning his forehead against the mirror. It reflects
only him.
HARRY
I swear. I swear!
As he says this he POUNDS the mirror with his fist. It
shatters and falls. Droplets of glass rain down. And there on
the other side of the universe is a neat little room. A
laboratory of some kind. A command center. A haunt.
Harry steps into that other world. Hanging from a hook is a
grinning green mask. He reaches toward it.
INT. MJ'S APARTMENT - DAY
MJ lies on the couch. Her leg in a really big cast. Reading
the Daily Bugle.
THE HEADLINE
WACKOS: ONE DOWN, ONE TO GO
She reaches for a squeeze bottle that is just out of reach.
MJ
Peter! Peter? I can't reach the--
108.
(CONT'D)
(CONT'D)
(CONT'D)
He's there. In his coat. Backpack on his back. Leaving.
MJ
Water.
She falls back against the sofa.
MJ
You said you'd stay.
PETER
Your mother's coming.
MJ
You also said... that you loved me.
PETER
I do love you. I have loved you all
my life, Mary Jane Watson. I just
can't have you, that's all. The
danger, the uncertainty. The
hatred. I can't ask that of you.
You don't know what it's like. This
is my deal. It's my destiny.
He nods toward the Bugle.
PETER
What's he saying?
MJ
He's saying you're evil incarnate.
Peter nods.
PETER
I'll call you tomorrow.
He goes out. She picks up the paper. Her face crumples. She
puts the paper down. Sees his CAMERA sitting there.
Lumbering, in pain, she pulls herself to her feet. Grabs her
crutch. Hobbles over to pick up the camera. Then as quickly
as she can to the window. Throws it open. Snow blows in. She
sticks her head out.
MJ
Peter! You forgot your camera!
He's on the street below. He turns and looks up. She
lumbers out onto her balcony. We can see the divots that Doc
Ock tore out of the face of the building.
MJ forms a quick resolve. Then throws herself over the side.
109.
(CONT'D)
PETER
MJ!
He darts under the balcony and catches her, awkwardly, but
sure.
MJ
Do you know how amazing it is than
I can trust you do that?
(beat)
You were given a gift, Peter. I
want to share that gift with you.
And I want you to share it with me.
You don't have to do it alone. I'll
help you.
PETER
MJ--
MJ
What, you think police officers
don't get to be in love?
Firefighters don't get to be
married? That's crazy.
PETER
But, MJ. This is just--this is just
so much weirder than being a
policeman.
MJ
It is weird.
(beat)
But you've always been weird, Peter
Parker.
PETER
Wait, did you say married?
She hits him, hard.
MJ
I already know your damn secret
identity!
He looks at her. Then around. Then he carries her over to the
building and, lightly, with just the tips of his feet, walks
right up it. Hops the balcony and ducks inside with her.
MJ
(O.S.)
Does this mean I get to see the
Spider Cave?
110.
(CONT'D)
(CONT'D)
PETER
(O.S.)
There is no Spider-Cave.
MJ
(O.S.)
That sucks.
INT. MJ'S APARTMENT - NIGHT
He sets her back down on the couch. Puts down his knapsack.
Then SIRENS. A lot of SIRENS. Peter goes to the window and
looks out. Face grim. Well, you asked for it.
MJ
Go. Go! I'll be fine.
He starts to peel off his shirt.
EXT. NEW YORK STREET — NIGHT
The sky glows orange; flashing sirens. Spider-Man takes off
into the night. MJ leans out of the balcony as he sails away
to be who he is.
MJ
You forgot your camera!
Spider-Man swings around a corner and straight through the
heart of a burning building.
PETER
(V.O.)
It was a five alarm fire. Gas fed.
300 firefighters. And the junior
Senator from New York on the
seventh floor.
He comes swinging out the other side, clutching a
DISTINGUISHED GENTLEMAN and a YOUNG WOMAN DRESSED AS A MAID.
PETER
(V.O.)
With his lovely companion.
He touches them down gently. ERT techs rush over.
PETER
(V.O.)
Look at that guy. Look at him! You
want to know the story of his life?
No choice in the matter. No way
out.
111.
(CONT'D)
Spider-Man sails back up into the roaring fire, toward a PAIR
OF CHILDREN, snatching them from the flames. Doing what he
was meant to do.
PETER
Didn't get a single damn picture of
any of it.
 THE END 
""")

print(f"Código finalizado, {linhas_enviadas} mensagens enviadas")
