grammar OVP;

// ============================================================
// PARSER RULES
// ============================================================

sentence
    : nounSubjectSentence
    | pronounSubjectSentence
    ;

// SOV order when subject is a noun
// e.g. "isha'-uu pagwi-noka u-zawa-dü"
nounSubjectSentence
    : subjectNoun objectNoun transitiveVerb   # NounSVO
    | subjectNoun intransitiveVerb            # NounSV
    ;

// OVS order when subject is a pronoun
// e.g. "pagwi-noka nüü ma-puni-ku"
pronounSubjectSentence
    : objectNoun SUBJECT_PRONOUN transitiveVerb  # PronounOVS
    | intransitiveVerb SUBJECT_PRONOUN           # PronounVS
    ;

subjectNoun      : NOUN HYPHEN subjectSuffix ;
objectNoun       : NOUN HYPHEN objectSuffix  ;
transitiveVerb   : OBJ_PRONOUN HYPHEN VERB HYPHEN tense ;
intransitiveVerb : VERB HYPHEN tense ;

subjectSuffix : II | UU ;
objectSuffix  : NEIKA | NOKA | EIKA | OKA ;
tense         : KU | TI | DU | WEI | GAA_WEI | PU ;

// ============================================================
// LEXER RULES
// Longer tokens take priority over shorter ones (maximal munch).
// Order within same length: first rule wins.
// ============================================================

// Structural separator between morphemes
HYPHEN : '-' ;

// --- Tense suffixes ---
// GAA_WEI contains a hyphen so must be defined before HYPHEN
GAA_WEI : 'gaa-wei' ;
KU      : 'ku'  ;
TI      : 'ti'  ;
DU      : 'dü'  ;
WEI     : 'wei' ;
PU      : 'pü'  ;

// --- Object suffixes ---
// Longer forms first: neika before eika, noka before oka
NEIKA : 'neika' ;
NOKA  : 'noka'  ;
EIKA  : 'eika'  ;
OKA   : 'oka'   ;

// --- Subject suffixes ---
// uu before u (maximal munch: uu wins over u)
UU : 'uu' ;
II : 'ii' ;

// --- Subject pronouns ---
// Longer tokens first to avoid partial matches
SUBJECT_PRONOUN
    : 'taagwa'   // we (inclusive)
    | 'nüügwa'   // we (exclusive)
    | 'üügwa'    // you (plural)
    | 'uhuw\u0303a'  // they (proximal): w + combining tilde
    | 'mahuw\u0303a' // they (distal)
    | 'ihiw\u0303a'  // these
    | 'mahu'     // he/she/it (distal)
    | 'nüü'      // I
    | 'uhu'      // he/she/it (proximal)
    | 'ihi'      // this
    | 'taa'      // you and I (dual)
    | 'üü'       // you (singular)
    ;

// --- Object pronouns (prefix on transitive verb) ---
// Longer tokens first
OBJ_PRONOUN
    : 'mai'  // them (proximal)
    | 'tei'  // us (inclusive)
    | 'üi'   // you (plural)
    | 'ui'   // them (distal)
    | 'ma'   // him/her/it (proximal)
    | 'ai'   // them (proximal, alternate)
    | 'ni'   // us (exclusive)
    | 'ta'   // us (dual)
    | 'a'    // him/her/it (proximal, alternate)
    | 'i'    // me
    | 'u'    // him/her/it (distal)
    | 'ü'    // you (singular)
    ;

// --- Verb stems ---
// Includes both base and lenited forms.
// Lenition rules: p->b, t->d, k->g, s->z, m->w̃
// Lexicon maps both base and lenited form to same English meaning.
VERB
    : 'tüka'    // eat (base)
    | 'düka'    // eat (lenited: t->d)
    | 'puni'    // see (base)
    | 'buni'    // see (lenited: p->b)
    | 'hibi'    // drink (h unchanged)
    | 'naka'    // hear (n unchanged)
    | 'kwana'   // smell (base)
    | 'gwana'   // smell (lenited: k->g)
    | 'kwati'   // hit (base)
    | 'gwati'   // hit (lenited: k->g)
    | 'yadohi'  // talk to (y unchanged)
    | 'naki'    // chase (n unchanged)
    | 'tsibui'  // climb (base, also intransitive)
    | 'sawa'    // cook (base)
    | 'zawa'    // cook (lenited: s->z)
    | 'tama\'i' // find (apostrophe = glottal stop, escaped)
    | 'nia'     // read (transitive)
    | 'mui'     // write (base)
    | 'w\u0303ui'  // write (lenited: m->w̃)
    | 'nobini'  // visit (n unchanged)
    | 'katü'    // sit (intransitive)
    | 'üwi'     // sleep
    | 'kwisha\'i' // sneeze
    | 'poyoha'  // run
    | 'mia'     // go
    | 'hukaw\u0303ia' // walk (w + combining tilde)
    | 'wünü'    // stand
    | 'habi'    // lie down
    | 'yadoha'  // talk (intransitive)
    | 'kwatsa\'i' // fall
    | 'waakü'   // work
    | 'wükihaa' // smile
    | 'hubiadu' // sing
    | 'nishua\'i' // laugh
    | 'tübinohi' // play
    | 'yotsi'   // fly
    | 'nüga'    // dance
    | 'pahabi'  // swim
    | 'tünia'   // read (intransitive)
    | 'tümui'   // write (intransitive)
    | 'tsiipe\'i' // chirp
    ;

// --- Nouns ---
// Apostrophes (glottal stops in OVP) escaped as \'
NOUN
    : 'isha\''      // coyote
    | 'isha\'pugu'  // dog
    | 'kidi\''      // cat
    | 'pugu'        // horse
    | 'wai'         // rice
    | 'tüba'        // pinenuts
    | 'maishibü'    // corn
    | 'paya'        // water
    | 'payahuupü'   // river
    | 'katünu'      // chair
    | 'toyabi'      // mountain
    | 'tuunapi'     // food
    | 'pasohobü'    // tree
    | 'nobi'        // house
    | 'toni'        // wickiup
    | 'apo'         // cup
    | 'küna'        // wood
    | 'tübbi'       // rock
    | 'tabuutsi\''  // cottontail
    | 'kamü'        // jackrabbit
    | 'aaponu\''    // apple
    | 'tüsüga'      // weasel
    | 'mukita'      // lizard
    | 'wo\'ada'     // mosquito
    | 'wükada'      // bird snake
    | 'wo\'abi'     // worm
    | 'aingwü'      // squirrel
    | 'tsiipa'      // bird
    | 'tüwoobü'     // earth
    | 'koopi\''     // coffee
    | 'pahabichi'   // bear
    | 'pagwi'       // fish
    | 'kwadzi'      // tail
    ;

WS : [ \t\n\r]+ -> skip ;
