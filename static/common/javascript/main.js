"use strict";

/**
 * Init Accordions
 */

function ds_accordions() {

	var _this,
	accordions,
	accordion,
	accordionTitle,
	accordionContent;

	// Loop through each tab
	$('.accordions').each(function(){

		accordions = $(this);
		accordion = $('.accordion', accordions );
		accordionTitle = $('.accordion-title', accordions );
		accordionContent = $('.accordion-content', accordions );

		// Active class to first item
		accordionTitle.first().closest('.accordion').addClass('current-accordion-item');

		// Hide all tab contents
		accordionContent.hide();

		// Show first tab content
		accordionContent.first().show();

	});

	$(document).on( 'click', '.accordion-title', function(e){

		e.preventDefault();

		_this = $(this);
		accordions = _this.closest('.accordions');
		accordion = $('.accordion', accordions );
		accordionTitle = $('.accordion-title', accordions );
		accordionContent = $('.accordion-content', accordions );

		// Hide previous content and show new
		accordions.find('.current-accordion-item').removeClass('current-accordion-item').find('.accordion-content').slideUp( 200 );
		_this.closest('.accordion').addClass('current-accordion-item').find('.accordion-content').slideDown( 200 );

	});

}

/** 
 * Init Tabs
 */

function ds_tabs() {

	var _this,
	tabs,
	tabsNav,
	tabNav,
	tabsContent,
	tabContent;

	// Loop through each tab
	$('.tabs').each(function(){

		tabs = $(this);
		tabsNav = $( '.tabs-nav', tabs );
		tabNav = $( '.tab-nav', tabs );
		tabsContent = $( '.tabs-content', tabs );
		tabContent = $( '.tab-content', tabs );

		// Active class to first nav item
		tabNav.first().addClass('current-tab-nav-item');

		// Hide all tab contents
		tabContent.hide();

		// Show first tab content
		tabContent.first().addClass('current-tab-content-item').show();

	});

	$(document).on( 'click', '.tab-nav', function(e){

		e.preventDefault();

		_this = $(this);
		tabs = _this.closest('.tabs');
		tabsNav = $( '.tabs-nav', tabs );
		tabNav = $( '.tab-nav', tabs );
		tabsContent = $( '.tabs-content', tabs );
		tabContent = $( '.tab-content', tabs );

		// Switch the active class
		tabsNav.find('.current-tab-nav-item').removeClass('current-tab-nav-item');
		$(this).addClass('current-tab-nav-item');

		// Hide previous content and show new
		tabsContent.find('.current-tab-content-item').removeClass('current-tab-content-item').animate({ opacity : 0 }, 200, function(){
			$(this).hide();
			tabContent.eq( _this.index() ).addClass('current-tab-content-item').show().animate({ opacity : 1 }, 200 );
		});

	});

}

/**
 * Init carousels
 */

