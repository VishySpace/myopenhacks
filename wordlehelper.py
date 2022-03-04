import sys, argparse

# seed random number generator

words =  ['SLANT','ROACH','CUMIN','ADMIT','MIMIC','USUAL','QUASI','BIOME','CLEAT','ELITE','QUACK','SALVO','SHORE','BENDS','LACER','RAIDS','BEING','COUGH','WARTS','FRANK','SHAPE','TEDDY','PRODS','WELLY','CLUCK','ODEON','MOURN','WAKEN','BRING','DRAFT','SEIZE','GRIPS','POLAR','ARDOR','NAVEL','DATES','THEFT','NADIR','WHACK','FIBRE','PIXEL','TRICE','ROBIN','SURED','POOPS','COBRA','HUFFS','THONG','VOMIT','NORTH','SMART','MENDS','GRATE','FLUSH','BOUGH','RANGE','SLING','TAMER','OZONE','SAVVY','TASTE','BATCH','BEGIN','GUILE','TWEAK','GERMY','TAPED','SULKY','SWELL','CLOWN','FORUM','STATE','INEPT','BRUSH','PRIED','TOKED','BOGGY','SHALE','SLOPS','PINED','HUNTS','FREER','BAYOU','BOULE','PHOTO','SPECK','GAMUT','SCAMP','WILLY','WRUNG','CACTI','SLEET','KNEED','STOVE','DECOY','ALERT','CRUDE','PIPED','EDIFY','WHILE','ROMAN','BLACK','CLASS','VIDEO','SNACK','WOKEN','CHOKE','GRILL','KINKY','FREES','CRAZE','FEWER','FUNGI','HOMEY','PINES','TAXED','CARGO','DOWNY','HERBY','CAMEL','URGES','DEITY','PAROL','OPTED','LAYER','SHADY','MUMMY','TUBER','SAUTE','NAKED','BASIC','RATES','PLUNK','CODER','VOWED','BYLAW','DIZZY','SPECS','DERBY','ENEMY','IDOLS','DINGO','SPELT','ALIEN','DANCE','YOLKS','FLOPS','METRO','FLASK','LOGOS','EVICT','YUMMY','HUSSY','INDIA','GATES','PARES','MALTS','SCRUB','KICKY','VAUNT','PIPER','PILES','PUSSY','FINDS','SPIED','BLIMP','ULTRA','STEEL','MEATY','LIMBS','CREDO','RIGOR','GNOME','BLINK','SAUCY','SLATS','METAL','LOBES','GLINT','BLADE','NYLON','CHUTE','TOUCH','ACORN','HIREE','GLORY','BLAND','PLANK','HOPES','DROID','PRIDE','SLAIN','SKIES','CHEAT','HOUND','DISKS','PAUSE','AMISS','BASIN','CLIMB','ROPER','CARAT','CABLE','GONAD','ENVOY','WANNA','ASKER','FENCE','FLOOD','TABBY','CAGEY','THUDS','LLAMA','LOLLY','SHAME','FORKS','SABER','CHIDE','PINEY','SWATH','LISPS','MOWED','SAVES','MOSSY','ISLET','LOVER','MIMED','TIRES','BLISS','PONDS','CRIED','FANNY','LUNGS','SOURS','ABOUT','PACER','FARMS','BLEND','TAMES','DITTO','BOSSY','HERON','ANNEX','VISTA','MEANS','DOUBT','WOMEN','DOPER','DORKS','GUAVA','GAILY','SUGAR','PARER','JOLTS','VEGIE','DADDY','SMASH','CROOK','STIFF','HOSED','FLESH','REPAY','WROTE','MAILS','BRAND','CORNS','TONER','AMAZE','TOOTH','PUPAL','SPIEL','GLASS','DAZED','FIRES','HONKS','GIRTH','TOXIN','POLIO','WAITS','WIRED','NULLS','WIDTH','LATER','POOCH','SIGHS','WHERE','WOULD','SPUDS','HURTS','EIGHT','FUNKY','REARS','GREEK','SPLIT','RAILS','CHAFF','FETUS','EARLY','SYRUP','EDICT','TORSO','NETTY','FLOAT','ITCHY','TOWEL','SINEW','LAMPS','ERASE','PAVED','BREAK','CAIRN','SPILL','DYING','SHIRE','SIREN','TOKER','SLITS','UNHAT','PUMPS','ROOMS','VOWER','LOCKS','HUNKY','HIPPO','DAMPS','ENACT','TRUCK','HOPPY','CANES','DUNCE','RECUT','TELLY','BETEL','PIKES','BUMPY','KITES','SPAMS','SWORD','DWEEB','GAYLY','SLOOP','PLUMS','FEAST','KICKS','SANER','LURCH','ICONS','FORTY','NYMPH','ROWER','BLOBS','RIPES','SHIRT','FROND','FURRY','MEATS','VAULT','GOODS','WADED','HOTEL','DATED','MOIST','BLAST','AGONY','ADOBE','JUNTO','LEECH','TRUMP','TEASE','CENTS','CREAM','NOSES','GIRLY','GAFFE','SEVEN','CRAZY','BAKED','AISLE','FLUKE','HAZEL','AUNTY','OUTER','SHARK','MILKY','BEGAN','SPIKY','RINSE','HEIST','GREAT','LINGO','BELTS','DULLY','VILLA','CURVY','DRINK','CAMEO','CRAFT','PULSE','ELBOW','HUMPS','CRANK','HIRER','MASKS','STUFF','ISSUE','FLOOR','POTTY','HUNCH','TWIGS','OAKEN','SCARY','DROOL','DATER','CANED','BASIL','BROTH','RAGER','SWIPE','MINED','CHICK','DRAIN','LOWLY','STEAD','URINE','RISEN','STUDY','PRUNE','BROIL','BIKES','TORCH','JETTY','AWAIT','MEETS','RAYON','RANCH','WHINY','PATIO','SEWED','DRIED','WRING','BESET','TEETH','MOONS','HALTS','COMFY','MAIZE','TWICE','LAUGH','LOOPY','HIKES','HOSES','STAYS','CLOUD','JEANS','SHAKE','UNLIT','SHRED','CONDO','GRAVE','BELIE','BREAD','SPEAK','MOVED','PALER','MAUVE','QUERY','CURVE','GLYPH','TASKS','GONER','ELECT','DEBTS','MEALY','RAINY','QUADS','BAKER','BUGGY','HYDRO','WINES','TRACK','REBUS','UNSET','UNCUT','FLUNG','DEVON','ROOST','SMOKE','HARSH','TACOS','DEMON','WATTS','CLOAK','ORALS','TIGHT','UTILE','BLUSH','ASSAY','DWELL','MOTTO','SHEEP','IDIOT','FATAL','ROWDY','CRANE','MUDDY','FIRMS','MAMBA','MOTOR','KOOKS','NEWER','DEIGN','PANGS','FIBER','MAMMY','POLLS','HELLO','EBONY','BOGUS','BOXES','PERKY','OVOID','GRAIN','NOVEL','JELLY','STILT','MANIA','ZAPPY','MYRRH','ATOMS','HATES','RISKS','TENDS','MORAL','RUSTY','LILAC','STUMP','JOKES','SQUAT','SATIN','WIMPS','HOVER','SPANK','CHIME','SCALE','KOALA','TODDY','FUMES','TRAYS','CIVIL','MINER','KNOBS','FANCY','FILED','HUBBY','BEARS','NEEDY','BICEP','IONIC','DREAM','CRONE','YIELD','FETID','SWIFT','HALVE','ROUGE','TUBED','BUDDY','STRAP','FOYER','CAPUT','HITCH','PHONE','FLIPS','PEAKY','TRUNK','MYTHS','STAVE','PACES','MATHS','ABODE','AROMA','BLITZ','TACKY','TRAIL','SHOCK','FAMES','CLOTS','TRIAD','NUKED','JOKER','PEACH','KNOTS','BADGE','CUBIC','STACK','CLUES','CHAOS','CRACK','TOFFY','GRUFF','PASTE','PROXY','IGLOO','POSES','PASTY','CYCLE','METRE','TIMES','SPELL','VERGE','DAMES','NIPPY','DOCKS','COMBS','AUDIT','DEBIT','SHYLY','SHRUB','SMILE','BULKS','SIEVE','FEIGN','SINCE','OMENS','SNUCK','SKILL','DRILL','LEAKS','FRETS','ZEBRA','IDYLL','WISER','FRONT','TERRA','BANGS','FEELS','GLOBE','DUMMY','TALON','DILLY','SLOSH','ROPEY','WOMBS','PAGER','UNLAY','BUSED','BEZEL','UNBOX','SACKS','SITES','CLANG','SNAPS','PORTS','KOOKY','TUMMY','CALLS','PINKS','RAMPS','RINGS','MOPPY','TEACH','FOLKS','BITTY','GRABS','GEARS','RARER','HOOKS','RACKS','SAUNA','CLINK','KNOWS','LOTTO','MOPEY','SLIPS','SANDS','FACTS','DUTCH','TWIXT','GENTS','VOILA','DRIVE','ROUGH','FILMS','HIDES','DORKY','ODDLY','CLUED','DIARY','SINGE','PAWNS','NINNY','KEEPS','MOLAR','BUILD','VENOM','CHIRP','SURER','PARIS','TAFFY','VIALS','JUNTA','SLIMY','SULLY','CRASS','SWORE','SLOPE','PIMPS','BAGEL','HIRED','HOPED','SCOOP','DRYER','BEAST','LYING','HUFFY','WIMPY','AWASH','BASTE','SHUTS','POSEY','DARER','WOOFY','GOATS','NUTTY','BRISK','GOOSE','SIXTY','SNORT','FELON','RACER','HOMER','DECKS','LINER','SLINK','BONGO','STUNS','IMPLY','LOSSY','PRIOR','DROIT','PIETY','TABOO','SOLID','HEADS','LIEGE','SMOCK','USAGE','HEARS','STANG','STEWS','TRADE','CAKEY','FUROR','SCRAP','REBID','SULKS','TOCKS','WALLY','KNOWN','LOSES','WANTS','MISER','STOOD','ANGST','BRAWL','NITRO','GLOOM','COATS','PAGES','METER','LATHE','PINTO','JUDGE','STARE','TOMBS','SPIKE','FAINT','WAFER','SLUGS','RUMBA','OBESE','TRUCE','FELLA','GUILT','TIGER','MIRTH','OARED','WALLS','SPORT','SNOWS','SCENT','SHREW','RETCH','SENDS','AIDER','SCREW','HANDS','FLUNK','RAMEN','CLICK','AXIAL','MOUND','ALTER','GLADE','JUICE','FATED','TROVE','COUNT','VITAL','FROZE','GOBBY','CRASH','SATYR','TROUT','TOOLS','LEVER','FETCH','ENJOY','KNOLL','WATER','ACTED','HOOCH','VALVE','PAPER','CHINS','FADES','PHASE','ABACK','ADOPT','GRIEF','GIANT','GRIME','GORGE','WASPS','WOMAN','LEANT','CORNY','WINKS','LOGON','FILLY','CANON','SMEAR','RIDES','FOLLY','DEBAR','EARTH','TENTH','TRASH','DISHY','CRAMS','MALES','FOOLS','FOODS','GROIN','CRUEL','OMEGA','FORTH','LORDS','BULGE','STRAW','RATIO','YOURS','WARMS','BINGE','CROCK','ASCOT','CANNY','CRUSH','HEFTY','RIPEN','THOSE','TRITE','GUTSY','CADET','PLAIT','ADEPT','RIOTS','BOXER','AGREE','FECAL','FJORD','DUKED','SURGE','FUDGE','CORAL','RIPER','WACKO','SHEET','BURPS','PRIMO','SILLY','SLICE','MANIC','SPIES','REMIX','WORSE','CHEFS','GULLY','STOMP','GRANT','SWIRL','TREND','PURES','CURER','SCOUT','TIERS','MAKER','NOTES','SPACE','TRAIT','BERRY','GLUES','CHURN','MOOED','TALLY','VERBS','SPANS','GRAIL','WISPY','BULLS','CHATS','MASTS','SHONE','SPARS','RATTY','RAKES','PESKY','FRIED','CRIER','AGLOW','GRUEL','ROVER','TAWNY','PLUSH','WORRY','OASIS','BEGET','NOTCH','SHOUT','ATONE','RALPH','SKIMP','PUNKS','TURFS','UNFIX','TROPE','SHAGS','SWORN','CAGED','SLEEK','TONGS','ELOPE','POACH','PURED','SADLY','GAMED','ENNUI','BINGO','GOLDY','VOIDS','DRAWL','RUSTS','CAKED','SUCKY','QUASH','GERMS','WELDS','AGATE','DECAL','NUDGE','VIGOR','SOILS','RHYME','DRONE','CIDER','STRAY','NAMED','GULPS','COUPE','CEASE','LANDS','CLING','SLURP','ASIDE','PIZZA','DELVE','COMBO','SABRE','WEIRD','PANSY','WHICH','TRIPS','DOTTY','FLOUR','CHIEF','LEAST','PENNE','TRYST','SEEKS','DINER','PRIME','THANK','WEDGE','CARVE','SAVER','TUNED','BEEPS','CREAK','TILLS','EASLE','GIPSY','DEATH','IRATE','NOMAD','STANK','MASSE','AWAKE','GRADE','FUMER','ABIDE','TERSE','NESTS','PIVOT','TOWNY','MAFIA','FARCE','PLIER','STAFF','PUDGY','SEEDS','NASAL','GLOVE','MANGA','REVEL','STINK','TALKS','MAGIC','REFER','SHEDS','BEGUN','VALOR','SLEDS','TENOR','CODES','MAYBE','FAIRS','PILLS','FROGS','SERVE','VOTED','MISTY','NAILS','SLIDE','AROSE','INPUT','CHEEP','FIXER','WIRES','SWEAT','PATHS','PEEKS','OVATE','CRIES','BLOAT','THERE','GRAVY','EMAIL','LENDS','BENCH','CHEAP','WARPS','LIKES','FRESH','DRUNK','BEANS','POESY','CABIN','GAMER','ALARM','ROAMS','MOOSE','WORDS','ALOUD','BORAX','AWFUL','FLAIL','IRONS','POISE','WHELP','ATOLL','STUNK','LOOSE','BLUNT','TOILS','THICK','DEFER','MUSIC','EMPTY','LURED','RASPY','SKATE','WORTH','PEARS','CURSE','GUSHY','PINTS','ADAPT','GECKO','LIMIT','LOOTS','OLDEN','WARNS','THING','LOYAL','WINCH','MOCKS','UNTIL','STOKE','UNDER','LIKED','SEEMS','HARRY','POSSE','MOVIE','CRUMB','VOTER','JOKED','TULLE','TONED','DONT','ABYSS','PULPY','MISTS','TUBES','KEBAB','RUNNY','FAIRY','LEFTY','UNITY','TOKES','SWANS','CLIPS','RISKY','PICKY','SILKY','BLURS','STEPS','COCOA','URBAN','WHISK','FREAK','ANGLE','STORE','CURDS','COLDS','SENSE','COURT','NOSEY','MOTEL','CIRCA','BLUFF','LITHE','OTHER','SPASM','COMIC','MACRO','CRIMP','LOBBY','HORSE','STORY','HONEY','PUPIL','EAGLE','PALSY','LICKS','CHUNK','LEGAL','SPARK','ASKED','STILL','STALL','DROWN','HASTY','STERN','TRIED','SWAPS','WEARY','CONCH','COVEN','TUBBY','HEATH','CAGES','PILER','POKIE','TREAT','EXAMS','UNITS','JOIST','ETHER','MAXIM','WEAVE','NANNY','SLOBS','HANDY','PLUMB','INLAY','NERDS','LADLE','DWELT','HOLDS','SPURN','TOUGH','PLONK','CLERK','SEWER','SPOTS','BURNT','TARED','STUCK','DOJOS','IVORY','CREPT','MORPH','RULER','HOWDY','RIFLE','WIELD','BORED','BLARE','STUNT','RAZOR','SOUND','DUDES','WAXEN','NINJA','ANGEL','CASED','OMBRE','PLUCK','PRISM','SPEED','MATTE','FIELD','PAPAL','ELVES','BRAKE','SWAMP','MEALS','PURER','TWEED','BASAL','INDEX','LIKER','SIDED','PEAKS','SWASH','LUMEN','PATCH','STOOP','WICCA','CARER','WAIVE','EERIE','KNIFE','PATTY','GOTTA','SPUNK','AMONG','AZURE','FUELS','CHORE','KNAVE','SCOUR','BANJO','REFRY','QUOTE','DICEY','CACAO','INCUR','ACTOR','ENDED','BLEED','TEMPS','HARPY','OPTIC','VEGAS','DIVES','POLED','APART','LIVID','XEROX','LYMPH','CHANT','PRICE','UNZIP','PARSE','STAKE','NUKES','HEDGE','HIDER','GRITS','TEARS','VEILS','GROWN','STATS','FIFTY','SHORT','VIRAL','QUIET','USERS','SOBER','TACIT','DAZES','SNUFF','COPER','LIVEN','NOBLE','SPITE','CAVIL','TUNIC','ACUTE','RAKED','SCORE','MOGUL','CREEP','TENET','TYRES','STEEP','DAISY','PREEN','SNOOP','TIBIA','DITTY','SURLY','PALMS','VEGES','ROMPS','THIGH','ARTSY','DOING','SHEAR','SUNNY','LIVED','SALLY','PEARL','STUDS','FLAKY','BURLY','ALGAE','STOIC','DIODE','AVERT','FAULT','VOCAL','BATHS','EARLS','SALTS','QUILL','AVAIL','INSET','FATTY','SCOPE','DESKS','GENIE','COWER','CLOCK','UNITE','WOODY','TRAMP','SNEER','SPEAR','CRISP','EXALT','HUSKS','DAILY','SHIRK','LUCID','PROBE','WAVEY','MEDAL','SCOOT','PURGE','BEAKY','SPINE','SHOOT','ALIKE','STAID','CASTS','MIGHT','TAKER','THORN','SPRAY','BANKS','GOLDS','BEVEL','REAPS','COULD','SKIDS','BEIGE','STALK','WACKY','EVENT','TUNER','AORTA','BONEY','JUICY','NEEDS','BITES','STABS','TURNS','BAKES','MEANT','COMES','SOUPY','TAKES','RAGES','CLUBS','GIFTS','MOVES','FERAL','SHAFT','UNMET','JADED','CLASP','INANE','PARED','ADAGE','SHARD','SLAVE','STRIP','BATON','SCRUM','SETUP','FUSED','REFIT','APNEA','KAPPA','FLATS','FORGO','GONGS','SAUCE','GLUED','TACTS','RAKER','HASTE','GEEKS','SAWED','OWING','SHARP','TAPES','DOZEN','HOWLS','EMCEE','LEPER','SHADE','BARNS','PULLS','RIDER','HOARD','SKIER','WARKS','YUCKS','PUSHY','GEESE','APRON','PRUDE','SEATS','RADIO','FRITZ','SCART','CUBES','FEMME','NICHE','LOAMY','OOZES','DISCO','TRICK','CONIC','OCCUR','NERVY','HINGE','DRIFT','APPLY','ABBOT','GLAZE','FACET','TAPIR','SQUID','SLAPS','INNER','BIDDY','SEGUE','HUMID','STALE','GROAN','OCTAL','RESIN','SHELF','PIGGY','BARFS','FLIER','PEELS','PLOYS','EXERT','STAGE','PUBES','SWIMS','EATER','SOWER','STICK','TUCKS','GRUBS','FLOWN','SHACK','OXIDE','REIGN','HERBS','APING','HOLES','AWARD','TARPS','GREED','DIALS','MOLES','LADEN','MOMMY','RELAY','BELOW','AMPLE','GREET','BOOED','SKIPS','AFOOT','FLANK','PORKS','PUNCH','CROSS','CRIBS','TARTS','PENAL','YELPS','GASSY','SEPIA','PARRY','CLOSE','HUSKY','GUNKY','ALONE','GROSS','WOOZY','FILES','REAKS','LASSO','BUNNY','FIGHT','STORM','STEAK','STEIN','TRAPS','CABBY','NUDIE','LIVES','TYRED','CAROL','FIZZY','PROUD','TECHS','ONLAY','GLUEY','PLAIN','BEACH','COLOR','STAND','SQUIB','UPSET','SALVE','ENTRY','POLYP','QUOTA','MOODY','SWARM','BIMBO','RIGID','LUMPS','KIOSK','VEGAN','DOZES','FIXED','POINT','STEAM','TOADS','TRUSS','LOGIC','HATED','BARON','FLAME','NOBLY','GOOEY','LEARN','TWINS','STEAL','CORKS','DOPES','TOURS','WICKS','REARM','DENTS','FADED','GRANS','DENSE','PICKS','CLOUT','OUTGO','SALON','SLABS','UNARM','UNFED','ROOTY','COALS','PATSY','SANDY','ALOOF','OFTEN','PINKY','GROPE','RAISE','TOWER','HARPS','HOSTS','ANNUL','JIFFY','INTEL','BILGE','ZONAL','CARED','PLUGS','SIGHT','VEINS','CALMS','TRUST','PITCH','NEGRO','STOUT','TREAD','THEIR','TOPIC','MOWER','STEER','LOATH','DOPED','LUSTY','TACKS','SCENE','PANIC','FULLY','NOUNS','CHAFE','PIECE','TILES','FORMS','CREPE','GAWKY','PRONG','TREKS','JEWEL','CLEFT','DEVIL','RELIC','HILLY','ABBEY','CYNIC','SALAD','FLUTE','GAUNT','SHOWS','AMBLE','FLAKE','DROLL','GRIPE','BRAVE','BOOTY','GABBY','WENCH','LUMPY','CHOPS','PEEPS','SPOOL','BRIBE','NAMES','KRILL','DINES','SHALT','WELCH','PUREE','COVEY','POSER','THESE','TRIAL','GEEKY','LEAPT','HACKS','WEEDS','WHIFF','DRAPE','LAPSE','GAUZE','SODAS','BUZZY','GLIDE','WEIGH','HAPPY','KARMA','TAKEN','PENDS','RETRO','FLOSS','BLOKE','STARS','SCUBA','DALLY','SOPPY','WOOLS','PLAYS','EJECT','DRAKE','LOVEY','SCARS','CURRY','WOWED','BOOTH','ARROW','LEMUR','QUAIL','STRUT','FARER','CHARD','VOGUE','FLEAS','BRAIN','RESET','QUICK','PIXIE','CLANK','GAZES','CLUMP','JOINS','LAKES','SEDAN','WAVER','MATES','DARES','STONY','MINOR','SHINE','AGENT','MERCY','TILDE','CASES','SPEWS','TRAMS','FAMED','TARTY','BENDY','FACES','PSYCH','FILMY','QUIRK','CUBED','GHOUL','CUPID','GENES','REBEL','HOLED','SLACK','BALER','MARSH','PILOT','SWEET','VALET','BRUTE','MAIDS','CHAIN','UNCAP','EXIST','MURAL','BLOWN','DONUT','HOIST','MINDS','MASON','FABLE','ARMOR','PLACE','SHINS','UNDID','TRIMS','DUMPY','SPIRE','DOWRY','ROSES','CHEEK','AUDIO','BELLY','DEMUR','DECAY','GRUNT','FATLY','CRAMP','BUTTE','FELTS','WHITE','SALSA','CREST','MILES','VISIT','RESTS','WINDS','BULLY','SNIFF','HOOTS','SHOVE','CUTIE','NEIGH','ANTIC','GRAPE','VIXEN','GAVEL','OUIJA','LOOPS','YANKS','CAPER','SPADE','BRAVO','REHAB','ROTOR','WELSH','SMOTE','BOUND','HAIRY','GUARD','TANGY','SAVED','WAKER','SUCKS','WIVES','ERECT','MANLY','MUMPS','MADAM','TILED','SIZED','SKUNK','AGAIN','MEMES','ALPHA','PAYEE','AFIRE','BRASS','FIFTH','KNEEL','RABBI','FAITH','WRONG','SLANG','EDITS','HOMIE','HELIX','CAGER','COPES','GULCH','GRASP','PLAID','ELFIN','WRACK','LITRE','MAGOT','BUILT','PARTS','HEEDS','TRULY','MEOWS','DOLLS','BEAKS','SUITS','CREEK','SPORE','LANES','BLURT','OUGHT','LOVED','ARISE','FUGUE','GOODY','QUEEN','HEADY','GUESS','SLATE','OLIVE','THIRD','BELLS','PERCH','GAWPS','ONSET','TRIPE','CATCH','TIRED','MUSTY','THROB','HONOR','DECOR','ALIBI','SUING','FLUID','EBOOK','HYMEN','MISSY','FIRED','MOONY','BOOBY','LEASE','DUSKY','CREME','BOOKS','POURS','SPOKE','PRICK','WIPED','NAIVE','GLOAT','SPAWN','SWEAR','ALLEY','HILLS','RAGED','REGAL','SWINE','DANDY','URGED','SONGS','COLON','BLOND','AVIAN','YEARN','FIEND','LOOFA','WEEPS','ITEMS','RANTS','ORBIT','MOATS','GUIDE','QUAKE','SCREE','REPEL','EASTS','BIRTH','SNIDE','WELTS','EVOKE','ILIAC','JOINT','SLASH','WRATH','ALLOY','PANDA','CYBER','TANGO','ALOFT','MACES','POEMS','RUSHY','LIMBO','SOOTY','SNAGS','CROWD','FOOTY','PUBIS','GODLY','MECCA','DINED','GUPPY','SCABS','PRONE','BOAST','STROP','SINKS','NINTH','HUMOR','RURAL','RENTS','SWILL','YAHOO','VIVID','GENRE','BORNE','CIVIC','LABOR','GAUDY','SIZES','REUSE','PAVES','FINAL','NIGHT','SKULL','OGLES','YEAST','KINGS','HURRY','FOLDS','LUNAR','ARENA','BRACE','EXITS','SWOOP','HINTS','RIVER','COUCH','MOPES','TAXER','WHEAT','RAGGY','REPOST','RATER','TRODS','EASEL','ARRAY','HUMPH','LOTUS','FEMUR','BIBLE','FLAPS','CREWS','QUILT','LIVER','RAJAH','NAGGY','BIGOT','IDLER','QUARK','RECON','ROGER','FINER','GLEAN','TALKY','BOWEL','PENNY','PLAZA','BARGE','ROBES','NIECE','HIKER','WOODS','BEECH','BEATS','TAXIS','TWANG','MAZES','GLEAM','DEBUT','POPPY','SAFES','DARED','SMITH','EQUAL','CANDY','SHIFT','TARES','UMBRA','HUMAN','BELLE','VISOR','RADAR','EXTRA','PANES','MINTY','SISSY','PRESS','TOTEM','RUMOR','OINKS','DUCHY','ORGAN','PACTS','SOOTH','VIPER','INGOT','FIVES','BLEEP','DIVER','APHID','BEEFY','ROOMY','SOUTH','EGRET','OVINE','SLUSH','MOUNT','TRACT','FORGE','AMBER','SCRAM','OBEYS','FLECK','HOLLY','FREED','TOWNS','LIFER','WHALE','VINYL','TONES','SWAMI','GLUER','SOFAS','HORNS','JAPAN','INTER','SCORN','HYENA','MELEE','IMPEL','FLICK','BRASH','CLAPS','HABIT','ABUSE','TRAIN','PALES','NAZIS','HOTTY','MELTY','RAINS','STUNG','PLEAT','IRONY','GUISE','DOGGY','TEMPT','HAUNT','WIPER','DINGY','MUSHY','POOLS','LINEN','CRATE','BREED','STOCK','CHART','EXILE','USURP','FOCUS','SEMEN','SHAWL','SKIRT','EXPEL','CHOCK','LEASH','CROWS','HISSY','MESSY','SPICY','SNOUT','PARTY','TOPAZ','WHOSE','BONES','PAVEN','PSALM','FAYRE','CHUCK','TOOTS','FLOUT','GRAFT','STINT','HEARD','ADDED','BLURB','WINCE','RUPEE','CHALK','PECAN','FRUIT','NOISE','CHEST','ZESTY','INKED','KIDDO','SEALS','SWISH','LOGIN','INDIE','ASHEN','NOTED','PERKS','TWEET','ELIDE','TUMOR','SPERM','FACED','FLING','THEME','MINIM','HEAVY','TUTOR','TAINT','WHOOP','HULKY','MOLDY','VICED','PRAWN','CROPS','STASH','YELLS','OFFER','HARDY','MINUS','CRICK','LAPEL','MERRY','IDEAS','TOKEN','GUSTS','BUXOM','BLUER','MOMMA','MOUTH','EMBED','ECLAT','RINDS','STAIN','BUSTS','TOWIE','SIEGE','CHEER','DARTS','SLUNG','OAKED','PELTS','BOSOM','SLOTH','PAGED','CHARM','SOILY','CURBS','ABASE','DROSS','NERDY','TITHE','PLUME','DOWDY','CHEWY','ENDOW','PURRS','COCKY','OFFAL','DIRTY','HALAL','PLIED','RIGHT','GLARY','RELAX','DEUCE','STOLE','ROARY','CHOMP','TONAL','AFFIX','ELEGY','LOSER','THUGS','STAGS','WORKS','SLUNK','STORK','OTTER','OPINE','HOTLY','START','GOTHS','HUMUS','WIDER','BASIS','GREEN','SUMAC','WATCH','ELUDE','BLOGS','SLICK','WRITE','DIVAS','VALID','SAVOR','MOLDS','WAVES','SHINY','WORMS','THREW','VAPOR','SOAPY','SIFTS','MANGY','WAKES','BLOOD','TURDS','ELDER','FISHY','TEXAS','PROPS','TOTTY','RAFTS','MONTH','TOXIC','HOBBY','SLYLY','TOWED','WARDS','LEACH','ANODE','MOVER','PLANS','GRIMY','ROBOT','SMELL','FARTS','GOUGE','ROLLS','SINUS','ROARS','ALLAY','OATHS','EQUIP','TREES','PROMS','SLOTS','PRISE','LYNCH','LAMBS','RIVET','AFOUL','HUTCH','SLIMS','PEDAL','SICKO','UPPER','POKEY','JELLO','SIGMA','WALTZ','NORMS','POLER','GUMBO','DRANK','SPINY','COVET','DENIM','SOLES','VOUCH','STARK','HOODS','YUCKY','EMBER','TINTS','BATHE','GNASH','GYPSY','SCANT','BILLY','WIRER','BAWDY','GAUGE','COVER','CLASH','FUNNY','BANAL','DROPS','MAMBO','SHELL','HYPED','UNFIT','BOARD','SCOLD','RIDGE','COAST','LISTS','SOAPS','SHRUG','FRIAR','HAREM','NUMBS','VICAR','WITTY','SLIME','FAXES','VENTS','DRIER','MACED','SORTS','SUITE','PURSE','SHILL','NEVER','GRIND','TONGA','VIEWS','SNORE','WAGGA','MUNCH','TARDY','WHEEL','BERET','DOUGH','SMACK','TESTS','LEERY','NOOSE','AHEAD','ENTER','FOAMS','SEEPS','ANIME','SHOWN','CURIO','STONE','POUND','HEART','DOLLY','ESSAY','BROOM','PEACE','SCARF','VAGUE','CLAYS','HOURS','NIFTY','JERKS','FRILL','CHOIR','FAVOR','MINTS','MULES','CATER','BEFIT','COMET','FETAL','POWER','ROPED','ROADS','FENDS','GAPED','AXION','FINCH','ROCKY','WREAK','WAHOO','TONIC','SIXTH','SHOPS','PIQUE','KINKS','DOWEL','UNIFY','MELON','CHILD','SNARL','VALUE','CODED','NEWED','KITTY','CORER','BLIPS','WAIST','CALFS','FICUS','UNBED','AVOID','DEPOT','FLASH','WRECK','GAYER','DUMPS','CRESS','RUDER','RENAL','BOOST','HERDS','RENEW','VIBES','WAGER','DONOR','CRAVE','HAVEN','FRAME','TULIP','DEALT','MAPLE','TOTAL','FILTH','POSIT','PROWL','BALLS','BROWN','PLATE','THUMP','DRIES','JAUNT','VOCAB','OVARY','ADORE','DODGY','PROOF','SWEEP','CLANS','SHARE','BLOCK','DITCH','SPREE','TAROT','FLORA','BEADY','FROTH','NASTY','CUPPY','GOWNS','VINES','ARSON','CLEAR','PUNTS','VESTS','CLUNG','FILER','SHAVE','SKINS','BOARS','NICER','NOSER','ONION','OLDIE','COYLY','MOULD','SNUBS','TAXES','QUEER','SCARE','GOURD','SOLVE','MORON','SHEIK','LARGE','CRAWL','SHUNT','EVERY','MIDGE','GULPY','CANOE','LOWER','SHEEN','TORUS','RAVEN','CHESS','SAVOY','BRUNT','CARTS','AMITY','BAGGY','HAVOC','CROWN','VIOLA','GRINS','WOOFS','KHAKI','TWINE','EVADE','CAUSE','VODKA','SHUSH','WANDS','WINGS','FRISK','FARES','LUNGE','PEERS','CHORD','BLESS','OVENS','BRINE','BISON','TITLE','WAGED','CURED','HYPER','COACH','FLUFF','HATCH','BITER','INBOX','PAYER','PORER','ROPES','LORRY','BERTH','THRUM','FOWLS','GIDDY','WALKS','POKER','FALSE','KINDS','ALONG','DUSTY','DEBUG','LOCAL','QUEUE','MOODS','CHAIR','BONDS','MAMMA','YEARS','BUCKS','CROAK','NOISY','FALLS','BRINK','SALTY','SONIC','SALES','SPILT','PAVER','TRAWL','JAZZY','LATCH','SILKS','REEKS','SHAKY','SKULK','CANAL','PANEL','LIPID','LEADS','DIMLY','ACHOO','CUPPA','CELLO','SERIF','LOVES','BACON','DELTA','SCUFF','TAMED','ROUSE','USING','IDIOM','BLING','BROOD','GOOFY','CHASE','AUGUR','STING','SPITS','LUPUS','LUNCH','HOMES','KAYAK','PHONY','TIPSY','MARRY','DRAWN','FIXES','STOPS','NERVE','ALTAR','INLET','FORTS','RULED','PYGMY','HAUTE','CHUMP','SMOKY','RHINO','OGLED','NAVAL','UNCLE','ICING','SPOOK','WORLD','WRIST','LURID','POUTY','WHARF','CEDAR','VEINY','ORDER','TASTY','STAIR','SERUM','SHEER','GLOWS','STEED','GRAPH','LINES','DAUNT','AGILE','RACED','BOOTS','REACT','SAINT','FOUND','BUNCH','REBAR','REFIX','SHOTS','PESTO','GRACE','AXIOM','SOUPS','NUDES','PACED','NIGER','BIRCH','PRIVY','PUFFY','CLAMP','MICRO','SHOAL','LIGHT','FAKES','PADDY','WHIRL','FUZZY','ABORT','NATAL','TROTS','TRUTH','PAINS','RUINS','ABATE','BOOZE','PETTY','BRIDE','GUEST','TRACE','BOLTS','LIPPY','RUDDY','MEADS','THYME','ERODE','REBUT','TRIES','CABAL','WIPES','BUNKS','LOFTY','LOUSE','CRUMP','EATEN','CONES','VERSE','MARKS','RERUN','DELAY','WAGES','JUROR','BOOZY','YOLKY','SPENT','WAFTS','BLAME','BARES','THUMB','WAVED','TENSE','DUVET','GASPS','ANNOY','RECUR','NANNA','MURKY','CARES','BEARD','FATSO','AWARE','BEGAT','FORTE','KNEAD','TROLL','DETOX','PASTA','HOLEY','DRYLY','CASTE','FLIRT','TOAST','MUCKS','ANGER','WORST','QUART','USHER','ATTIC','RABID','SMITE','ESTER','DRAMA','BROAD','SHALL','DRUID','NEWLY','GRASS','SLEEP','CLACK','SASSY','WIDEN','QUALM','VERVE','ALIGN','BRINY','DROOP','SHANK','THREE','MATED','COPSE','CINCH','EPOCH','GIVER','HEALS','HUGGY','VOLTS','ROUND','SMELT','FOAMY','REACH','HIRES','APPLE','THIEF','SEVER','NAPPY','ROYAL','FRAIL','BROOK','FLAIR','MOCHA','OPIUM','LUCKS','KNELT','REMIT','ASKEW','LYRIC','WOVEN','DICED','DODGE','OCTET','SCALP','SOGGY','LURES','JUMBO','STUBS','FIVER','HOVEL','GAZER','ROMEO','UNION','CATTY','RETRY','SINGS','ENSUE','CHILI','CRONY','MONKS','CURLY','CLONE','OLDER','PLEAD','SPOUT','ERROR','SNAKE','CHINA','OPERA','PRINT','CARDS','STAMP','GRAND','BALMY','FORCE','CLOTH','TURBO','BLOOM','AMASS','CLOVE','OGLER','POKED','TEENY','BLIND','SNEAK','TEPEE','GROWS','PROMO','SPINS','KIDDY','FAKER','JUMPY','FOCAL','SHOWY','FISTS','ROOTS','SNAKY','EASES','ALIVE','RANDY','PLOPS','IDEAL','DETER','WINDY','FLUME','INTRO','GOLLY','LEDGE','WHOLE','BIKER','LANKY','ENDER','JOLLY','STYLE','SPRIG','REEKY','MOUSE','BLEAK','PAINT','GROUP','ERUPT','POETS','ETHOS','MONEY','SPEND','FIRST','SPICE','CURES','HYPES','RECAP','GROWL','EXACT','SUSHI','TWIRL','UDDER','WIGHT','RODEO','GAINS','ABHOR','MITES','POLEY','VENUE','SHIED','GAMMA','CAULK','PROVE','SWOON','PAGAN','FAUNA','SCOWL','CLAMS','CIGAR','ADORN','MATEY','KNACK','FLINT','SWUNG','FLOCK','MAYOR','SPLAT','WOOLY','WANES','IMAGE','BLEAT','SWAYS','TIMID','FROST','SOAKS','CACHE','VICES','LEAVE','PARKA','QUITS','ELATE','GHOST','PUPPY','SPOIL','LOCUS','STOOL','BRAID','POUCH','NOSED','TEENS','RISER','FRIES','HIPPY','TIMER','LUCKY','DIRGE','SHUCK','MILKS','WORDY','HATER','ADMIN','VYING','BULBS','GOING','CARRY','WOOER','LEMON','PANTS','SWIGS','DEPTH','ACIDY','FRIER','MOULT','OVERS','DINKY','RIVAL','TICKS','AMEND','LEEKS','MANOR','TIDAL','MELTS','EDGES','DOPEY','PERIL','WOUND','WARTY','MIMES','PRANK','BURST','GIVEN','TEPID','HOPER','THROW','GUMMY','REPLY','WRYLY','SIGNS','ROAST','MUCUS','ROUTE','NACHO','LEAFY','BOTCH','AGORA','SCOFF','SWEPT','CHOSE','MIDST','TUBAL','GOLFS','SONSE','BOWLS','GETUP','LOFTS','PETAL','UTTER','WIDOW','CLAIM','PUBIC','ABOVE','GROOM','HORDE','MUCKY','LANCE','TROOP','RISES','EAGER','FILET','SQUAD','SNAIL','TRUER','LASER','JADES','WITCH','ENEMA','FAKED','FEVER','WHIPS','ASSET','EYING','EMITS','DEALS','COMMA','CREED','PENCE','TOLLS','VOWEL','MANGO','ALLOT','SHOOK','AIRED','JOUST','BADLY','FLACK','CADDY','GRIFT','WOOED','SIDER','TWIST','KNOCK','HEAPS','TEXTS','SPOOF','RACES','SKIFF','AGING','BRIEF','HORAH','PRIZE','THETA','LEVEL','POSED','ACRID','READY','APTLY','OILED','UNLID','SCALD','MOPED','HEELS','AMPLY','GLAND','YOUTH','GLARE','QUITE','BUDGE','MARCH','ARGUE','TAPER','FEATS','SIDES','FUSSY','FAILS','VISAS','WELLS','ANVIL','HOUSE','BUSTY','GLOSS','BUGLE','BLANK','TAUNT','PORCH','SYNOD','WASTE','REELS','RATED','CROUP','SORRY','GUSTO','LARVA','MACAW','MODEL','BARKS','FINED','HEATS','MINES','HAIRS','SOCKS','ALLOW','SWABS','EXTOL','FROWN','PLANT','FORAY','DWARF','HEAVE','UNTIE','WANED','PAIRS','UNPIN','BATTY','DEMOS','REMAP','SNARE','TODAY','YACKS','LOUSY','CHILL','EPOXY','AWOKE','MOSES','YACHT','HOODY','SLUMP','ALBUM','GROUT','MOTIF','BULKY','TABLE','DISCS','DRIPS','JIHAD','DROVE','UNWED','JESUS','MOANS','CHAMP','SMALL','SKINT','TAILS','BUYER','SCALY','TITAN','GAMES','YARDS','DRESS','LIBEL','HORNY','SNOWY','FUMED','OWNED','POLES','FLARE','TRIBE','DUNKS','CLAWS','PITHY','TANKS','CLEAN','BOATS','POKES','LACEY','REFLY','DREAD','GIVES','WREST','DUMBO','DEEDS','HAWKS','RANKS','DOGMA','FLEET','SHORN','TUNES','RAPID','WEEDY','ROCKS','WAKED','MERGE','CRIME','BELCH','CHASM','GUILD','WHINE','CLOGS','TYING','VOICE','TIDES','BEADS','EASED','TEARY','RARES','TATTY','SLUMS','EXCEL','HAILS','PANTY','CHIMP','ETHIC','EGGED','CRYPT','DIGIT','PORES','TOONS','INERT','FOIST','SCION','CURLS','ANGRY','FONTS','DIVED','INFER','VOTES','GRAZE','WRAPS','ETUDE','IMBUE','MODEM','TENTS','SPOON','FLYER','LEGGY','BRICK','ANKLE','RUGBY','TELLS','OSCAR','BOBBY','TIMED','PLANE','TIARA','SLEPT','FERRY','FRAUD','MODAL','MULCH','QUOTH','GUSTY','PLUMP','ABLED','ULCER','PUTTY','SAPPY','BOOBS','SEEDY','MINCY','MAJOR','CHIPS','VIGIL','FROCK','MUSKY','DATUM','CHECK','BUTCH','SCONE','JUMPS','SOLOS','REVUE','RALLY','BUSHY','WAGON','TARRY','HENCE','PRATS','CLIFF','AMUSE','SMIRK','THINK','BRAWN','LIKEN','SUPER','EXULT','SLAMS','GOLEM','TESTY','CAKES','FIERY','PORED','JERKY','DAIRY','MERIT','AGAPE','BROKE','QUELL','SUAVE','RIPED','CHEWS','VAPID','SNIPE','FINES','SAFER','SHOES','EKING','UNDUE','MINCE','VIRUS','ADULT','ROGUE','GIRLS','HIKED','NURSE','SONAR','QUEST','FOLIO','PINCH','UNJAM','FISTY','BLOWS','FARED','MALTY','OVERT','FATES','LEAKY','BONUS','MEDIA','ICILY','AFTER','MATCH','FANGS','GROVE','OCEAN','TEMPO','OUTDO','FOGGY','PORKY','CAMPS','BLAZE','MACHO','DOILY','PSYOP','OWNER','BRIAR','SCAMS','PANTO','SPATS','ODOUR','LABEL','GOOFS','SPURT','ODDER','LATTE','REALM','YOUNG','SNOBS','REEDY','CARBS','PLOTS','MADLY','TERMS','LACED','DECRY','MEDIC','KINDA','OUNCE','VERSO','SOLAR','COINS','PINGS','SWING','SPARE','MAGMA','ARBOR','MOPER','MANGE','POLKA','RULES','PIPES','LODGE','CRUST','SNIPS','PIANO','RINKS','NODES','LACES','LAGER','PROSE','SHIPS','GANGS','RADII','NOTER','YONKS','GAZED']

