import os

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

import sys
DJANGO_PATH = os.path.join(ROOT_PATH, "django")
sys.path.append(DJANGO_PATH)

#Directories
LAYOUT_DIR = os.path.join(ROOT_PATH, 'layout')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')

BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')
BACKUP = False

SITE_ROOT = "/"
SITE_WWW_URL = "http://joshbohde.com"
SITE_NAME = "Josh Bohde"
SITE_AUTHOR = "Josh Bohde"

#Url Configuration
GENERATE_ABSOLUTE_FS_URLS = False

# Clean urls causes Hyde to generate urls without extensions. Examples:
# http://example.com/section/page.html becomes
# http://example.com/section/page/, and the listing for that section becomes
# http://example.com/section/
# The built-in CherryPy webserver is capable of serving pages with clean urls
# without any additional configuration, but Apache will need to use Mod_Rewrite
# to map the clean urls to the actual html files.  The HtaccessGenerator site
# post processor is capable of automatically generating the necessary
# RewriteRules for use with Apache.
GENERATE_CLEAN_URLS = True

# A list of filenames (without extensions) that will be considered listing
# pages for their enclosing folders.
# LISTING_PAGE_NAMES = ['index']
LISTING_PAGE_NAMES = ['listing', 'index', 'default']

# Determines whether or not to append a trailing slash to generated urls when
# clean urls are enabled.
APPEND_SLASH = False

# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported as an indicator for folders. Path 
# should be specified. No wildcard card support yet.
 
# Starting under the media folder. For example, if you have media/css under 
# your site root,you should specify just css. If you have media/css/ie you 
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.

MEDIA_PROCESSORS = {
    '*':{
        '.css':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CSSmin',),
        '.ccss':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CleverCSS',
                'hydeengine.media_processors.CSSmin',),
        '.scss':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.Compass',
                'hydeengine.media_processors.CSSmin',),                
        '.less':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.LessCSS',
                'hydeengine.media_processors.CSSmin',),                
        '.hss':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.HSS',
                'hydeengine.media_processors.CSSmin',),
        '.js':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.JSmin',),
        '.coffee':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CoffeeScript',
                'hydeengine.media_processors.JSmin',),
    } 
}

CONTENT_PROCESSORS = {
    'prerendered/': {
        '*.*' : 
            ('hydeengine.content_processors.PassthroughProcessor',)
            }
}

SITE_POST_PROCESSORS = {
    '/': {
        'zipper.site_post_processors.GzipCompress' : {
            'filetypes': ['*html', '*.css', '*.js', '*.xml', '*.txt'],
            'level': 9,
        },
    }
}

from gitrevision import utils

CONTEXT = {
    'GENERATE_CLEAN_URLS': GENERATE_CLEAN_URLS,
    'REVISION': utils.GIT_REVISION,
    'ANALYTICS_SERVER': "http://joshbohde.com:3000/tracking.gif"
}

FILTER = { 
    'include': (".htaccess",),
    'exclude': (".*","*~")
}        


#Processor Configuration 

# 
#  Set this to the output of `which growlnotify`. If `which`  returns emtpy,
#  install growlnotify from the Extras package that comes with the Growl disk image.
# 
#
GROWL = None

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
YUI_COMPRESSOR = "./lib/yuicompressor-2.4.2.jar"
#YUI_COMPRESSOR = None 

# path for Closure Compiler, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://closure-compiler.googlecode.com/
#CLOSURE_COMPILER = "./lib/compiler.jar"
CLOSURE_COMPRILER = None 

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
#HSS_PATH = "./lib/hss-1.0-osx"
HSS_PATH = None # if you don't want to use HSS

COFFEE_PATH = "/usr/local/bin/coffee"
COMPASS_PATH = "/usr/bin/compass"
#Django settings

TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR, MEDIA_DIR)

PYGMENTS_OPTIONS = {
    "cssclass": "syntax"
}

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
    'verbatim',
)