function ds_carousel() {

	// Loop through each carousel
	jQuery('.carousel, .slider').each(function() {
		
		// Variables
		var carousel, container, defSettings, usrSettings, settings;

		// Elements
		carousel = jQuery( this );
		container = carousel;

		if ( carousel.closest('.carousel-container').length ) {
			container = carousel.closest('.carousel-container');
		}

		// Default settings
		defSettings = {
			items : 4,
			pagination : true,
			singleItem : false,
			itemsScaleUp : false,
			slideSpeed : 200,
			paginationSpeed : 800,
			rewindSpeed : 1000,
			autoPlay : false,
			stopOnHover : false,
			lazyLoad : false,
			lazyFollow : true,
			autoHeight : false,
			mouseDrag : true,
			touchDrag : true,
			addClassActive : true,
			transitionStyle : 'fade',
			scrollPerPage : true
		};

		// Custom Settings
		usrSettings = {
			items : carousel.data( 'columns' ),
			pagination : carousel.data( 'pagination' ),
			itemsScaleUp : carousel.data( 'scale-up' ),
			slideSpeed : carousel.data( 'slide-speed' ),
			paginationSpeed : carousel.data( 'pagination-speed' ),
			rewindSpeed : carousel.data( 'rewind-speed' ),
			autoPlay : carousel.data( 'autoplay' ),
			stopOnHover : carousel.data( 'stop-on-hover' ),
			lazyLoad : carousel.data( 'lazy-load' ),
			lazyFollow : carousel.data( 'lazy-follow' ),
			autoHeight : carousel.data( 'flexible-height' ),
			mouseDrag : carousel.data( 'mouse-drag' ),
			touchDrag : carousel.data( 'touch-drag' ),
			addClassActive : carousel.data( 'active-class' ),
			transitionStyle : carousel.data( 'animation' ),
			scrollPerPage : carousel.data( 'scroll-per-page' )
		};

		// Merge default and custom settings
		settings = jQuery.extend( {}, defSettings, usrSettings );

		// If it's a slider set singleItem to true
		if ( carousel.hasClass( 'slider' ) || settings.items == 1 ) {
			settings.singleItem = true;
		}

		// If autoplay is 0 set to false
		if ( settings.autoPlay == 0 )
			settings.autoPlay = false;

		// Initialize
		carousel.owlCarousel({

			items : settings.items,
			pagination : settings.pagination,
			singleItem : settings.singleItem,
			itemsScaleUp : settings.itemsScaleUp,
			slideSpeed : settings.slideSpeed,
			paginationSpeed : settings.paginationSpeed,
			rewindSpeed : settings.rewindSpeed,
			autoPlay : settings.autoPlay,
			stopOnHover : settings.stopOnHover,
			lazyLoad : settings.lazyLoad,
			lazyFollow : settings.lazyFollow,
			mouseDrag : settings.mouseDrag,
			touchDrag : settings.touchDrag,
			scrollPerPage : settings.scrollPerPage,
			transitionStyle : settings.transitionStyle,
			autoHeight : settings.autoHeight,
			itemsDesktop : false,
			itemsDesktopSmall : false,
			itemsTablet : false,
			itemsMobile : [766,1],
			afterInit: function() {
				carousel.prev( '.carousel-loader, .slider-loader' ).remove();
				carousel.css({
					opacity : 1,
					maxHeight : 'none'
				});
			},
			afterAction : function(){
				var visible_items = this.owl.visibleItems;
				carousel.find('.carousel-item-visible').removeClass('carousel-item-visible');
				carousel.find('.owl-item').filter(function(index) {
					return visible_items.indexOf(index) > -1;
				}).addClass('carousel-item-visible');				
			}

		});

		// Previous
		jQuery( container ).on( 'click', '.carousel-go-next', function(e) {
			e.preventDefault();
			carousel.data( 'owlCarousel' ).next();
		});

		// Next
		jQuery( container ).on( 'click', '.carousel-go-prev', function(e) {
			e.preventDefault();
			carousel.data( 'owlCarousel' ).prev();
		});
		
	});

}

/**
 * Init Featured Posts
 */

function ds_featured_posts() {

	$('.featured-blog-posts .carousel').each(function(){

		var firstItem = $(this).find('.carousel-item:first');

		var duplicateContent = $(this).html();

		if( ! navigator.userAgent.match(/iPhone/i) ) {

			if ( $(this).find('.carousel-item').length < 12 ) {

				$(this).prepend( duplicateContent );
				$(this).prepend( duplicateContent );
				$(this).append( duplicateContent );
				$(this).append( duplicateContent );		

			} else {

				$(this).prepend( duplicateContent );
				$(this).append( duplicateContent );

			}

		}

		firstItem.addClass('first-carousel-blog-post');

	});

}

/**
 * Hambuger Navigation
 */

function ds_navigation_hamburger() {

	var navLabel,
	navURL;

	$('#navigation li a').each(function(){

		navLabel = $(this).text();
		navURL = $(this).attr('href');
		$('#navigation-hamburger select').append( '<option value="' + navURL + '">' + navLabel + '</option>' );

	});

	$('#navigation-hamburger select').change(function() {
		window.location = $(this).val();
	});

}

$(document).ready(function($){

	// Init featured posts carousel
	ds_featured_posts();

	// Init carousels
	ds_carousel();

	// Init tabs
	ds_tabs();

	// Init accordions
	ds_accordions();

	// Init hamburger menu
	ds_navigation_hamburger();

});

$(window).load(function() {

	if ( $('.featured-blog-posts .carousel').length ) {
		var owl = $('.featured-blog-posts .carousel').data('owlCarousel');
		owl.jumpTo( $('.featured-blog-posts .carousel .first-carousel-blog-post').closest('.owl-item').index() );
	}

});