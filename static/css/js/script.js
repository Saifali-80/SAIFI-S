$(document).ready(function() {
    // Sidebar Toggle
    $('#sidebarToggle').click(function() {
        $('#sidebar').addClass('active');
        $('#sidebarOverlay').addClass('active');
        $('body').css('overflow', 'hidden');
    });

    // Close Sidebar
    $('#sidebarClose, #sidebarOverlay').click(function() {
        $('#sidebar').removeClass('active');
        $('#sidebarOverlay').removeClass('active');
        $('body').css('overflow', 'auto');
    });

    // Mobile Search Toggle
    $('#searchToggleMobile').click(function() {
        $('#mobileSearch').addClass('active');
    });

    $('#mobileSearchClose').click(function() {
        $('#mobileSearch').removeClass('active');
    });

    // Search Functionality
    $('#searchBtn').click(function() {
        performSearch();
    });

    $('#searchInput').keypress(function(e) {
        if (e.which === 13) {
            performSearch();
        }
    });

    function performSearch() {
        const query = $('#searchInput').val().trim();
        if (query) {
            // Send search request
            $.ajax({
                url: '/search',
                method: 'GET',
                data: { q: query },
                success: function(response) {
                    console.log('Search results:', response);
                    // Handle search results here
                    // You can redirect to search results page or display results
                    window.location.href = `/search?q=${encodeURIComponent(query)}`;
                },
                error: function(error) {
                    console.error('Search error:', error);
                }
            });
        }
    }

    // Add to Cart Functionality (Example)
    $('.add-to-cart-btn').click(function() {
        const itemData = {
            id: $(this).data('id'),
            name: $(this).data('name'),
            price: $(this).data('price')
        };

        $.ajax({
            url: '/add-to-cart',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(itemData),
            success: function(response) {
                if (response.success) {
                    updateCartCount(response.cart_count);
                    // Show success animation
                    showNotification('Item added to cart!');
                }
            }
        });
    });

    // Update Cart Count
    function updateCartCount(count) {
        $('#cartCount').text(count);
        if (count > 0) {
            $('#cartCount').addClass('has-items');
        }
    }

    // Get initial cart count
    function getCartCount() {
        $.get('/get-cart-count', function(response) {
            updateCartCount(response.cart_count);
        });
    }

    // Notification System
    function showNotification(message) {
        const notification = $('<div>')
            .addClass('notification')
            .text(message)
            .appendTo('body');
        
        setTimeout(() => {
            notification.addClass('show');
        }, 100);

        setTimeout(() => {
            notification.removeClass('show');
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 2000);
    }

    // Initialize cart count
    getCartCount();

    // Close sidebar with Escape key
    $(document).keydown(function(e) {
        if (e.key === 'Escape') {
            $('#sidebar').removeClass('active');
            $('#sidebarOverlay').removeClass('active');
            $('#mobileSearch').removeClass('active');
            $('body').css('overflow', 'auto');
        }
    });

    // Add animation classes on scroll
    $(window).scroll(function() {
        const scroll = $(window).scrollTop();
        if (scroll > 50) {
            $('.navbar').addClass('navbar-scrolled');
        } else {
            $('.navbar').removeClass('navbar-scrolled');
        }
    });
});