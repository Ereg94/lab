/**
 * Example @VERSION - 
 *
 * Copyright (c) 2008-2009 ClayoolJS
 *
 */
(function($){    
	//-------------------------------------------------------------------------------------//
	//  -   ENVIRONMENTAL CONFIGURATION   -
	//______________________________________________________________________________________//
	$.config("env", {
	    defaults:{
			templates:'media/js/app/views/templates',
	        rest: {
	            SERVICE: "Any",
	            URL: "/rest",
	            AJAX: "jQuery"
	        }
	    },
	    //-------------------------------------------------------------------------------------//
	    //  -   DEVELOPMENT CONFIGURATION   -
	    //______________________________________________________________________________________//
	    dev:{
	        client:{
	        }
	    },
	    //-------------------------------------------------------------------------------------//
	    //  -   PRODUCTION CONFIGURATION   -
	    //______________________________________________________________________________________//
	    prod:{
	        client:{
	        }
	    },
	    //-------------------------------------------------------------------------------------//
	    //  -   TEST CONFIGURATION   -
	    //______________________________________________________________________________________//
	    test:{
	        client:{
	        }
	    }
	}); 
    
})(jQuery);
    
