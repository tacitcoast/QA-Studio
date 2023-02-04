describe('Тестирование покупки на сайте testqastudio.me', function () {
    it('Позитивная проверка покупки', function () {
        cy.visit('https://testqastudio.me/');
        cy.get('.post-11342 > .product-inner > .product-thumbnail > .woocommerce-LoopProduct-link > .attachment-woocommerce_thumbnail').click();
        cy.get('.summary > .cart > .product-button-wrapper > .quantity > .increase > svg').click().click();
        cy.get('.summary > .cart > .product-button-wrapper > .single_add_to_cart_button').click();
        cy.get('.cart-panel-content > .modal-header > .close-account-panel > .razzi-svg-icon > svg').click();
        cy.get('.header-left-items > .site-branding > .logo > .logo-dark').click();
        cy.get('.post-11337 > .product-inner > .product-thumbnail > .woocommerce-LoopProduct-link > .attachment-woocommerce_thumbnail').click();
        cy.get('.summary > .cart > .product-button-wrapper > .single_add_to_cart_button').click();
        cy.intercept('POST', '/product/**').as('ajax-product');
        cy.intercept('/?wc-ajax=get_refreshed_fragments').as('ajax-reload');
        cy.get('.product-button-wrapper > button[name="add-to-cart"]:visible').click();
        cy.wait('@ajax-product');
        cy.wait('@ajax-reload');
        cy.get('.checkout').click();
        cy.get('#billing_first_name').type('Иван');
        cy.get('#billing_last_name').type('Иванов');
        cy.get('#billing_address_1').type('LINDA-A-VELHA RUA ENG JOSE FREDERICO ULRICH NR 33');
        cy.get('#billing_city').type('Portugal');
        cy.get('#billing_state').type('Portugal');
        cy.get('#billing_postcode').type('2795-113');
        cy.get('#billing_phone').type('89119590535');
        cy.get('#billing_email').type('german@dolnikov.ru');
        cy.get('#place_order').click();
        cy.contains('Ваш заказ принят. Благодарим вас.');
        })

 })