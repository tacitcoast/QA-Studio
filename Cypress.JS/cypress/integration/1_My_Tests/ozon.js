describe('Тестирование Ozon', function () {
    it('Дохожу до корзины в Ozon', function () {
        cy.visit('https://www.ozon.ru/');
        cy.get("input[type='text']:first").type('айфон').type('{enter}');
        cy.contains('iPhone');
        cy.get('div').should('have.class', 'ys')
        .contains('span', 'Apple');
        cy.get(':nth-child(1) > .pi4 > .i5p > .tile-hover-target > .de0 > span')
        .click();
        cy.get('[data-replace-layout-path="[5][0][2][0][1][0][1][0][0][2]"] > .jm6 > .j7j > .ui-j8 > .m5j > :nth-child(2) > .ui-c1 > .ui-c3 > .ui-c4 > .ui-g0')
        .click();
        cy.get('[href="/cart"]').click();
        cy.get('.o8a > .de1 > span').contains('Герман');
    })
})