# print (','.join(map("'{0}'".format, words)))
found = []
args = []

def checkcolors (wrd):
    global args
    for i in range(len(args.green)):
        if (wrd[args.greenpos[i]] != args.green[i]):
            return 0
    for i in range(len(wrd)):
        if (wrd[i] in args.grey):
#            print("failed grey ", wrd[i], grey)
            return 0
    for i in range(len(args.yellow)):
        if (not (args.yellow[i] in wrd)):
            return 0
        if (wrd[args.yellowpos[i]] == args.yellow[i]):
            return 0
#    print("check passed", wrd)
    return 1

def checkpos(w1, w2):
    global args
    for i in range(len(args.matchpos)):
        if (w1[args.matchpos[i]] != w2[args.matchpos[i]]):
            return 0
    for m in range(len(args.notmatchpos)):
        if (w1[args.notmatchpos[m]] == w2[args.notmatchpos[m]]):
            return 0
    return 1

def main():
    global args

    parser = argparse.ArgumentParser(description='Wordle Helper')

    parser.add_argument('-dopos', action='store_true', help='Match Positions', required=False)
    parser.add_argument('-docolors', action='store_true', help='Match Colors', required=False)
    parser.add_argument('-MinMatches', help='Min Matches on Positions', default=2, type=int, required=False)
    parser.add_argument('-MaxMatches', help='Max Matches on Positions', default=100, type=int, required=False)
    parser.add_argument('-matchpos', nargs='+', help='Matching Positions', type=int, default=[], required=False)
    parser.add_argument('-notmatchpos', nargs='+', help='Not Matching Positions', type=int, default=[], required=False)
    parser.add_argument('-grey', nargs='?', default='', help='Grey String', required=False)
    parser.add_argument('-green', nargs='?', default='', help='Green String', required=False)
    parser.add_argument('-yellow', nargs='?', default='', help='Yellow String', required=False)
    parser.add_argument('-greenpos', nargs='+', help='Green Positions', type=int, default=[], required=False)
    parser.add_argument('-yellowpos', nargs='+', help='Yellow Positions', type=int, default=[], required=False)

    args = parser.parse_args()
    print(args)
    numw = len(words)
    numc = 0
    nump = 0
    for j in range(numw):
        w1 = words[j]
        if (args.docolors):
            if checkcolors(w1):
                numc += 1
                if (not args.dopos):
                    print(w1, "CCCCC")
            else:
                continue
        if (args.dopos):
            if (w1 in found):
                continue
            nmat = 1
            temp = []
            for k in range(numw):
                w2 = words[k]
                if ((w1 == w2) or (w2 in found)):
                    continue
                if (checkpos(w1, w2)):
                    temp.append(w2)
                    nmat += 1
            if ((nmat >= args.MinMatches) and (nmat <= args.MaxMatches)):
                print(w1, temp, nmat, "PPPPP")
                nump += 1
                found.append(w1)
                found.extend(temp)
    print("Num Color Matches = ", numc, " Num Color & Position Matches = ", nump)
main()