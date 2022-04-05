/* See LICENSE file for copyright and license details. */
/* Default settings; can be overriden by command line. */

static int topbar = 1;                      /* -b  option; if 0, dmenu appears at bottom     */
/* -fn option overrides fonts[0]; default X11 font or font set */
static const char *fonts[] = {
	"monospace:size=12", "Noto Color Emoji:size=12"
};
static const char *prompt      = NULL;      /* -p  option; prompt to the left of input field */
/* custom color scheme https://colorhunt.co/palette/151d3bd821486ebf8bdadbbd */
static const char col_navy[]        = "#151D3B";
static const char col_red[]        = "#D82148";
static const char col_teal[]        = "#6EBF8B";
static const char col_beige[]        = "#DADBBD";

static const char *colors[SchemeLast][2] = {
	        	/*     fg         bg       */
	[SchemeNorm] = {col_beige, col_navy },
	[SchemeSel] = { col_red, col_navy },
	[SchemeOut] = { "#000000", "#00ffff" },
};
/* -l option; if nonzero, dmenu uses vertical list with given number of lines */
static unsigned int lines      = 0;

/*
 * Characters not considered part of a word while deleting words
 * for example: " /?\"&[]"
 */
static const char worddelimiters[] = " ";
