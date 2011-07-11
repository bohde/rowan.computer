(function(w){
    var onload = function(event){
        if(w.addEventListener){
            w.addEventListener('load', event, false);
        }else if(w.attachEvent){
            w.attachEvent('onload', event);
        }
    };

    w._gaq = [['_setAccount', 'UA-9518092-1'], ['_trackPageview'], ['_trackPageLoadTime']];

    onload(function(){
        var loaded = new Date();
        Modernizr.load({
            load: {
                jquery: "//ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js", 
                timeago:"http://cachedcommons.org/cache/jquery-timeago/0.9.0/javascripts/jquery-timeago-min.js",
                boomr: "{{site.url}}/media/js/boomerang.js",
                ga: ('https:'==document.location.protocol?'https://ssl':'http://www')+'.google-analytics.com/ga.js',
                disqus: 'http://joshbohde.disqus.com/embed.js'
            }, 
            callback: {
                timeago: function(){
                    $('time').timeago();
                },
                boomr: function(){
                    BOOMR.addVar('revision', '{{ REVISION }}');
                    BOOMR.init({
                        beacon_url: '{{ ANALYTICS_SERVER }}',
                        site_domain: '{{ COOKIE_URL }}', 
                        BW: { enabled: false  },
		                    autorun: false
                    });
                    BOOMR.page_ready();
                }
            }
        });
    });
})(window);
